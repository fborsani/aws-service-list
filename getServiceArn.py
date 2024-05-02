import requests
import concurrent.futures
from bs4 import BeautifulSoup 

AWS_DOC_BASE_URL = "https://docs.aws.amazon.com/service-authorization/latest/reference/"
AWS_DOC_REF_LIST = "reference_policies_actions-resources-contextkeys.html"
TABLE_MATCH_STRING = "ARN"
MAX_THREADS = 15

def thread_worker(url: str):
    row_values = []
    success = True
    msg = None

    if url is not None and url != "":
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        tables = soup.select("table")  
        for t in tables:
            if t.find("th", string=TABLE_MATCH_STRING):
                for r in t.find_all("tr"):
                    cols = r.find_all("td")
                    if cols:
                        row_values.append(
                            {
                                "link": cols[0].find("a")["href"] if cols[0].find("a") else cols[0].text.strip(),
                                "name": cols[0].text.strip(),
                                "arn": cols[1].text.strip()
                            }
                        )
                break
    else:
        success = False
        msg = "Url missing or empty"

    return {
        "success": success,
        "msg": msg,
        "result": row_values,
        "url": url
        }

def get_full_path(url:str):
    if url is not None and url != "" and url.startswith("./"):
        return AWS_DOC_BASE_URL+url[2:]
    return url
    
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

def print_text(data: list) -> str:
    output = ""
    for i in data:
        output += "========== "+i["resource"]+" ==========\n\n"
        output += print_table(i["services"], ["Service Type", "ARN"], ["name", "arn"], [40, 135])
        output +="\n\n"
    return output

def print_html(data: list) -> str:
    output = ""
    for resource in data:
        output += '''<h1>{}</h1>
        <p>Doc reference: {}</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="800px">ARN</th> 
            </thead>
            <tbody>
        '''.format(resource["resource"], resource["doc_url"])
        for service in resource["services"]:
            output += '''   <tr>
                    <td><a href="{}">{}</a></td>
                    <td>{}</td>
                </tr>
            '''.format(service["link"], service["name"], service["arn"].replace("$","\$") )
        output += '''</tbody>
        </table>
        '''
    return output


def write_to_file(path:str, value:str):
    with open(path, "w+") as f:
        f.write(value)

def main():
    aws_doc_start_url = AWS_DOC_BASE_URL + AWS_DOC_REF_LIST
    r = requests.get(aws_doc_start_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    links = {l.text : get_full_path(l.find("a")["href"]) for l in soup.find(class_="highlights").find_all("li")}

    resources = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as threadPool:
         threads = {threadPool.submit(thread_worker, links[resource]): resource for resource in links.keys()}
         for thread in concurrent.futures.as_completed(threads):
            res = thread.result()
            if res["success"]:
                print("[+] "+res["url"])
                resources.append(
                    {
                        "resource": threads[thread],
                        "doc_url": res["url"],
                        "services": res["result"]
                    }
                )
            else:
                print("[-] Error for page {}: {}".format(res["url"], res["msg"]))

    write_to_file("./generated_docs/aws_services.txt",print_text(resources))
    write_to_file("./generated_docs/aws_services.md",print_html(resources))


if __name__ == "__main__":
    main()
