import requests
import concurrent.futures
from bs4 import BeautifulSoup 

AWS_DOC_BASE_URL = "https://docs.aws.amazon.com/service-authorization/latest/reference/"
AWS_DOC_REF_LIST = "reference_policies_actions-resources-contextkeys.html"
TABLE_MATCH_STRING = "ARN"
MAX_THREADS = 15

def thread_worker(url: str):
    row_values = []
    if url is not None and url != "":
            link = url
            if url.startswith("./"):
                link = AWS_DOC_BASE_URL+url[2:]
            print("l "+link)
            r = requests.get(link)
            soup = BeautifulSoup(r.text, 'html.parser')
            tables = soup.select("table")  
            for t in tables:
                if t.find("th", string=TABLE_MATCH_STRING):
                    for r in t.find_all("tr"):
                        cols = r.find_all("td")
                        if cols:
                            row_values.append(
                                {
                                    "service_html": cols[0].find("a") if cols[0].find("a") else cols[0].text.strip(),
                                    "service_text": cols[0].text.strip(),
                                    "arn": cols[1].text.strip(),
                                    "page_url": url
                                }
                            )
    return row_values

def print_table(rows:list, cols:list, keys:list, padding:list):
        sep = "|"
        placeholder_none = "*"
        sep_row = ""
        
        for p in range(0, len(padding)):
            chars_lt = ""
            chars_rt = ""

            if p == 0:
                sep_row += "\n"
                chars_lt = sep

            if p < (len(padding) - 1):
                chars_rt = "+"
            else:
                chars_rt = sep

            sep_row += chars_lt + "-" * (padding[p]) + chars_rt
            
        header = ""
        body = ""

        for c in range(0,len(cols)):
            header += sep + f"{' '+cols[c]:<{padding[c]}s}"
        header += sep

        for r in rows:         
            row = sep
            for k in range(0,len(cols)):
                val = r[keys[k]] if r[keys[k]] else placeholder_none
                row += f"{' '+val:<{padding[k]}s}"+sep 
            body += "\n" + row + sep_row

        return header + sep_row + body

def print_text(data: dict) -> str:
    output = ""
    for k,v in data.items():
        output += "========== "+k+" ==========\n\n"
        output += print_table(v, ["Service Type", "ARN"], ["service_text", "arn"], [40, 135])
        output +="\n\n"
    return output

def print_markdown(data: dict) -> str:
    pass

def print_html(data: dict) -> str:
    pass

def write_to_file(path:str, value:str):
    with open(path, "w+") as f:
        f.write(value)

def main():
    aws_doc_start_url = AWS_DOC_BASE_URL + AWS_DOC_REF_LIST
    r = requests.get(aws_doc_start_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    links = {l.text : l.find("a")["href"] for l in soup.find(class_="highlights").find_all("li")}

    service_dict = {}

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as threadPool:
         threads = {threadPool.submit(thread_worker, links[page]): page for page in links.keys()}

         for thread in concurrent.futures.as_completed(threads):
             res = thread.result()
             if res:
                 service_dict[threads[thread]] = res

    write_to_file("./generated_docs/aws_services.txt",print_text(service_dict))


if __name__ == "__main__":
    main()
