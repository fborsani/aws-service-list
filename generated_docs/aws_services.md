<h1>AWS Account Management</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsaccountmanagement.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/accounts/latest/reference/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources">account</a></td>
                    <td>arn:\${Partition}:account::\${Account}:account</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/accounts/latest/reference/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources">accountInOrganization</a></td>
                    <td>arn:\${Partition}:account::\${ManagementAccountId}:account/o-\${OrganizationId}/\${MemberAccountId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon API Gateway</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonapigateway.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="execute-api-general">execute-api-general</a></td>
                    <td>arn:\${Partition}:execute-api:\${Region}:\${Account}:\${ApiId}/\${Stage}/\${Method}/\${ApiSpecificResourcePath}</td>
                </tr>
            </tbody>
        </table>
        <h1>AmazonMediaImport</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmediaimport.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS App Mesh Preview</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsappmeshpreview.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/meshes.html">mesh</a></td>
                    <td>arn:\${Partition}:appmesh-preview:\${Region}:\${Account}:mesh/\${MeshName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_services.html">virtualService</a></td>
                    <td>arn:\${Partition}:appmesh-preview:\${Region}:\${Account}:mesh/\${MeshName}/virtualService/\${VirtualServiceName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_nodes.html">virtualNode</a></td>
                    <td>arn:\${Partition}:appmesh-preview:\${Region}:\${Account}:mesh/\${MeshName}/virtualNode/\${VirtualNodeName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_routers.html">virtualRouter</a></td>
                    <td>arn:\${Partition}:appmesh-preview:\${Region}:\${Account}:mesh/\${MeshName}/virtualRouter/\${VirtualRouterName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/routes.html">route</a></td>
                    <td>arn:\${Partition}:appmesh-preview:\${Region}:\${Account}:mesh/\${MeshName}/virtualRouter/\${VirtualRouterName}/route/\${RouteName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_gateways.html">virtualGateway</a></td>
                    <td>arn:\${Partition}:appmesh-preview:\${Region}:\${Account}:mesh/\${MeshName}/virtualGateway/\${VirtualGatewayName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_gateways.html">gatewayRoute</a></td>
                    <td>arn:\${Partition}:appmesh-preview:\${Region}:\${Account}:mesh/\${MeshName}/virtualGateway/\${VirtualGatewayName}/gatewayRoute/\${GatewayRouteName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Amplify</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsamplify.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html">apps</a></td>
                    <td>arn:\${Partition}:amplify:\${Region}:\${Account}:apps/\${AppId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html">branches</a></td>
                    <td>arn:\${Partition}:amplify:\${Region}:\${Account}:apps/\${AppId}/branches/\${BranchName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html">jobs</a></td>
                    <td>arn:\${Partition}:amplify:\${Region}:\${Account}:apps/\${AppId}/branches/\${BranchName}/jobs/\${JobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html">domains</a></td>
                    <td>arn:\${Partition}:amplify:\${Region}:\${Account}:apps/\${AppId}/domains/\${DomainName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html">webhooks</a></td>
                    <td>arn:\${Partition}:amplify:\${Region}:\${Account}:webhooks/\${WebhookId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS App2Container</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsapp2container.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Activate</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsactivate.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Apache Kafka APIs for Amazon MSK clusters</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_apachekafkaapisforamazonmskclusters.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#msk-iam-resources">cluster</a></td>
                    <td>arn:\${Partition}:kafka:\${Region}:\${Account}:cluster/\${ClusterName}/\${ClusterUuid}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#msk-iam-resources">topic</a></td>
                    <td>arn:\${Partition}:kafka:\${Region}:\${Account}:topic/\${ClusterName}/\${ClusterUuid}/\${TopicName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#msk-iam-resources">group</a></td>
                    <td>arn:\${Partition}:kafka:\${Region}:\${Account}:group/\${ClusterName}/\${ClusterUuid}/\${GroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#msk-iam-resources">transactional-id</a></td>
                    <td>arn:\${Partition}:kafka:\${Region}:\${Account}:transactional-id/\${ClusterName}/\${ClusterUuid}/\${TransactionalId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Amplify Admin</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsamplifyadmin.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend.html">created-backend</a></td>
                    <td>arn:\${Partition}:amplifybackend:\${Region}:\${Account}:/backend/*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend.html">backend</a></td>
                    <td>arn:\${Partition}:amplifybackend:\${Region}:\${Account}:/backend/\${AppId}/*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-api-backendenvironmentname-details.html">environment</a></td>
                    <td>arn:\${Partition}:amplifybackend:\${Region}:\${Account}:/backend/\${AppId}/environments/*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-api.html">api</a></td>
                    <td>arn:\${Partition}:amplifybackend:\${Region}:\${Account}:/backend/\${AppId}/api/*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-auth.html">auth</a></td>
                    <td>arn:\${Partition}:amplifybackend:\${Region}:\${Account}:/backend/\${AppId}/auth/*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-job-backendenvironmentname.html">job</a></td>
                    <td>arn:\${Partition}:amplifybackend:\${Region}:\${Account}:/backend/\${AppId}/job/*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-config.html">config</a></td>
                    <td>arn:\${Partition}:amplifybackend:\${Region}:\${Account}:/backend/\${AppId}/config/*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-token.html">token</a></td>
                    <td>arn:\${Partition}:amplifybackend:\${Region}:\${Account}:/backend/\${AppId}/challenge/*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-storage.html">storage</a></td>
                    <td>arn:\${Partition}:amplifybackend:\${Region}:\${Account}:/backend/\${AppId}/storage/*</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS App Runner</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsapprunner.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="${UserGuideDocPage}architecture.html#architecture.resources">service</a></td>
                    <td>arn:\${Partition}:apprunner:\${Region}:\${Account}:service/\${ServiceName}/\${ServiceId}</td>
                </tr>
               <tr>
                    <td><a href="${UserGuideDocPage}architecture.html#architecture.resources">connection</a></td>
                    <td>arn:\${Partition}:apprunner:\${Region}:\${Account}:connection/\${ConnectionName}/\${ConnectionId}</td>
                </tr>
               <tr>
                    <td><a href="${UserGuideDocPage}architecture.html#architecture.resources">autoscalingconfiguration</a></td>
                    <td>arn:\${Partition}:apprunner:\${Region}:\${Account}:autoscalingconfiguration/\${AutoscalingConfigurationName}/\${AutoscalingConfigurationVersion}/\${AutoscalingConfigurationId}</td>
                </tr>
               <tr>
                    <td><a href="${UserGuideDocPage}architecture.html#architecture.resources">observabilityconfiguration</a></td>
                    <td>arn:\${Partition}:apprunner:\${Region}:\${Account}:observabilityconfiguration/\${ObservabilityConfigurationName}/\${ObservabilityConfigurationVersion}/\${ObservabilityConfigurationId}</td>
                </tr>
               <tr>
                    <td><a href="${UserGuideDocPage}architecture.html#architecture.resources">vpcconnector</a></td>
                    <td>arn:\${Partition}:apprunner:\${Region}:\${Account}:vpcconnector/\${VpcConnectorName}/\${VpcConnectorVersion}/\${VpcConnectorId}</td>
                </tr>
               <tr>
                    <td><a href="${UserGuideDocPage}architecture.html#architecture.resources">vpcingressconnection</a></td>
                    <td>arn:\${Partition}:apprunner:\${Region}:\${Account}:vpcingressconnection/\${VpcIngressConnectionName}/\${VpcIngressConnectionId}</td>
                </tr>
               <tr>
                    <td><a href="${UserGuideDocPage}waf.html">webacl</a></td>
                    <td>arn:\${Partition}:wafv2:\${Region}:\${Account}:\${Scope}/webacl/\${Name}/\${Id}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Amplify UI Builder</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsamplifyuibuilder.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CodegenJob.html">CodegenJobResource</a></td>
                    <td>arn:\${Partition}:amplifyuibuilder:\${Region}:\${Account}:app/\${AppId}/environment/\${EnvironmentName}/codegen-jobs/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_Component.html">ComponentResource</a></td>
                    <td>arn:\${Partition}:amplifyuibuilder:\${Region}:\${Account}:app/\${AppId}/environment/\${EnvironmentName}/components/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_Form.html">FormResource</a></td>
                    <td>arn:\${Partition}:amplifyuibuilder:\${Region}:\${Account}:app/\${AppId}/environment/\${EnvironmentName}/forms/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_Theme.html">ThemeResource</a></td>
                    <td>arn:\${Partition}:amplifyuibuilder:\${Region}:\${Account}:app/\${AppId}/environment/\${EnvironmentName}/themes/\${Id}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Application Cost Profiler Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsapplicationcostprofilerservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon API Gateway Management V2</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonapigatewaymanagementv2.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">AccessLogSettings</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/stages/\${StageName}/accesslogsettings</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">Api</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">Apis</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/apis</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">ApiMapping</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/domainnames/\${DomainName}/apimappings/\${ApiMappingId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">ApiMappings</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/domainnames/\${DomainName}/apimappings</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">Authorizer</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/authorizers/\${AuthorizerId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">Authorizers</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/authorizers</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">AuthorizersCache</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/stages/\${StageName}/cache/authorizers</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">Cors</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/cors</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">Deployment</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/deployments/\${DeploymentId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">Deployments</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/deployments</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">ExportedAPI</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/exports/\${Specification}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">Integration</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/integrations/\${IntegrationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">Integrations</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/integrations</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">IntegrationResponse</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/integrations/\${IntegrationId}/integrationresponses/\${IntegrationResponseId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">IntegrationResponses</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/integrations/\${IntegrationId}/integrationresponses</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">Model</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/models/\${ModelId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">Models</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/models</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">ModelTemplate</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/models/\${ModelId}/template</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">Route</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/routes/\${RouteId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">Routes</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/routes</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">RouteResponse</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/routes/\${RouteId}/routeresponses/\${RouteResponseId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">RouteResponses</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/routes/\${RouteId}/routeresponses</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">RouteRequestParameter</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/routes/\${RouteId}/requestparameters/\${RequestParameterKey}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">RouteSettings</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/stages/\${StageName}/routesettings/\${RouteKey}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">Stage</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/stages/\${StageName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">Stages</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/stages</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">VpcLink</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/vpclinks/\${VpcLinkId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">VpcLinks</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/vpclinks</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS App Mesh</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsappmesh.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/meshes.html">mesh</a></td>
                    <td>arn:\${Partition}:appmesh:\${Region}:\${Account}:mesh/\${MeshName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_services.html">virtualService</a></td>
                    <td>arn:\${Partition}:appmesh:\${Region}:\${Account}:mesh/\${MeshName}/virtualService/\${VirtualServiceName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_nodes.html">virtualNode</a></td>
                    <td>arn:\${Partition}:appmesh:\${Region}:\${Account}:mesh/\${MeshName}/virtualNode/\${VirtualNodeName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_routers.html">virtualRouter</a></td>
                    <td>arn:\${Partition}:appmesh:\${Region}:\${Account}:mesh/\${MeshName}/virtualRouter/\${VirtualRouterName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/routes.html">route</a></td>
                    <td>arn:\${Partition}:appmesh:\${Region}:\${Account}:mesh/\${MeshName}/virtualRouter/\${VirtualRouterName}/route/\${RouteName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_gateways.html">virtualGateway</a></td>
                    <td>arn:\${Partition}:appmesh:\${Region}:\${Account}:mesh/\${MeshName}/virtualGateway/\${VirtualGatewayName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_gateways.html">gatewayRoute</a></td>
                    <td>arn:\${Partition}:appmesh:\${Region}:\${Account}:mesh/\${MeshName}/virtualGateway/\${VirtualGatewayName}/gatewayRoute/\${GatewayRouteName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon AppFlow</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonappflow.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ConnectorProfile.html">connectorprofile</a></td>
                    <td>arn:\${Partition}:appflow:\${Region}:\${Account}:connectorprofile/\${ProfileName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appflow/1.0/APIReference/API_FlowDefinition.html">flow</a></td>
                    <td>arn:\${Partition}:appflow:\${Region}:\${Account}:flow/\${FlowName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ConnectorDetail.html">connector</a></td>
                    <td>arn:\${Partition}:appflow:\${Region}:\${Account}:connector/\${ConnectorLabel}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon API Gateway Management</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonapigatewaymanagement.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">Account</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/account</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_ApiKey.html">ApiKey</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/apikeys/\${ApiKeyId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_ApiKey.html">ApiKeys</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/apikeys</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_Authorizer.html">Authorizer</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/authorizers/\${AuthorizerId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_Authorizer.html">Authorizers</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/authorizers</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_BasePathMapping.html">BasePathMapping</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/domainnames/\${DomainName}/basepathmappings/\${BasePath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_BasePathMapping.html">BasePathMappings</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/domainnames/\${DomainName}/basepathmappings</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_ClientCertificate.html">ClientCertificate</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/clientcertificates/\${ClientCertificateId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_ClientCertificate.html">ClientCertificates</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/clientcertificates</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_Deployment.html">Deployment</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/deployments/\${DeploymentId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_Deployment.html">Deployments</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/deployments</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_DocumentationPart.html">DocumentationPart</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/documentation/parts/\${DocumentationPartId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_DocumentationPart.html">DocumentationParts</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/documentation/parts</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_DocumentationVersion.html">DocumentationVersion</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/documentation/versions/\${DocumentationVersionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_DocumentationVersion.html">DocumentationVersions</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/documentation/versions</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_DomainName.html">DomainName</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/domainnames/\${DomainName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_DomainName.html">DomainNames</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/domainnames</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_GatewayResponse.html">GatewayResponse</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/gatewayresponses/\${ResponseType}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_GatewayResponse.html">GatewayResponses</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/gatewayresponses</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_Integration.html">Integration</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/resources/\${ResourceId}/methods/\${HttpMethodType}/integration</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_IntegrationResponse.html">IntegrationResponse</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/resources/\${ResourceId}/methods/\${HttpMethodType}/integration/responses/\${StatusCode}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_Method.html">Method</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/resources/\${ResourceId}/methods/\${HttpMethodType}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_MethodResponse.html">MethodResponse</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/resources/\${ResourceId}/methods/\${HttpMethodType}/responses/\${StatusCode}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_Model.html">Model</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/models/\${ModelName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_Model.html">Models</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/models</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_RequestValidator.html">RequestValidator</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/requestvalidators/\${RequestValidatorId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_RequestValidator.html">RequestValidators</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/requestvalidators</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_Resource.html">Resource</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/resources/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_Resource.html">Resources</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/resources</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_RestApi.html">RestApi</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_RestApi.html">RestApis</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/restapis</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">Sdk</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/stages/\${StageName}/sdks/\${SdkType}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_Stage.html">Stage</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/stages/\${StageName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_Stage.html">Stages</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/stages</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html">Template</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/restapis/models/\${ModelName}/template</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_UsagePlan.html">UsagePlan</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/usageplans/\${UsagePlanId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_UsagePlan.html">UsagePlans</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/usageplans</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_UsagePlanKey.html">UsagePlanKey</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/usageplans/\${UsagePlanId}/keys/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_UsagePlanKey.html">UsagePlanKeys</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/usageplans/\${UsagePlanId}/keys</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_VpcLink.html">VpcLink</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/vpclinks/\${VpcLinkId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/api/API_VpcLink.html">VpcLinks</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/vpclinks</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-tagging.html">Tags</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/tags/\${UrlEncodedResourceARN}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS AppConfig</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsappconfig.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-application.html">application</a></td>
                    <td>arn:\${Partition}:appconfig:\${Region}:\${Account}:application/\${ApplicationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-environment.html">environment</a></td>
                    <td>arn:\${Partition}:appconfig:\${Region}:\${Account}:application/\${ApplicationId}/environment/\${EnvironmentId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile.html">configurationprofile</a></td>
                    <td>arn:\${Partition}:appconfig:\${Region}:\${Account}:application/\${ApplicationId}/configurationprofile/\${ConfigurationProfileId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy.html">deploymentstrategy</a></td>
                    <td>arn:\${Partition}:appconfig:\${Region}:\${Account}:deploymentstrategy/\${DeploymentStrategyId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-deploying.html">deployment</a></td>
                    <td>arn:\${Partition}:appconfig:\${Region}:\${Account}:application/\${ApplicationId}/environment/\${EnvironmentId}/deployment/\${DeploymentNumber}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile.html">hostedconfigurationversion</a></td>
                    <td>arn:\${Partition}:appconfig:\${Region}:\${Account}:application/\${ApplicationId}/configurationprofile/\${ConfigurationProfileId}/hostedconfigurationversion/\${VersionNumber}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-retrieving-the-configuration.html">configuration</a></td>
                    <td>arn:\${Partition}:appconfig:\${Region}:\${Account}:application/\${ApplicationId}/environment/\${EnvironmentId}/configuration/\${ConfigurationProfileId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html">extension</a></td>
                    <td>arn:\${Partition}:appconfig:\${Region}:\${Account}:extension/\${ExtensionId}/\${ExtensionVersionNumber}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html">extensionassociation</a></td>
                    <td>arn:\${Partition}:appconfig:\${Region}:\${Account}:extensionassociation/\${ExtensionAssociationId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Application Auto Scaling</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsapplicationautoscaling.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/autoscaling/application/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources">ScalableTarget</a></td>
                    <td>arn:\${Partition}:application-autoscaling:\${Region}:\${Account}:scalable-target/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Application Discovery Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsapplicationdiscoveryservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Application Discovery Arsenal</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_applicationdiscoveryarsenal.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS AppFabric</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsappfabric.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/appfabric/latest/api/API_AppBundle.html">appbundle</a></td>
                    <td>arn:\${Partition}:appfabric:\${Region}:\${Account}:appbundle/\${AppBundleIdentifier}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appfabric/latest/api/API_AppAuthorization.html">appauthorization</a></td>
                    <td>arn:\${Partition}:appfabric:\${Region}:\${Account}:appbundle/\${AppbundleId}/appauthorization/\${AppAuthorizationIdentifier}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appfabric/latest/api/API_Ingestion.html">ingestion</a></td>
                    <td>arn:\${Partition}:appfabric:\${Region}:\${Account}:appbundle/\${AppbundleId}/ingestion/\${IngestionIdentifier}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appfabric/latest/api/API_IngestionDestination.html">ingestiondestination</a></td>
                    <td>arn:\${Partition}:appfabric:\${Region}:\${Account}:appbundle/\${AppbundleId}/ingestion/\${IngestionIdentifier}/ingestiondestination/\${IngestionDestinationIdentifier}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon AppIntegrations</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonappintegrations.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_EventIntegration.html">event-integration</a></td>
                    <td>arn:\${Partition}:app-integrations:\${Region}:\${Account}:event-integration/\${EventIntegrationName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_EventIntegrationAssociation.html">event-integration-association</a></td>
                    <td>arn:\${Partition}:app-integrations:\${Region}:\${Account}:event-integration-association/\${EventIntegrationName}/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DataIntegrationSummary.html">data-integration</a></td>
                    <td>arn:\${Partition}:app-integrations:\${Region}:\${Account}:data-integration/\${DataIntegrationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DataIntegrationAssociationSummary.html">data-integration-association</a></td>
                    <td>arn:\${Partition}:app-integrations:\${Region}:\${Account}:data-integration-association/\${DataIntegrationId}/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ApplicationSummary.html">application</a></td>
                    <td>arn:\${Partition}:app-integrations:\${Region}:\${Account}:application/\${ApplicationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ApplicationAssociationSummary.html">application-association</a></td>
                    <td>arn:\${Partition}:app-integrations:\${Region}:\${Account}:application-association/\${ApplicationId}/\${ApplicationAssociationId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Application Migration Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsapplicationmigrationservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/mgn/latest/ug/launching-target-servers.html">JobResource</a></td>
                    <td>arn:\${Partition}:mgn:\${Region}:\${Account}:job/\${JobID}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mgn/latest/ug/replication-settings-template.html">ReplicationConfigurationTemplateResource</a></td>
                    <td>arn:\${Partition}:mgn:\${Region}:\${Account}:replication-configuration-template/\${ReplicationConfigurationTemplateID}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mgn/latest/ug/post-launch-settings.html">LaunchConfigurationTemplateResource</a></td>
                    <td>arn:\${Partition}:mgn:\${Region}:\${Account}:launch-configuration-template/\${LaunchConfigurationTemplateID}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mgn/latest/ug/agentless-mgn.html">VcenterClientResource</a></td>
                    <td>arn:\${Partition}:mgn:\${Region}:\${Account}:vcenter-client/\${VcenterClientID}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mgn/latest/ug/source-servers.html">SourceServerResource</a></td>
                    <td>arn:\${Partition}:mgn:\${Region}:\${Account}:source-server/\${SourceServerID}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mgn/latest/ug/applications.html">ApplicationResource</a></td>
                    <td>arn:\${Partition}:mgn:\${Region}:\${Account}:application/\${ApplicationID}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mgn/latest/ug/waves.html">WaveResource</a></td>
                    <td>arn:\${Partition}:mgn:\${Region}:\${Account}:wave/\${WaveID}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mgn/latest/ug/imports.html">ImportResource</a></td>
                    <td>arn:\${Partition}:mgn:\${Region}:\${Account}:import/\${ImportID}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mgn/latest/ug/exports.html">ExportResource</a></td>
                    <td>arn:\${Partition}:mgn:\${Region}:\${Account}:export/\${ExportID}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mgn/latest/ug/connectors.html">ConnectorResource</a></td>
                    <td>arn:\${Partition}:mgn:\${Region}:\${Account}:connector/\${ConnectorID}</td>
                </tr>
            </tbody>
        </table>
        <h1>Alexa for Business</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_alexaforbusiness.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/a4b/latest/APIReference/API_Profile.html">profile</a></td>
                    <td>arn:\${Partition}:a4b:\${Region}:\${Account}:profile/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/a4b/latest/APIReference/API_Room.html">room</a></td>
                    <td>arn:\${Partition}:a4b:\${Region}:\${Account}:room/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/a4b/latest/APIReference/API_Device.html">device</a></td>
                    <td>arn:\${Partition}:a4b:\${Region}:\${Account}:device/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/a4b/latest/APIReference/API_SkillGroup.html">skillgroup</a></td>
                    <td>arn:\${Partition}:a4b:\${Region}:\${Account}:skill-group/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/a4b/latest/APIReference/API_UserData.html">user</a></td>
                    <td>arn:\${Partition}:a4b:\${Region}:\${Account}:user/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/a4b/latest/APIReference/API_AddressBook.html">addressbook</a></td>
                    <td>arn:\${Partition}:a4b:\${Region}:\${Account}:address-book/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/a4b/latest/APIReference/API_ConferenceProvider.html">conferenceprovider</a></td>
                    <td>arn:\${Partition}:a4b:\${Region}:\${Account}:conference-provider/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/a4b/latest/APIReference/API_Contact.html">contact</a></td>
                    <td>arn:\${Partition}:a4b:\${Region}:\${Account}:contact/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/a4b/latest/APIReference/API_BusinessReportSchedule.html">schedule</a></td>
                    <td>arn:\${Partition}:a4b:\${Region}:\${Account}:schedule/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/a4b/latest/APIReference/API_NetworkProfile.html">networkprofile</a></td>
                    <td>arn:\${Partition}:a4b:\${Region}:\${Account}:network-profile/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/a4b/latest/APIReference/API_Gateway.html">gateway</a></td>
                    <td>arn:\${Partition}:a4b:\${Region}:\${Account}:gateway/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/a4b/latest/APIReference/API_GatewayGroup.html">gatewaygroup</a></td>
                    <td>arn:\${Partition}:a4b:\${Region}:\${Account}:gateway-group/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Artifact</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsartifact.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html">report-package</a></td>
                    <td>arn:\${Partition}:artifact:::report-package/*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/artifact/latest/ug/managing-agreements.html">customer-agreement</a></td>
                    <td>arn:\${Partition}:artifact::\${Account}:customer-agreement/*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/artifact/latest/ug/managing-agreements.html">agreement</a></td>
                    <td>arn:\${Partition}:artifact:::agreement/*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html">report</a></td>
                    <td>arn:\${Partition}:artifact:\${Region}::report/\${ReportId}:\${Version}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Auto Scaling</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsautoscaling.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Application Transformation Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsapplicationtransformationservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS AppSync</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsappsync.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/appsync/latest/devguide/attaching-a-data-source.html">datasource</a></td>
                    <td>arn:\${Partition}:appsync:\${Region}:\${Account}:apis/\${GraphQLAPIId}/datasources/\${DatasourceName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appsync/latest/devguide/custom-domain-name.html">domain</a></td>
                    <td>arn:\${Partition}:appsync:\${Region}:\${Account}:domainnames/\${DomainName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appsync/latest/devguide/designing-a-graphql-api.html">graphqlapi</a></td>
                    <td>arn:\${Partition}:appsync:\${Region}:\${Account}:apis/\${GraphQLAPIId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appsync/latest/devguide/configuring-resolvers.html">field</a></td>
                    <td>arn:\${Partition}:appsync:\${Region}:\${Account}:apis/\${GraphQLAPIId}/types/\${TypeName}/fields/\${FieldName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appsync/latest/devguide/designing-your-schema.html#adding-a-root-query-type">type</a></td>
                    <td>arn:\${Partition}:appsync:\${Region}:\${Account}:apis/\${GraphQLAPIId}/types/\${TypeName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appsync/latest/devguide/pipeline-resolvers.html">function</a></td>
                    <td>arn:\${Partition}:appsync:\${Region}:\${Account}:apis/\${GraphQLAPIId}/functions/\${FunctionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appsync/latest/devguide/merged-api.html">sourceApiAssociation</a></td>
                    <td>arn:\${Partition}:appsync:\${Region}:\${Account}:apis/\${MergedGraphQLAPIId}/sourceApiAssociations/\${Associationid}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appsync/latest/devguide/merged-api.html">mergedApiAssociation</a></td>
                    <td>arn:\${Partition}:appsync:\${Region}:\${Account}:apis/\${SourceGraphQLAPIId}/mergedApiAssociations/\${Associationid}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS B2B Data Interchange</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsb2bdatainterchange.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/b2bi/latest/userguide/">profile</a></td>
                    <td>arn:\${Partition}:b2bi:\${Region}:\${Account}:profile/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/b2bi/latest/userguide/">capability</a></td>
                    <td>arn:\${Partition}:b2bi:\${Region}:\${Account}:capability/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/b2bi/latest/userguide/">partnership</a></td>
                    <td>arn:\${Partition}:b2bi:\${Region}:\${Account}:partnership/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/b2bi/latest/userguide/">transformer</a></td>
                    <td>arn:\${Partition}:b2bi:\${Region}:\${Account}:transformer/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Billing</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbilling.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Audit Manager</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsauditmanager.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/API_Assessment.html">assessment</a></td>
                    <td>arn:\${Partition}:auditmanager:\${Region}:\${Account}:assessment/\${AssessmentId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/API_AssessmentFramework.html">assessmentFramework</a></td>
                    <td>arn:\${Partition}:auditmanager:\${Region}:\${Account}:assessmentFramework/\${AssessmentFrameworkId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/API_AssessmentControlSet.html">assessmentControlSet</a></td>
                    <td>arn:\${Partition}:auditmanager:\${Region}:\${Account}:assessment/\${AssessmentId}/controlSet/\${ControlSetId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/API_Control.html">control</a></td>
                    <td>arn:\${Partition}:auditmanager:\${Region}:\${Account}:control/\${ControlId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Backup Gateway</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbackupgateway.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_Gateway.html">gateway</a></td>
                    <td>arn:\${Partition}:backup-gateway::\${Account}:gateway/\${GatewayId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_Hypervisor.html">hypervisor</a></td>
                    <td>arn:\${Partition}:backup-gateway::\${Account}:hypervisor/\${HypervisorId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_VirtualMachine.html">virtualmachine</a></td>
                    <td>arn:\${Partition}:backup-gateway::\${Account}:vm/\${VirtualmachineId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Athena</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonathena.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/athena/latest/ug/datacatalogs-example-policies.html">datacatalog</a></td>
                    <td>arn:\${Partition}:athena:\${Region}:\${Account}:datacatalog/\${DataCatalogName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/athena/latest/ug/example-policies-workgroup.html">workgroup</a></td>
                    <td>arn:\${Partition}:athena:\${Region}:\${Account}:workgroup/\${WorkGroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/athena/latest/ug/example-policies-capacity-reservations.html">capacity-reservation</a></td>
                    <td>arn:\${Partition}:athena:\${Region}:\${Account}:capacity-reservation/\${CapacityReservationName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Backup</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbackup.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/vaults.html">backupVault</a></td>
                    <td>arn:\${Partition}:backup:\${Region}:\${Account}:backup-vault:\${BackupVaultName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/about-backup-plans.html">backupPlan</a></td>
                    <td>arn:\${Partition}:backup:\${Region}:\${Account}:backup-plan:\${BackupPlanId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/recovery-points.html">recoveryPoint</a></td>
                    <td>arn:\${Partition}:\${Vendor}:\${Region}:*:\${ResourceType}:\${RecoveryPointId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/working-with-audit-frameworks.html">framework</a></td>
                    <td>arn:\${Partition}:backup:\${Region}:\${Account}:framework:\${FrameworkName}-\${FrameworkId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/create-report-plan-api.html">reportPlan</a></td>
                    <td>arn:\${Partition}:backup:\${Region}:\${Account}:report-plan:\${ReportPlanName}-\${ReportPlanId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/legalhold.html">legalHold</a></td>
                    <td>arn:\${Partition}:backup:\${Region}:\${Account}:legal-hold:\${LegalHoldId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing.html">restoreTestingPlan</a></td>
                    <td>arn:\${Partition}:backup:\${Region}:\${Account}:restore-testing-plan:\${RestoreTestingPlanName}-\${RestoreTestingPlanId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Backup storage</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbackupstorage.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon AppStream 2.0</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonappstream2.0.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html#what-is-concepts">fleet</a></td>
                    <td>arn:\${Partition}:appstream:\${Region}:\${Account}:fleet/\${FleetName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html#what-is-concepts">image</a></td>
                    <td>arn:\${Partition}:appstream:\${Region}:\${Account}:image/\${ImageName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html#what-is-concepts">image-builder</a></td>
                    <td>arn:\${Partition}:appstream:\${Region}:\${Account}:image-builder/\${ImageBuilderName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html#what-is-concepts">stack</a></td>
                    <td>arn:\${Partition}:appstream:\${Region}:\${Account}:stack/\${StackName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html#what-is-concepts">app-block</a></td>
                    <td>arn:\${Partition}:appstream:\${Region}:\${Account}:app-block/\${AppBlockName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html#what-is-concepts">application</a></td>
                    <td>arn:\${Partition}:appstream:\${Region}:\${Account}:application/\${ApplicationName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html#what-is-concepts">app-block-builder</a></td>
                    <td>arn:\${Partition}:appstream:\${Region}:\${Account}:app-block-builder/\${AppBlockBuilderName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Billing Conductor</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbillingconductor.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/billingconductor/latest/userguide/understanding-abc.html">billinggroup</a></td>
                    <td>arn:\${Partition}:billingconductor::\${Account}:billinggroup/\${BillingGroupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/billingconductor/latest/userguide/understanding-abc.html">pricingplan</a></td>
                    <td>arn:\${Partition}:billingconductor::\${Account}:pricingplan/\${PricingPlanId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/billingconductor/latest/userguide/understanding-abc.html">pricingrule</a></td>
                    <td>arn:\${Partition}:billingconductor::\${Account}:pricingrule/\${PricingRuleId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/billingconductor/latest/userguide/understanding-abc.html">customlineitem</a></td>
                    <td>arn:\${Partition}:billingconductor::\${Account}:customlineitem/\${CustomLineItemId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Braket</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbraket.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/braket/latest/developerguide/braket-manage-access.html#resources">quantum-task</a></td>
                    <td>arn:\${Partition}:braket:\${Region}:\${Account}:quantum-task/\${RandomId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/braket/latest/developerguide/braket-manage-access.html#resources">job</a></td>
                    <td>arn:\${Partition}:braket:\${Region}:\${Account}:job/\${JobName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Batch</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbatch.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html">compute-environment</a></td>
                    <td>arn:\${Partition}:batch:\${Region}:\${Account}:compute-environment/\${ComputeEnvironmentName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/batch/latest/userguide/job_queues.html">job-queue</a></td>
                    <td>arn:\${Partition}:batch:\${Region}:\${Account}:job-queue/\${JobQueueName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/batch/latest/userguide/job_definitions.html">job-definition</a></td>
                    <td>arn:\${Partition}:batch:\${Region}:\${Account}:job-definition/\${JobDefinitionName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/batch/latest/userguide/job_definitions.html">job-definition-revision</a></td>
                    <td>arn:\${Partition}:batch:\${Region}:\${Account}:job-definition/\${JobDefinitionName}:\${Revision}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/batch/latest/userguide/jobs.html">job</a></td>
                    <td>arn:\${Partition}:batch:\${Region}:\${Account}:job/\${JobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/batch/latest/userguide/scheduling-policies.html">scheduling-policy</a></td>
                    <td>arn:\${Partition}:batch:\${Region}:\${Account}:scheduling-policy/\${SchedulingPolicyName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Billing Console</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbillingconsole.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon Bedrock</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrock.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html">foundation-model</a></td>
                    <td>arn:\${Partition}:bedrock:\${Region}::foundation-model/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html">custom-model</a></td>
                    <td>arn:\${Partition}:bedrock:\${Region}:\${Account}:custom-model/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html">provisioned-model</a></td>
                    <td>arn:\${Partition}:bedrock:\${Region}:\${Account}:provisioned-model/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html">model-customization-job</a></td>
                    <td>arn:\${Partition}:bedrock:\${Region}:\${Account}:model-customization-job/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html">agent</a></td>
                    <td>arn:\${Partition}:bedrock:\${Region}:\${Account}:agent/\${AgentId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html">agent-alias</a></td>
                    <td>arn:\${Partition}:bedrock:\${Region}:\${Account}:agent-alias/\${AgentId}/\${AgentAliasId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html">knowledge-base</a></td>
                    <td>arn:\${Partition}:bedrock:\${Region}:\${Account}:knowledge-base/\${KnowledgeBaseId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html">model-evaluation-job</a></td>
                    <td>arn:\${Partition}:bedrock:\${Region}:\${Account}:model-evaluation-job/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html">evaluation-job</a></td>
                    <td>arn:\${Partition}:bedrock:\${Region}:\${Account}:evaluation-job/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html">model-invocation-job</a></td>
                    <td>arn:\${Partition}:bedrock:\${Region}:\${Account}:model-invocation-job/\${JobIdentifier}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html">guardrail</a></td>
                    <td>arn:\${Partition}:bedrock:\${Region}:\${Account}:guardrail/\${GuardrailId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Billing And Cost Management Data Exports</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbillingandcostmanagementdataexports.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Export.html">export</a></td>
                    <td>arn:\${Partition}:bcm-data-exports:\${Region}:\${Account}:export/\${Identifier}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Table.html">table</a></td>
                    <td>arn:\${Partition}:bcm-data-exports:\${Region}:\${Account}:table/\${Identifier}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Budget Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbudgetservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html">budget</a></td>
                    <td>arn:\${Partition}:budgets::\${Account}:budget/\${BudgetName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html">budgetAction</a></td>
                    <td>arn:\${Partition}:budgets::\${Account}:budget/\${BudgetName}/action/\${ActionId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS BugBust</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbugbust.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/event-managing.html">Event</a></td>
                    <td>arn:\${Partition}:bugbust:\${Region}:\${Account}:events/\${EventId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Certificate Manager</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscertificatemanager.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html#concept-acm-cert">certificate</a></td>
                    <td>arn:\${Partition}:acm:\${Region}:\${Account}:certificate/\${CertificateId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Chatbot</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awschatbot.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html">ChatbotConfiguration</a></td>
                    <td>arn:\${Partition}:chatbot::\${Account}:chat-configuration/\${ConfigurationType}/\${ChatbotConfigurationName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Clean Rooms ML</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscleanroomsml.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_TrainingDatasetSummary.html">trainingdataset</a></td>
                    <td>arn:\${Partition}:cleanrooms-ml:\${Region}:\${Account}:training-dataset/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_AudienceModelSummary.html">audiencemodel</a></td>
                    <td>arn:\${Partition}:cleanrooms-ml:\${Region}:\${Account}:audience-model/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ConfiguredAudienceModelSummary.html">configuredaudiencemodel</a></td>
                    <td>arn:\${Partition}:cleanrooms-ml:\${Region}:\${Account}:configured-audience-model/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_AudienceGenerationJobSummary.html">audiencegenerationjob</a></td>
                    <td>arn:\${Partition}:cleanrooms-ml:\${Region}:\${Account}:audience-generation-job/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Cloud Map</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscloudmap.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/cloud-map/latest/dg/API_Namespace.html">namespace</a></td>
                    <td>arn:\${Partition}:servicediscovery:\${Region}:\${Account}:namespace/\${NamespaceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/cloud-map/latest/dg/API_Service.html">service</a></td>
                    <td>arn:\${Partition}:servicediscovery:\${Region}:\${Account}:service/\${ServiceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Clean Rooms</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscleanrooms.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam.html">analysistemplate</a></td>
                    <td>arn:\${Partition}:cleanrooms:\${Region}:\${Account}:membership/\${MembershipId}/analysistemplate/\${AnalysisTemplateId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam.html">collaboration</a></td>
                    <td>arn:\${Partition}:cleanrooms:\${Region}:\${Account}:collaboration/\${CollaborationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam.html">configuredaudiencemodelassociation</a></td>
                    <td>arn:\${Partition}:cleanrooms:\${Region}:\${Account}:membership/\${MembershipId}/configuredaudiencemodelassociation/\${ConfiguredAudienceModelAssociationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam.html">configuredtable</a></td>
                    <td>arn:\${Partition}:cleanrooms:\${Region}:\${Account}:configuredtable/\${ConfiguredTableId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam.html">configuredtableassociation</a></td>
                    <td>arn:\${Partition}:cleanrooms:\${Region}:\${Account}:membership/\${MembershipId}/configuredtableassociation/\${ConfiguredTableAssociationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam.html">membership</a></td>
                    <td>arn:\${Partition}:cleanrooms:\${Region}:\${Account}:membership/\${MembershipId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam.html">privacybudgettemplate</a></td>
                    <td>arn:\${Partition}:cleanrooms:\${Region}:\${Account}:membership/\${MembershipId}/privacybudgettemplate/\${PrivacyBudgetTemplateId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Cloud Control API</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscloudcontrolapi.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon CloudFront KeyValueStore</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudfrontkeyvaluestore.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/kvs-with-functions.html">key-value-store</a></td>
                    <td>arn:\${Partition}:cloudfront::\${Account}:key-value-store/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Cloud Directory</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonclouddirectory.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/directoryservice/latest/admin-guide/cd_key_concepts.html#whatisdirectory">appliedSchema</a></td>
                    <td>arn:\${Partition}:clouddirectory:\${Region}:\${Account}:directory/\${DirectoryId}/schema/\${SchemaName}/\${Version}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/directoryservice/latest/admin-guide/cd_key_concepts.html#whatisdirectory">developmentSchema</a></td>
                    <td>arn:\${Partition}:clouddirectory:\${Region}:\${Account}:schema/development/\${SchemaName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/directoryservice/latest/admin-guide/cd_key_concepts.html#whatisdirectory">directory</a></td>
                    <td>arn:\${Partition}:clouddirectory:\${Region}:\${Account}:directory/\${DirectoryId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/directoryservice/latest/admin-guide/cd_key_concepts.html#whatisdirectory">publishedSchema</a></td>
                    <td>arn:\${Partition}:clouddirectory:\${Region}:\${Account}:schema/published/\${SchemaName}/\${Version}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS CloudHSM</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscloudhsm.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/backups.html">backup</a></td>
                    <td>arn:\${Partition}:cloudhsm:\${Region}:\${Account}:backup/\${CloudHsmBackupInstanceName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/clusters.html">cluster</a></td>
                    <td>arn:\${Partition}:cloudhsm:\${Region}:\${Account}:cluster/\${CloudHsmClusterInstanceName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS CloudTrail Data</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscloudtraildata.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/how-cloudtrail-works.html#how-cloudtrail-works-channels">channel</a></td>
                    <td>arn:\${Partition}:cloudtrail:\${Region}:\${Account}:channel/\${ChannelId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon CloudFront</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudfront.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-working-with.html">distribution</a></td>
                    <td>arn:\${Partition}:cloudfront::\${Account}:distribution/\${DistributionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-working-with.html">streaming-distribution</a></td>
                    <td>arn:\${Partition}:cloudfront::\${Account}:streaming-distribution/\${DistributionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html#private-content-restricting-access-to-s3-overview">origin-access-identity</a></td>
                    <td>arn:\${Partition}:cloudfront::\${Account}:origin-access-identity/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html">field-level-encryption-config</a></td>
                    <td>arn:\${Partition}:cloudfront::\${Account}:field-level-encryption-config/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html">field-level-encryption-profile</a></td>
                    <td>arn:\${Partition}:cloudfront::\${Account}:field-level-encryption-profile/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/working-with-policies.html">cache-policy</a></td>
                    <td>arn:\${Partition}:cloudfront::\${Account}:cache-policy/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/working-with-policies.html">origin-request-policy</a></td>
                    <td>arn:\${Partition}:cloudfront::\${Account}:origin-request-policy/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html">realtime-log-config</a></td>
                    <td>arn:\${Partition}:cloudfront::\${Account}:realtime-log-config/\${Name}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.html">function</a></td>
                    <td>arn:\${Partition}:cloudfront::\${Account}:function/\${Name}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/kvs-with-functions.html">key-value-store</a></td>
                    <td>arn:\${Partition}:cloudfront::\${Account}:key-value-store/\${Name}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/working-with-policies.html">response-headers-policy</a></td>
                    <td>arn:\${Partition}:cloudfront::\${Account}:response-headers-policy/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/working-with-policies.html">origin-access-control</a></td>
                    <td>arn:\${Partition}:cloudfront::\${Account}:origin-access-control/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/working-with-policies.html">continuous-deployment-policy</a></td>
                    <td>arn:\${Partition}:cloudfront::\${Account}:continuous-deployment-policy/\${Id}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Cloud9</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscloud9.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awscloud9.html##awscloud9-environment">environment</a></td>
                    <td>arn:\${Partition}:cloud9:\${Region}:\${Account}:environment:\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon CloudSearch</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudsearch.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/cloudsearch/latest/developerguide/creating-domains.html">domain</a></td>
                    <td>arn:\${Partition}:cloudsearch:\${Region}:\${Account}:domain/\${DomainName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Chime</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonchime.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/chime/latest/APIReference/API_Meeting.html">meeting</a></td>
                    <td>arn:\${Partition}:chime::\${AccountId}:meeting/\${MeetingId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_AppInstance.html">app-instance</a></td>
                    <td>arn:\${Partition}:chime:\${Region}:\${AccountId}:app-instance/\${AppInstanceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_AppInstanceUser.html">app-instance-user</a></td>
                    <td>arn:\${Partition}:chime:\${Region}:\${AccountId}:app-instance/\${AppInstanceId}/user/\${AppInstanceUserId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_AppInstanceBot.html">app-instance-bot</a></td>
                    <td>arn:\${Partition}:chime:\${Region}:\${AccountId}:app-instance/\${AppInstanceId}/bot/\${AppInstanceBotId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_Channel.html">channel</a></td>
                    <td>arn:\${Partition}:chime:\${Region}:\${AccountId}:app-instance/\${AppInstanceId}/channel/\${ChannelId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelFlow.html">channel-flow</a></td>
                    <td>arn:\${Partition}:chime:\${Region}:\${AccountId}:app-instance/\${AppInstanceId}/channel-flow/\${ChannelFlowId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaPipeline.html">media-pipeline</a></td>
                    <td>arn:\${Partition}:chime:\${Region}:\${AccountId}:media-pipeline/\${MediaPipelineId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaInsightsPipelineConfiguration.html">media-insights-pipeline-configuration</a></td>
                    <td>arn:\${Partition}:chime:\${Region}:\${AccountId}:media-insights-pipeline-configuration/\${ConfigurationName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_KinesisVideoStreamPoolConfiguration.html">media-pipeline-kinesis-video-stream-pool</a></td>
                    <td>arn:\${Partition}:chime:\${Region}:\${AccountId}:media-pipeline-kinesis-video-stream-pool/\${PoolName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceProfileDomain.html">voice-profile-domain</a></td>
                    <td>arn:\${Partition}:chime:\${Region}:\${AccountId}:voice-profile-domain/\${VoiceProfileDomainId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceProfile.html">voice-profile</a></td>
                    <td>arn:\${Partition}:chime:\${Region}:\${AccountId}:voice-profile/\${VoiceProfileId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_VoiceConnector.html">voice-connector</a></td>
                    <td>arn:\${Partition}:chime:\${Region}:\${AccountId}:vc/\${VoiceConnectorId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_SipMediaApplication.html">sip-media-application</a></td>
                    <td>arn:\${Partition}:chime:\${Region}:\${AccountId}:sma/\${SipMediaApplicationId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS CloudFormation</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscloudformation.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html#w2ab1b5c15c11">changeset</a></td>
                    <td>arn:\${Partition}:cloudformation:\${Region}:\${Account}:changeSet/\${ChangeSetName}/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html#w2ab1b5c15b9">stack</a></td>
                    <td>arn:\${Partition}:cloudformation:\${Region}:\${Account}:stack/\${StackName}/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stacksets-concepts-stackset">stackset</a></td>
                    <td>arn:\${Partition}:cloudformation:\${Region}:\${Account}:stackset/\${StackSetName}:\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html">stackset-target</a></td>
                    <td>arn:\${Partition}:cloudformation:\${Region}:\${Account}:stackset-target/\${StackSetTarget}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html">type</a></td>
                    <td>arn:\${Partition}:cloudformation:\${Region}:\${Account}:type/resource/\${Type}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/generate-IaC.html">generatedtemplate</a></td>
                    <td>arn:\${Partition}:cloudformation:\${Region}:\${Account}:generatedTemplate/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/generate-IaC.html">resourcescan</a></td>
                    <td>arn:\${Partition}:cloudformation:\${Region}:\${Account}:resourceScan/\${Id}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS CloudShell</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscloudshell.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/cloudshell/latest/userguide/sec-auth-with-identities.html#Environment">Environment</a></td>
                    <td>arn:\${Partition}:cloudshell:\${Region}:\${Account}:environment/\${EnvironmentId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon CloudWatch Application Insights</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudwatchapplicationinsights.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon CloudWatch</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudwatch.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html">alarm</a></td>
                    <td>arn:\${Partition}:cloudwatch:\${Region}:\${Account}:alarm:\${AlarmName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html">dashboard</a></td>
                    <td>arn:\${Partition}:cloudwatch::\${Account}:dashboard/\${DashboardName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html">insight-rule</a></td>
                    <td>arn:\${Partition}:cloudwatch:\${Region}:\${Account}:insight-rule/\${InsightRuleName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html">metric-stream</a></td>
                    <td>arn:\${Partition}:cloudwatch:\${Region}:\${Account}:metric-stream/\${MetricStreamName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html">slo</a></td>
                    <td>arn:\${Partition}:cloudwatch:\${Region}:\${Account}:slo/\${SloName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html">service</a></td>
                    <td>arn:\${Partition}:cloudwatch:\${Region}:\${Account}:service/\${ServiceName}-\${UniqueAttributesHex}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS CloudTrail</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscloudtrail.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/how-cloudtrail-works.html#how-cloudtrail-works-trails">trail</a></td>
                    <td>arn:\${Partition}:cloudtrail:\${Region}:\${Account}:trail/\${TrailName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/how-cloudtrail-works.html#how-cloudtrail-works-lake">eventdatastore</a></td>
                    <td>arn:\${Partition}:cloudtrail:\${Region}:\${Account}:eventdatastore/\${EventDataStoreId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/how-cloudtrail-works.html#how-cloudtrail-works-channels">channel</a></td>
                    <td>arn:\${Partition}:cloudtrail:\${Region}:\${Account}:channel/\${ChannelId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon CloudWatch Evidently</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudwatchevidently.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_Project.html">Project</a></td>
                    <td>arn:\${Partition}:evidently:\${Region}:\${Account}:project/\${ProjectName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_Feature.html">Feature</a></td>
                    <td>arn:\${Partition}:evidently:\${Region}:\${Account}:project/\${ProjectName}/feature/\${FeatureName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_Experiment.html">Experiment</a></td>
                    <td>arn:\${Partition}:evidently:\${Region}:\${Account}:project/\${ProjectName}/experiment/\${ExperimentName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_Launch.html">Launch</a></td>
                    <td>arn:\${Partition}:evidently:\${Region}:\${Account}:project/\${ProjectName}/launch/\${LaunchName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_Segment.html">Segment</a></td>
                    <td>arn:\${Partition}:evidently:\${Region}:\${Account}:segment/\${SegmentName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon CloudWatch Network Monitor</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudwatchnetworkmonitor.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NM-components.html">monitor</a></td>
                    <td>arn:\${Partition}:networkmonitor:\${Region}:\${Account}:monitor/\${MonitorName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NM-components.html">probe</a></td>
                    <td>arn:\${Partition}:networkmonitor:\${Region}:\${Account}:probe/\${ProbeId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon CloudWatch Observability Access Manager</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudwatchobservabilityaccessmanager.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html">Link</a></td>
                    <td>arn:\${Partition}:oam:\${Region}:\${Account}:link/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html">Sink</a></td>
                    <td>arn:\${Partition}:oam:\${Region}:\${Account}:sink/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon CloudWatch Internet Monitor</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudwatchinternetmonitor.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-components.html">HealthEvent</a></td>
                    <td>arn:\${Partition}:internetmonitor:\${Region}:\${Account}:monitor/\${MonitorName}/health-event/\${EventId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-components.html">Monitor</a></td>
                    <td>arn:\${Partition}:internetmonitor:\${Region}:\${Account}:monitor/\${MonitorName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-components.html">InternetEvent</a></td>
                    <td>arn:\${Partition}:internetmonitor::\${Account}:internet-event/\${InternetEventId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon CloudWatch Synthetics</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudwatchsynthetics.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html">canary</a></td>
                    <td>arn:\${Partition}:synthetics:\${Region}:\${Account}:canary:\${CanaryName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Groups.html">group</a></td>
                    <td>arn:\${Partition}:synthetics:\${Region}:\${Account}:group:\${GroupId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS CloudWatch RUM</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscloudwatchrum.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_AppMonitor.html">AppMonitorResource</a></td>
                    <td>arn:\${Partition}:rum:\${Region}:\${Account}:appmonitor/\${Name}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS CodeDeploy</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscodedeploy.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/auth-and-access-control-permissions-reference.html">application</a></td>
                    <td>arn:\${Partition}:codedeploy:\${Region}:\${Account}:application:\${ApplicationName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/auth-and-access-control-permissions-reference.html">deploymentconfig</a></td>
                    <td>arn:\${Partition}:codedeploy:\${Region}:\${Account}:deploymentconfig:\${DeploymentConfigurationName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/auth-and-access-control-permissions-reference.html">deploymentgroup</a></td>
                    <td>arn:\${Partition}:codedeploy:\${Region}:\${Account}:deploymentgroup:\${ApplicationName}/\${DeploymentGroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/auth-and-access-control-permissions-reference.html">instance</a></td>
                    <td>arn:\${Partition}:codedeploy:\${Region}:\${Account}:instance:\${InstanceName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon CodeCatalyst</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncodecatalyst.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/codecatalyst/latest/userguide/#">connections</a></td>
                    <td>arn:\${Partition}:codecatalyst:\${Region}:\${Account}:/connections/\${ConnectionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/codecatalyst/latest/userguide/#">identity-center-applications</a></td>
                    <td>arn:\${Partition}:codecatalyst:\${Region}:\${Account}:/identity-center-applications/\${IdentityCenterApplicationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/codecatalyst/latest/userguide/#">space</a></td>
                    <td>arn:\${Partition}:codecatalyst:::space/\${SpaceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/codecatalyst/latest/userguide/#">project</a></td>
                    <td>arn:\${Partition}:codecatalyst:::space/\${SpaceId}/project/\${ProjectId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS CodeArtifact</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscodeartifact.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/codeartifact/latest/ug/domains.html">domain</a></td>
                    <td>arn:\${Partition}:codeartifact:\${Region}:\${Account}:domain/\${DomainName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/codeartifact/latest/ug/repos.html">repository</a></td>
                    <td>arn:\${Partition}:codeartifact:\${Region}:\${Account}:repository/\${DomainName}/\${RepositoryName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/codeartifact/latest/ug/package-groups.html">package-group</a></td>
                    <td>arn:\${Partition}:codeartifact:\${Region}:\${Account}:package-group/\${DomainName}\${EncodedPackageGroupPattern}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/codeartifact/latest/ug/packages.html">package</a></td>
                    <td>arn:\${Partition}:codeartifact:\${Region}:\${Account}:package/\${DomainName}/\${RepositoryName}/\${PackageFormat}/\${PackageNamespace}/\${PackageName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon CodeGuru</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncodeguru.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon CloudWatch Logs</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudwatchlogs.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_LogGroup.html">log-group</a></td>
                    <td>arn:\${Partition}:logs:\${Region}:\${Account}:log-group:\${LogGroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_LogStream.html">log-stream</a></td>
                    <td>arn:\${Partition}:logs:\${Region}:\${Account}:log-group:\${LogGroupName}:log-stream:\${LogStreamName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_Destination.html">destination</a></td>
                    <td>arn:\${Partition}:logs:\${Region}:\${Account}:destination:\${DestinationName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeliverySource.html">delivery-source</a></td>
                    <td>arn:\${Partition}:logs:\${Region}:\${Account}:delivery-source:\${DeliverySourceName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_Delivery.html">delivery</a></td>
                    <td>arn:\${Partition}:logs:\${Region}:\${Account}:delivery:\${DeliveryName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeliveryDestination.html">delivery-destination</a></td>
                    <td>arn:\${Partition}:logs:\${Region}:\${Account}:delivery-destination:\${DeliveryDestinationName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_AnomalyDetector.html">anomaly-detector</a></td>
                    <td>arn:\${Partition}:logs:\${Region}:\${Account}:anomaly-detector:\${DetectorId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS CodeCommit</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscodecommit.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control.html#arn-formats">repository</a></td>
                    <td>arn:\${Partition}:codecommit:\${Region}:\${Account}:\${RepositoryName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS CodeConnections</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscodeconnections.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/dtconsole/latest/userguide/connections.html">Connection</a></td>
                    <td>arn:\${Partition}:codeconnections:\${Region}:\${Account}:connection/\${ConnectionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-hosts.html">Host</a></td>
                    <td>arn:\${Partition}:codeconnections:\${Region}:\${Account}:host/\${HostId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/dtconsole/latest/userguide/repositorylinks.html">RepositoryLink</a></td>
                    <td>arn:\${Partition}:codeconnections:\${Region}:\${Account}:repository-link/\${RepositoryLinkId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS CodeDeploy secure host commands service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscodedeploysecurehostcommandsservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon CodeGuru Security</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncodegurusecurity.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/codeguru/latest/security-ug/working-with-code-scans.html">ScanName</a></td>
                    <td>arn:\${Partition}:codeguru-security:\${Region}:\${Account}:scans/\${ScanName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon CodeGuru Reviewer</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncodegurureviewer.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/working-with-repositories.html">association</a></td>
                    <td>arn:\${Partition}:codeguru-reviewer:\${Region}:\${Account}:association:\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/code-reviews.html">codereview</a></td>
                    <td>arn:\${Partition}:codeguru-reviewer:\${Region}:\${Account}:association:\${ResourceId}:codereview:\${CodeReviewId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS CodePipeline</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscodepipeline.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/iam-access-control-identity-based.html#ACP_ARN_Format">action</a></td>
                    <td>arn:\${Partition}:codepipeline:\${Region}:\${Account}:\${PipelineName}/\${StageName}/\${ActionName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/iam-access-control-identity-based.html#ACP_ARN_Format">actiontype</a></td>
                    <td>arn:\${Partition}:codepipeline:\${Region}:\${Account}:actiontype:\${Owner}/\${Category}/\${Provider}/\${Version}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/iam-access-control-identity-based.html#ACP_ARN_Format">pipeline</a></td>
                    <td>arn:\${Partition}:codepipeline:\${Region}:\${Account}:\${PipelineName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/iam-access-control-identity-based.html#ACP_ARN_Format">stage</a></td>
                    <td>arn:\${Partition}:codepipeline:\${Region}:\${Account}:\${PipelineName}/\${StageName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/iam-access-control-identity-based.html#ACP_ARN_Format">webhook</a></td>
                    <td>arn:\${Partition}:codepipeline:\${Region}:\${Account}:webhook:\${WebhookName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS CodeStar Notifications</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscodestarnotifications.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/codestar-notifications/latest/userguide/security_iam_service-with-iam.html">notificationrule</a></td>
                    <td>arn:\${Partition}:codestar-notifications:\${Region}:\${Account}:notificationrule/\${NotificationRuleId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon CodeWhisperer</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncodewhisperer.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/codewhisperer/latest/userguide/as-whisper-admin.html#about-profiles">profile</a></td>
                    <td>arn:\${Partition}:codewhisperer::\${Account}:profile/\${Identifier}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/codewhisperer/latest/userguide/as-whisper-admin.html#about-customizations">customization</a></td>
                    <td>arn:\${Partition}:codewhisperer::\${Account}:customization/\${Identifier}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS CodeBuild</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscodebuild.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats">build</a></td>
                    <td>arn:\${Partition}:codebuild:\${Region}:\${Account}:build/\${BuildId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats">build-batch</a></td>
                    <td>arn:\${Partition}:codebuild:\${Region}:\${Account}:build-batch/\${BuildBatchId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats">project</a></td>
                    <td>arn:\${Partition}:codebuild:\${Region}:\${Account}:project/\${ProjectName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats">report-group</a></td>
                    <td>arn:\${Partition}:codebuild:\${Region}:\${Account}:report-group/\${ReportGroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats">report</a></td>
                    <td>arn:\${Partition}:codebuild:\${Region}:\${Account}:report/\${ReportGroupName}:\${ReportId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats">fleet</a></td>
                    <td>arn:\${Partition}:codebuild:\${Region}:\${Account}:fleet/\${FleetName}:\${FleetId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS CodeStar</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscodestar.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/codestar/latest/userguide/working-with-projects.html">project</a></td>
                    <td>arn:\${Partition}:codestar:\${Region}:\${Account}:project/\${ProjectId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/codestar/latest/userguide/working-with-user-info.html">user</a></td>
                    <td>arn:\${Partition}:iam::\${Account}:user/\${AwsUserName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon CodeGuru Profiler</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncodeguruprofiler.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-profiling-groups.html">ProfilingGroup</a></td>
                    <td>arn:\${Partition}:codeguru-profiler:\${Region}:\${Account}:profilingGroup/\${ProfilingGroupName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Cognito Sync</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncognitosync.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/cognito/latest/developerguide/synchronizing-data.html#understanding-datasets">dataset</a></td>
                    <td>arn:\${Partition}:cognito-sync:\${Region}:\${Account}:identitypool/\${IdentityPoolId}/identity/\${IdentityId}/dataset/\${DatasetName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html#authenticated-and-unauthenticated-identities">identity</a></td>
                    <td>arn:\${Partition}:cognito-sync:\${Region}:\${Account}:identitypool/\${IdentityPoolId}/identity/\${IdentityId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html">identitypool</a></td>
                    <td>arn:\${Partition}:cognito-sync:\${Region}:\${Account}:identitypool/\${IdentityPoolId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Cognito Identity</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncognitoidentity.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html">identitypool</a></td>
                    <td>arn:\${Partition}:cognito-identity:\${Region}:\${Account}:identitypool/\${IdentityPoolId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS CodeStar Connections</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscodestarconnections.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/dtconsole/latest/userguide/connections.html">Connection</a></td>
                    <td>arn:\${Partition}:codestar-connections:\${Region}:\${Account}:connection/\${ConnectionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-hosts.html">Host</a></td>
                    <td>arn:\${Partition}:codestar-connections:\${Region}:\${Account}:host/\${HostId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/dtconsole/latest/userguide/repositorylinks.html">RepositoryLink</a></td>
                    <td>arn:\${Partition}:codestar-connections:\${Region}:\${Account}:repository-link/\${RepositoryLinkId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Cognito User Pools</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncognitouserpools.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html">userpool</a></td>
                    <td>arn:\${Partition}:cognito-idp:\${Region}:\${Account}:userpool/\${UserPoolId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-waf.html">webacl</a></td>
                    <td>arn:\${Partition}:wafv2:\${Region}:\${Account}:\${Scope}/webacl/\${Name}/\${Id}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Comprehend Medical</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncomprehendmedical.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon Comprehend</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncomprehend.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartTargetedSentimentDetectionJob.html">targeted-sentiment-detection-job</a></td>
                    <td>arn:\${Partition}:comprehend:\${Region}:\${Account}:targeted-sentiment-detection-job/\${JobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/comprehend/latest/dg/how-document-classification-training.html">document-classifier</a></td>
                    <td>arn:\${Partition}:comprehend:\${Region}:\${Account}:document-classifier/\${DocumentClassifierName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html">document-classifier-endpoint</a></td>
                    <td>arn:\${Partition}:comprehend:\${Region}:\${Account}:document-classifier-endpoint/\${DocumentClassifierEndpointName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/comprehend/latest/dg/training-recognizers.html">entity-recognizer</a></td>
                    <td>arn:\${Partition}:comprehend:\${Region}:\${Account}:entity-recognizer/\${EntityRecognizerName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html">entity-recognizer-endpoint</a></td>
                    <td>arn:\${Partition}:comprehend:\${Region}:\${Account}:entity-recognizer-endpoint/\${EntityRecognizerEndpointName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartDominantLanguageDetectionJob.html">dominant-language-detection-job</a></td>
                    <td>arn:\${Partition}:comprehend:\${Region}:\${Account}:dominant-language-detection-job/\${JobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartEntitiesDetectionJob.html">entities-detection-job</a></td>
                    <td>arn:\${Partition}:comprehend:\${Region}:\${Account}:entities-detection-job/\${JobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartPiiEntitiesDetectionJob.html">pii-entities-detection-job</a></td>
                    <td>arn:\${Partition}:comprehend:\${Region}:\${Account}:pii-entities-detection-job/\${JobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartEventsDetectionJob.html">events-detection-job</a></td>
                    <td>arn:\${Partition}:comprehend:\${Region}:\${Account}:events-detection-job/\${JobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartKeyPhrasesDetectionJob.html">key-phrases-detection-job</a></td>
                    <td>arn:\${Partition}:comprehend:\${Region}:\${Account}:key-phrases-detection-job/\${JobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartSentimentDetectionJob.html">sentiment-detection-job</a></td>
                    <td>arn:\${Partition}:comprehend:\${Region}:\${Account}:sentiment-detection-job/\${JobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartTopicsDetectionJob.html">topics-detection-job</a></td>
                    <td>arn:\${Partition}:comprehend:\${Region}:\${Account}:topics-detection-job/\${JobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartDocumentClassificationJob.html">document-classification-job</a></td>
                    <td>arn:\${Partition}:comprehend:\${Region}:\${Account}:document-classification-job/\${JobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/comprehend/latest/APIReference/API_CreateFlywheel.html">flywheel</a></td>
                    <td>arn:\${Partition}:comprehend:\${Region}:\${Account}:flywheel/\${FlywheelName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/comprehend/latest/APIReference/API_CreateDataset.html">flywheel-dataset</a></td>
                    <td>arn:\${Partition}:comprehend:\${Region}:\${Account}:flywheel/\${FlywheelName}/dataset/\${DatasetName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Compute Optimizer</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscomputeoptimizer.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Config</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsconfig.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AggregationAuthorization.html">AggregationAuthorization</a></td>
                    <td>arn:\${Partition}:config:\${Region}:\${Account}:aggregation-authorization/\${AggregatorAccount}/\${AggregatorRegion}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigurationAggregator.html">ConfigurationAggregator</a></td>
                    <td>arn:\${Partition}:config:\${Region}:\${Account}:config-aggregator/\${AggregatorId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigRule.html">ConfigRule</a></td>
                    <td>arn:\${Partition}:config:\${Region}:\${Account}:config-rule/\${ConfigRuleId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/config/latest/APIReference/API_ConformancePackDetail.html">ConformancePack</a></td>
                    <td>arn:\${Partition}:config:\${Region}:\${Account}:conformance-pack/\${ConformancePackName}/\${ConformancePackId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/config/latest/APIReference/API_OrganizationConfigRule.html">OrganizationConfigRule</a></td>
                    <td>arn:\${Partition}:config:\${Region}:\${Account}:organization-config-rule/\${OrganizationConfigRuleId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/config/latest/APIReference/API_OrganizationConformancePack.html">OrganizationConformancePack</a></td>
                    <td>arn:\${Partition}:config:\${Region}:\${Account}:organization-conformance-pack/\${OrganizationConformancePackId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/config/latest/APIReference/API_RemediationConfiguration.html">RemediationConfiguration</a></td>
                    <td>arn:\${Partition}:config:\${Region}:\${Account}:remediation-configuration/\${RemediationConfigurationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/config/latest/APIReference/API_StoredQuery.html">StoredQuery</a></td>
                    <td>arn:\${Partition}:config:\${Region}:\${Account}:stored-query/\${StoredQueryName}/\${StoredQueryId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Consolidated Billing</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsconsolidatedbilling.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Connector Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsconnectorservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Cost and Usage Report</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscostandusagereport.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html">cur</a></td>
                    <td>arn:\${Partition}:cur:\${Region}:\${Account}:definition/\${ReportName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Connect Voice ID</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonconnectvoiceid.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/enable-voiceid.html#voiceid-domain">domain</a></td>
                    <td>arn:\${Partition}:voiceid:\${Region}:\${Account}:domain/\${DomainId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Management Console Mobile App</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsconsolemobileapp.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/consolemobileapp/latest/userguide/permissions-policies.html">DeviceIdentity</a></td>
                    <td>arn:\${Partition}:consoleapp::\${Account}:device/\${DeviceId}/identity/\${IdentityId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Control Catalog</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscontrolcatalog.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_CommonControlSummary.html">common-control</a></td>
                    <td>arn:\${Partition}:controlcatalog:::common-control/\${CommonControlId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_DomainSummary.html">domain</a></td>
                    <td>arn:\${Partition}:controlcatalog:::domain/\${DomainId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ObjectiveSummary.html">objective</a></td>
                    <td>arn:\${Partition}:controlcatalog:::objective/\${ObjectiveId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Connect Customer Profiles</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonconnectcustomerprofiles.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/customerprofiles/latest/APIReference/">domains</a></td>
                    <td>arn:\${Partition}:profile:\${Region}:\${Account}:domains/\${DomainName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/customerprofiles/latest/APIReference/">object-types</a></td>
                    <td>arn:\${Partition}:profile:\${Region}:\${Account}:domains/\${DomainName}/object-types/\${ObjectTypeName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/customerprofiles/latest/APIReference/">integrations</a></td>
                    <td>arn:\${Partition}:profile:\${Region}:\${Account}:domains/\${DomainName}/integrations/\${Uri}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/customerprofiles/latest/APIReference/">event-streams</a></td>
                    <td>arn:\${Partition}:profile:\${Region}:\${Account}:domains/\${DomainName}/event-streams/\${EventStreamName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/customerprofiles/latest/APIReference/">calculated-attributes</a></td>
                    <td>arn:\${Partition}:profile:\${Region}:\${Account}:domains/\${DomainName}/calculated-attributes/\${CalculatedAttributeName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Connect Cases</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonconnectcases.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/cases.html">Case</a></td>
                    <td>arn:\${Partition}:cases:\${Region}:\${Account}:domain/\${DomainId}/case/\${CaseId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/cases.html">Domain</a></td>
                    <td>arn:\${Partition}:cases:\${Region}:\${Account}:domain/\${DomainId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-fields.html">Field</a></td>
                    <td>arn:\${Partition}:cases:\${Region}:\${Account}:domain/\${DomainId}/field/\${FieldId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-layouts.html">Layout</a></td>
                    <td>arn:\${Partition}:cases:\${Region}:\${Account}:domain/\${DomainId}/layout/\${LayoutId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/associatecontactandcase.html">RelatedItem</a></td>
                    <td>arn:\${Partition}:cases:\${Region}:\${Account}:domain/\${DomainId}/case/\${CaseId}/related-item/\${RelatedItemId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-templates.html">Template</a></td>
                    <td>arn:\${Partition}:cases:\${Region}:\${Account}:domain/\${DomainId}/template/\${TemplateId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Control Tower</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscontroltower.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnableControl.html">EnabledControl</a></td>
                    <td>arn:\${Partition}:controltower:\${Region}:\${Account}:enabledcontrol/\${EnabledControlId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetBaseline.html">Baseline</a></td>
                    <td>arn:\${Partition}:controltower:\${Region}::baseline/\${BaselineId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnableBaseline.html">EnabledBaseline</a></td>
                    <td>arn:\${Partition}:controltower:\${Region}:\${Account}:enabledbaseline/\${EnabledBaselineId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/controltower/latest/APIReference/API_CreateLandingZone.html">LandingZone</a></td>
                    <td>arn:\${Partition}:controltower:\${Region}:\${Account}:landingzone/\${LandingZoneId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Customer Verification Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscustomerverificationservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Data Pipeline</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatapipeline.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatapipeline.html">pipeline</a></td>
                    <td>arn:\${Partition}:datapipeline:\${Region}:\${Account}:pipeline/\${PipelineId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Cost Explorer Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscostexplorerservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalySubscription.html">anomalysubscription</a></td>
                    <td>arn:\${Partition}:ce::\${Account}:anomalysubscription/\${Identifier}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalyMonitor.html">anomalymonitor</a></td>
                    <td>arn:\${Partition}:ce::\${Account}:anomalymonitor/\${Identifier}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategory.html">costcategory</a></td>
                    <td>arn:\${Partition}:ce::\${Account}:costcategory/\${Identifier}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Cost Optimization Hub</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscostoptimizationhub.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Database Query Metadata Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_databasequerymetadataservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Data Exchange</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdataexchange.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/data-exchange/latest/userguide/jobs.html">jobs</a></td>
                    <td>arn:\${Partition}:dataexchange:\${Region}:\${Account}:jobs/\${JobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/data-exchange/latest/userguide/data-sets.html">data-sets</a></td>
                    <td>arn:\${Partition}:dataexchange:\${Region}:\${Account}:data-sets/\${DataSetId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/data-exchange/latest/userguide/data-sets.html">entitled-data-sets</a></td>
                    <td>arn:\${Partition}:dataexchange:\${Region}::data-sets/\${DataSetId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/data-exchange/latest/userguide/data-sets.html#revisions">revisions</a></td>
                    <td>arn:\${Partition}:dataexchange:\${Region}:\${Account}:data-sets/\${DataSetId}/revisions/\${RevisionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/data-exchange/latest/userguide/data-sets.html#revisions">entitled-revisions</a></td>
                    <td>arn:\${Partition}:dataexchange:\${Region}::data-sets/\${DataSetId}/revisions/\${RevisionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/data-exchange/latest/userguide/data-sets.html#assets">assets</a></td>
                    <td>arn:\${Partition}:dataexchange:\${Region}:\${Account}:data-sets/\${DataSetId}/revisions/\${RevisionId}/assets/\${AssetId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/data-exchange/latest/userguide/data-sets.html#assets">entitled-assets</a></td>
                    <td>arn:\${Partition}:dataexchange:\${Region}::data-sets/\${DataSetId}/revisions/\${RevisionId}/assets/\${AssetId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/data-exchange/latest/userguide/data-sets.html">event-actions</a></td>
                    <td>arn:\${Partition}:dataexchange:\${Region}:\${Account}:event-actions/\${EventActionId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS DeepLens</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdeeplens.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="device">device</a></td>
                    <td>arn:\${Partition}:deeplens:\${Region}:\${Account}:device/\${DeviceName}</td>
                </tr>
               <tr>
                    <td><a href="project">project</a></td>
                    <td>arn:\${Partition}:deeplens:\${Region}:\${Account}:project/\${ProjectName}</td>
                </tr>
               <tr>
                    <td><a href="model">model</a></td>
                    <td>arn:\${Partition}:deeplens:\${Region}:\${Account}:model/\${ModelName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Data Lifecycle Manager</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazondatalifecyclemanager.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/dlm/latest/APIReference/API_LifecyclePolicy.html">policy</a></td>
                    <td>arn:\${Partition}:dlm:\${Region}:\${Account}:policy/\${ResourceName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS DeepComposer</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdeepcomposer.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/deepcomposer/latest/devguide/get-started-custom-model.html">model</a></td>
                    <td>arn:\${Partition}:deepcomposer:\${Region}:\${Account}:model/\${ModelId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/deepcomposer/latest/devguide/get-started-learn-from-pre-trained-models.html">composition</a></td>
                    <td>arn:\${Partition}:deepcomposer:\${Region}:\${Account}:composition/\${CompositionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/deepcomposer/latest/devguide/get-started-learn-from-pre-trained-models.html">audio</a></td>
                    <td>arn:\${Partition}:deepcomposer:\${Region}:\${Account}:audio/\${AudioId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon DevOps Guru</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazondevopsguru.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/devops-guru/latest/userguide/setting-up.html#setting-up-notifications">topic</a></td>
                    <td>arn:\${Partition}:sns:\${Region}:\${Account}:\${TopicName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS DataSync</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatasync.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/datasync/latest/userguide/working-with-agents.html">agent</a></td>
                    <td>arn:\${Partition}:datasync:\${Region}:\${AccountId}:agent/\${AgentId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html">location</a></td>
                    <td>arn:\${Partition}:datasync:\${Region}:\${AccountId}:location/\${LocationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/datasync/latest/userguide/working-with-tasks.html">task</a></td>
                    <td>arn:\${Partition}:datasync:\${Region}:\${AccountId}:task/\${TaskId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/datasync/latest/userguide/working-with-task-executions.html">taskexecution</a></td>
                    <td>arn:\${Partition}:datasync:\${Region}:\${AccountId}:task/\${TaskId}/execution/\${ExecutionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/datasync/latest/userguide/discovery-configure-storage.html">storagesystem</a></td>
                    <td>arn:\${Partition}:datasync:\${Region}:\${AccountId}:system/\${StorageSystemId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/datasync/latest/userguide/discovery-job-create.html">discoveryjob</a></td>
                    <td>arn:\${Partition}:datasync:\${Region}:\${AccountId}:system/\${StorageSystemId}/job/\${DiscoveryJobId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS DeepRacer</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdeepracer.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-choose-race-type.html">car</a></td>
                    <td>arn:\${Partition}:deepracer:\${Region}:\${Account}:car/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-get-started-test-in-simulator.html">evaluation_job</a></td>
                    <td>arn:\${Partition}:deepracer:\${Region}:\${Account}:evaluation_job/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-submit-model-to-leaderboard.html">leaderboard</a></td>
                    <td>arn:\${Partition}:deepracer:\${Region}::leaderboard/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-submit-model-to-leaderboard.html">leaderboard_evaluation_job</a></td>
                    <td>arn:\${Partition}:deepracer:\${Region}:\${Account}:leaderboard_evaluation_job/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-get-started-training-model.html">reinforcement_learning_model</a></td>
                    <td>arn:\${Partition}:deepracer:\${Region}:\${Account}:model/reinforcement_learning/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-console-train-evaluate-models.html">track</a></td>
                    <td>arn:\${Partition}:deepracer:\${Region}::track/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-get-started-training-model.html">training_job</a></td>
                    <td>arn:\${Partition}:deepracer:\${Region}:\${Account}:training_job/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon DataZone</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazondatazone.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/datazone/latest/userguide/create-domain.html">domain</a></td>
                    <td>arn:\${Partition}:datazone:\${Region}:\${Account}:domain/\${DomainId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Deadline Cloud</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdeadlinecloud.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_Budget.html">budget</a></td>
                    <td>arn:\${Partition}:deadline:\${Region}:\${Account}:farm/\${FarmId}/budget/\${BudgetId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_Farm.html">farm</a></td>
                    <td>arn:\${Partition}:deadline:\${Region}:\${Account}:farm/\${FarmId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_Fleet.html">fleet</a></td>
                    <td>arn:\${Partition}:deadline:\${Region}:\${Account}:farm/\${FarmId}/fleet/\${FleetId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_Job.html">job</a></td>
                    <td>arn:\${Partition}:deadline:\${Region}:\${Account}:farm/\${FarmId}/queue/\${QueueId}/job/\${JobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_LicenseEndpoint.html">license-endpoint</a></td>
                    <td>arn:\${Partition}:deadline:\${Region}:\${Account}:license-endpoint/\${LicenseEndpointId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_MeteredProduct.html">metered-product</a></td>
                    <td>arn:\${Partition}:deadline:\${Region}:\${Account}:license-endpoint/\${LicenseEndpointId}/metered-product/\${ProductId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_Monitor.html">monitor</a></td>
                    <td>arn:\${Partition}:deadline:\${Region}:\${Account}:monitor/\${MonitorId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_Queue.html">queue</a></td>
                    <td>arn:\${Partition}:deadline:\${Region}:\${Account}:farm/\${FarmId}/queue/\${QueueId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_Worker.html">worker</a></td>
                    <td>arn:\${Partition}:deadline:\${Region}:\${Account}:farm/\${FarmId}/fleet/\${FleetId}/worker/\${WorkerId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Database Migration Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_Certificate.html">Certificate</a></td>
                    <td>arn:\${Partition}:dms:\${Region}:\${Account}:cert:*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html">DataProvider</a></td>
                    <td>arn:\${Partition}:dms:\${Region}:\${Account}:data-provider:*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html">DataMigration</a></td>
                    <td>arn:\${Partition}:dms:\${Region}:\${Account}:data-migration:*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_Endpoint.html">Endpoint</a></td>
                    <td>arn:\${Partition}:dms:\${Region}:\${Account}:endpoint:*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_EventSubscription.html">EventSubscription</a></td>
                    <td>arn:\${Partition}:dms:\${Region}:\${Account}:es:*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html">InstanceProfile</a></td>
                    <td>arn:\${Partition}:dms:\${Region}:\${Account}:instance-profile:*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html">MigrationProject</a></td>
                    <td>arn:\${Partition}:dms:\${Region}:\${Account}:migration-project:*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html">ReplicationConfig</a></td>
                    <td>arn:\${Partition}:dms:\${Region}:\${Account}:replication-config:*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_ReplicationInstance.html">ReplicationInstance</a></td>
                    <td>arn:\${Partition}:dms:\${Region}:\${Account}:rep:*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_ReplicationSubnetGroup.html">ReplicationSubnetGroup</a></td>
                    <td>arn:\${Partition}:dms:\${Region}:\${Account}:subgrp:*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_ReplicationTask.html">ReplicationTask</a></td>
                    <td>arn:\${Partition}:dms:\${Region}:\${Account}:task:*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_ReplicationTaskAssessmentRun.html">ReplicationTaskAssessmentRun</a></td>
                    <td>arn:\${Partition}:dms:\${Region}:\${Account}:assessment-run:*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_ReplicationTaskIndividualAssessment.html">ReplicationTaskIndividualAssessment</a></td>
                    <td>arn:\${Partition}:dms:\${Region}:\${Account}:individual-assessment:*</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Detective</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazondetective.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/detective/latest/adminguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources">Graph</a></td>
                    <td>arn:\${Partition}:detective:\${Region}:\${Account}:graph:\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Diagnostic tools</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdiagnostictools.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_Execution.html">execution</a></td>
                    <td>arn:\${Partition}:ts::\${Account}:execution/\${UserId}/\${ToolId}/\${ExecutionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_Tool.html">tool</a></td>
                    <td>arn:\${Partition}:ts::aws:tool/\${ToolId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Connect</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonconnect.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-instances.html">instance</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/connect-contact-attributes.html">contact</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/contact/\${ContactId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/connect-agents.html">user</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/agent/\${UserId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/routing-profiles.html">routing-profile</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/routing-profile/\${RoutingProfileId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/connect-security-profiles.html">security-profile</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/security-profile/\${SecurityProfileId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/agent-hierarchy.html">hierarchy-group</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/agent-group/\${HierarchyGroupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/create-queue.html">queue</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/queue/\${QueueId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/create-queue.html">wildcard-queue</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/queue/*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/quick-connects.html">quick-connect</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/transfer-destination/\${QuickConnectId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/quick-connects.html">wildcard-quick-connect</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/transfer-destination/*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/connect-contact-flows.html">contact-flow</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/contact-flow/\${ContactFlowId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/task-templates.html">task-template</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/task-template/\${TaskTemplateId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/contact-flow-modules.html">contact-flow-module</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/flow-module/\${ContactFlowModuleId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/connect-contact-flows.html">wildcard-contact-flow</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/contact-flow/*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/set-hours-operation.html">hours-of-operation</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/operating-hours/\${HoursOfOperationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-agent-status.html">agent-status</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/agent-state/\${AgentStatusId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-agent-status.html">wildcard-agent-status</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/agent-state/*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/ag-overview-numbers.html">legacy-phone-number</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/phone-number/\${PhoneNumberId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/ag-overview-numbers.html">wildcard-legacy-phone-number</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/phone-number/*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/ag-overview-numbers.html">phone-number</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:phone-number/\${PhoneNumberId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/ag-overview-numbers.html">wildcard-phone-number</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:phone-number/*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/connect-rules.html">integration-association</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/integration-association/\${IntegrationAssociationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/add-rules-task-creation.html">use-case</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/use-case/\${UseCaseId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/add-custom-vocabulary.html">vocabulary</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/vocabulary/\${VocabularyId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/setup-traffic-distribution-groups.html">traffic-distribution-group</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:traffic-distribution-group/\${TrafficDistributionGroupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/connect-rules.html">rule</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/rule/\${RuleId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/create-evaluation-forms.html">evaluation-form</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/evaluation-form/\${FormId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/evaluations.html">contact-evaluation</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/contact-evaluation/\${EvaluationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/prompts.html">prompt</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/prompt/\${PromptId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/view-resources-sg.html">customer-managed-view</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/view/\${ViewId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/view-resources-sg.html">aws-managed-view</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:aws:view/\${ViewId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/view-resources-sg.html">qualified-customer-managed-view</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/view/\${ViewId}:\${ViewQualifier}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/view-resources-sg.html">qualified-aws-managed-view</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:aws:view/\${ViewId}:\${ViewQualifier}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/view-resources-sg.html">customer-managed-view-version</a></td>
                    <td>arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/view/\${ViewId}:\${ViewVersion}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Directory Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdirectoryservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/directoryservice/latest/devguide/welcome.html">directory</a></td>
                    <td>arn:\${Partition}:ds:\${Region}:\${Account}:directory/\${DirectoryId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Direct Connect</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdirectconnect.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/directconnect/latest/APIReference/API_Connection.html">dxcon</a></td>
                    <td>arn:\${Partition}:directconnect:\${Region}:\${Account}:dxcon/\${ConnectionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/directconnect/latest/APIReference/API_Lag.html">dxlag</a></td>
                    <td>arn:\${Partition}:directconnect:\${Region}:\${Account}:dxlag/\${LagId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/directconnect/latest/APIReference/API_VirtualInterface.html">dxvif</a></td>
                    <td>arn:\${Partition}:directconnect:\${Region}:\${Account}:dxvif/\${VirtualInterfaceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DirectConnectGateway.html">dx-gateway</a></td>
                    <td>arn:\${Partition}:directconnect::\${Account}:dx-gateway/\${DirectConnectGatewayId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon DocumentDB Elastic Clusters</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazondocumentdbelasticclusters.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/documentdb/latest/developerguide/elastic-managing.html">cluster</a></td>
                    <td>arn:\${Partition}:docdb-elastic:\${Region}:\${Account}:cluster/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/documentdb/latest/developerguide/elastic-managing.html#elastic-manage-snapshots">cluster-snapshot</a></td>
                    <td>arn:\${Partition}:docdb-elastic:\${Region}:\${Account}:cluster-snapshot/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Elastic Block Store</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelasticblockstore.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html">snapshot</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}::snapshot/\${SnapshotId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon EKS Auth</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoneksauth.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/eks/latest/userguide/clusters.html">cluster</a></td>
                    <td>arn:\${Partition}:eks:\${Region}:\${Account}:cluster/\${ClusterName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon EC2 Instance Connect</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2instanceconnect.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format">instance</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:instance/\${InstanceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/permissions-for-ec2-instance-connect-endpoint.html#iam-CreateInstanceConnectEndpoint">instance-connect-endpoint</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:instance-connect-endpoint/\${InstanceConnectEndpointId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Device Farm</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdevicefarm.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Project.html">project</a></td>
                    <td>arn:\${Partition}:devicefarm:\${Region}:\${Account}:project:\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Run.html">run</a></td>
                    <td>arn:\${Partition}:devicefarm:\${Region}:\${Account}:run:\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Job.html">job</a></td>
                    <td>arn:\${Partition}:devicefarm:\${Region}:\${Account}:job:\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Suite.html">suite</a></td>
                    <td>arn:\${Partition}:devicefarm:\${Region}:\${Account}:suite:\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Test.html">test</a></td>
                    <td>arn:\${Partition}:devicefarm:\${Region}:\${Account}:test:\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Upload.html">upload</a></td>
                    <td>arn:\${Partition}:devicefarm:\${Region}:\${Account}:upload:\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Artifact.html">artifact</a></td>
                    <td>arn:\${Partition}:devicefarm:\${Region}:\${Account}:artifact:\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Sample.html">sample</a></td>
                    <td>arn:\${Partition}:devicefarm:\${Region}:\${Account}:sample:\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_NetworkProfile.html">networkprofile</a></td>
                    <td>arn:\${Partition}:devicefarm:\${Region}:\${Account}:networkprofile:\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_DeviceInstance.html">deviceinstance</a></td>
                    <td>arn:\${Partition}:devicefarm:\${Region}::deviceinstance:\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_RemoteAccessSession.html">session</a></td>
                    <td>arn:\${Partition}:devicefarm:\${Region}:\${Account}:session:\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_DevicePool.html">devicepool</a></td>
                    <td>arn:\${Partition}:devicefarm:\${Region}:\${Account}:devicepool:\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Device.html">device</a></td>
                    <td>arn:\${Partition}:devicefarm:\${Region}::device:\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_InstanceProfile.html">instanceprofile</a></td>
                    <td>arn:\${Partition}:devicefarm:\${Region}:\${Account}:instanceprofile:\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_VPCEConfiguration.html">vpceconfiguration</a></td>
                    <td>arn:\${Partition}:devicefarm:\${Region}:\${Account}:vpceconfiguration:\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_TestGridProject.html">testgrid-project</a></td>
                    <td>arn:\${Partition}:devicefarm:\${Region}:\${Account}:testgrid-project:\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_TestGridSession.html">testgrid-session</a></td>
                    <td>arn:\${Partition}:devicefarm:\${Region}:\${Account}:testgrid-session:\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon DynamoDB</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazondynamodb.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.PrimaryKey">index</a></td>
                    <td>arn:\${Partition}:dynamodb:\${Region}:\${Account}:table/\${TableName}/index/\${IndexName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.Streams">stream</a></td>
                    <td>arn:\${Partition}:dynamodb:\${Region}:\${Account}:table/\${TableName}/stream/\${StreamLabel}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.TablesItemsAttributes">table</a></td>
                    <td>arn:\${Partition}:dynamodb:\${Region}:\${Account}:table/\${TableName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/backuprestore_HowItWorks.html">backup</a></td>
                    <td>arn:\${Partition}:dynamodb:\${Region}:\${Account}:table/\${TableName}/backup/\${BackupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/S3DataExport.HowItWorks.html">export</a></td>
                    <td>arn:\${Partition}:dynamodb:\${Region}:\${Account}:table/\${TableName}/export/\${ExportName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_HowItWorks.html">global-table</a></td>
                    <td>arn:\${Partition}:dynamodb::\${Account}:global-table/\${GlobalTableName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/S3DataImport.HowItWorks.html">import</a></td>
                    <td>arn:\${Partition}:dynamodb:\${Region}:\${Account}:table/\${TableName}/import/\${ImportName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon DynamoDB Accelerator (DAX)</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazondynamodbacceleratordax.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.access-control.html">application</a></td>
                    <td>arn:\${Partition}:dax:\${Region}:\${Account}:cache/\${ClusterName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon EC2 Auto Scaling</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2autoscaling.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-resources">autoScalingGroup</a></td>
                    <td>arn:\${Partition}:autoscaling:\${Region}:\${Account}:autoScalingGroup:\${GroupId}:autoScalingGroupName/\${GroupFriendlyName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-resources">launchConfiguration</a></td>
                    <td>arn:\${Partition}:autoscaling:\${Region}:\${Account}:launchConfiguration:\${Id}:launchConfigurationName/\${LaunchConfigurationName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Elastic Container Registry Public</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelasticcontainerregistrypublic.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/iam-policy-structure.html#ECR-Public_ARN_Format">repository</a></td>
                    <td>arn:\${Partition}:ecr-public::\${Account}:repository/\${RepositoryName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/iam-policy-structure.html#ECR-Public_ARN_Format">registry</a></td>
                    <td>arn:\${Partition}:ecr-public::\${Account}:registry/\${RegistryId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon EC2 Image Builder</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2imagebuilder.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_Component.html">component</a></td>
                    <td>arn:\${Partition}:imagebuilder:\${Region}:\${Account}:component/\${ComponentName}/\${ComponentVersion}/\${ComponentBuildVersion}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ComponentVersion.html">componentVersion</a></td>
                    <td>arn:\${Partition}:imagebuilder:\${Region}:\${Account}:component/\${ComponentName}/\${ComponentVersion}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_DistributionConfiguration.html">distributionConfiguration</a></td>
                    <td>arn:\${Partition}:imagebuilder:\${Region}:\${Account}:distribution-configuration/\${DistributionConfigurationName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_Image.html">image</a></td>
                    <td>arn:\${Partition}:imagebuilder:\${Region}:\${Account}:image/\${ImageName}/\${ImageVersion}/\${ImageBuildVersion}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImageVersion.html">imageVersion</a></td>
                    <td>arn:\${Partition}:imagebuilder:\${Region}:\${Account}:image/\${ImageName}/\${ImageVersion}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImageRecipe.html">imageRecipe</a></td>
                    <td>arn:\${Partition}:imagebuilder:\${Region}:\${Account}:image-recipe/\${ImageRecipeName}/\${ImageRecipeVersion}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ContainerRecipe.html">containerRecipe</a></td>
                    <td>arn:\${Partition}:imagebuilder:\${Region}:\${Account}:container-recipe/\${ContainerRecipeName}/\${ContainerRecipeVersion}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImagePipeline.html">imagePipeline</a></td>
                    <td>arn:\${Partition}:imagebuilder:\${Region}:\${Account}:image-pipeline/\${ImagePipelineName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_InfrastructureConfiguration.html">infrastructureConfiguration</a></td>
                    <td>arn:\${Partition}:imagebuilder:\${Region}:\${Account}:infrastructure-configuration/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys">kmsKey</a></td>
                    <td>arn:\${Partition}:kms:\${Region}:\${Account}:key/\${KeyId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_LifecycleExecution.html">lifecycleExecution</a></td>
                    <td>arn:\${Partition}:imagebuilder:\${Region}:\${Account}:lifecycle-execution/\${LifecycleExecutionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_LifecyclePolicy.html">lifecyclePolicy</a></td>
                    <td>arn:\${Partition}:imagebuilder:\${Region}:\${Account}:lifecycle-policy/\${LifecyclePolicyName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_Workflow.html">workflow</a></td>
                    <td>arn:\${Partition}:imagebuilder:\${Region}:\${Account}:workflow/\${WorkflowType}/\${WorkflowName}/\${WorkflowVersion}/\${WorkflowBuildVersion}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_WorkflowVersion.html">workflowVersion</a></td>
                    <td>arn:\${Partition}:imagebuilder:\${Region}:\${Account}:workflow/\${WorkflowType}/\${WorkflowName}/\${WorkflowVersion}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_WorkflowExecutionMetadata.html">workflowExecution</a></td>
                    <td>arn:\${Partition}:imagebuilder:\${Region}:\${Account}:workflow-execution/\${WorkflowExecutionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_WorkflowStepMetadata.html">workflowStepExecution</a></td>
                    <td>arn:\${Partition}:imagebuilder:\${Region}:\${Account}:workflow-step-execution/\${WorkflowStepExecutionId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Elastic Beanstalk</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselasticbeanstalk.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.arn.html">application</a></td>
                    <td>arn:\${Partition}:elasticbeanstalk:\${Region}:\${Account}:application/\${ApplicationName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.arn.html">applicationversion</a></td>
                    <td>arn:\${Partition}:elasticbeanstalk:\${Region}:\${Account}:applicationversion/\${ApplicationName}/\${VersionLabel}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.arn.html">configurationtemplate</a></td>
                    <td>arn:\${Partition}:elasticbeanstalk:\${Region}:\${Account}:configurationtemplate/\${ApplicationName}/\${TemplateName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.arn.html">environment</a></td>
                    <td>arn:\${Partition}:elasticbeanstalk:\${Region}:\${Account}:environment/\${ApplicationName}/\${EnvironmentName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.arn.html">solutionstack</a></td>
                    <td>arn:\${Partition}:elasticbeanstalk:\${Region}::solutionstack/\${SolutionStackName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.arn.html">platform</a></td>
                    <td>arn:\${Partition}:elasticbeanstalk:\${Region}::platform/\${PlatformNameWithVersion}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Elastic Inference</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelasticinference.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="accelerator">accelerator</a></td>
                    <td>arn:\${Partition}:elastic-inference:\${Region}:\${Account}:elastic-inference-accelerator/\${AcceleratorId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Elastic Container Registry</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelasticcontainerregistry.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/Repositories.html">repository</a></td>
                    <td>arn:\${Partition}:ecr:\${Region}:\${Account}:repository/\${RepositoryName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Elastic File System</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelasticfilesystem.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/efs/latest/ug/access-control-overview.html#access-control-resources">file-system</a></td>
                    <td>arn:\${Partition}:elasticfilesystem:\${Region}:\${Account}:file-system/\${FileSystemId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/efs/latest/ug/access-control-overview.html#access-control-resources">access-point</a></td>
                    <td>arn:\${Partition}:elasticfilesystem:\${Region}:\${Account}:access-point/\${AccessPointId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Elastic Kubernetes Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelastickubernetesservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/eks/latest/userguide/clusters.html">cluster</a></td>
                    <td>arn:\${Partition}:eks:\${Region}:\${Account}:cluster/\${ClusterName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html">nodegroup</a></td>
                    <td>arn:\${Partition}:eks:\${Region}:\${Account}:nodegroup/\${ClusterName}/\${NodegroupName}/\${UUID}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html">addon</a></td>
                    <td>arn:\${Partition}:eks:\${Region}:\${Account}:addon/\${ClusterName}/\${AddonName}/\${UUID}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/eks/latest/userguide/fargate-profile.html">fargateprofile</a></td>
                    <td>arn:\${Partition}:eks:\${Region}:\${Account}:fargateprofile/\${ClusterName}/\${FargateProfileName}/\${UUID}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/eks/latest/userguide/authenticate-oidc-identity-provider.html">identityproviderconfig</a></td>
                    <td>arn:\${Partition}:eks:\${Region}:\${Account}:identityproviderconfig/\${ClusterName}/\${IdentityProviderType}/\${IdentityProviderConfigName}/\${UUID}</td>
                </tr>
               <tr>
                    <td><a href="https://anywhere.eks.amazonaws.com/docs/clustermgmt/support/cluster-license/">eks-anywhere-subscription</a></td>
                    <td>arn:\${Partition}:eks:\${Region}:\${Account}:eks-anywhere-subscription/\${UUID}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html">podidentityassociation</a></td>
                    <td>arn:\${Partition}:eks:\${Region}:\${Account}:podidentityassociation/\${ClusterName}/\${UUID}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html">access-entry</a></td>
                    <td>arn:\${Partition}:eks:\${Region}:\${Account}:access-entry/\${ClusterName}/\${IamIdentityType}/\${IamIdentityAccountID}/\${IamIdentityName}/\${UUID}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/eks/latest/userguide/access-policies.html">access-policy</a></td>
                    <td>arn:\${Partition}:eks::aws:cluster-access-policy/\${AccessPolicyName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Elastic Transcoder</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelastictranscoder.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/operations-jobs.html">job</a></td>
                    <td>arn:\${Partition}:elastictranscoder:\${Region}:\${Account}:job/\${JobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/operations-pipelines.html">pipeline</a></td>
                    <td>arn:\${Partition}:elastictranscoder:\${Region}:\${Account}:pipeline/\${PipelineId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/operations-presets.html">preset</a></td>
                    <td>arn:\${Partition}:elastictranscoder:\${Region}:\${Account}:preset/\${PresetId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Elastic Container Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelasticcontainerservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/clusters.html">cluster</a></td>
                    <td>arn:\${Partition}:ecs:\${Region}:\${Account}:cluster/\${ClusterName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/manage-capacity.html">container-instance</a></td>
                    <td>arn:\${Partition}:ecs:\${Region}:\${Account}:container-instance/\${ClusterName}/\${ContainerInstanceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html">service</a></td>
                    <td>arn:\${Partition}:ecs:\${Region}:\${Account}:service/\${ClusterName}/\${ServiceName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html">task</a></td>
                    <td>arn:\${Partition}:ecs:\${Region}:\${Account}:task/\${ClusterName}/\${TaskId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html">task-definition</a></td>
                    <td>arn:\${Partition}:ecs:\${Region}:\${Account}:task-definition/\${TaskDefinitionFamilyName}:\${TaskDefinitionRevisionNumber}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-capacity-providers.html">capacity-provider</a></td>
                    <td>arn:\${Partition}:ecs:\${Region}:\${Account}:capacity-provider/\${CapacityProviderName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-external.html">task-set</a></td>
                    <td>arn:\${Partition}:ecs:\${Region}:\${Account}:task-set/\${ClusterName}/\${ServiceName}/\${TaskSetId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Elastic Load Balancing</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselasticloadbalancing.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html">loadbalancer</a></td>
                    <td>arn:\${Partition}:elasticloadbalancing:\${Region}:\${Account}:loadbalancer/\${LoadBalancerName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Elastic Disaster Recovery</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselasticdisasterrecovery.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/drs/latest/userguide/failback-overview.html">JobResource</a></td>
                    <td>arn:\${Partition}:drs:\${Region}:\${Account}:job/\${JobID}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/drs/latest/userguide/recovery-instances.html">RecoveryInstanceResource</a></td>
                    <td>arn:\${Partition}:drs:\${Region}:\${Account}:recovery-instance/\${RecoveryInstanceID}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/drs/latest/userguide/replication-settings-template.html">ReplicationConfigurationTemplateResource</a></td>
                    <td>arn:\${Partition}:drs:\${Region}:\${Account}:replication-configuration-template/\${ReplicationConfigurationTemplateID}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/drs/latest/userguide/default-drs-launch-settings.html">LaunchConfigurationTemplateResource</a></td>
                    <td>arn:\${Partition}:drs:\${Region}:\${Account}:launch-configuration-template/\${LaunchConfigurationTemplateID}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/drs/latest/userguide/source-servers.html">SourceServerResource</a></td>
                    <td>arn:\${Partition}:drs:\${Region}:\${Account}:source-server/\${SourceServerID}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/drs/latest/userguide/source-networks.html">SourceNetworkResource</a></td>
                    <td>arn:\${Partition}:drs:\${Region}:\${Account}:source-network/\${SourceNetworkID}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Elemental Appliances and Software Activation Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselementalappliancesandsoftwareactivationservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/elemental-appliances-software/">activation</a></td>
                    <td>arn:\${Partition}:elemental-activations:\${Region}:\${Account}:activation/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Elastic MapReduce</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelasticmapreduce.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-overview.html">cluster</a></td>
                    <td>arn:\${Partition}:elasticmapreduce:\${Region}:\${Account}:cluster/\${ClusterId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks.html">editor</a></td>
                    <td>arn:\${Partition}:elasticmapreduce:\${Region}:\${Account}:editor/\${EditorId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-headless.html">notebook-execution</a></td>
                    <td>arn:\${Partition}:elasticmapreduce:\${Region}:\${Account}:notebook-execution/\${NotebookExecutionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio.html">studio</a></td>
                    <td>arn:\${Partition}:elasticmapreduce:\${Region}:\${Account}:studio/\${StudioId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Elemental Appliances and Software</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselementalappliancesandsoftware.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/elemental-appliances-software">quote</a></td>
                    <td>arn:\${Partition}:elemental-appliances-software:\${Region}:\${Account}:quote/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Elemental MediaPackage V2</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselementalmediapackagev2.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/mediapackage/latest/userguide/channel-groups.html">ChannelGroup</a></td>
                    <td>arn:\${Partition}:mediapackagev2:\${Region}:\${Account}:channelGroup/\${ChannelGroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mediapackage/latest/userguide/channels.html">Channel</a></td>
                    <td>arn:\${Partition}:mediapackagev2:\${Region}:\${Account}:channelGroup/\${ChannelGroupName}/channel/\${ChannelName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mediapackage/latest/userguide/endpoints.html">OriginEndpoint</a></td>
                    <td>arn:\${Partition}:mediapackagev2:\${Region}:\${Account}:channelGroup/\${ChannelGroupName}/channel/\${ChannelName}/originEndpoint/\${OriginEndpointName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Elastic Load Balancing V2</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselasticloadbalancingv2.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html">listener/app</a></td>
                    <td>arn:\${Partition}:elasticloadbalancing:\${Region}:\${Account}:listener/app/\${LoadBalancerName}/\${LoadBalancerId}/\${ListenerId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-update-rules.html">listener-rule/app</a></td>
                    <td>arn:\${Partition}:elasticloadbalancing:\${Region}:\${Account}:listener-rule/app/\${LoadBalancerName}/\${LoadBalancerId}/\${ListenerId}/\${ListenerRuleId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html">listener/net</a></td>
                    <td>arn:\${Partition}:elasticloadbalancing:\${Region}:\${Account}:listener/net/\${LoadBalancerName}/\${LoadBalancerId}/\${ListenerId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-update-rules.html">listener-rule/net</a></td>
                    <td>arn:\${Partition}:elasticloadbalancing:\${Region}:\${Account}:listener-rule/net/\${LoadBalancerName}/\${LoadBalancerId}/\${ListenerId}/\${ListenerRuleId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html#application-load-balancer-overview">loadbalancer/app/</a></td>
                    <td>arn:\${Partition}:elasticloadbalancing:\${Region}:\${Account}:loadbalancer/app/\${LoadBalancerName}/\${LoadBalancerId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html#network-load-balancer-overview">loadbalancer/net/</a></td>
                    <td>arn:\${Partition}:elasticloadbalancing:\${Region}:\${Account}:loadbalancer/net/\${LoadBalancerName}/\${LoadBalancerId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html">targetgroup</a></td>
                    <td>arn:\${Partition}:elasticloadbalancing:\${Region}:\${Account}:targetgroup/\${TargetGroupName}/\${TargetGroupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/trust-store.html">truststore</a></td>
                    <td>arn:\${Partition}:elasticloadbalancing:\${Region}:\${Account}:truststore/\${TrustStoreName}/\${TrustStoreId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Elemental MediaConnect</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselementalmediaconnect.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/mediaconnect/latest/ug/entitlements.html">Entitlement</a></td>
                    <td>arn:\${Partition}:mediaconnect:\${Region}:\${Account}:entitlement:\${FlowId}:\${EntitlementName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mediaconnect/latest/ug/flows.html">Flow</a></td>
                    <td>arn:\${Partition}:mediaconnect:\${Region}:\${Account}:flow:\${FlowId}:\${FlowName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mediaconnect/latest/ug/outputs.html">Output</a></td>
                    <td>arn:\${Partition}:mediaconnect:\${Region}:\${Account}:output:\${OutputId}:\${OutputName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mediaconnect/latest/ug/sources.html">Source</a></td>
                    <td>arn:\${Partition}:mediaconnect:\${Region}:\${Account}:source:\${SourceId}:\${SourceName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mediaconnect/latest/ug/gateway.html">Gateway</a></td>
                    <td>arn:\${Partition}:mediaconnect:\${Region}:\${Account}:gateway:\${GatewayId}:\${GatewayName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mediaconnect/latest/ug/gateway-components-bridges.html">Bridge</a></td>
                    <td>arn:\${Partition}:mediaconnect:\${Region}:\${Account}:bridge:\${FlowId}:\${FlowName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mediaconnect/latest/ug/gateway-components-instances.html">GatewayInstance</a></td>
                    <td>arn:\${Partition}:mediaconnect:\${Region}:\${Account}:gateway:\${GatewayId}:\${GatewayName}:instance:\${InstanceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Elemental MediaConvert</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselementalmediaconvert.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/mediaconvert/latest/apireference/jobs.html">Job</a></td>
                    <td>arn:\${Partition}:mediaconvert:\${Region}:\${Account}:jobs/\${JobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mediaconvert/latest/apireference/queues.html">Queue</a></td>
                    <td>arn:\${Partition}:mediaconvert:\${Region}:\${Account}:queues/\${QueueName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mediaconvert/latest/apireference/presets.html">Preset</a></td>
                    <td>arn:\${Partition}:mediaconvert:\${Region}:\${Account}:presets/\${PresetName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mediaconvert/latest/apireference/jobtemplates.html">JobTemplate</a></td>
                    <td>arn:\${Partition}:mediaconvert:\${Region}:\${Account}:jobTemplates/\${JobTemplateName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mediaconvert/latest/apireference/certificates.html">CertificateAssociation</a></td>
                    <td>arn:\${Partition}:mediaconvert:\${Region}:\${Account}:certificates/\${CertificateArn}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Elemental MediaPackage</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselementalmediapackage.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/mediapackage/latest/ug/channels.html">channels</a></td>
                    <td>arn:\${Partition}:mediapackage:\${Region}:\${Account}:channels/\${ChannelIdentifier}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints.html">origin_endpoints</a></td>
                    <td>arn:\${Partition}:mediapackage:\${Region}:\${Account}:origin_endpoints/\${OriginEndpointIdentifier}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mediapackage/latest/ug/harvest-jobs.html">harvest_jobs</a></td>
                    <td>arn:\${Partition}:mediapackage:\${Region}:\${Account}:harvest_jobs/\${HarvestJobIdentifier}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Elemental MediaLive</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselementalmedialive.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/medialive/latest/ug/container-channel.html">channel</a></td>
                    <td>arn:\${Partition}:medialive:\${Region}:\${Account}:channel:\${ChannelId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/medialive/latest/ug/creating-input.html">input</a></td>
                    <td>arn:\${Partition}:medialive:\${Region}:\${Account}:input:\${InputId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/medialive/latest/ug/eml-devices.html">input-device</a></td>
                    <td>arn:\${Partition}:medialive:\${Region}:\${Account}:inputDevice:\${DeviceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/medialive/latest/ug/working-with-input-security-groups.html">input-security-group</a></td>
                    <td>arn:\${Partition}:medialive:\${Region}:\${Account}:inputSecurityGroup:\${InputSecurityGroupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/medialive/latest/ug/eml-multiplex.html">multiplex</a></td>
                    <td>arn:\${Partition}:medialive:\${Region}:\${Account}:multiplex:\${MultiplexId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/medialive/latest/ug/reservations.html">reservation</a></td>
                    <td>arn:\${Partition}:medialive:\${Region}:\${Account}:reservation:\${ReservationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/medialive/latest/ug/input-output-reservations.html">offering</a></td>
                    <td>arn:\${Partition}:medialive:\${Region}:\${Account}:offering:\${OfferingId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-create.html">signal-map</a></td>
                    <td>arn:\${Partition}:medialive:\${Region}:\${Account}:signal-map:\${SignalMapId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-alarms-templates-create.html">cloudwatch-alarm-template-group</a></td>
                    <td>arn:\${Partition}:medialive:\${Region}:\${Account}:cloudwatch-alarm-template-group:\${CloudWatchAlarmTemplateGroupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-alarms-templates-create.html">cloudwatch-alarm-template</a></td>
                    <td>arn:\${Partition}:medialive:\${Region}:\${Account}:cloudwatch-alarm-template:\${CloudWatchAlarmTemplateId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-notifications-template-create.html">eventbridge-rule-template-group</a></td>
                    <td>arn:\${Partition}:medialive:\${Region}:\${Account}:eventbridge-rule-template-group:\${EventBridgeRuleTemplateGroupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-notifications-template-create.html">eventbridge-rule-template</a></td>
                    <td>arn:\${Partition}:medialive:\${Region}:\${Account}:eventbridge-rule-template:\${EventBridgeRuleTemplateId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Elemental MediaPackage VOD</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselementalmediapackagevod.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/mediapackage/latest/ug/asset.html">assets</a></td>
                    <td>arn:\${Partition}:mediapackage-vod:\${Region}:\${Account}:assets/\${AssetIdentifier}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-cfig.html">packaging-configurations</a></td>
                    <td>arn:\${Partition}:mediapackage-vod:\${Region}:\${Account}:packaging-configurations/\${PackagingConfigurationIdentifier}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-group.html">packaging-groups</a></td>
                    <td>arn:\${Partition}:mediapackage-vod:\${Region}:\${Account}:packaging-groups/\${PackagingGroupIdentifier}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Elemental Support Cases</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselementalsupportcases.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Elemental MediaTailor</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselementalmediatailor.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/mediatailor/latest/apireference/playbackconfiguration.html">playbackConfiguration</a></td>
                    <td>arn:\${Partition}:mediatailor:\${Region}:\${Account}:playbackConfiguration/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mediatailor/latest/apireference/prefetchschedule-playbackconfigurationname-name.html">prefetchSchedule</a></td>
                    <td>arn:\${Partition}:mediatailor:\${Region}:\${Account}:prefetchSchedule/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname.html">channel</a></td>
                    <td>arn:\${Partition}:mediatailor:\${Region}:\${Account}:channel/\${ChannelName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname-program-programname.html">program</a></td>
                    <td>arn:\${Partition}:mediatailor:\${Region}:\${Account}:program/\${ChannelName}/\${ProgramName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname.html">sourceLocation</a></td>
                    <td>arn:\${Partition}:mediatailor:\${Region}:\${Account}:sourceLocation/\${SourceLocationName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-vodsource-vodsourcename.html">vodSource</a></td>
                    <td>arn:\${Partition}:mediatailor:\${Region}:\${Account}:vodSource/\${SourceLocationName}/\${VodSourceName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-livesource-livesourcename.html">liveSource</a></td>
                    <td>arn:\${Partition}:mediatailor:\${Region}:\${Account}:liveSource/\${SourceLocationName}/\${LiveSourceName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Elemental Support Content</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselementalsupportcontent.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Elemental MediaStore</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselementalmediastore.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/mediastore/latest/ug/containers.html">container</a></td>
                    <td>arn:\${Partition}:mediastore:\${Region}:\${Account}:container/\${ContainerName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mediastore/latest/ug/objects.html">object</a></td>
                    <td>arn:\${Partition}:mediastore:\${Region}:\${Account}:container/\${ContainerName}/\${ObjectPath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mediastore/latest/ug/folders.html">folder</a></td>
                    <td>arn:\${Partition}:mediastore:\${Region}:\${Account}:container/\${ContainerName}/\${FolderPath}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon ElastiCache</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelasticache.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.Components.html#WhatIs.Components.ParameterGroups">parametergroup</a></td>
                    <td>arn:\${Partition}:elasticache:\${Region}:\${Account}:parametergroup:\${CacheParameterGroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.Components.html#WhatIs.Components.SecurityGroups">securitygroup</a></td>
                    <td>arn:\${Partition}:elasticache:\${Region}:\${Account}:securitygroup:\${CacheSecurityGroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.Components.html#WhatIs.Components.SubnetGroups">subnetgroup</a></td>
                    <td>arn:\${Partition}:elasticache:\${Region}:\${Account}:subnetgroup:\${CacheSubnetGroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.Components.html#WhatIs.Components.ReplicationGroups">replicationgroup</a></td>
                    <td>arn:\${Partition}:elasticache:\${Region}:\${Account}:replicationgroup:\${ReplicationGroupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.Components.html#WhatIs.Components.Clusters">cluster</a></td>
                    <td>arn:\${Partition}:elasticache:\${Region}:\${Account}:cluster:\${CacheClusterId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/reserved-nodes.html">reserved-instance</a></td>
                    <td>arn:\${Partition}:elasticache:\${Region}:\${Account}:reserved-instance:\${ReservedCacheNodeId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.Components.html#WhatIs.Components.Snapshots">snapshot</a></td>
                    <td>arn:\${Partition}:elasticache:\${Region}:\${Account}:snapshot:\${SnapshotName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Redis-Global-Datastore.html">globalreplicationgroup</a></td>
                    <td>arn:\${Partition}:elasticache::\${Account}:globalreplicationgroup:\${GlobalReplicationGroupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.RBAC.html">user</a></td>
                    <td>arn:\${Partition}:elasticache:\${Region}:\${Account}:user:\${UserId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.RBAC.html">usergroup</a></td>
                    <td>arn:\${Partition}:elasticache:\${Region}:\${Account}:usergroup:\${UserGroupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html">serverlesscache</a></td>
                    <td>arn:\${Partition}:elasticache:\${Region}:\${Account}:serverlesscache:\${ServerlessCacheName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html">serverlesscachesnapshot</a></td>
                    <td>arn:\${Partition}:elasticache:\${Region}:\${Account}:serverlesscachesnapshot:\${ServerlessCacheSnapshotName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon EventBridge Pipes</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoneventbridgepipes.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html">pipe</a></td>
                    <td>arn:\${Partition}:pipes:\${Region}:\${Account}:pipe/\${Name}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon EMR Serverless</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonemrserverless.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless.html">application</a></td>
                    <td>arn:\${Partition}:emr-serverless:\${Region}:\${Account}:/applications/\${ApplicationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless.html">jobRun</a></td>
                    <td>arn:\${Partition}:emr-serverless:\${Region}:\${Account}:/applications/\${ApplicationId}/jobruns/\${JobRunId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon EMR on EKS (EMR Containers)</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonemroneksemrcontainers.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/virtual-cluster.html">virtualCluster</a></td>
                    <td>arn:\${Partition}:emr-containers:\${Region}:\${Account}:/virtualclusters/\${VirtualClusterId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/job-runs.html">jobRun</a></td>
                    <td>arn:\${Partition}:emr-containers:\${Region}:\${Account}:/virtualclusters/\${VirtualClusterId}/jobruns/\${JobRunId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/job-templates.html">jobTemplate</a></td>
                    <td>arn:\${Partition}:emr-containers:\${Region}:\${Account}:/jobtemplates/\${JobTemplateId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-create-eks-cluster.html#emr-studio-create-managed-endpoint">managedEndpoint</a></td>
                    <td>arn:\${Partition}:emr-containers:\${Region}:\${Account}:/virtualclusters/\${VirtualClusterId}/endpoints/\${EndpointId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/security-configurations.html">securityConfiguration</a></td>
                    <td>arn:\${Partition}:emr-containers:\${Region}:\${Account}:/securityconfigurations/\${SecurityConfigurationId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Entity Resolution</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsentityresolution.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/entityresolution/latest/userguide/">MatchingWorkflow</a></td>
                    <td>arn:\${Partition}:entityresolution::\${Account}:matchingworkflow/\${WorkflowName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/entityresolution/latest/userguide/">SchemaMapping</a></td>
                    <td>arn:\${Partition}:entityresolution::\${Account}:schemamapping/\${SchemaName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/entityresolution/latest/userguide/">IdMappingWorkflow</a></td>
                    <td>arn:\${Partition}:entityresolution::\${Account}:idmappingworkflow/\${WorkflowName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/entityresolution/latest/userguide/">ProviderService</a></td>
                    <td>arn:\${Partition}:entityresolution::\${Account}:providerservice/\${ProviderName}/\${ProviderServiceName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/entityresolution/latest/userguide/">IdNamespace</a></td>
                    <td>arn:\${Partition}:entityresolution::\${Account}:idnamespace/\${IdNamespaceName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon EventBridge</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoneventbridge.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format">event-source</a></td>
                    <td>arn:\${Partition}:events:\${Region}::event-source/\${EventSourceName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format">event-bus</a></td>
                    <td>arn:\${Partition}:events:\${Region}:\${Account}:event-bus/\${EventBusName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format">rule-on-default-event-bus</a></td>
                    <td>arn:\${Partition}:events:\${Region}:\${Account}:rule/\${RuleName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format">rule-on-custom-event-bus</a></td>
                    <td>arn:\${Partition}:events:\${Region}:\${Account}:rule/\${EventBusName}/\${RuleName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format">archive</a></td>
                    <td>arn:\${Partition}:events:\${Region}:\${Account}:archive/\${ArchiveName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format">replay</a></td>
                    <td>arn:\${Partition}:events:\${Region}:\${Account}:replay/\${ReplayName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format">connection</a></td>
                    <td>arn:\${Partition}:events:\${Region}:\${Account}:connection/\${ConnectionName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format">api-destination</a></td>
                    <td>arn:\${Partition}:events:\${Region}:\${Account}:api-destination/\${ApiDestinationName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format">endpoint</a></td>
                    <td>arn:\${Partition}:events:\${Region}:\${Account}:endpoint/\${EndpointName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon EventBridge Schemas</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoneventbridgeschemas.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-schema.html">discoverer</a></td>
                    <td>arn:\${Partition}:schemas:\${Region}:\${Account}:discoverer/\${DiscovererId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-schema.html">registry</a></td>
                    <td>arn:\${Partition}:schemas:\${Region}:\${Account}:registry/\${RegistryName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-schema.html">schema</a></td>
                    <td>arn:\${Partition}:schemas:\${Region}:\${Account}:schema/\${RegistryName}/\${SchemaName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Free Tier</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsfreetier.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon FinSpace API</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfinspaceapi.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html">credential</a></td>
                    <td>arn:\${Partition}:finspace-api:\${Region}:\${Account}:/credentials/programmatic</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon FreeRTOS</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfreertos.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/freertos/latest/userguide/freertos-ocw.html">configuration</a></td>
                    <td>arn:\${Partition}:freertos:\${Region}:\${Account}:configuration/\${ConfigurationName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/freertos/latest/userguide/freertos-getting-started-emp.html">subscription</a></td>
                    <td>arn:\${Partition}:freertos:\${Region}:\${Account}:subscription/\${SubscriptionID}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon FinSpace</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfinspace.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html">environment</a></td>
                    <td>arn:\${Partition}:finspace:\${Region}:\${Account}:environment/\${EnvironmentId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html">user</a></td>
                    <td>arn:\${Partition}:finspace:\${Region}:\${Account}:user/\${UserId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html">kxEnvironment</a></td>
                    <td>arn:\${Partition}:finspace:\${Region}:\${Account}:kxEnvironment/\${EnvironmentId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html">kxUser</a></td>
                    <td>arn:\${Partition}:finspace:\${Region}:\${Account}:kxEnvironment/\${EnvironmentId}/kxUser/\${UserName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html">kxCluster</a></td>
                    <td>arn:\${Partition}:finspace:\${Region}:\${Account}:kxEnvironment/\${EnvironmentId}/kxCluster/\${KxCluster}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html">kxDatabase</a></td>
                    <td>arn:\${Partition}:finspace:\${Region}:\${Account}:kxEnvironment/\${EnvironmentId}/kxDatabase/\${KxDatabase}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html">kxScalingGroup</a></td>
                    <td>arn:\${Partition}:finspace:\${Region}:\${Account}:kxEnvironment/\${EnvironmentId}/kxScalingGroup/\${KxScalingGroup}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html">kxDataview</a></td>
                    <td>arn:\${Partition}:finspace:\${Region}:\${Account}:kxEnvironment/\${EnvironmentId}/kxDatabase/\${KxDatabase}/kxDataview/\${KxDataview}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html">kxVolume</a></td>
                    <td>arn:\${Partition}:finspace:\${Region}:\${Account}:kxEnvironment/\${EnvironmentId}/kxVolume/\${KxVolume}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Fault Injection Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsfaultinjectionservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/fis/latest/userguide/actions.html">action</a></td>
                    <td>arn:\${Partition}:fis:\${Region}:\${Account}:action/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/fis/latest/userguide/experiments.html">experiment</a></td>
                    <td>arn:\${Partition}:fis:\${Region}:\${Account}:experiment/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/fis/latest/userguide/working-with-templates.html">experiment-template</a></td>
                    <td>arn:\${Partition}:fis:\${Region}:\${Account}:experiment-template/\${Id}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon EventBridge Scheduler</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoneventbridgescheduler.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-schedule-group.html">schedule-group</a></td>
                    <td>arn:\${Partition}:scheduler:\${Region}:\${Account}:schedule-group/\${GroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-schedule.html">schedule</a></td>
                    <td>arn:\${Partition}:scheduler:\${Region}:\${Account}:schedule/\${GroupName}/\${ScheduleName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Firewall Manager</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsfirewallmanager.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_Policy.html">policy</a></td>
                    <td>arn:\${Partition}:fms:\${Region}:\${Account}:policy/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_AppsListData.html">applications-list</a></td>
                    <td>arn:\${Partition}:fms:\${Region}:\${Account}:applications-list/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ProtocolsListData.html">protocols-list</a></td>
                    <td>arn:\${Partition}:fms:\${Region}:\${Account}:protocols-list/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ResourceSet.html">resource-set</a></td>
                    <td>arn:\${Partition}:fms:\${Region}:\${Account}:resource-set/\${Id}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Ground Station</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsgroundstation.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ConfigListItem.html">Config</a></td>
                    <td>arn:\${Partition}:groundstation:\${Region}:\${Account}:config/\${ConfigType}/\${ConfigId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ContactData.html">Contact</a></td>
                    <td>arn:\${Partition}:groundstation:\${Region}:\${Account}:contact/\${ContactId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DataflowEndpoint.html">DataflowEndpointGroup</a></td>
                    <td>arn:\${Partition}:groundstation:\${Region}:\${Account}:dataflow-endpoint-group/\${DataflowEndpointGroupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ground-station/latest/APIReference/API_EphemerisItem.html">EphemerisItem</a></td>
                    <td>arn:\${Partition}:groundstation:\${Region}:\${Account}:ephemeris/\${EphemerisId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GroundStationData.html">GroundStationResource</a></td>
                    <td>arn:\${Partition}:groundstation:\${Region}:\${Account}:groundstation:\${GroundStationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ground-station/latest/APIReference/API_MissionProfileListItem.html">MissionProfile</a></td>
                    <td>arn:\${Partition}:groundstation:\${Region}:\${Account}:mission-profile/\${MissionProfileId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ground-station/latest/APIReference/API_SatelliteListItem.html">Satellite</a></td>
                    <td>arn:\${Partition}:groundstation:\${Region}:\${Account}:satellite/\${SatelliteId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AgentDetails.html">Agent</a></td>
                    <td>arn:\${Partition}:groundstation:\${Region}:\${Account}:agent/\${AgentId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Forecast</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonforecast.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html">dataset</a></td>
                    <td>arn:\${Partition}:forecast:\${Region}:\${Account}:dataset/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetGroup.html">datasetGroup</a></td>
                    <td>arn:\${Partition}:forecast:\${Region}:\${Account}:dataset-group/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetImportJob.html">datasetImportJob</a></td>
                    <td>arn:\${Partition}:forecast:\${Region}:\${Account}:dataset-import-job/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/forecast/latest/dg/aws-forecast-choosing-recipes.html">algorithm</a></td>
                    <td>arn:\${Partition}:forecast:::algorithm/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreatePredictor.html">predictor</a></td>
                    <td>arn:\${Partition}:forecast:\${Region}:\${Account}:predictor/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreatePredictorBacktestExportJob.html">predictorBacktestExportJob</a></td>
                    <td>arn:\${Partition}:forecast:\${Region}:\${Account}:predictor-backtest-export-job/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateForecast.html">forecast</a></td>
                    <td>arn:\${Partition}:forecast:\${Region}:\${Account}:forecast/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateForecastExportJob.html">forecastExport</a></td>
                    <td>arn:\${Partition}:forecast:\${Region}:\${Account}:forecast-export-job/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateExplainability.html">explainability</a></td>
                    <td>arn:\${Partition}:forecast:\${Region}:\${Account}:explainability/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateExplainabilityExport.html">explainabilityExport</a></td>
                    <td>arn:\${Partition}:forecast:\${Region}:\${Account}:explainability-export/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateMonitor.html">monitor</a></td>
                    <td>arn:\${Partition}:forecast:\${Region}:\${Account}:monitor/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateWhatIfAnalysis.html">whatIfAnalysis</a></td>
                    <td>arn:\${Partition}:forecast:\${Region}:\${Account}:what-if-analysis/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateWhatIfForecast.html">whatIfForecast</a></td>
                    <td>arn:\${Partition}:forecast:\${Region}:\${Account}:what-if-forecast/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateWhatIfForecastExport.html">whatIfForecastExport</a></td>
                    <td>arn:\${Partition}:forecast:\${Region}:\${Account}:what-if-forecast-export/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/forecast/latest/dg/what-is-forecast.html">endpoint</a></td>
                    <td>arn:\${Partition}:forecast:\${Region}:\${Account}:forecast-endpoint/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon FSx</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfsx.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/access-control-overview.html#access-control-resources">file-system</a></td>
                    <td>arn:\${Partition}:fsx:\${Region}:\${Account}:file-system/\${FileSystemId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/security-iam.html">file-cache</a></td>
                    <td>arn:\${Partition}:fsx:\${Region}:\${Account}:file-cache/\${FileCacheId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/access-control-overview.html#access-control-resources">backup</a></td>
                    <td>arn:\${Partition}:fsx:\${Region}:\${Account}:backup/\${BackupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/security-iam.html">storage-virtual-machine</a></td>
                    <td>arn:\${Partition}:fsx:\${Region}:\${Account}:storage-virtual-machine/\${FileSystemId}/\${StorageVirtualMachineId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/fsx/latest/LustreGuide/access-control-overview.html#access-control-resources">task</a></td>
                    <td>arn:\${Partition}:fsx:\${Region}:\${Account}:task/\${TaskId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/fsx/latest/LustreGuide/access-control-overview.html#access-control-resources">association</a></td>
                    <td>arn:\${Partition}:fsx:\${Region}:\${Account}:association/\${FileSystemIdOrFileCacheId}/\${DataRepositoryAssociationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/security-iam.html">volume</a></td>
                    <td>arn:\${Partition}:fsx:\${Region}:\${Account}:volume/\${FileSystemId}/\${VolumeId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/access-control-overview.html#access-control-resources">snapshot</a></td>
                    <td>arn:\${Partition}:fsx:\${Region}:\${Account}:snapshot/\${VolumeId}/\${SnapshotId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Fraud Detector</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies">batch-prediction</a></td>
                    <td>arn:\${Partition}:frauddetector:\${Region}:\${Account}:batch-prediction/\${ResourcePath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies">detector</a></td>
                    <td>arn:\${Partition}:frauddetector:\${Region}:\${Account}:detector/\${ResourcePath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies">detector-version</a></td>
                    <td>arn:\${Partition}:frauddetector:\${Region}:\${Account}:detector-version/\${ResourcePath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies">entity-type</a></td>
                    <td>arn:\${Partition}:frauddetector:\${Region}:\${Account}:entity-type/\${ResourcePath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies">external-model</a></td>
                    <td>arn:\${Partition}:frauddetector:\${Region}:\${Account}:external-model/\${ResourcePath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies">event-type</a></td>
                    <td>arn:\${Partition}:frauddetector:\${Region}:\${Account}:event-type/\${ResourcePath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies">label</a></td>
                    <td>arn:\${Partition}:frauddetector:\${Region}:\${Account}:label/\${ResourcePath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies">model</a></td>
                    <td>arn:\${Partition}:frauddetector:\${Region}:\${Account}:model/\${ResourcePath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies">model-version</a></td>
                    <td>arn:\${Partition}:frauddetector:\${Region}:\${Account}:model-version/\${ResourcePath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies">outcome</a></td>
                    <td>arn:\${Partition}:frauddetector:\${Region}:\${Account}:outcome/\${ResourcePath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies">rule</a></td>
                    <td>arn:\${Partition}:frauddetector:\${Region}:\${Account}:rule/\${ResourcePath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies">variable</a></td>
                    <td>arn:\${Partition}:frauddetector:\${Region}:\${Account}:variable/\${ResourcePath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies">batch-import</a></td>
                    <td>arn:\${Partition}:frauddetector:\${Region}:\${Account}:batch-import/\${ResourcePath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies">list</a></td>
                    <td>arn:\${Partition}:frauddetector:\${Region}:\${Account}:list/\${ResourcePath}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Global Accelerator</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsglobalaccelerator.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/global-accelerator/latest/api/API_Accelerator.html">accelerator</a></td>
                    <td>arn:\${Partition}:globalaccelerator::\${Account}:accelerator/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/global-accelerator/latest/api/API_Listener.html">listener</a></td>
                    <td>arn:\${Partition}:globalaccelerator::\${Account}:accelerator/\${ResourceId}/listener/\${ListenerId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/global-accelerator/latest/api/API_EndpointGroup.html">endpointgroup</a></td>
                    <td>arn:\${Partition}:globalaccelerator::\${Account}:accelerator/\${ResourceId}/listener/\${ListenerId}/endpoint-group/\${EndpointGroupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/global-accelerator/latest/api/API_CrossAccountAttachment.html">attachment</a></td>
                    <td>arn:\${Partition}:globalaccelerator::\${Account}:attachment/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS HealthImaging</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awshealthimaging.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/healthimaging/latest/devguide/API_DatastoreProperties.html">datastore</a></td>
                    <td>arn:\${Partition}:medical-imaging:\${Region}:\${Account}:datastore/\${DatastoreId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/healthimaging/latest/devguide/API_ImageSetProperties.html">imageset</a></td>
                    <td>arn:\${Partition}:medical-imaging:\${Region}:\${Account}:datastore/\${DatastoreId}/imageset/\${ImageSetId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon GameLift</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazongamelift.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-console-aliases.html">alias</a></td>
                    <td>arn:\${Partition}:gamelift:\${Region}::alias/\${AliasId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-console-builds.html">build</a></td>
                    <td>arn:\${Partition}:gamelift:\${Region}:\${Account}:build/\${BuildId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/containers-create-groups.html">containerGroupDefinition</a></td>
                    <td>arn:\${Partition}:gamelift:\${Region}:\${Account}:containergroupdefinition/\${Name}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-console-fleets.html">fleet</a></td>
                    <td>arn:\${Partition}:gamelift:\${Region}:\${Account}:fleet/\${FleetId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-integrate-gameservergroup.html">gameServerGroup</a></td>
                    <td>arn:\${Partition}:gamelift:\${Region}:\${Account}:gameservergroup/\${GameServerGroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-console.html">gameSessionQueue</a></td>
                    <td>arn:\${Partition}:gamelift:\${Region}:\${Account}:gamesessionqueue/\${GameSessionQueueName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-anywhere.html#fleet-anywhere-location">location</a></td>
                    <td>arn:\${Partition}:gamelift:\${Region}:\${Account}:location/\${LocationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-create-configuration.html">matchmakingConfiguration</a></td>
                    <td>arn:\${Partition}:gamelift:\${Region}:\${Account}:matchmakingconfiguration/\${MatchmakingConfigurationName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-rulesets.html">matchmakingRuleSet</a></td>
                    <td>arn:\${Partition}:gamelift:\${Region}:\${Account}:matchmakingruleset/\${MatchmakingRuleSetName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-console-scripts.html">script</a></td>
                    <td>arn:\${Partition}:gamelift:\${Region}:\${Account}:script/\${ScriptId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Health APIs and Notifications</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awshealthapisandnotifications.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/health/latest/ug/supported-operations.html">event</a></td>
                    <td>arn:\${Partition}:health:*::event/\${Service}/\${EventTypeCode}/*</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon GroundTruth Labeling</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazongroundtruthlabeling.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon GuardDuty</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonguardduty.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_managing_access.html#guardduty-resources">detector</a></td>
                    <td>arn:\${Partition}:guardduty:\${Region}:\${Account}:detector/\${DetectorId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_managing_access.html#guardduty-resources">filter</a></td>
                    <td>arn:\${Partition}:guardduty:\${Region}:\${Account}:detector/\${DetectorId}/filter/\${FilterName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_managing_access.html#guardduty-resources">ipset</a></td>
                    <td>arn:\${Partition}:guardduty:\${Region}:\${Account}:detector/\${DetectorId}/ipset/\${IPSetId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_managing_access.html#guardduty-resources">threatintelset</a></td>
                    <td>arn:\${Partition}:guardduty:\${Region}:\${Account}:detector/\${DetectorId}/threatintelset/\${ThreatIntelSetId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_managing_access.html#guardduty-resources">publishingDestination</a></td>
                    <td>arn:\${Partition}:guardduty:\${Region}:\${Account}:detector/\${DetectorId}/publishingDestination/\${PublishingDestinationId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS HealthLake</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awshealthlake.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DatastoreProperties.html">datastore</a></td>
                    <td>arn:\${Partition}:healthlake:\${Region}:\${Account}:datastore/fhir/\${DatastoreId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Glue DataBrew</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsgluedatabrew.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/databrew/latest/dg/projects.html">Project</a></td>
                    <td>arn:\${Partition}:databrew:\${Region}:\${Account}:project/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/databrew/latest/dg/datasets.html">Dataset</a></td>
                    <td>arn:\${Partition}:databrew:\${Region}:\${Account}:dataset/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/databrew/latest/dg/rulesets.html">Ruleset</a></td>
                    <td>arn:\${Partition}:databrew:\${Region}:\${Account}:ruleset/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/databrew/latest/dg/recipes.html">Recipe</a></td>
                    <td>arn:\${Partition}:databrew:\${Region}:\${Account}:recipe/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/databrew/latest/dg/jobs.html">Job</a></td>
                    <td>arn:\${Partition}:databrew:\${Region}:\${Account}:job/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/databrew/latest/dg/jobs.html#jobs.scheduling">Schedule</a></td>
                    <td>arn:\${Partition}:databrew:\${Region}:\${Account}:schedule/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS IAM Access Analyzer</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiamaccessanalyzer.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">Analyzer</a></td>
                    <td>arn:\${Partition}:access-analyzer:\${Region}:\${Account}:analyzer/\${AnalyzerName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">ArchiveRule</a></td>
                    <td>arn:\${Partition}:access-analyzer:\${Region}:\${Account}:analyzer/\${AnalyzerName}/archive-rule/\${RuleName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS IAM Identity Center OIDC service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiamidentitycenteroidcservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/get-started-enable-identity-center.html">Application</a></td>
                    <td>arn:\${Partition}:sso::\${AccountId}:application/\${InstanceId}/\${ApplicationId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Honeycode</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonhoneycode.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/honeycode/latest/UserGuide/resource-workbook.html">workbook</a></td>
                    <td>arn:\${Partition}:honeycode:\${Region}:\${Account}:workbook:workbook/\${WorkbookId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/honeycode/latest/UserGuide/resource-table.html">table</a></td>
                    <td>arn:\${Partition}:honeycode:\${Region}:\${Account}:table:workbook/\${WorkbookId}/table/\${TableId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/honeycode/latest/UserGuide/resource-screen.html">screen</a></td>
                    <td>arn:\${Partition}:honeycode:\${Region}:\${Account}:screen:workbook/\${WorkbookId}/app/\${AppId}/screen/\${ScreenId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/honeycode/latest/UserGuide/resource-screen-automation.html">screen-automation</a></td>
                    <td>arn:\${Partition}:honeycode:\${Region}:\${Account}:screen-automation:workbook/\${WorkbookId}/app/\${AppId}/screen/\${ScreenId}/automation/\${AutomationId}</td>
                </tr>
            </tbody>
        </table>
        <h1>High-volume outbound communications</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_high-volumeoutboundcommunications.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/connect/latest/adminguide/enable-high-volume-outbound-communications.html">campaign</a></td>
                    <td>arn:\${Partition}:connect-campaigns:\${Region}:\${Account}:campaign/\${CampaignId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Identity Sync</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsidentitysync.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/security-iam-awsmanpol.html">SyncProfileResource</a></td>
                    <td>arn:\${Partition}:identity-sync:\${Region}:\${Account}:profile/\${SyncProfileName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/security-iam-awsmanpol.html">SyncTargetResource</a></td>
                    <td>arn:\${Partition}:identity-sync:\${Region}:\${Account}:target/\${SyncProfileName}/\${SyncTargetName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS HealthOmics</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awshealthomics.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/omics/latest/api/API_AnnotationImportJobItem.html">AnnotationImportJob</a></td>
                    <td>arn:\${Partition}:omics:\${Region}:\${Account}:annotationImportJob/\${AnnotationImportJobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/omics/latest/api/API_AnnotationStoreItem.html">AnnotationStore</a></td>
                    <td>arn:\${Partition}:omics:\${Region}:\${Account}:annotationStore/\${AnnotationStoreId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/omics/latest/api/API_AnnotationStoreVersionItem.html">AnnotationStoreVersion</a></td>
                    <td>arn:\${Partition}:omics:\${Region}:\${Account}:annotationStore/\${AnnotationStoreName}/version/\${AnnotationStoreVersionName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/omics/latest/api/API_ReadSetFiles.html">readSet</a></td>
                    <td>arn:\${Partition}:omics:\${Region}:\${Account}:sequenceStore/\${SequenceStoreId}/readSet/\${ReadSetId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/omics/latest/api/API_ReferenceFiles.html">reference</a></td>
                    <td>arn:\${Partition}:omics:\${Region}:\${Account}:referenceStore/\${ReferenceStoreId}/reference/\${ReferenceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/omics/latest/api/API_ReferenceStoreDetail.html">referenceStore</a></td>
                    <td>arn:\${Partition}:omics:\${Region}:\${Account}:referenceStore/\${ReferenceStoreId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/omics/latest/api/API_RunListItem.html">run</a></td>
                    <td>arn:\${Partition}:omics:\${Region}:\${Account}:run/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/omics/latest/api/API_RunGroupListItem.html">runGroup</a></td>
                    <td>arn:\${Partition}:omics:\${Region}:\${Account}:runGroup/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/omics/latest/api/API_SequenceStoreDetail.html">sequenceStore</a></td>
                    <td>arn:\${Partition}:omics:\${Region}:\${Account}:sequenceStore/\${SequenceStoreId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/omics/latest/api/API_TagResource.html">TaggingResource</a></td>
                    <td>arn:\${Partition}:omics:\${Region}:\${Account}:tag/\${TagKey}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/omics/latest/api/API_TaskListItem.html">TaskResource</a></td>
                    <td>arn:\${Partition}:omics:\${Region}:\${Account}:task/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/omics/latest/api/API_VariantImportJobItem.html">VariantImportJob</a></td>
                    <td>arn:\${Partition}:omics:\${Region}:\${Account}:variantImportJob/\${VariantImportJobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/omics/latest/api/API_VariantStoreItem.html">VariantStore</a></td>
                    <td>arn:\${Partition}:omics:\${Region}:\${Account}:variantStore/\${VariantStoreId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/omics/latest/api/API_WorkflowListItem.html">workflow</a></td>
                    <td>arn:\${Partition}:omics:\${Region}:\${Account}:workflow/\${Id}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS IAM Identity Center (successor to AWS Single Sign-On) directory</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiamidentitycentersuccessortoawssinglesign-ondirectory.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS IAM Identity Center (successor to AWS Single Sign-On)</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiamidentitycentersuccessortoawssinglesign-on.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html">PermissionSet</a></td>
                    <td>arn:\${Partition}:sso:::permissionSet/\${InstanceId}/\${PermissionSetId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html">Account</a></td>
                    <td>arn:\${Partition}:sso:::account/\${AccountId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_InstanceMetadata.html">Instance</a></td>
                    <td>arn:\${Partition}:sso:::instance/\${InstanceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_Application.html">Application</a></td>
                    <td>arn:\${Partition}:sso::\${AccountId}:application/\${InstanceId}/\${ApplicationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_TrustedTokenIssuerMetadata.html">TrustedTokenIssuer</a></td>
                    <td>arn:\${Partition}:sso::\${AccountId}:trustedTokenIssuer/\${InstanceId}/\${TrustedTokenIssuerId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ApplicationProvider.html">ApplicationProvider</a></td>
                    <td>arn:\${Partition}:sso::aws:applicationProvider/\${ApplicationProviderId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Inspector</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoninspector.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Identity Store Auth</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsidentitystoreauth.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Identity Store</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsidentitystore.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/singlesignon/latest/">Identitystore</a></td>
                    <td>arn:\${Partition}:identitystore::\${Account}:identitystore/\${IdentityStoreId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/singlesignon/latest/">User</a></td>
                    <td>arn:\${Partition}:identitystore:::user/\${UserId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/singlesignon/latest/">Group</a></td>
                    <td>arn:\${Partition}:identitystore:::group/\${GroupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/singlesignon/latest/">GroupMembership</a></td>
                    <td>arn:\${Partition}:identitystore:::membership/\${MembershipId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/singlesignon/latest/">AllUsers</a></td>
                    <td>arn:\${Partition}:identitystore:::user/*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/singlesignon/latest/">AllGroups</a></td>
                    <td>arn:\${Partition}:identitystore:::group/*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/singlesignon/latest/">AllGroupMemberships</a></td>
                    <td>arn:\${Partition}:identitystore:::membership/*</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Import Export Disk Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsimportexportdiskservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Invoicing Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsinvoicingservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Identity and Access Management Roles Anywhere</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsidentityandaccessmanagementrolesanywhere.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html#first-time-user">trust-anchor</a></td>
                    <td>arn:\${Partition}:rolesanywhere:\${Region}:\${Account}:trust-anchor/\${TrustAnchorId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html#first-time-user">profile</a></td>
                    <td>arn:\${Partition}:rolesanywhere:\${Region}:\${Account}:profile/\${ProfileId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html#first-time-user">subject</a></td>
                    <td>arn:\${Partition}:rolesanywhere:\${Region}:\${Account}:subject/\${SubjectId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html#first-time-user">crl</a></td>
                    <td>arn:\${Partition}:rolesanywhere:\${Region}:\${Account}:crl/\${CrlId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon InspectorScan</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoninspectorscan.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Glue</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsglue.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html">catalog</a></td>
                    <td>arn:\${Partition}:glue:\${Region}:\${Account}:catalog</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html">database</a></td>
                    <td>arn:\${Partition}:glue:\${Region}:\${Account}:database/\${DatabaseName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html">table</a></td>
                    <td>arn:\${Partition}:glue:\${Region}:\${Account}:table/\${DatabaseName}/\${TableName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html">tableversion</a></td>
                    <td>arn:\${Partition}:glue:\${Region}:\${Account}:tableVersion/\${DatabaseName}/\${TableName}/\${TableVersionName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html">connection</a></td>
                    <td>arn:\${Partition}:glue:\${Region}:\${Account}:connection/\${ConnectionName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html">userdefinedfunction</a></td>
                    <td>arn:\${Partition}:glue:\${Region}:\${Account}:userDefinedFunction/\${DatabaseName}/\${UserDefinedFunctionName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html">devendpoint</a></td>
                    <td>arn:\${Partition}:glue:\${Region}:\${Account}:devEndpoint/\${DevEndpointName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html">job</a></td>
                    <td>arn:\${Partition}:glue:\${Region}:\${Account}:job/\${JobName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html">trigger</a></td>
                    <td>arn:\${Partition}:glue:\${Region}:\${Account}:trigger/\${TriggerName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html">crawler</a></td>
                    <td>arn:\${Partition}:glue:\${Region}:\${Account}:crawler/\${CrawlerName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html">workflow</a></td>
                    <td>arn:\${Partition}:glue:\${Region}:\${Account}:workflow/\${WorkflowName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html">blueprint</a></td>
                    <td>arn:\${Partition}:glue:\${Region}:\${Account}:blueprint/\${BlueprintName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html">mlTransform</a></td>
                    <td>arn:\${Partition}:glue:\${Region}:\${Account}:mlTransform/\${TransformId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html">registry</a></td>
                    <td>arn:\${Partition}:glue:\${Region}:\${Account}:registry/\${RegistryName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html">schema</a></td>
                    <td>arn:\${Partition}:glue:\${Region}:\${Account}:schema/\${SchemaName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html">session</a></td>
                    <td>arn:\${Partition}:glue:\${Region}:\${Account}:session/\${SessionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html">dataQualityRuleset</a></td>
                    <td>arn:\${Partition}:glue:\${Region}:\${Account}:dataQualityRuleset/\${RulesetName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html">customEntityType</a></td>
                    <td>arn:\${Partition}:glue:\${Region}:\${Account}:customEntityType/\${CustomEntityTypeId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html">completion</a></td>
                    <td>arn:\${Partition}:glue:\${Region}:\${Account}:completion/\${CompletionId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Interactive Video Service Chat</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoninteractivevideoservicechat.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_Room.html">Room</a></td>
                    <td>arn:\${Partition}:ivschat:\${Region}:\${Account}:room/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_LoggingConfiguration.html">Logging-Configuration</a></td>
                    <td>arn:\${Partition}:ivschat:\${Region}:\${Account}:logging-configuration/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Inspector2</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoninspector2.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html">Filter</a></td>
                    <td>arn:\${Partition}:inspector2:\${Region}:\${Account}:owner/\${OwnerId}/filter/\${FilterId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html">Finding</a></td>
                    <td>arn:\${Partition}:inspector2:\${Region}:\${Account}:finding/\${FindingId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html">CIS Scan Configuration</a></td>
                    <td>arn:\${Partition}:inspector2:\${Region}:\${Account}:owner/\${OwnerId}/cis-configuration/\${CISScanConfigurationId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Interactive Video Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoninteractivevideoservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_Channel.html">Channel</a></td>
                    <td>arn:\${Partition}:ivs:\${Region}:\${Account}:channel/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_StreamKey.html">Stream-Key</a></td>
                    <td>arn:\${Partition}:ivs:\${Region}:\${Account}:stream-key/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_PlaybackKeyPair.html">Playback-Key-Pair</a></td>
                    <td>arn:\${Partition}:ivs:\${Region}:\${Account}:playback-key/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_PlaybackRestrictionPolicy.html">Playback-Restriction-Policy</a></td>
                    <td>arn:\${Partition}:ivs:\${Region}:\${Account}:playback-restriction-policy/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_RecordingConfiguration.html">Recording-Configuration</a></td>
                    <td>arn:\${Partition}:ivs:\${Region}:\${Account}:recording-configuration/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_Stage.html">Stage</a></td>
                    <td>arn:\${Partition}:ivs:\${Region}:\${Account}:stage/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_Composition.html">Composition</a></td>
                    <td>arn:\${Partition}:ivs:\${Region}:\${Account}:composition/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_EncoderConfiguration.html">Encoder-Configuration</a></td>
                    <td>arn:\${Partition}:ivs:\${Region}:\${Account}:encoder-configuration/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_StorageConfiguration.html">Storage-Configuration</a></td>
                    <td>arn:\${Partition}:ivs:\${Region}:\${Account}:storage-configuration/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS IoT Device Tester</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotdevicetester.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS IoT 1-Click</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot1-click.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-1-click/1.0/devices-apireference/resources.html">device</a></td>
                    <td>arn:\${Partition}:iot1click:\${Region}:\${Account}:devices/\${DeviceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-1-click/latest/projects-apireference/API_Operations.html">project</a></td>
                    <td>arn:\${Partition}:iot1click:\${Region}:\${Account}:projects/\${ProjectName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS IoT Events</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotevents.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-getting-started.html">detectorModel</a></td>
                    <td>arn:\${Partition}:iotevents:\${Region}:\${Account}:detectorModel/\${DetectorModelName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-getting-started.html">alarmModel</a></td>
                    <td>arn:\${Partition}:iotevents:\${Region}:\${Account}:alarmModel/\${AlarmModelName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-getting-started.html">input</a></td>
                    <td>arn:\${Partition}:iotevents:\${Region}:\${Account}:input/\${InputName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS IoT Fleet Hub for Device Management</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotfleethubfordevicemanagement.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/apireference/API_iotfleethub_ApplicationSummary.html">application</a></td>
                    <td>arn:\${Partition}:iotfleethub:\${Region}:\${Account}:application/\${ApplicationId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS IoT Jobs DataPlane</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotjobsdataplane.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html">thing</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:thing/\${ThingName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Identity and Access Management (IAM)</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsidentityandaccessmanagementiam.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor-view-data-orgs.html">access-report</a></td>
                    <td>arn:\${Partition}:iam::\${Account}:access-report/\${EntityPath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html">assumed-role</a></td>
                    <td>arn:\${Partition}:iam::\${Account}:assumed-role/\${RoleName}/\${RoleSessionName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html">federated-user</a></td>
                    <td>arn:\${Partition}:iam::\${Account}:federated-user/\${UserName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html">group</a></td>
                    <td>arn:\${Partition}:iam::\${Account}:group/\${GroupNameWithPath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html">instance-profile</a></td>
                    <td>arn:\${Partition}:iam::\${Account}:instance-profile/\${InstanceProfileNameWithPath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html">mfa</a></td>
                    <td>arn:\${Partition}:iam::\${Account}:mfa/\${MfaTokenIdWithPath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html">oidc-provider</a></td>
                    <td>arn:\${Partition}:iam::\${Account}:oidc-provider/\${OidcProviderName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html">policy</a></td>
                    <td>arn:\${Partition}:iam::\${Account}:policy/\${PolicyNameWithPath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html">role</a></td>
                    <td>arn:\${Partition}:iam::\${Account}:role/\${RoleNameWithPath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html">saml-provider</a></td>
                    <td>arn:\${Partition}:iam::\${Account}:saml-provider/\${SamlProviderName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html">server-certificate</a></td>
                    <td>arn:\${Partition}:iam::\${Account}:server-certificate/\${CertificateNameWithPath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html">sms-mfa</a></td>
                    <td>arn:\${Partition}:iam::\${Account}:sms-mfa/\${MfaTokenIdWithPath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html">user</a></td>
                    <td>arn:\${Partition}:iam::\${Account}:user/\${UserNameWithPath}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS IoT Analytics</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotanalytics.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/iotanalytics/latest/userguide/welcome.html#aws-iot-analytics-how">channel</a></td>
                    <td>arn:\${Partition}:iotanalytics:\${Region}:\${Account}:channel/\${ChannelName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iotanalytics/latest/userguide/welcome.html#aws-iot-analytics-how">dataset</a></td>
                    <td>arn:\${Partition}:iotanalytics:\${Region}:\${Account}:dataset/\${DatasetName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iotanalytics/latest/userguide/welcome.html#aws-iot-analytics-how">datastore</a></td>
                    <td>arn:\${Partition}:iotanalytics:\${Region}:\${Account}:datastore/\${DatastoreName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iotanalytics/latest/userguide/welcome.html#aws-iot-analytics-how">pipeline</a></td>
                    <td>arn:\${Partition}:iotanalytics:\${Region}:\${Account}:pipeline/\${PipelineName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS IoT Core Device Advisor</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotcoredeviceadvisor.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-workflow.html#device-advisor-workflow-create-suite-definition">Suitedefinition</a></td>
                    <td>arn:\${Partition}:iotdeviceadvisor:\${Region}:\${Account}:suitedefinition/\${SuiteDefinitionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-workflow.html#device-advisor-workflow-start-suite-run">Suiterun</a></td>
                    <td>arn:\${Partition}:iotdeviceadvisor:\${Region}:\${Account}:suiterun/\${SuiteDefinitionId}/\${SuiteRunId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS IoT Greengrass V2</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotgreengrassv2.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ConnectivityInfo.html">connectivityInfo</a></td>
                    <td>arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/things/\${ThingName}/connectivityInfo</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/greengrass/v2/APIReference/API_Component.html">component</a></td>
                    <td>arn:\${Partition}:greengrass:\${Region}:\${Account}:components:\${ComponentName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/greengrass/v2/APIReference/API_Component.html">componentVersion</a></td>
                    <td>arn:\${Partition}:greengrass:\${Region}:\${Account}:components:\${ComponentName}:versions:\${ComponentVersion}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/greengrass/v2/APIReference/API_CoreDevice.html">coreDevice</a></td>
                    <td>arn:\${Partition}:greengrass:\${Region}:\${Account}:coreDevices:\${CoreDeviceThingName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/greengrass/v2/APIReference/API_Deployment.html">deployment</a></td>
                    <td>arn:\${Partition}:greengrass:\${Region}:\${Account}:deployments:\${DeploymentId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS IoT RoboRunner</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotroborunner.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/iotroborunner/latest/api/">DestinationResource</a></td>
                    <td>arn:\${Partition}:iotroborunner:\${Region}:\${Account}:site/\${SiteId}/destination/\${DestinationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iotroborunner/latest/api/">SiteResource</a></td>
                    <td>arn:\${Partition}:iotroborunner:\${Region}:\${Account}:site/\${SiteId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iotroborunner/latest/api/">WorkerFleetResource</a></td>
                    <td>arn:\${Partition}:iotroborunner:\${Region}:\${Account}:site/\${SiteId}/worker-fleet/\${WorkerFleetId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iotroborunner/latest/api/">WorkerResource</a></td>
                    <td>arn:\${Partition}:iotroborunner:\${Region}:\${Account}:site/\${SiteId}/worker-fleet/\${WorkerFleetId}/worker/\${WorkerId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS IoT FleetWise</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotfleetwise.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/campaigns.html">campaign</a></td>
                    <td>arn:\${Partition}:iotfleetwise:\${Region}:\${Account}:campaign/\${CampaignName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/decoder-manifests.html">decodermanifest</a></td>
                    <td>arn:\${Partition}:iotfleetwise:\${Region}:\${Account}:decoder-manifest/\${Name}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleets.html">fleet</a></td>
                    <td>arn:\${Partition}:iotfleetwise:\${Region}:\${Account}:fleet/\${FleetId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/vehicle-models.html">modelmanifest</a></td>
                    <td>arn:\${Partition}:iotfleetwise:\${Region}:\${Account}:model-manifest/\${Name}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/signal-catalogs.html">signalcatalog</a></td>
                    <td>arn:\${Partition}:iotfleetwise:\${Region}:\${Account}:signal-catalog/\${Name}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/vehicles.html">vehicle</a></td>
                    <td>arn:\${Partition}:iotfleetwise:\${Region}:\${Account}:vehicle/\${VehicleId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS IQ Permissions</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiqpermissions.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://aws.amazon.com/iq/">permission</a></td>
                    <td>arn:\${Partition}:iq-permission:\${Region}::permission/\${PermissionRequestId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS IoT TwinMaker</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiottwinmaker.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CreateWorkspace.html">workspace</a></td>
                    <td>arn:\${Partition}:iottwinmaker:\${Region}:\${Account}:workspace/\${WorkspaceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CreateEntity.html">entity</a></td>
                    <td>arn:\${Partition}:iottwinmaker:\${Region}:\${Account}:workspace/\${WorkspaceId}/entity/\${EntityId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CreateComponentType.html">componentType</a></td>
                    <td>arn:\${Partition}:iottwinmaker:\${Region}:\${Account}:workspace/\${WorkspaceId}/component-type/\${ComponentTypeId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CreateScene.html">scene</a></td>
                    <td>arn:\${Partition}:iottwinmaker:\${Region}:\${Account}:workspace/\${WorkspaceId}/scene/\${SceneId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CreateSyncJob.html">syncJob</a></td>
                    <td>arn:\${Partition}:iottwinmaker:\${Region}:\${Account}:workspace/\${WorkspaceId}/sync-job/\${SyncJobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CreateMetadataTransferJob.html">metadataTransferJob</a></td>
                    <td>arn:\${Partition}:iottwinmaker:\${Region}:\${Account}:metadata-transfer-job/\${MetadataTransferJobId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Keyspaces (for Apache Cassandra)</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkeyspacesforapachecassandra.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/what-is.html">keyspace</a></td>
                    <td>arn:\${Partition}:cassandra:\${Region}:\${Account}:/keyspace/\${KeyspaceName}/</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/what-is.html">table</a></td>
                    <td>arn:\${Partition}:cassandra:\${Region}:\${Account}:/keyspace/\${KeyspaceName}/table/\${TableName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS IoT Wireless</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotwireless.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_CreateWirelessDevice.html">WirelessDevice</a></td>
                    <td>arn:\${Partition}:iotwireless:\${Region}:\${Account}:WirelessDevice/\${WirelessDeviceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_CreateWirelessGateway.html">WirelessGateway</a></td>
                    <td>arn:\${Partition}:iotwireless:\${Region}:\${Account}:WirelessGateway/\${WirelessGatewayId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_CreateDeviceProfile.html">DeviceProfile</a></td>
                    <td>arn:\${Partition}:iotwireless:\${Region}:\${Account}:DeviceProfile/\${DeviceProfileId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_CreateServiceProfile.html">ServiceProfile</a></td>
                    <td>arn:\${Partition}:iotwireless:\${Region}:\${Account}:ServiceProfile/\${ServiceProfileId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_CreateDestination.html">Destination</a></td>
                    <td>arn:\${Partition}:iotwireless:\${Region}:\${Account}:Destination/\${DestinationName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_AssociateAwsAccountWithPartnerAccount.html">SidewalkAccount</a></td>
                    <td>arn:\${Partition}:iotwireless:\${Region}:\${Account}:SidewalkAccount/\${SidewalkAccountId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_CreateWirelessGatewayTaskDefinition.html">WirelessGatewayTaskDefinition</a></td>
                    <td>arn:\${Partition}:iotwireless:\${Region}:\${Account}:WirelessGatewayTaskDefinition/\${WirelessGatewayTaskDefinitionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_CreateFuotaTask.html">FuotaTask</a></td>
                    <td>arn:\${Partition}:iotwireless:\${Region}:\${Account}:FuotaTask/\${FuotaTaskId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_CreateMulticastGroup.html">MulticastGroup</a></td>
                    <td>arn:\${Partition}:iotwireless:\${Region}:\${Account}:MulticastGroup/\${MulticastGroupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_CreateNetworkAnalyzerConfiguration.html">NetworkAnalyzerConfiguration</a></td>
                    <td>arn:\${Partition}:iotwireless:\${Region}:\${Account}:NetworkAnalyzerConfiguration/\${NetworkAnalyzerConfigurationName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html">thing</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:thing/\${ThingName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/x509-client-certs.html">cert</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:cert/\${Certificate}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_StartWirelessDeviceImportTask.html">ImportTask</a></td>
                    <td>arn:\${Partition}:iotwireless:\${Region}:\${Account}:ImportTask/\${ImportTaskId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS IoT Greengrass</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotgreengrass.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-connectivityinfo.html">connectivityInfo</a></td>
                    <td>arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/things/\${ThingName}/connectivityInfo</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/greengrass/latest/developerguide/gg-sec.html">certificateAuthority</a></td>
                    <td>arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/groups/\${GroupId}/certificateauthorities/\${CertificateAuthorityId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-createdeploymentrequest.html">deployment</a></td>
                    <td>arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/groups/\${GroupId}/deployments/\${DeploymentId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/greengrass/latest/developerguide/bulk-deploy-cli.html">bulkDeployment</a></td>
                    <td>arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/bulk/deployments/\${BulkDeploymentId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-groupinformation.html">group</a></td>
                    <td>arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/groups/\${GroupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-groupversion.html">groupVersion</a></td>
                    <td>arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/groups/\${GroupId}/versions/\${VersionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-core.html">coreDefinition</a></td>
                    <td>arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/cores/\${CoreDefinitionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-coredefinitionversion.html">coreDefinitionVersion</a></td>
                    <td>arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/cores/\${CoreDefinitionId}/versions/\${VersionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-device.html">deviceDefinition</a></td>
                    <td>arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/devices/\${DeviceDefinitionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-devicedefinitionversion.html">deviceDefinitionVersion</a></td>
                    <td>arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/devices/\${DeviceDefinitionId}/versions/\${VersionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-function.html">functionDefinition</a></td>
                    <td>arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/functions/\${FunctionDefinitionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-functiondefinitionversion.html">functionDefinitionVersion</a></td>
                    <td>arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/functions/\${FunctionDefinitionId}/versions/\${VersionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-subscription.html">subscriptionDefinition</a></td>
                    <td>arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/subscriptions/\${SubscriptionDefinitionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-subscriptiondefinitionversion.html">subscriptionDefinitionVersion</a></td>
                    <td>arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/subscriptions/\${SubscriptionDefinitionId}/versions/\${VersionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-logger.html">loggerDefinition</a></td>
                    <td>arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/loggers/\${LoggerDefinitionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-loggerdefinitionversion.html">loggerDefinitionVersion</a></td>
                    <td>arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/loggers/\${LoggerDefinitionId}/versions/\${VersionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-resource.html">resourceDefinition</a></td>
                    <td>arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/resources/\${ResourceDefinitionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-resourcedefinitionversion.html">resourceDefinitionVersion</a></td>
                    <td>arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/resources/\${ResourceDefinitionId}/versions/\${VersionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-connector.html">connectorDefinition</a></td>
                    <td>arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/connectors/\${ConnectorDefinitionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-connectordefinitionversion.html">connectorDefinitionVersion</a></td>
                    <td>arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/connectors/\${ConnectorDefinitionId}/versions/\${VersionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html">thing</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:thing/\${ThingName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html">thingRuntimeConfig</a></td>
                    <td>arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/things/\${ThingName}/runtimeconfig</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS IoT SiteWise</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotsitewise.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAsset.html">asset</a></td>
                    <td>arn:\${Partition}:iotsitewise:\${Region}:\${Account}:asset/\${AssetId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModel.html">asset-model</a></td>
                    <td>arn:\${Partition}:iotsitewise:\${Region}:\${Account}:asset-model/\${AssetModelId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeTimeSeries.html">time-series</a></td>
                    <td>arn:\${Partition}:iotsitewise:\${Region}:\${Account}:time-series/\${TimeSeriesId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateGateway.html">gateway</a></td>
                    <td>arn:\${Partition}:iotsitewise:\${Region}:\${Account}:gateway/\${GatewayId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreatePortal.html">portal</a></td>
                    <td>arn:\${Partition}:iotsitewise:\${Region}:\${Account}:portal/\${PortalId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateProject.html">project</a></td>
                    <td>arn:\${Partition}:iotsitewise:\${Region}:\${Account}:project/\${ProjectId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateDashboard.html">dashboard</a></td>
                    <td>arn:\${Partition}:iotsitewise:\${Region}:\${Account}:dashboard/\${DashboardId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAccessPolicy.html">access-policy</a></td>
                    <td>arn:\${Partition}:iotsitewise:\${Region}:\${Account}:access-policy/\${AccessPolicyId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Kinesis Analytics</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkinesisanalytics.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works.html">application</a></td>
                    <td>arn:\${Partition}:kinesisanalytics:\${Region}:\${Account}:application/\${ApplicationName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Kinesis Data Streams</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkinesisdatastreams.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/kinesis/latest/dev/amazon-kinesis-streams.html">stream</a></td>
                    <td>arn:\${Partition}:kinesis:\${Region}:\${Account}:stream/\${StreamName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/kinesis/latest/dev/amazon-kinesis-consumers.html">consumer</a></td>
                    <td>arn:\${Partition}:kinesis:\${Region}:\${Account}:\${StreamType}/\${StreamName}/consumer/\${ConsumerName}:\${ConsumerCreationTimpstamp}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/kinesis/latest/dev/concepts.html#kms_keys">kmsKey</a></td>
                    <td>arn:\${Partition}:kms:\${Region}:\${Account}:key/\${KeyId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Kinesis Analytics V2</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkinesisanalyticsv2.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/kinesisanalytics/latest/java/how-it-works.html">application</a></td>
                    <td>arn:\${Partition}:kinesisanalytics:\${Region}:\${Account}:application/\${ApplicationName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS IoT</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-message-broker.html">client</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:client/\${ClientId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-indexing.html">index</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:index/\${IndexName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-indexing.html">fleetmetric</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:fleetmetric/\${FleetMetricName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-jobs.html">job</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:job/\${JobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/job-templates.html">jobtemplate</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:jobtemplate/\${JobTemplateId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-tunnels.html">tunnel</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:tunnel/\${TunnelId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html">thing</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:thing/\${ThingName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/thing-groups.html">thinggroup</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:thinggroup/\${ThingGroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/billing-groups.html">billinggroup</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:billinggroup/\${BillingGroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/dynamic-thing-groups.html">dynamicthinggroup</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:thinggroup/\${ThingGroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/thing-types.html">thingtype</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:thingtype/\${ThingTypeName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-message-broker.html">topic</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:topic/\${TopicName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/topics.html">topicfilter</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:topicfilter/\${TopicFilter}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/authorizing-direct-aws.html">rolealias</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:rolealias/\${RoleAlias}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/custom-authorizer.html">authorizer</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:authorizer/\${AuthorizerName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html">policy</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:policy/\${PolicyName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/x509-certs.html">cert</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:cert/\${Certificate}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/x509-certs.html">cacert</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:cacert/\${CACertificate}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/freertos/latest/userguide/freertos-ota-dev.html">stream</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:stream/\${StreamId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/freertos/latest/userguide/freertos-ota-dev.html">otaupdate</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:otaupdate/\${OtaUpdateId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-audit.html">scheduledaudit</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:scheduledaudit/\${ScheduleName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-mitigation-actions.html">mitigationaction</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:mitigationaction/\${MitigationActionName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-detect.html">securityprofile</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:securityprofile/\${SecurityProfileName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-detect.html">custommetric</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:custommetric/\${MetricName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-detect.html">dimension</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:dimension/\${DimensionName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html">rule</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:rule/\${RuleName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/rule-destination.html">destination</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:destination/\${DestinationType}/\${Uuid}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/provision-template.html">provisioningtemplate</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:provisioningtemplate/\${ProvisioningTemplate}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/domain-configuration.html">domainconfiguration</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:domainconfiguration/\${DomainConfigurationName}/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/software-package-catalog.html">package</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:package/\${PackageName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/software-package-catalog.html">packageversion</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:package/\${PackageName}/version/\${VersionName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/provisioning-cert-provider.html">certificateprovider</a></td>
                    <td>arn:\${Partition}:iot:\${Region}:\${Account}:certificateprovider/\${CertificateProviderName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS IQ</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiq.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://aws.amazon.com/iq/">conversation</a></td>
                    <td>arn:\${Partition}:iq:\${Region}::conversation/\${ConversationId}</td>
                </tr>
               <tr>
                    <td><a href="https://aws.amazon.com/iq/">buyer</a></td>
                    <td>arn:\${Partition}:iq:\${Region}::buyer/\${BuyerId}</td>
                </tr>
               <tr>
                    <td><a href="https://aws.amazon.com/iq/">expert</a></td>
                    <td>arn:\${Partition}:iq:\${Region}::expert/\${ExpertId}</td>
                </tr>
               <tr>
                    <td><a href="https://aws.amazon.com/iq/">call</a></td>
                    <td>arn:\${Partition}:iq:\${Region}::call/\${CallId}</td>
                </tr>
               <tr>
                    <td><a href="https://aws.amazon.com/iq/">token</a></td>
                    <td>arn:\${Partition}:iq:\${Region}::token/\${TokenId}</td>
                </tr>
               <tr>
                    <td><a href="https://aws.amazon.com/iq/">proposal</a></td>
                    <td>arn:\${Partition}:iq:\${Region}::proposal/\${ConversationId}/\${ProposalId}</td>
                </tr>
               <tr>
                    <td><a href="https://aws.amazon.com/iq/">paymentRequest</a></td>
                    <td>arn:\${Partition}:iq:\${Region}::paymentRequest/\${ConversationId}/\${ProposalId}/\${PaymentRequestId}</td>
                </tr>
               <tr>
                    <td><a href="https://aws.amazon.com/iq/">paymentSchedule</a></td>
                    <td>arn:\${Partition}:iq:\${Region}::paymentSchedule/\${ConversationId}/\${ProposalId}/\${VersionId}</td>
                </tr>
               <tr>
                    <td><a href="https://aws.amazon.com/iq/">seller</a></td>
                    <td>arn:\${Partition}:iq:\${Region}::seller/\${SellerAwsAccountId}</td>
                </tr>
               <tr>
                    <td><a href="https://aws.amazon.com/iq/">company</a></td>
                    <td>arn:\${Partition}:iq:\${Region}::company/\${CompanyId}</td>
                </tr>
               <tr>
                    <td><a href="https://aws.amazon.com/iq/">request</a></td>
                    <td>arn:\${Partition}:iq:\${Region}::request/\${RequestId}</td>
                </tr>
               <tr>
                    <td><a href="https://aws.amazon.com/iq/">listing</a></td>
                    <td>arn:\${Partition}:iq:\${Region}::listing/\${ListingId}</td>
                </tr>
               <tr>
                    <td><a href="https://aws.amazon.com/iq/">attachment</a></td>
                    <td>arn:\${Partition}:iq:\${Region}::attachment/\${AttachmentId}</td>
                </tr>
               <tr>
                    <td><a href="https://aws.amazon.com/iq/">permission</a></td>
                    <td>arn:\${Partition}:iq-permission:\${Region}::permission/\${PermissionRequestId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Kendra Intelligent Ranking</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkendraintelligentranking.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/kendra/latest/dg/search-service-rerank.html">rescore-execution-plan</a></td>
                    <td>arn:\${Partition}:kendra-ranking:\${Region}:\${Account}:rescore-execution-plan/\${RescoreExecutionPlanId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Kendra</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkendra.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/kendra/latest/dg/index.html">index</a></td>
                    <td>arn:\${Partition}:kendra:\${Region}:\${Account}:index/\${IndexId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/kendra/latest/dg/data-source.html">data-source</a></td>
                    <td>arn:\${Partition}:kendra:\${Region}:\${Account}:index/\${IndexId}/data-source/\${DataSourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/kendra/latest/dg/faq.html">faq</a></td>
                    <td>arn:\${Partition}:kendra:\${Region}:\${Account}:index/\${IndexId}/faq/\${FaqId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html">experience</a></td>
                    <td>arn:\${Partition}:kendra:\${Region}:\${Account}:index/\${IndexId}/experience/\${ExperienceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/kendra/latest/dg/thesaurus.html">thesaurus</a></td>
                    <td>arn:\${Partition}:kendra:\${Region}:\${Account}:index/\${IndexId}/thesaurus/\${ThesaurusId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/kendra/latest/dg/query-suggestions-block-list.html">query-suggestions-block-list</a></td>
                    <td>arn:\${Partition}:kendra:\${Region}:\${Account}:index/\${IndexId}/query-suggestions-block-list/\${QuerySuggestionsBlockListId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/kendra/latest/dg/featured-results.html">featured-results-set</a></td>
                    <td>arn:\${Partition}:kendra:\${Region}:\${Account}:index/\${IndexId}/featured-results-set/\${FeaturedResultsSetId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/kendra/latest/dg/API_CreateAccessControlConfiguration.html">access-control-configuration</a></td>
                    <td>arn:\${Partition}:kendra:\${Region}:\${Account}:index/\${IndexId}/access-control-configuration/\${AccessControlConfigurationId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Key Management Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awskeymanagementservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#alias-concept">alias</a></td>
                    <td>arn:\${Partition}:kms:\${Region}:\${Account}:alias/\${Alias}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms_keys">key</a></td>
                    <td>arn:\${Partition}:kms:\${Region}:\${Account}:key/\${KeyId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Launch Wizard</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awslaunchwizard.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon Kinesis Firehose</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkinesisfirehose.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/firehose/latest/dev/basic-create.html">deliverystream</a></td>
                    <td>arn:\${Partition}:firehose:\${Region}:\${Account}:deliverystream/\${DeliveryStreamName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Lake Formation</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awslakeformation.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon Lex</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonlex.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/lex/latest/dg/API_BotMetadata.html">bot</a></td>
                    <td>arn:\${Partition}:lex:\${Region}:\${Account}:bot:\${BotName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lex/latest/dg/API_BotMetadata.html">bot version</a></td>
                    <td>arn:\${Partition}:lex:\${Region}:\${Account}:bot:\${BotName}:\${BotVersion}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lex/latest/dg/API_BotAliasMetadata.html">bot alias</a></td>
                    <td>arn:\${Partition}:lex:\${Region}:\${Account}:bot:\${BotName}:\${BotAlias}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lex/latest/dg/API_BotChannelAssociation.html">channel</a></td>
                    <td>arn:\${Partition}:lex:\${Region}:\${Account}:bot-channel:\${BotName}:\${BotAlias}:\${ChannelName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lex/latest/dg/API_Intent.html">intent version</a></td>
                    <td>arn:\${Partition}:lex:\${Region}:\${Account}:intent:\${IntentName}:\${IntentVersion}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lex/latest/dg/API_SlotTypeMetadata.html">slottype version</a></td>
                    <td>arn:\${Partition}:lex:\${Region}:\${Account}:slottype:\${SlotName}:\${SlotVersion}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Kinesis Video Streams</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkinesisvideostreams.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-it-works.html">stream</a></td>
                    <td>arn:\${Partition}:kinesisvideo:\${Region}:\${Account}:stream/\${StreamName}/\${CreationTime}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-how-it-works.html">channel</a></td>
                    <td>arn:\${Partition}:kinesisvideo:\${Region}:\${Account}:channel/\${ChannelName}/\${CreationTime}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Lex V2</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonlexv2.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-it-works.html">bot</a></td>
                    <td>arn:\${Partition}:lex:\${Region}:\${Account}:bot/\${BotId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-it-works.html">bot alias</a></td>
                    <td>arn:\${Partition}:lex:\${Region}:\${Account}:bot-alias/\${BotId}/\${BotAliasId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lexv2/latest/dg/test-workbench.html">test set</a></td>
                    <td>arn:\${Partition}:lex:\${Region}:\${Account}:test-set/\${TestSetId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS License Manager User Subscriptions</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awslicensemanagerusersubscriptions.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Lambda</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awslambda.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html">code signing config</a></td>
                    <td>arn:\${Partition}:lambda:\${Region}:\${Account}:code-signing-config:\${CodeSigningConfigId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html">eventSourceMapping</a></td>
                    <td>arn:\${Partition}:lambda:\${Region}:\${Account}:event-source-mapping:\${UUID}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html">function</a></td>
                    <td>arn:\${Partition}:lambda:\${Region}:\${Account}:function:\${FunctionName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html">function alias</a></td>
                    <td>arn:\${Partition}:lambda:\${Region}:\${Account}:function:\${FunctionName}:\${Alias}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html">function version</a></td>
                    <td>arn:\${Partition}:lambda:\${Region}:\${Account}:function:\${FunctionName}:\${Version}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html">layer</a></td>
                    <td>arn:\${Partition}:lambda:\${Region}:\${Account}:layer:\${LayerName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html">layerVersion</a></td>
                    <td>arn:\${Partition}:lambda:\${Region}:\${Account}:layer:\${LayerName}:\${LayerVersion}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS License Manager Linux Subscriptions Manager</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awslicensemanagerlinuxsubscriptionsmanager.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon Lookout for Equipment</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonlookoutforequipment.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/dataset.html">dataset</a></td>
                    <td>arn:\${Partition}:lookoutequipment:\${Region}:\${Account}:dataset/\${DatasetName}/\${DatasetId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/model.html">model</a></td>
                    <td>arn:\${Partition}:lookoutequipment:\${Region}:\${Account}:model/\${ModelName}/\${ModelId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/model-version.html">model-version</a></td>
                    <td>arn:\${Partition}:lookoutequipment:\${Region}:\${Account}:model/\${ModelName}/\${ModelId}/model-version/\${ModelVersionNumber}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/inference-scheduler.html">inference-scheduler</a></td>
                    <td>arn:\${Partition}:lookoutequipment:\${Region}:\${Account}:inference-scheduler/\${InferenceSchedulerName}/\${InferenceSchedulerId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/label-group.html">label-group</a></td>
                    <td>arn:\${Partition}:lookoutequipment:\${Region}:\${Account}:label-group/\${LabelGroupName}/\${LabelGroupId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Lookout for Vision</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonlookoutforvision.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/lookout-for-vision/latest/developer-guide/model-create-project.html">model</a></td>
                    <td>arn:\${Partition}:lookoutvision:\${Region}:\${Account}:model/\${ProjectName}/\${ModelVersion}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lookout-for-vision/latest/developer-guide/model-create-project.html">project</a></td>
                    <td>arn:\${Partition}:lookoutvision:\${Region}:\${Account}:project/\${ProjectName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS License Manager</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awslicensemanager.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/license-manager/latest/userguide/license-configurations.html">license-configuration</a></td>
                    <td>arn:\${Partition}:license-manager:\${Region}:\${Account}:license-configuration:\${LicenseConfigurationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/license-manager/latest/userguide/seller-issued-licenses.html">license</a></td>
                    <td>arn:\${Partition}:license-manager::\${Account}:license:\${LicenseId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/license-manager/latest/userguide/granted-licenses.html">grant</a></td>
                    <td>arn:\${Partition}:license-manager::\${Account}:grant:\${GrantId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/license-manager/latest/userguide/report-generators.html">report-generator</a></td>
                    <td>arn:\${Partition}:license-manager:\${Region}:\${Account}:report-generator:\${ReportGeneratorId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon EC2</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html">elastic-ip</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:elastic-ip/\${AllocationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format">capacity-reservation-fleet</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:capacity-reservation-fleet/\${CapacityReservationFleetId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html">capacity-reservation</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:capacity-reservation/\${CapacityReservationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/userguide/Carrier_Gateway.html">carrier-gateway</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:carrier-gateway/\${CarrierGatewayId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/acm/latest/userguide/authen-overview.html#acm-resources-operations">certificate</a></td>
                    <td>arn:\${Partition}:acm:\${Region}:\${Account}:certificate/\${CertificateId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html">client-vpn-endpoint</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:client-vpn-endpoint/\${ClientVpnEndpointId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html">customer-gateway</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:customer-gateway/\${CustomerGatewayId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-overview.html">dedicated-host</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:dedicated-host/\${DedicatedHostId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html">dhcp-options</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:dhcp-options/\${DhcpOptionsId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/userguide/egress-only-internet-gateway.html">egress-only-internet-gateway</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:egress-only-internet-gateway/\${EgressOnlyInternetGatewayId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/elastic-gpus.html">elastic-gpu</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:elastic-gpu/\${ElasticGpuId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/elastic-inference/latest/developerguide/what-is-ei.html">elastic-inference</a></td>
                    <td>arn:\${Partition}:elastic-inference:\${Region}:\${Account}:elastic-inference-accelerator/\${AcceleratorId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-image-import.html#export-vm-image">export-image-task</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:export-image-task/\${ExportImageTaskId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport.html">export-instance-task</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:export-instance-task/\${ExportTaskId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet.html">fleet</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:fleet/\${FleetId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format">fpga-image</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:fpga-image/\${FpgaImageId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format">host-reservation</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:host-reservation/\${HostReservationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html">image</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}::image/\${ImageId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-image-import.html#import-vm-image">import-image-task</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:import-image-task/\${ImportImageTaskId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-import-snapshot.html">import-snapshot-task</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:import-snapshot-task/\${ImportSnapshotTaskId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format">instance-connect-endpoint</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:instance-connect-endpoint/\${InstanceConnectEndpointId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format">instance-event-window</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:instance-event-window/\${InstanceEventWindowId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Instances.html">instance</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:instance/\${InstanceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html">internet-gateway</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:internet-gateway/\${InternetGatewayId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format">ipam</a></td>
                    <td>arn:\${Partition}:ec2::\${Account}:ipam/\${IpamId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format">ipam-pool</a></td>
                    <td>arn:\${Partition}:ec2::\${Account}:ipam-pool/\${IpamPoolId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format">ipam-resource-discovery-association</a></td>
                    <td>arn:\${Partition}:ec2::\${Account}:ipam-resource-discovery-association/\${IpamResourceDiscoveryAssociationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format">ipam-resource-discovery</a></td>
                    <td>arn:\${Partition}:ec2::\${Account}:ipam-resource-discovery/\${IpamResourceDiscoveryId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format">ipam-scope</a></td>
                    <td>arn:\${Partition}:ec2::\${Account}:ipam-scope/\${IpamScopeId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format">coip-pool</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:coip-pool/\${Ipv4PoolCoipId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#ip-addressing-eips">ipv4pool-ec2</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:ipv4pool-ec2/\${Ipv4PoolEc2Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#ipv6-addressing">ipv6pool-ec2</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:ipv6pool-ec2/\${Ipv6PoolEc2Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html">key-pair</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:key-pair/\${KeyPairName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html">launch-template</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:launch-template/\${LaunchTemplateId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/license-manager/latest/userguide/create-license-configuration.html">license-configuration</a></td>
                    <td>arn:\${Partition}:license-manager:\${Region}:\${Account}:license-configuration:\${LicenseConfigurationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html#lgw">local-gateway</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:local-gateway/\${LocalGatewayId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html">local-gateway-route-table-virtual-interface-group-association</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:local-gateway-route-table-virtual-interface-group-association/\${LocalGatewayRouteTableVirtualInterfaceGroupAssociationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html#vpc-associations">local-gateway-route-table-vpc-association</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:local-gateway-route-table-vpc-association/\${LocalGatewayRouteTableVpcAssociationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html#route-tables">local-gateway-route-table</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:local-gateway-route-table/\${LocalGatewayRoutetableId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html">local-gateway-virtual-interface-group</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:local-gateway-virtual-interface-group/\${LocalGatewayVirtualInterfaceGroupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html">local-gateway-virtual-interface</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:local-gateway-virtual-interface/\${LocalGatewayVirtualInterfaceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html">natgateway</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:natgateway/\${NatGatewayId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html">network-acl</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:network-acl/\${NaclId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format">network-insights-access-scope-analysis</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:network-insights-access-scope-analysis/\${NetworkInsightsAccessScopeAnalysisId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format">network-insights-access-scope</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:network-insights-access-scope/\${NetworkInsightsAccessScopeId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format">network-insights-analysis</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:network-insights-analysis/\${NetworkInsightsAnalysisId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format">network-insights-path</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:network-insights-path/\${NetworkInsightsPathId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html">network-interface</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:network-interface/\${NetworkInterfaceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html">placement-group</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:placement-group/\${PlacementGroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/userguide/managed-prefix-lists.html">prefix-list</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:prefix-list/\${PrefixListId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/replace-root.html">replace-root-volume-task</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:replace-root-volume-task/\${ReplaceRootVolumeTaskId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html">reserved-instances</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:reserved-instances/\${ReservationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html">group</a></td>
                    <td>arn:\${Partition}:resource-groups:\${Region}:\${Account}:group/\${GroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html">role</a></td>
                    <td>arn:\${Partition}:iam::\${Account}:role/\${RoleNameWithPath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html">route-table</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:route-table/\${RouteTableId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html">security-group</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:security-group/\${SecurityGroupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format">security-group-rule</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:security-group-rule/\${SecurityGroupRuleId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html">snapshot</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}::snapshot/\${SnapshotId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format">spot-fleet-request</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:spot-fleet-request/\${SpotFleetRequestId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html">spot-instances-request</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:spot-instances-request/\${SpotInstanceRequestId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/userguide/subnet-cidr-reservation.html">subnet-cidr-reservation</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:subnet-cidr-reservation/\${SubnetCidrReservationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html">subnet</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:subnet/\${SubnetId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-filter.html">traffic-mirror-filter</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:traffic-mirror-filter/\${TrafficMirrorFilterId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-filter.html">traffic-mirror-filter-rule</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:traffic-mirror-filter-rule/\${TrafficMirrorFilterRuleId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-session.html">traffic-mirror-session</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:traffic-mirror-session/\${TrafficMirrorSessionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-target.html">traffic-mirror-target</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:traffic-mirror-target/\${TrafficMirrorTargetId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/tgw/how-transit-gateways-work.html">transit-gateway-attachment</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:transit-gateway-attachment/\${TransitGatewayAttachmentId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format">transit-gateway-connect-peer</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:transit-gateway-connect-peer/\${TransitGatewayConnectPeerId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/tgw/how-transit-gateways-work.html">transit-gateway</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:transit-gateway/\${TransitGatewayId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/tgw/tgw-multicast-overview.html">transit-gateway-multicast-domain</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:transit-gateway-multicast-domain/\${TransitGatewayMulticastDomainId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format">transit-gateway-policy-table</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:transit-gateway-policy-table/\${TransitGatewayPolicyTableId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format">transit-gateway-route-table-announcement</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:transit-gateway-route-table-announcement/\${TransitGatewayRouteTableAnnouncementId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/tgw/how-transit-gateways-work.html">transit-gateway-route-table</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:transit-gateway-route-table/\${TransitGatewayRouteTableId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format">verified-access-endpoint</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:verified-access-endpoint/\${VerifiedAccessEndpointId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format">verified-access-group</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:verified-access-group/\${VerifiedAccessGroupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format">verified-access-instance</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:verified-access-instance/\${VerifiedAccessInstanceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format">verified-access-policy</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:verified-access-policy/\${VerifiedAccessPolicyId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format">verified-access-trust-provider</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:verified-access-trust-provider/\${VerifiedAccessTrustProviderId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volumes.html">volume</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:volume/\${VolumeId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-services-overview.html">vpc-endpoint-connection</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:vpc-endpoint-connection/\${VpcEndpointConnectionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-services-overview.html">vpc-endpoint</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:vpc-endpoint/\${VpcEndpointId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-services-overview.html">vpc-endpoint-service</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:vpc-endpoint-service/\${VpcEndpointServiceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html#vpc-endpoint-policies">vpc-endpoint-service-permission</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:vpc-endpoint-service-permission/\${VpcEndpointServicePermissionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html">vpc-flow-log</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:vpc-flow-log/\${VpcFlowLogId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html">vpc</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:vpc/\${VpcId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html">vpc-peering-connection</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:vpc-peering-connection/\${VpcPeeringConnectionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html">vpn-connection-device-type</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:vpn-connection-device-type/\${VpnConnectionDeviceTypeId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html">vpn-connection</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:vpn-connection/\${VpnConnectionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html">vpn-gateway</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:vpn-gateway/\${VpnGatewayId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Mainframe Modernization Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmainframemodernizationservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/m2/latest/userguide/concept-m2.html#application-concept">Application</a></td>
                    <td>arn:\${Partition}:m2:\${Region}:\${Account}:app/\${ApplicationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/m2/latest/userguide/concept-m2.html#environment-concept">Environment</a></td>
                    <td>arn:\${Partition}:m2:\${Region}:\${Account}:env/\${EnvironmentId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Managed Streaming for Apache Kafka</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmanagedstreamingforapachekafka.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn.html">cluster</a></td>
                    <td>arn:\${Partition}:kafka:\${Region}:\${Account}:cluster/\${ClusterName}/\${Uuid}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/msk/1.0/apireference/configurations-arn.html">configuration</a></td>
                    <td>arn:\${Partition}:kafka:\${Region}:\${Account}:configuration/\${ConfigurationName}/\${Uuid}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/msk/1.0/apireference/vpc-connections-arn.html">vpc-connection</a></td>
                    <td>arn:\${Partition}:kafka:\${Region}:\${VpcOwnerAccount}:vpc-connection/\${ClusterOwnerAccount}/\${ClusterName}/\${Uuid}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/msk/latest/developerguide/v1-replicators.html">replicator</a></td>
                    <td>arn:\${Partition}:kafka:\${Region}:\${Account}:replicator/\${ReplicatorName}/\${Uuid}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#msk-iam-resources">topic</a></td>
                    <td>arn:\${Partition}:kafka:\${Region}:\${Account}:topic/\${ClusterName}/\${ClusterUuid}/\${TopicName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#msk-iam-resources">group</a></td>
                    <td>arn:\${Partition}:kafka:\${Region}:\${Account}:group/\${ClusterName}/\${ClusterUuid}/\${GroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#msk-iam-resources">transactional-id</a></td>
                    <td>arn:\${Partition}:kafka:\${Region}:\${Account}:transactional-id/\${ClusterName}/\${ClusterUuid}/\${TransactionalId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Location</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonlocation.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html">api-key</a></td>
                    <td>arn:\${Partition}:geo:\${Region}:\${Account}:api-key/\${KeyName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/location/latest/developerguide/geofence-tracker-concepts.html">geofence-collection</a></td>
                    <td>arn:\${Partition}:geo:\${Region}:\${Account}:geofence-collection/\${GeofenceCollectionName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/location/latest/developerguide/map-concepts.html">map</a></td>
                    <td>arn:\${Partition}:geo:\${Region}:\${Account}:map/\${MapName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/location/latest/developerguide/places-concepts.html">place-index</a></td>
                    <td>arn:\${Partition}:geo:\${Region}:\${Account}:place-index/\${IndexName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/location/latest/developerguide/route-concepts.html">route-calculator</a></td>
                    <td>arn:\${Partition}:geo:\${Region}:\${Account}:route-calculator/\${CalculatorName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/location/latest/developerguide/geofence-tracker-concepts.html">tracker</a></td>
                    <td>arn:\${Partition}:geo:\${Region}:\${Account}:tracker/\${TrackerName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Machine Learning</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmachinelearning.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/machine-learning/latest/dg/amazon-machine-learning-key-concepts.html#batch-predictions">batchprediction</a></td>
                    <td>arn:\${Partition}:machinelearning:\${Region}:\${Account}:batchprediction/\${BatchPredictionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/machine-learning/latest/dg/amazon-machine-learning-key-concepts.html#datasources">datasource</a></td>
                    <td>arn:\${Partition}:machinelearning:\${Region}:\${Account}:datasource/\${DatasourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/machine-learning/latest/dg/amazon-machine-learning-key-concepts.html#evaluations">evaluation</a></td>
                    <td>arn:\${Partition}:machinelearning:\${Region}:\${Account}:evaluation/\${EvaluationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/machine-learning/latest/dg/amazon-machine-learning-key-concepts.html#ml-models">mlmodel</a></td>
                    <td>arn:\${Partition}:machinelearning:\${Region}:\${Account}:mlmodel/\${MlModelId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Managed Service for Prometheus</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmanagedserviceforprometheus.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/prometheus/latest/userguide/security-iam.html">workspace</a></td>
                    <td>arn:\${Partition}:aps:\${Region}:\${Account}:workspace/\${WorkspaceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/prometheus/latest/userguide/security-iam.html">rulegroupsnamespace</a></td>
                    <td>arn:\${Partition}:aps:\${Region}:\${Account}:rulegroupsnamespace/\${WorkspaceId}/\${Namespace}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/prometheus/latest/userguide/security-iam.html">scraper</a></td>
                    <td>arn:\${Partition}:aps:\${Region}:\${Account}:scraper/\${ScraperId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/eks/latest/userguide/clusters.html">cluster</a></td>
                    <td>arn:\${Partition}:eks:\${Region}:\${Account}:cluster/\${ClusterName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Managed Blockchain</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmanagedblockchain.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_Network.html">network</a></td>
                    <td>arn:\${Partition}:managedblockchain:\${Region}::networks/\${NetworkId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_Member.html">member</a></td>
                    <td>arn:\${Partition}:managedblockchain:\${Region}:\${Account}:members/\${MemberId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_Node.html">node</a></td>
                    <td>arn:\${Partition}:managedblockchain:\${Region}:\${Account}:nodes/\${NodeId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_Proposal.html">proposal</a></td>
                    <td>arn:\${Partition}:managedblockchain:\${Region}::proposals/\${ProposalId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_Invitation.html">invitation</a></td>
                    <td>arn:\${Partition}:managedblockchain:\${Region}:\${Account}:invitations/\${InvitationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_Accessor.html">accessor</a></td>
                    <td>arn:\${Partition}:managedblockchain:\${Region}:\${Account}:accessors/\${AccessorId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Managed Blockchain Query</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmanagedblockchainquery.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon Macie</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmacie.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html">AllowList</a></td>
                    <td>arn:\${Partition}:macie2:\${Region}:\${Account}:allow-list/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html">ClassificationJob</a></td>
                    <td>arn:\${Partition}:macie2:\${Region}:\${Account}:classification-job/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html.html">CustomDataIdentifier</a></td>
                    <td>arn:\${Partition}:macie2:\${Region}:\${Account}:custom-data-identifier/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html">FindingsFilter</a></td>
                    <td>arn:\${Partition}:macie2:\${Region}:\${Account}:findings-filter/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html">Member</a></td>
                    <td>arn:\${Partition}:macie2:\${Region}:\${Account}:member/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Managed Grafana</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmanagedgrafana.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/grafana/latest/userguide/security-iam.html">workspace</a></td>
                    <td>arn:\${Partition}:grafana:\${Region}:\${Account}:/workspaces/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Marketplace Catalog</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacecatalog.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeEntity.html#API_DescribeEntity_ResponseSyntax">Entity</a></td>
                    <td>arn:\${Partition}:aws-marketplace:\${Region}:\${Account}:\${Catalog}/\${EntityType}/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_StartChangeSet.html#API_StartChangeSet_ResponseSyntax">ChangeSet</a></td>
                    <td>arn:\${Partition}:aws-marketplace:\${Region}:\${Account}:\${Catalog}/ChangeSet/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Managed Streaming for Kafka Connect</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmanagedstreamingforkafkaconnect.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/MSKC/latest/mskc/API_ConnectorSummary.html">connector</a></td>
                    <td>arn:\${Partition}:kafkaconnect:\${Region}:\${Account}:connector/\${ConnectorName}/\${UUID}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/MSKC/latest/mskc/API_CustomPlugin.html">custom plugin</a></td>
                    <td>arn:\${Partition}:kafkaconnect:\${Region}:\${Account}:custom-plugin/\${CustomPluginName}/\${UUID}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/MSKC/latest/mskc/API_WorkerConfiguration.html">worker configuration</a></td>
                    <td>arn:\${Partition}:kafkaconnect:\${Region}:\${Account}:worker-configuration/\${WorkerConfigurationName}/\${UUID}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Lookout for Metrics</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonlookoutformetrics.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_AnomalyDetectorSummary.html">AnomalyDetector</a></td>
                    <td>arn:\${Partition}:lookoutmetrics:\${Region}:\${Account}:AnomalyDetector:\${AnomalyDetectorName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_MetricSetSummary.html">MetricSet</a></td>
                    <td>arn:\${Partition}:lookoutmetrics:\${Region}:\${Account}:MetricSet/\${AnomalyDetectorName}/\${MetricSetName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_AlertSummary.html">Alert</a></td>
                    <td>arn:\${Partition}:lookoutmetrics:\${Region}:\${Account}:Alert:\${AlertName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Marketplace Deployment Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacedeploymentservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/marketplace-deployment/latest/api-reference/API_DeploymentParameterInput.html">DeploymentParameter</a></td>
                    <td>arn:\${Partition}:aws-marketplace:\${Region}:\${Account}:DeploymentParameter:catalogs/\${CatalogName}/products/\${ProductId}/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Managed Workflows for Apache Airflow</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmanagedworkflowsforapacheairflow.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/mwaa/latest/userguide/using-mwaa.html">environment</a></td>
                    <td>arn:\${Partition}:airflow:\${Region}:\${Account}:environment/\${EnvironmentName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/mwaa/latest/userguide/access-policies.html">rbac-role</a></td>
                    <td>arn:\${Partition}:airflow:\${Region}:\${Account}:role/\${EnvironmentName}/\${RoleName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Marketplace Commerce Analytics Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacecommerceanalyticsservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Marketplace</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplace.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Marketplace Management Portal</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacemanagementportal.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Marketplace Private Marketplace</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplaceprivatemarketplace.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon Lightsail</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonlightsail.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_Domain.html">Domain</a></td>
                    <td>arn:\${Partition}:lightsail:\${Region}:\${Account}:Domain/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_Instance.html">Instance</a></td>
                    <td>arn:\${Partition}:lightsail:\${Region}:\${Account}:Instance/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_InstanceSnapshot.html">InstanceSnapshot</a></td>
                    <td>arn:\${Partition}:lightsail:\${Region}:\${Account}:InstanceSnapshot/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_KeyPair.html">KeyPair</a></td>
                    <td>arn:\${Partition}:lightsail:\${Region}:\${Account}:KeyPair/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_StaticIp.html">StaticIp</a></td>
                    <td>arn:\${Partition}:lightsail:\${Region}:\${Account}:StaticIp/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_Disk.html">Disk</a></td>
                    <td>arn:\${Partition}:lightsail:\${Region}:\${Account}:Disk/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_DiskSnapshot.html">DiskSnapshot</a></td>
                    <td>arn:\${Partition}:lightsail:\${Region}:\${Account}:DiskSnapshot/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_LoadBalancer.html">LoadBalancer</a></td>
                    <td>arn:\${Partition}:lightsail:\${Region}:\${Account}:LoadBalancer/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_LoadBalancerTlsCertificate.html">LoadBalancerTlsCertificate</a></td>
                    <td>arn:\${Partition}:lightsail:\${Region}:\${Account}:LoadBalancerTlsCertificate/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_ExportSnapshotRecord.html">ExportSnapshotRecord</a></td>
                    <td>arn:\${Partition}:lightsail:\${Region}:\${Account}:ExportSnapshotRecord/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CloudFormationStackRecord.html">CloudFormationStackRecord</a></td>
                    <td>arn:\${Partition}:lightsail:\${Region}:\${Account}:CloudFormationStackRecord/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_RelationalDatabase.html">RelationalDatabase</a></td>
                    <td>arn:\${Partition}:lightsail:\${Region}:\${Account}:RelationalDatabase/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_RelationalDatabaseSnapshot.html">RelationalDatabaseSnapshot</a></td>
                    <td>arn:\${Partition}:lightsail:\${Region}:\${Account}:RelationalDatabaseSnapshot/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_Alarm.html">Alarm</a></td>
                    <td>arn:\${Partition}:lightsail:\${Region}:\${Account}:Alarm/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_Certificate.html">Certificate</a></td>
                    <td>arn:\${Partition}:lightsail:\${Region}:\${Account}:Certificate/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_ContactMethod.html">ContactMethod</a></td>
                    <td>arn:\${Partition}:lightsail:\${Region}:\${Account}:ContactMethod/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_ContainerService.html">ContainerService</a></td>
                    <td>arn:\${Partition}:lightsail:\${Region}:\${Account}:ContainerService/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_LightsailDistribution.html">Distribution</a></td>
                    <td>arn:\${Partition}:lightsail:\${Region}:\${Account}:Distribution/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_Bucket.html">Bucket</a></td>
                    <td>arn:\${Partition}:lightsail:\${Region}:\${Account}:Bucket/\${Id}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Marketplace Discovery</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacediscovery.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Marketplace Metering Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacemeteringservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Marketplace Image Building Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplaceimagebuildingservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Marketplace Entitlement Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplaceentitlementservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Marketplace Seller Reporting</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacesellerreporting.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/marketplace/latest/userguide/dashboards.html#reports-accessing">SellerDashboard</a></td>
                    <td>arn:\${Partition}:aws-marketplace::\${Account}:\${Catalog}/ReportingData/\${FactTable}/Dashboard/\${DashboardName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Marketplace Procurement Systems Integration</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplaceprocurementsystemsintegration.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Marketplace Vendor Insights</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacevendorinsights.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacevendorinsights.html#awsmarketplacevendorinsights-resources-for-iam-policies">DataSource</a></td>
                    <td>arn:\${Partition}:vendor-insights:::data-source:\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacevendorinsights.html#awsmarketplacevendorinsights-resources-for-iam-policies">SecurityProfile</a></td>
                    <td>arn:\${Partition}:vendor-insights:::security-profile:\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Message Delivery Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmessagedeliveryservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon Message Gateway Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmessagegatewayservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon Mechanical Turk</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmechanicalturk.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Microservice Extractor for .NET</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmicroserviceextractorfor.net.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Migration Hub</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmigrationhub.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/migrationhub/latest/ug/API_ProgressUpdateStreamSummary.html">progressUpdateStream</a></td>
                    <td>arn:\${Partition}:mgh:\${Region}:\${Account}:progressUpdateStream/\${Stream}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/migrationhub/latest/ug/API_MigrationTask.html">migrationTask</a></td>
                    <td>arn:\${Partition}:mgh:\${Region}:\${Account}:progressUpdateStream/\${Stream}/migrationTask/\${Task}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Migration Acceleration Program Credits</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmigrationaccelerationprogramcredits.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html">agreement</a></td>
                    <td>arn:\${Partition}:mapcredits:::\${Agreement}/\${AgreementId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Migration Hub Strategy Recommendations</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmigrationhubstrategyrecommendations.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Migration Hub Refactor Spaces</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmigrationhubrefactorspaces.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources">environment</a></td>
                    <td>arn:\${Partition}:refactor-spaces:\${Region}:\${Account}:environment/\${EnvironmentId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources">application</a></td>
                    <td>arn:\${Partition}:refactor-spaces:\${Region}:\${Account}:environment/\${EnvironmentId}/application/\${ApplicationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources">service</a></td>
                    <td>arn:\${Partition}:refactor-spaces:\${Region}:\${Account}:environment/\${EnvironmentId}/application/\${ApplicationId}/service/\${ServiceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources">route</a></td>
                    <td>arn:\${Partition}:refactor-spaces:\${Region}:\${Account}:environment/\${EnvironmentId}/application/\${ApplicationId}/route/\${RouteId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Mobile Analytics</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmobileanalytics.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon Monitron</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmonitron.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/Monitron/latest/user-guide/projects-chapter.html">project</a></td>
                    <td>arn:\${Partition}:monitron:\${Region}:\${Account}:project/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Migration Hub Orchestrator</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmigrationhuborchestrator.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/workflow.html">workflow</a></td>
                    <td>arn:\${Partition}:migrationhub-orchestrator:\${Region}:\${Account}:workflow/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/templates.html">template</a></td>
                    <td>arn:\${Partition}:migrationhub-orchestrator:\${Region}:\${Account}:template/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon MemoryDB</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmemorydb.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/memorydb/latest/devguide/WhatIs.Components.html">parametergroup</a></td>
                    <td>arn:\${Partition}:memorydb:\${Region}:\${Account}:parametergroup/\${ParameterGroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/memorydb/latest/devguide/WhatIs.Components.html">subnetgroup</a></td>
                    <td>arn:\${Partition}:memorydb:\${Region}:\${Account}:subnetgroup/\${SubnetGroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/memorydb/latest/devguide/WhatIs.Components.html">cluster</a></td>
                    <td>arn:\${Partition}:memorydb:\${Region}:\${Account}:cluster/\${ClusterName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/memorydb/latest/devguide/WhatIs.Components.html">snapshot</a></td>
                    <td>arn:\${Partition}:memorydb:\${Region}:\${Account}:snapshot/\${SnapshotName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/memorydb/latest/devguide/WhatIs.Components.html">user</a></td>
                    <td>arn:\${Partition}:memorydb:\${Region}:\${Account}:user/\${UserName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/memorydb/latest/devguide/WhatIs.Components.html">acl</a></td>
                    <td>arn:\${Partition}:memorydb:\${Region}:\${Account}:acl/\${AclName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/memorydb/latest/devguide/WhatIs.Components.html">reservednode</a></td>
                    <td>arn:\${Partition}:memorydb:\${Region}:\${Account}:reservednode/\${ReservationID}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Neptune</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonneptune.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-resources.html">database</a></td>
                    <td>arn:\${Partition}:neptune-db:\${Region}:\${Account}:\${RelativeId}/database</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Network Manager Chat</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsnetworkmanagerchat.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon MQ</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmq.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-how-it-works.html">brokers</a></td>
                    <td>arn:\${Partition}:mq:\${Region}:\${Account}:broker:\${BrokerName}:\${BrokerId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-how-it-works.html">configurations</a></td>
                    <td>arn:\${Partition}:mq:\${Region}:\${Account}:configuration:\${ConfigurationId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Nimble Studio</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonnimblestudio.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_Studio.html">studio</a></td>
                    <td>arn:\${Partition}:nimble:\${Region}:\${Account}:studio/\${StudioId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_StreamingImage.html">streaming-image</a></td>
                    <td>arn:\${Partition}:nimble:\${Region}:\${Account}:streaming-image/\${StreamingImageId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_StudioComponent.html">studio-component</a></td>
                    <td>arn:\${Partition}:nimble:\${Region}:\${Account}:studio-component/\${StudioComponentId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_LaunchProfile.html">launch-profile</a></td>
                    <td>arn:\${Partition}:nimble:\${Region}:\${Account}:launch-profile/\${LaunchProfileId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_StreamingSession.html">streaming-session</a></td>
                    <td>arn:\${Partition}:nimble:\${Region}:\${Account}:streaming-session/\${StreamingSessionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_StreamingSessionBackup.html">streaming-session-backup</a></td>
                    <td>arn:\${Partition}:nimble:\${Region}:\${Account}:streaming-session-backup/\${StreamingSessionBackupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_Eula.html">eula</a></td>
                    <td>arn:\${Partition}:nimble:\${Region}:\${Account}:eula/\${EulaId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_EulaAcceptance.html">eula-acceptance</a></td>
                    <td>arn:\${Partition}:nimble:\${Region}:\${Account}:eula-acceptance/\${EulaAcceptanceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon OpenSearch Ingestion</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonopensearchingestion.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_Pipeline.html">pipeline</a></td>
                    <td>arn:\${Partition}:osis:\${Region}:\${Account}:pipeline/\${PipelineName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_PipelineBlueprint.html">pipeline-blueprint</a></td>
                    <td>arn:\${Partition}:osis:\${Region}:\${Account}:blueprint/\${BlueprintName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Network Manager</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsnetworkmanager.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/tgw/what-is-network-manager.html">global-network</a></td>
                    <td>arn:\${Partition}:networkmanager::\${Account}:global-network/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/tgw/what-is-network-manager.html">site</a></td>
                    <td>arn:\${Partition}:networkmanager::\${Account}:site/\${GlobalNetworkId}/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/tgw/what-is-network-manager.html">link</a></td>
                    <td>arn:\${Partition}:networkmanager::\${Account}:link/\${GlobalNetworkId}/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/tgw/what-is-network-manager.html">device</a></td>
                    <td>arn:\${Partition}:networkmanager::\${Account}:device/\${GlobalNetworkId}/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/tgw/what-is-network-manager.html">connection</a></td>
                    <td>arn:\${Partition}:networkmanager::\${Account}:connection/\${GlobalNetworkId}/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/tgw/what-is-network-manager.html">core-network</a></td>
                    <td>arn:\${Partition}:networkmanager::\${Account}:core-network/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/tgw/what-is-network-manager.html">attachment</a></td>
                    <td>arn:\${Partition}:networkmanager::\${Account}:attachment/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/tgw/what-is-network-manager.html">connect-peer</a></td>
                    <td>arn:\${Partition}:networkmanager::\${Account}:connect-peer/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/tgw/what-is-network-manager.html">peering</a></td>
                    <td>arn:\${Partition}:networkmanager::\${Account}:peering/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS OpsWorks Configuration Management</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsopsworksconfigurationmanagement.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="server">server</a></td>
                    <td>arn:\${Partition}:opsworks-cm::\${Account}:server/\${ServerName}/\${UniqueId}</td>
                </tr>
               <tr>
                    <td><a href="backup">backup</a></td>
                    <td>arn:\${Partition}:opsworks-cm::\${Account}:backup/\${ServerName}-{Date-and-Time-Stamp-of-Backup}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon OpenSearch Serverless</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonopensearchserverless.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-overview.html">Collection</a></td>
                    <td>arn:\${Partition}:aoss:\${Region}:\${Account}:collection/\${CollectionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-overview.html">Dashboards</a></td>
                    <td>arn:\${Partition}:aoss:\${Region}:\${Account}:dashboards/default</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS OpsWorks</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsopsworks.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks.html">stack</a></td>
                    <td>arn:\${Partition}:opsworks:\${Region}:\${Account}:stack/\${StackId}/</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Network Firewall</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsnetworkfirewall.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_Firewall.html">Firewall</a></td>
                    <td>arn:\${Partition}:network-firewall:\${Region}:\${Account}:firewall/\${Name}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_FirewallPolicyResponse.html">FirewallPolicy</a></td>
                    <td>arn:\${Partition}:network-firewall:\${Region}:\${Account}:firewall-policy/\${Name}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_RuleGroupResponse.html">StatefulRuleGroup</a></td>
                    <td>arn:\${Partition}:network-firewall:\${Region}:\${Account}:stateful-rulegroup/\${Name}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_RuleGroupResponse.html">StatelessRuleGroup</a></td>
                    <td>arn:\${Partition}:network-firewall:\${Region}:\${Account}:stateless-rulegroup/\${Name}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_TLSInspectionConfigurationResponse.html">TLSInspectionConfiguration</a></td>
                    <td>arn:\${Partition}:network-firewall:\${Region}:\${Account}:tls-configuration/\${Name}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Partner central account management</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awspartnercentralaccountmanagement.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Outposts</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsoutposts.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/outposts/latest/userguide/work-with-outposts.html">outpost</a></td>
                    <td>arn:\${Partition}:outposts:\${Region}:\${Account}:outpost/\${OutpostId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/outposts/latest/userguide/work-with-outposts.html">site</a></td>
                    <td>arn:\${Partition}:outposts:\${Region}:\${Account}:site/\${SiteId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Neptune Analytics</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonneptuneanalytics.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/neptune-analytics/latest/userguide/iam-resources.html#graph">graph</a></td>
                    <td>arn:\${Partition}:neptune-graph:\${Region}:\${Account}:graph/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/neptune-analytics/latest/userguide/iam-resources.html#graph-snapshot">graph-snapshot</a></td>
                    <td>arn:\${Partition}:neptune-graph:\${Region}:\${Account}:graph-snapshot/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/neptune-analytics/latest/userguide/iam-resources.html#import-task">import-task</a></td>
                    <td>arn:\${Partition}:neptune-graph:\${Region}:\${Account}:import-task/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon One Enterprise</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazononeenterprise.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-device-instance.html">device-instance</a></td>
                    <td>arn:\${Partition}:one:\${Region}:\${Account}:device-instance/\${DeviceInstanceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/one-enterprise/latest/userguide/configure-instance.html">configuration</a></td>
                    <td>arn:\${Partition}:one:\${Region}:\${Account}:device-instance/\${DeviceInstanceId}/configuration/\${Version}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-config-template.html">device-configuration-template</a></td>
                    <td>arn:\${Partition}:one:\${Region}:\${Account}:device-configuration-template/\${TemplateId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-sites.html">site</a></td>
                    <td>arn:\${Partition}:one:\${Region}:\${Account}:site/\${SiteId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/one-enterprise/latest/userguide/enrollment-entry.html">user</a></td>
                    <td>arn:\${Partition}:one:\${Region}:\${Account}:user/\${UserId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Panorama</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awspanorama.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/panorama/latest/dev/gettingstarted-concepts.html#gettingstarted-concepts-appliance">device</a></td>
                    <td>arn:\${Partition}:panorama:\${Region}:\${Account}:device/\${DeviceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/panorama/latest/dev/gettingstarted-concepts.html#gettingstarted-concepts-node">package</a></td>
                    <td>arn:\${Partition}:panorama:\${Region}:\${Account}:package/\${PackageId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/panorama/latest/dev/gettingstarted-concepts.html#gettingstarted-concepts-application">applicationInstance</a></td>
                    <td>arn:\${Partition}:panorama:\${Region}:\${Account}:applicationInstance/\${ApplicationInstanceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Organizations</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_arn-formats.html">account</a></td>
                    <td>arn:\${Partition}:organizations::\${Account}:account/o-\${OrganizationId}/\${AccountId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_arn-formats.html">handshake</a></td>
                    <td>arn:\${Partition}:organizations::\${Account}:handshake/o-\${OrganizationId}/\${HandshakeType}/h-\${HandshakeId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_arn-formats.html">organization</a></td>
                    <td>arn:\${Partition}:organizations::\${Account}:organization/o-\${OrganizationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_arn-formats.html">organizationalunit</a></td>
                    <td>arn:\${Partition}:organizations::\${Account}:ou/o-\${OrganizationId}/ou-\${OrganizationalUnitId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_arn-formats.html">policy</a></td>
                    <td>arn:\${Partition}:organizations::\${Account}:policy/o-\${OrganizationId}/\${PolicyType}/p-\${PolicyId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_arn-formats.html">resourcepolicy</a></td>
                    <td>arn:\${Partition}:organizations::\${Account}:resourcepolicy/o-\${OrganizationId}/rp-\${ResourcePolicyId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_arn-formats.html">awspolicy</a></td>
                    <td>arn:\${Partition}:organizations::aws:policy/\${PolicyType}/p-\${PolicyId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_arn-formats.html">root</a></td>
                    <td>arn:\${Partition}:organizations::\${Account}:root/o-\${OrganizationId}/r-\${RootId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Performance Insights</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsperformanceinsights.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.access-control.html">metric-resource</a></td>
                    <td>arn:\${Partition}:pi:\${Region}:\${Account}:metrics/\${ServiceType}/\${Identifier}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.access-control.html">perf-reports-resource</a></td>
                    <td>arn:\${Partition}:pi:\${Region}:\${Account}:perf-reports/\${ServiceType}/\${Identifier}/\${ReportId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Payment Cryptography</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awspaymentcryptography.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="${APIReferenceDocPage}API_Key.html">key</a></td>
                    <td>arn:\${Partition}:payment-cryptography:\${Region}:\${Account}:key/\${KeyId}</td>
                </tr>
               <tr>
                    <td><a href="${APIReferenceDocPage}API_Alias.html">alias</a></td>
                    <td>arn:\${Partition}:payment-cryptography:\${Region}:\${Account}:alias/\${Alias}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon OpenSearch Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonopensearchservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac.html">domain</a></td>
                    <td>arn:\${Partition}:es:\${Region}:\${Account}:domain/\${DomainName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/slr.html">es_role</a></td>
                    <td>arn:\${Partition}:iam::\${Account}:role/aws-service-role/es.amazonaws.com/AWSServiceRoleForAmazonOpenSearchService</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/slr.html">opensearchservice_role</a></td>
                    <td>arn:\${Partition}:iam::\${Account}:role/aws-service-role/opensearchservice.amazonaws.com/AWSServiceRoleForAmazonOpenSearchService</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Pinpoint Email Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonpinpointemailservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_CreateConfigurationSet.html">configuration-set</a></td>
                    <td>arn:\${Partition}:ses:\${Region}:\${Account}:configuration-set/\${ConfigurationSetName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DedicatedIp.html">dedicated-ip-pool</a></td>
                    <td>arn:\${Partition}:ses:\${Region}:\${Account}:dedicated-ip-pool/\${DedicatedIPPool}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DeliverabilityTestReport.html">deliverability-test-report</a></td>
                    <td>arn:\${Partition}:ses:\${Region}:\${Account}:deliverability-test-report/\${ReportId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_IdentityInfo.html">identity</a></td>
                    <td>arn:\${Partition}:ses:\${Region}:\${Account}:identity/\${IdentityName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Price List</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awspricelist.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Payments</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awspayments.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon Polly</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonpolly.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html">lexicon</a></td>
                    <td>arn:\${Partition}:polly:\${Region}:\${Account}:lexicon/\${LexiconName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Private CA Connector for Active Directory</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsprivatecaconnectorforactivedirectory.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_Connector.html">Connector</a></td>
                    <td>arn:\${Partition}:pca-connector-ad:\${Region}:\${Account}:connector/\${ConnectorId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_DirectoryRegistration.html">DirectoryRegistration</a></td>
                    <td>arn:\${Partition}:pca-connector-ad:\${Region}:\${Account}:directory-registration/\${DirectoryId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ServicePrincipalName.html">ServicePrincipalName</a></td>
                    <td>arn:\${Partition}:pca-connector-ad:\${Region}:\${Account}:directory-registration/\${DirectoryId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_Template.html">Template</a></td>
                    <td>arn:\${Partition}:pca-connector-ad:\${Region}:\${Account}:connector/\${ConnectorId}/template/\${TemplateId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_AccessControlEntry.html">TemplateGroupAccessControlEntry</a></td>
                    <td>arn:\${Partition}:pca-connector-ad:\${Region}:\${Account}:connector/\${ConnectorId}/template/\${TemplateId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Pinpoint SMS and Voice Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonpinpointsmsandvoiceservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Private Certificate Authority</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsprivatecertificateauthority.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/privateca/latest/userguide/api-permissions.html">certificate-authority</a></td>
                    <td>arn:\${Partition}:acm-pca:\${Region}:\${Account}:certificate-authority/\${CertificateAuthorityId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Purchase Orders Console</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awspurchaseordersconsole.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions">purchase-order</a></td>
                    <td>arn:\${Partition}:purchase-orders::\${Account}:purchase-order/\${ResourceName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Pinpoint</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonpinpoint.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id.html">app</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps.html">apps</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-campaigns-campaign-id.html">campaign</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/campaigns/\${CampaignId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys-journey-id.html">journey</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/journeys/\${JourneyId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys.html">journeys</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/journeys</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-segments-segment-id.html">segment</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/segments/\${SegmentId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/templates.html">template</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:templates/\${TemplateName}/\${TemplateType}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/templates.html">templates</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:templates</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/recommenders.html">recommender</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:recommenders/\${RecommenderId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/recommenders.html">recommenders</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:recommenders/*</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/phone-number-validate.html">phone-number-validate</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:phone/number/validate</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels.html">channels</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/channels</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels.html">channel</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/channels/\${ChannelType}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-eventstream.html">event-stream</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/eventstream</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-events.html">events</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/events</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html">messages</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/messages</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-verify-otp.html">verify-otp</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/verify-otp</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-verify-otp.html">otp</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/otp</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-attributes-attribute-type.html">attribute</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/attributes/\${AttributeType}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-users-user-id.html">user</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/users/\${UserId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-endpoints-endpoint-id.html">endpoint</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/endpoints/\${EndpointId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-jobs-import-job-id.html">import-job</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/jobs/import/\${JobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-jobs-export-job-id.html">export-job</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/jobs/export/\${JobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-kpis-daterange-kpi-name.html">application-metrics</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/kpis/daterange/\${KpiName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-campaigns-campaign-id-kpis-daterange-kpi-name.html">campaign-metrics</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/campaigns/\${CampaignId}/kpis/daterange/\${KpiName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys-journey-id-kpis-daterange-kpi-name.html">journey-metrics</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/journeys/\${JourneyId}/kpis/daterange/\${KpiName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys-journey-id-execution-metrics.html">journey-execution-metrics</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/journeys/\${JourneyId}/execution-metrics</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys-journey-id-activities-journey-activity-id-execution-metrics.html">journey-execution-activity-metrics</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/journeys/\${JourneyId}/activities/\${JourneyActivityId}/execution-metrics</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/reports.html">reports</a></td>
                    <td>arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:reports</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Q</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonq.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon Q Business Q Apps</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonqbusinessqapps.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-app.html">application</a></td>
                    <td>arn:\${Partition}:qbusiness:\${Region}:\${Account}:application/\${ApplicationId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Personalize</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonpersonalize.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/personalize/latest/dg/how-it-works-dataset-schema.html#schema-examples">schema</a></td>
                    <td>arn:\${Partition}:personalize:\${Region}:\${Account}:schema/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/personalize/latest/dg/API_FeatureTransformation.html">featureTransformation</a></td>
                    <td>arn:\${Partition}:personalize:\${Region}:\${Account}:feature-transformation/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/personalize/latest/dg/API_Dataset.html">dataset</a></td>
                    <td>arn:\${Partition}:personalize:\${Region}:\${Account}:dataset/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DatasetGroup.html">datasetGroup</a></td>
                    <td>arn:\${Partition}:personalize:\${Region}:\${Account}:dataset-group/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DatasetImportJob.html">datasetImportJob</a></td>
                    <td>arn:\${Partition}:personalize:\${Region}:\${Account}:dataset-import-job/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/personalize/latest/dg/analyzing-data.html">dataInsightsJob</a></td>
                    <td>arn:\${Partition}:personalize:\${Region}:\${Account}:data-insights-job/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DatasetExportJob.html">datasetExportJob</a></td>
                    <td>arn:\${Partition}:personalize:\${Region}:\${Account}:dataset-export-job/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/personalize/latest/dg/API_Solution.html">solution</a></td>
                    <td>arn:\${Partition}:personalize:\${Region}:\${Account}:solution/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/personalize/latest/dg/API_Campaign.html">campaign</a></td>
                    <td>arn:\${Partition}:personalize:\${Region}:\${Account}:campaign/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/personalize/latest/dg/API_EventTracker.html">eventTracker</a></td>
                    <td>arn:\${Partition}:personalize:\${Region}:\${Account}:event-tracker/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/personalize/latest/dg/API_Recipe.html">recipe</a></td>
                    <td>arn:\${Partition}:personalize:\${Region}:\${Account}:recipe/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/personalize/latest/dg/API_Algorithm.html">algorithm</a></td>
                    <td>arn:\${Partition}:personalize:\${Region}:\${Account}:algorithm/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/personalize/latest/dg/API_BatchInferenceJob.html">batchInferenceJob</a></td>
                    <td>arn:\${Partition}:personalize:\${Region}:\${Account}:batch-inference-job/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/personalize/latest/dg/API_Filter.html">filter</a></td>
                    <td>arn:\${Partition}:personalize:\${Region}:\${Account}:filter/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/personalize/latest/dg/API_Recommender.html">recommender</a></td>
                    <td>arn:\${Partition}:personalize:\${Region}:\${Account}:recommender/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/personalize/latest/dg/API_BatchSegmentJob.html">batchSegmentJob</a></td>
                    <td>arn:\${Partition}:personalize:\${Region}:\${Account}:batch-segment-job/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/personalize/latest/dg/API_MetricAttribution.html">metricAttribution</a></td>
                    <td>arn:\${Partition}:personalize:\${Region}:\${Account}:metric-attribution/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Q Business</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonqbusiness.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="${UserGuideDocPage}create-application.html">application</a></td>
                    <td>arn:\${Partition}:qbusiness:\${Region}:\${Account}:application/\${ApplicationId}</td>
                </tr>
               <tr>
                    <td><a href="${UserGuideDocPage}select-retriever.html">retriever</a></td>
                    <td>arn:\${Partition}:qbusiness:\${Region}:\${Account}:application/\${ApplicationId}/retriever/\${RetrieverId}</td>
                </tr>
               <tr>
                    <td><a href="${UserGuideDocPage}select-retriever.html">index</a></td>
                    <td>arn:\${Partition}:qbusiness:\${Region}:\${Account}:application/\${ApplicationId}/index/\${IndexId}</td>
                </tr>
               <tr>
                    <td><a href="${UserGuideDocPage}connect-data.html">data-source</a></td>
                    <td>arn:\${Partition}:qbusiness:\${Region}:\${Account}:application/\${ApplicationId}/index/\${IndexId}/data-source/\${DataSourceId}</td>
                </tr>
               <tr>
                    <td><a href="${UserGuideDocPage}plugins.html">plugin</a></td>
                    <td>arn:\${Partition}:qbusiness:\${Region}:\${Account}:application/\${ApplicationId}/plugin/\${PluginId}</td>
                </tr>
               <tr>
                    <td><a href="${UserGuideDocPage}using-web-experience.html">web-experience</a></td>
                    <td>arn:\${Partition}:qbusiness:\${Region}:\${Account}:application/\${ApplicationId}/web-experience/\${WebExperienceId}</td>
                </tr>
               <tr>
                    <td><a href="${UserGuideDocPage}provisioning.html">user-license</a></td>
                    <td>arn:\${Partition}:qbusiness:\${Region}:\${Account}:application/\${ApplicationId}/user-license/\${UserLicenseId}</td>
                </tr>
               <tr>
                    <td><a href="${UserGuideDocPage}subscriptions.html">subscription</a></td>
                    <td>arn:\${Partition}:qbusiness:\${Region}:\${Account}:application/\${ApplicationId}/subscription/\${SubscriptionId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Q in Connect</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonqinconnect.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_AssistantData.html">Assistant</a></td>
                    <td>arn:\${Partition}:wisdom:\${Region}:\${Account}:assistant/\${AssistantId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_AssistantAssociationData.html">AssistantAssociation</a></td>
                    <td>arn:\${Partition}:wisdom:\${Region}:\${Account}:association/\${AssistantId}/\${AssistantAssociationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_ContentData.html">Content</a></td>
                    <td>arn:\${Partition}:wisdom:\${Region}:\${Account}:content/\${KnowledgeBaseId}/\${ContentId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_KnowledgeBaseData.html">KnowledgeBase</a></td>
                    <td>arn:\${Partition}:wisdom:\${Region}:\${Account}:knowledge-base/\${KnowledgeBaseId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_SessionData.html">Session</a></td>
                    <td>arn:\${Partition}:wisdom:\${Region}:\${Account}:session/\${AssistantId}/\${SessionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_QuickResponseData.html">QuickResponse</a></td>
                    <td>arn:\${Partition}:wisdom:\${Region}:\${Account}:quick-response/\${KnowledgeBaseId}/\${QuickResponseId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Recycle Bin</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsrecyclebin.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-recycle-bin.html#recycle-bin-concepts">rule</a></td>
                    <td>arn:\${Partition}:rbin:\${Region}:\${Account}:rule/\${ResourceName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon RDS IAM Authentication</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonrdsiamauthentication.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.DBAccounts.html">db-user</a></td>
                    <td>arn:\${Partition}:rds-db:\${Region}:\${Account}:dbuser:\${DbiResourceId}/\${DbUserName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Pinpoint SMS Voice V2</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonpinpointsmsvoicev2.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateConfigurationSet.html">ConfigurationSet</a></td>
                    <td>arn:\${Partition}:sms-voice:\${Region}:\${Account}:configuration-set/\${ConfigurationSetName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateOptOutList.html">OptOutList</a></td>
                    <td>arn:\${Partition}:sms-voice:\${Region}:\${Account}:opt-out-list/\${OptOutListName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RequestPhoneNumber.html">PhoneNumber</a></td>
                    <td>arn:\${Partition}:sms-voice:\${Region}:\${Account}:phone-number/\${PhoneNumberId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreatePool.html">Pool</a></td>
                    <td>arn:\${Partition}:sms-voice:\${Region}:\${Account}:pool/\${PoolId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_ProtectConfiguration.html">ProtectConfiguration</a></td>
                    <td>arn:\${Partition}:sms-voice:\${Region}:\${Account}:protect-configuration/\${ProtectConfigurationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeSenderIds.html">SenderId</a></td>
                    <td>arn:\${Partition}:sms-voice:\${Region}:\${Account}:sender-id/\${SenderId}/\${IsoCountryCode}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeRegistrations.html">Registration</a></td>
                    <td>arn:\${Partition}:sms-voice:\${Region}:\${Account}:registration/\${RegistrationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeRegistrationAttachments.html">RegistrationAttachment</a></td>
                    <td>arn:\${Partition}:sms-voice:\${Region}:\${Account}:registration-attachment/\${RegistrationAttachmentId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeVerifiedDestinationNumbers.html">VerifiedDestinationNumber</a></td>
                    <td>arn:\${Partition}:sms-voice:\${Region}:\${Account}:verified-destination-number/\${VerifiedDestinationNumberId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon RDS Data API</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonrdsdataapi.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Aurora.Managing.html">cluster</a></td>
                    <td>arn:\${Partition}:rds:\${Region}:\${Account}:cluster:\${DbClusterInstanceName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS re:Post Private</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsre_postprivate.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/repostprivate/latest/UserGuide/">space</a></td>
                    <td>arn:\${Partition}:repostspace:\${Region}:\${Account}:space/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Proton</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsproton.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/proton/latest/adminguide/ag-env-templates.html">environment-template</a></td>
                    <td>arn:\${Partition}:proton:\${Region}:\${Account}:environment-template/\${Name}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/proton/latest/adminguide/ag-env-templates.html">environment-template-version</a></td>
                    <td>arn:\${Partition}:proton:\${Region}:\${Account}:environment-template/\${TemplateName}:\${MajorVersion}.\${MinorVersion}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/proton/latest/adminguide/ag-env-templates.html">environment-template-major-version</a></td>
                    <td>arn:\${Partition}:proton:\${Region}:\${Account}:environment-template/\${TemplateName}:\${MajorVersionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/proton/latest/adminguide/ag-env-templates.html">environment-template-minor-version</a></td>
                    <td>arn:\${Partition}:proton:\${Region}:\${Account}:environment-template/\${TemplateName}:\${MajorVersionId}.\${MinorVersionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/proton/latest/adminguide/managing-svc-templates.html">service-template</a></td>
                    <td>arn:\${Partition}:proton:\${Region}:\${Account}:service-template/\${Name}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/proton/latest/adminguide/managing-svc-templates.html">service-template-version</a></td>
                    <td>arn:\${Partition}:proton:\${Region}:\${Account}:service-template/\${TemplateName}:\${MajorVersion}.\${MinorVersion}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/proton/latest/adminguide/managing-svc-templates.html">service-template-major-version</a></td>
                    <td>arn:\${Partition}:proton:\${Region}:\${Account}:service-template/\${TemplateName}:\${MajorVersionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/proton/latest/adminguide/managing-svc-templates.html">service-template-minor-version</a></td>
                    <td>arn:\${Partition}:proton:\${Region}:\${Account}:service-template/\${TemplateName}:\${MajorVersionId}.\${MinorVersionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/proton/latest/adminguide/ag-environments.html">environment</a></td>
                    <td>arn:\${Partition}:proton:\${Region}:\${Account}:environment/\${Name}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/proton/latest/adminguide/ag-services.html">service</a></td>
                    <td>arn:\${Partition}:proton:\${Region}:\${Account}:service/\${Name}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/proton/latest/adminguide/ag-services.html">service-instance</a></td>
                    <td>arn:\${Partition}:proton:\${Region}:\${Account}:service/\${ServiceName}/service-instance/\${Name}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/proton/latest/adminguide/ag-env-account-connections.html">environment-account-connection</a></td>
                    <td>arn:\${Partition}:proton:\${Region}:\${Account}:environment-account-connection/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/proton/latest/adminguide/ag-repositories.html">repository</a></td>
                    <td>arn:\${Partition}:proton:\${Region}:\${Account}:repository/\${Provider}:\${Name}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/proton/latest/adminguide/ag-components.html">component</a></td>
                    <td>arn:\${Partition}:proton:\${Region}:\${Account}:component/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/proton/latest/adminguide/ag-deployments.html">deployment</a></td>
                    <td>arn:\${Partition}:proton:\${Region}:\${Account}:deployment/\${Id}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon QLDB</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonqldb.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/qldb/latest/developerguide/ledger-structure.html">ledger</a></td>
                    <td>arn:\${Partition}:qldb:\${Region}:\${Account}:ledger/\${LedgerName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/qldb/latest/developerguide/streams.html">stream</a></td>
                    <td>arn:\${Partition}:qldb:\${Region}:\${Account}:stream/\${LedgerName}/\${StreamId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/qldb/latest/developerguide/working.manage-tables.html">table</a></td>
                    <td>arn:\${Partition}:qldb:\${Region}:\${Account}:ledger/\${LedgerName}/table/\${TableId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/qldb/latest/developerguide/working.catalog.html">catalog</a></td>
                    <td>arn:\${Partition}:qldb:\${Region}:\${Account}:ledger/\${LedgerName}/information_schema/user_tables</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Resource Group Tagging API</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonresourcegrouptaggingapi.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon QuickSight</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonquicksight.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AccountInfo.html">account</a></td>
                    <td>arn:\${Partition}:quicksight:\${Region}:\${Account}:account/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_User.html">user</a></td>
                    <td>arn:\${Partition}:quicksight:\${Region}:\${Account}:user/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Group.html">group</a></td>
                    <td>arn:\${Partition}:quicksight:\${Region}:\${Account}:group/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Analysis.html">analysis</a></td>
                    <td>arn:\${Partition}:quicksight:\${Region}:\${Account}:analysis/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Dashboard.html">dashboard</a></td>
                    <td>arn:\${Partition}:quicksight:\${Region}:\${Account}:dashboard/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Template.html">template</a></td>
                    <td>arn:\${Partition}:quicksight:\${Region}:\${Account}:template/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_VPCConnection.html">vpcconnection</a></td>
                    <td>arn:\${Partition}:quicksight:\${Region}:\${Account}:vpcConnection/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AssetBundleExportJob.html">assetBundleExportJob</a></td>
                    <td>arn:\${Partition}:quicksight:\${Region}:\${Account}:asset-bundle-export-job/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AssetBundleImportJob.html">assetBundleImportJob</a></td>
                    <td>arn:\${Partition}:quicksight:\${Region}:\${Account}:asset-bundle-import-job/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataSource.html">datasource</a></td>
                    <td>arn:\${Partition}:quicksight:\${Region}:\${Account}:datasource/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataSet.html">dataset</a></td>
                    <td>arn:\${Partition}:quicksight:\${Region}:\${Account}:dataset/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Ingestion.html">ingestion</a></td>
                    <td>arn:\${Partition}:quicksight:\${Region}:\${Account}:dataset/\${DatasetId}/ingestion/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RefreshSchedule.html">refreshschedule</a></td>
                    <td>arn:\${Partition}:quicksight:\${Region}:\${Account}:dataset/\${DatasetId}/refresh-schedule/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Theme.html">theme</a></td>
                    <td>arn:\${Partition}:quicksight:\${Region}:\${Account}:theme/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_IAMPolicyAssignment.html">assignment</a></td>
                    <td>arn:\${Partition}:quicksight::\${Account}:assignment/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AccountCustomization.html">customization</a></td>
                    <td>arn:\${Partition}:quicksight:\${Region}:\${Account}:customization/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_NamespaceInfoV2.html">namespace</a></td>
                    <td>arn:\${Partition}:quicksight:\${Region}:\${Account}:namespace/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Folder.html">folder</a></td>
                    <td>arn:\${Partition}:quicksight:\${Region}:\${Account}:folder/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/quicksight/latest/user/customizing-quicksight-email-templates.html">emailCustomizationTemplate</a></td>
                    <td>arn:\${Partition}:quicksight:\${Region}:\${Account}:email-customization-template/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicDetails.html">topic</a></td>
                    <td>arn:\${Partition}:quicksight:\${Region}:\${Account}:topic/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DashboardSnapshotJob.html">dashboardSnapshotJob</a></td>
                    <td>arn:\${Partition}:quicksight:\${Region}:\${Account}:dashboard/\${DashboardId}/snapshot-job/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Redshift Data API</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonredshiftdataapi.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html">cluster</a></td>
                    <td>arn:\${Partition}:redshift:\${Region}:\${Account}:cluster:\${ClusterName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-serverless.html">workgroup</a></td>
                    <td>arn:\${Partition}:redshift-serverless:\${Region}:\${Account}:workgroup/\${WorkgroupId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Redshift Serverless</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonredshiftserverless.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-workgroup-namespace.html">namespace</a></td>
                    <td>arn:\${Partition}:redshift-serverless:\${Region}:\${Account}:namespace/\${NamespaceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-snapshots-recovery.html">snapshot</a></td>
                    <td>arn:\${Partition}:redshift-serverless:\${Region}:\${Account}:snapshot/\${SnapshotId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-workgroup-namespace.html">workgroup</a></td>
                    <td>arn:\${Partition}:redshift-serverless:\${Region}:\${Account}:workgroup/\${WorkgroupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-snapshots-recovery.html">recoveryPoint</a></td>
                    <td>arn:\${Partition}:redshift-serverless:\${Region}:\${Account}:recoverypoint/\${RecoveryPointId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-connecting.html">endpointAccess</a></td>
                    <td>arn:\${Partition}:redshift-serverless:\${Region}:\${Account}:managedvpcendpoint/\${EndpointAccessId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Resource Access Manager (RAM)</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsresourceaccessmanagerram.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/ram/latest/APIReference/API_ResourceShare.html">resource-share</a></td>
                    <td>arn:\${Partition}:ram:\${Region}:\${Account}:resource-share/\${ResourcePath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ram/latest/APIReference/API_ResourceShareInvitation.html">resource-share-invitation</a></td>
                    <td>arn:\${Partition}:ram:\${Region}:\${Account}:resource-share-invitation/\${ResourcePath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ram/latest/APIReference/API_ResourceSharePermissionDetail.html">permission</a></td>
                    <td>arn:\${Partition}:ram::\${Account}:permission/\${ResourcePath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ram/latest/APIReference/API_ResourceSharePermissionDetail.html">customer-managed-permission</a></td>
                    <td>arn:\${Partition}:ram:\${Region}:\${Account}:permission/\${ResourcePath}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Rekognition</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonrekognition.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/rekognition/latest/dg/collections.html">collection</a></td>
                    <td>arn:\${Partition}:rekognition:\${Region}:\${Account}:collection/\${CollectionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/rekognition/latest/dg/streaming-video.html">streamprocessor</a></td>
                    <td>arn:\${Partition}:rekognition:\${Region}:\${Account}:streamprocessor/\${StreamprocessorId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/mp-create-project.html">project</a></td>
                    <td>arn:\${Partition}:rekognition:\${Region}:\${Account}:project/\${ProjectName}/\${CreationTimestamp}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/training-model.html">projectversion</a></td>
                    <td>arn:\${Partition}:rekognition:\${Region}:\${Account}:project/\${ProjectName}/version/\${VersionName}/\${CreationTimestamp}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/creating-datasets.html">dataset</a></td>
                    <td>arn:\${Partition}:rekognition:\${Region}:\${Account}:project/\${ProjectName}/dataset/\${DatasetType}/\${CreationTimestamp}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Resilience Hub</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsresiliencehub.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ResiliencyPolicy.html">resiliency-policy</a></td>
                    <td>arn:\${Partition}:resiliencehub:\${Region}:\${Account}:resiliency-policy/\${ResiliencyPolicyId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_App.html">application</a></td>
                    <td>arn:\${Partition}:resiliencehub:\${Region}:\${Account}:app/\${AppId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_AppAssessment.html">app-assessment</a></td>
                    <td>arn:\${Partition}:resiliencehub:\${Region}:\${Account}:app-assessment/\${AppAssessmentId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_RecommendationTemplate.html">recommendation-template</a></td>
                    <td>arn:\${Partition}:resiliencehub:\${Region}:\${Account}:recommendation-template/\${RecommendationTemplateId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon RHEL Knowledgebase Portal</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonrhelknowledgebaseportal.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Resource Groups</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsresourcegroups.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html">group</a></td>
                    <td>arn:\${Partition}:resource-groups:\${Region}:\${Account}:group/\${GroupName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon RDS</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonrds.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Aurora.html">cluster</a></td>
                    <td>arn:\${Partition}:rds:\${Region}:\${Account}:cluster:\${DbClusterInstanceName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.DBShardGroup.html">shardgrp</a></td>
                    <td>arn:\${Partition}:rds:\${Region}:\${Account}:shard-group:\${DbShardGroupResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html">cluster-auto-backup</a></td>
                    <td>arn:\${Partition}:rds:\${Region}:\${Account}:cluster-auto-backup:\${DbClusterAutomatedBackupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html">auto-backup</a></td>
                    <td>arn:\${Partition}:rds:\${Region}:\${Account}:auto-backup:\${DbInstanceAutomatedBackupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.Endpoints.html">cluster-endpoint</a></td>
                    <td>arn:\${Partition}:rds:\${Region}:\${Account}:cluster-endpoint:\${DbClusterEndpoint}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html">cluster-pg</a></td>
                    <td>arn:\${Partition}:rds:\${Region}:\${Account}:cluster-pg:\${ClusterParameterGroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html">cluster-snapshot</a></td>
                    <td>arn:\${Partition}:rds:\${Region}:\${Account}:cluster-snapshot:\${ClusterSnapshotName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.html">db</a></td>
                    <td>arn:\${Partition}:rds:\${Region}:\${Account}:db:\${DbInstanceName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html">es</a></td>
                    <td>arn:\${Partition}:rds:\${Region}:\${Account}:es:\${SubscriptionName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html">global-cluster</a></td>
                    <td>arn:\${Partition}:rds::\${Account}:global-cluster:\${GlobalCluster}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.html">og</a></td>
                    <td>arn:\${Partition}:rds:\${Region}:\${Account}:og:\${OptionGroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html">pg</a></td>
                    <td>arn:\${Partition}:rds:\${Region}:\${Account}:pg:\${ParameterGroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html">proxy</a></td>
                    <td>arn:\${Partition}:rds:\${Region}:\${Account}:db-proxy:\${DbProxyId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html">proxy-endpoint</a></td>
                    <td>arn:\${Partition}:rds:\${Region}:\${Account}:db-proxy-endpoint:\${DbProxyEndpointId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html">ri</a></td>
                    <td>arn:\${Partition}:rds:\${Region}:\${Account}:ri:\${ReservedDbInstanceName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html">secgrp</a></td>
                    <td>arn:\${Partition}:rds:\${Region}:\${Account}:secgrp:\${SecurityGroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html">snapshot</a></td>
                    <td>arn:\${Partition}:rds:\${Region}:\${Account}:snapshot:\${SnapshotName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Scenarios.html#USER_VPC.Scenario1">subgrp</a></td>
                    <td>arn:\${Partition}:rds:\${Region}:\${Account}:subgrp:\${SubnetGroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html">target-group</a></td>
                    <td>arn:\${Partition}:rds:\${Region}:\${Account}:target-group:\${TargetGroupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev.html">cev</a></td>
                    <td>arn:\${Partition}:rds:\${Region}:\${Account}:cev:\${Engine}/\${EngineVersion}/\${CustomDbEngineVersionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html">deployment</a></td>
                    <td>arn:\${Partition}:rds:\${Region}:\${Account}:deployment:\${BlueGreenDeploymentIdentifier}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.html">integration</a></td>
                    <td>arn:\${Partition}:rds:\${Region}:\${Account}:integration:\${IntegrationIdentifier}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.single-tenant.snapshots.html#br-cdb.db-snapshots">snapshot-tenant-database</a></td>
                    <td>arn:\${Partition}:rds:\${Region}:\${Account}:snapshot-tenant-database:\${SnapshotName}:\${TenantResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.CDBs.html#multi-tenant-configuration">tenant-database</a></td>
                    <td>arn:\${Partition}:rds:\${Region}:\${Account}:tenant-database:\${TenantResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Route 53 Recovery Controls</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/recovery-cluster/latest/api/cluster.html">cluster</a></td>
                    <td>arn:\${Partition}:route53-recovery-control::\${Account}:cluster/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel.html">controlpanel</a></td>
                    <td>arn:\${Partition}:route53-recovery-control::\${Account}:controlpanel/\${ControlPanelId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/recovery-cluster/latest/api/routingcontrol.html">routingcontrol</a></td>
                    <td>arn:\${Partition}:route53-recovery-control::\${Account}:controlpanel/\${ControlPanelId}/routingcontrol/\${RoutingControlId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/recovery-cluster/latest/api/safetyrule.html">safetyrule</a></td>
                    <td>arn:\${Partition}:route53-recovery-control::\${Account}:controlpanel/\${ControlPanelId}/safetyrule/\${SafetyRuleId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Resource Explorer</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsresourceexplorer.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_View.html">view</a></td>
                    <td>arn:\${Partition}:resource-explorer-2:\${Region}:\${Account}:view/\${ViewName}/\${ViewUuid}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_Index.html">index</a></td>
                    <td>arn:\${Partition}:resource-explorer-2:\${Region}:\${Account}:index/\${IndexUuid}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Route 53 Profiles enables sharing DNS settings with VPCs</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53profilesenablessharingdnssettingswithvpcs.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/Route53/latest/APIReference/#access-control-resources">profile</a></td>
                    <td>arn:\${Partition}:route53profiles:\${Region}:\${Account}:profile/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/Route53/latest/APIReference/#access-control-resources">profile-association</a></td>
                    <td>arn:\${Partition}:route53profiles:\${Region}:\${Account}:profile-association/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Route 53 Application Recovery Controller - Zonal Shift</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53applicationrecoverycontroller-zonalshift.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.html">ALB</a></td>
                    <td>arn:\${Partition}:elasticloadbalancing:\${Region}:\${Account}:loadbalancer/app/\${LoadBalancerName}/\${LoadBalancerId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.html">NLB</a></td>
                    <td>arn:\${Partition}:elasticloadbalancing:\${Region}:\${Account}:loadbalancer/net/\${LoadBalancerName}/\${LoadBalancerId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS RoboMaker</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsrobomaker.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/robomaker/latest/dg/managing-robot-applications.html">robotApplication</a></td>
                    <td>arn:\${Partition}:robomaker:\${Region}:\${Account}:robot-application/\${ApplicationName}/\${CreatedOnEpoch}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/robomaker/latest/dg/managing-simulation-applications.html">simulationApplication</a></td>
                    <td>arn:\${Partition}:robomaker:\${Region}:\${Account}:simulation-application/\${ApplicationName}/\${CreatedOnEpoch}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/robomaker/latest/dg/simulation.html">simulationJob</a></td>
                    <td>arn:\${Partition}:robomaker:\${Region}:\${Account}:simulation-job/\${SimulationJobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/robomaker/latest/dg/simulation-job-batch.html">simulationJobBatch</a></td>
                    <td>arn:\${Partition}:robomaker:\${Region}:\${Account}:simulation-job-batch/\${SimulationJobBatchId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/robomaker/latest/dg/deployment.html">deploymentJob</a></td>
                    <td>arn:\${Partition}:robomaker:\${Region}:\${Account}:deployment-job/\${DeploymentJobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/robomaker/latest/dg/fleets.html">robot</a></td>
                    <td>arn:\${Partition}:robomaker:\${Region}:\${Account}:robot/\${RobotName}/\${CreatedOnEpoch}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/robomaker/latest/dg/managing-simulation-applications.html">deploymentFleet</a></td>
                    <td>arn:\${Partition}:robomaker:\${Region}:\${Account}:deployment-fleet/\${FleetName}/\${CreatedOnEpoch}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/robomaker/latest/dg/worlds-managing-generation-jobs.html">worldGenerationJob</a></td>
                    <td>arn:\${Partition}:robomaker:\${Region}:\${Account}:world-generation-job/\${WorldGenerationJobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/robomaker/latest/dg/worlds-managing-export-jobs.html">worldExportJob</a></td>
                    <td>arn:\${Partition}:robomaker:\${Region}:\${Account}:world-export-job/\${WorldExportJobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/robomaker/latest/dg/worlds-managing-simworld-templates.html">worldTemplate</a></td>
                    <td>arn:\${Partition}:robomaker:\${Region}:\${Account}:world-template/\${WorldTemplateJobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/robomaker/latest/dg/worlds-managing-generated-worlds.html">world</a></td>
                    <td>arn:\${Partition}:robomaker:\${Region}:\${Account}:world/\${WorldId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Route 53 Recovery Cluster</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycluster.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/recovery-cluster/latest/api/routingcontrol.html">routingcontrol</a></td>
                    <td>arn:\${Partition}:route53-recovery-control::\${Account}:controlpanel/\${ControlPanelId}/routingcontrol/\${RoutingControlId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Route 53 Domains</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53domains.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon Redshift</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonredshift.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html">cluster</a></td>
                    <td>arn:\${Partition}:redshift:\${Region}:\${Account}:cluster:\${ClusterName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/dg/datashare-overview.html">datashare</a></td>
                    <td>arn:\${Partition}:redshift:\${Region}:\${Account}:datashare:\${ProducerClusterNamespace}/\${DataShareName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_GROUP.html">dbgroup</a></td>
                    <td>arn:\${Partition}:redshift:\${Region}:\${Account}:dbgroup:\${ClusterName}/\${DbGroup}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/dg/t_creating_database.html">dbname</a></td>
                    <td>arn:\${Partition}:redshift:\${Region}:\${Account}:dbname:\${ClusterName}/\${DbName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/dg/r_Users.html">dbuser</a></td>
                    <td>arn:\${Partition}:redshift:\${Region}:\${Account}:dbuser:\${ClusterName}/\${DbUser}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-events.html">eventsubscription</a></td>
                    <td>arn:\${Partition}:redshift:\${Region}:\${Account}:eventsubscription:\${EventSubscriptionName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html#working-with-HSM">hsmclientcertificate</a></td>
                    <td>arn:\${Partition}:redshift:\${Region}:\${Account}:hsmclientcertificate:\${HSMClientCertificateId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html#working-with-HSM">hsmconfiguration</a></td>
                    <td>arn:\${Partition}:redshift:\${Region}:\${Account}:hsmconfiguration:\${HSMConfigurationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/dg/concepts.html">namespace</a></td>
                    <td>arn:\${Partition}:redshift:\${Region}:\${Account}:namespace:\${ClusterNamespace}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html">parametergroup</a></td>
                    <td>arn:\${Partition}:redshift:\${Region}:\${Account}:parametergroup:\${ParameterGroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html">securitygroup</a></td>
                    <td>arn:\${Partition}:redshift:\${Region}:\${Account}:securitygroup:\${SecurityGroupName}/ec2securitygroup/\${Owner}/\${Ec2SecurityGroupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html">securitygroupingress-cidr</a></td>
                    <td>arn:\${Partition}:redshift:\${Region}:\${Account}:securitygroupingress:\${SecurityGroupName}/cidrip/\${IpRange}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html">securitygroupingress-ec2securitygroup</a></td>
                    <td>arn:\${Partition}:redshift:\${Region}:\${Account}:securitygroupingress:\${SecurityGroupName}/ec2securitygroup/\${Owner}/\${Ece2SecuritygroupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html">snapshot</a></td>
                    <td>arn:\${Partition}:redshift:\${Region}:\${Account}:snapshot:\${ClusterName}/\${SnapshotName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html#configure-snapshot-copy-grant">snapshotcopygrant</a></td>
                    <td>arn:\${Partition}:redshift:\${Region}:\${Account}:snapshotcopygrant:\${SnapshotCopyGrantName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html">snapshotschedule</a></td>
                    <td>arn:\${Partition}:redshift:\${Region}:\${Account}:snapshotschedule:\${ParameterGroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-cluster-subnet-groups.html">subnetgroup</a></td>
                    <td>arn:\${Partition}:redshift:\${Region}:\${Account}:subnetgroup:\${SubnetGroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-usage-limits.html">usagelimit</a></td>
                    <td>arn:\${Partition}:redshift:\${Region}:\${Account}:usagelimit:\${UsageLimitId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-idp-connect.html">redshiftidcapplication</a></td>
                    <td>arn:\${Partition}:redshift:\${Region}:\${Account}:redshiftidcapplication:\${RedshiftIdcApplicationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-idp-connect.html">qev2idcapplication</a></td>
                    <td>arn:\${Partition}:redshift:\${Region}:\${Account}:qev2idcapplication:\${Qev2IdcApplicationId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon S3 Express</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3express.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-zonal-buckets.html">bucket</a></td>
                    <td>arn:\${Partition}:s3express:\${Region}:\${Account}:bucket/\${BucketName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Route 53 Recovery Readiness</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoveryreadiness.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.readiness-checks.html">readinesscheck</a></td>
                    <td>arn:\${Partition}:route53-recovery-readiness::\${Account}:readiness-check/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.readiness-checks.html">resourceset</a></td>
                    <td>arn:\${Partition}:route53-recovery-readiness::\${Account}:resource-set/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.recovery-groups.html">cell</a></td>
                    <td>arn:\${Partition}:route53-recovery-readiness::\${Account}:cell/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.recovery-groups.html">recoverygroup</a></td>
                    <td>arn:\${Partition}:route53-recovery-readiness::\${Account}:recovery-group/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Route 53</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="API_CidrCollection.html">cidrcollection</a></td>
                    <td>arn:\${Partition}:route53:::cidrcollection/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_Change.html">change</a></td>
                    <td>arn:\${Partition}:route53:::change/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-concepts.html#route-53-concepts-reusable-delegation-set">delegationset</a></td>
                    <td>arn:\${Partition}:route53:::delegationset/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-concepts.html#route-53-concepts-health-check">healthcheck</a></td>
                    <td>arn:\${Partition}:route53:::healthcheck/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-concepts.html#route-53-concepts-hosted-zone">hostedzone</a></td>
                    <td>arn:\${Partition}:route53:::hostedzone/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/traffic-policies.html">trafficpolicy</a></td>
                    <td>arn:\${Partition}:route53:::trafficpolicy/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/traffic-policy-records.html">trafficpolicyinstance</a></td>
                    <td>arn:\${Partition}:route53:::trafficpolicyinstance/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html">queryloggingconfig</a></td>
                    <td>arn:\${Partition}:route53:::queryloggingconfig/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html">vpc</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:vpc/\${VpcId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Route 53 Resolver</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53resolver.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/access-control-overview.html#access-control-resources">resolver-dnssec-config</a></td>
                    <td>arn:\${Partition}:route53resolver:\${Region}:\${Account}:resolver-dnssec-config/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/access-control-overview.html#access-control-resources">resolver-query-log-config</a></td>
                    <td>arn:\${Partition}:route53resolver:\${Region}:\${Account}:resolver-query-log-config/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/access-control-overview.html#access-control-resources">resolver-rule</a></td>
                    <td>arn:\${Partition}:route53resolver:\${Region}:\${Account}:resolver-rule/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/access-control-overview.html#access-control-resources">resolver-endpoint</a></td>
                    <td>arn:\${Partition}:route53resolver:\${Region}:\${Account}:resolver-endpoint/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/access-control-overview.html#access-control-resources">firewall-rule-group</a></td>
                    <td>arn:\${Partition}:route53resolver:\${Region}:\${Account}:firewall-rule-group/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/access-control-overview.html#access-control-resources">firewall-rule-group-association</a></td>
                    <td>arn:\${Partition}:route53resolver:\${Region}:\${Account}:firewall-rule-group-association/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/access-control-overview.html#access-control-resources">firewall-domain-list</a></td>
                    <td>arn:\${Partition}:route53resolver:\${Region}:\${Account}:firewall-domain-list/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/access-control-overview.html#access-control-resources">firewall-config</a></td>
                    <td>arn:\${Partition}:route53resolver:\${Region}:\${Account}:firewall-config/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/access-control-overview.html#access-control-resources">resolver-config</a></td>
                    <td>arn:\${Partition}:route53resolver:\${Region}:\${Account}:resolver-config/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/access-control-overview.html#access-control-resources">outpost-resolver</a></td>
                    <td>arn:\${Partition}:route53resolver:\${Region}:\${Account}:outpost-resolver/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon S3 Glacier</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3glacier.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-vaults.html">vault</a></td>
                    <td>arn:\${Partition}:glacier:\${Region}:\${Account}:vaults/\${VaultName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Savings Plans</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssavingsplans.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html">savingsplan</a></td>
                    <td>arn:\${Partition}:savingsplans::\${Account}:savingsplan/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon SageMaker Ground Truth Synthetic</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsagemakergroundtruthsynthetic.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon SageMaker geospatial capabilities</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsagemakergeospatialcapabilities.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-eoj.html">EarthObservationJob</a></td>
                    <td>arn:\${Partition}:sagemaker-geospatial:\${Region}:\${Account}:earth-observation-job/\${JobID}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-data-collections.html">RasterDataCollection</a></td>
                    <td>arn:\${Partition}:sagemaker-geospatial:\${Region}:\${Account}:raster-data-collection/\${CollectionID}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-vej.html">VectorEnrichmentJob</a></td>
                    <td>arn:\${Partition}:sagemaker-geospatial:\${Region}:\${Account}:vector-enrichment-job/\${JobID}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Security Lake</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsecuritylake.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DataLakeResource.html">data-lake</a></td>
                    <td>arn:\${Partition}:securitylake:\${Region}:\${Account}:data-lake/default</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/security-lake/latest/APIReference/API_SubscriberResource.html">subscriber</a></td>
                    <td>arn:\${Partition}:securitylake:\${Region}:\${Account}:subscriber/\${SubscriberId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon S3 Object Lambda</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3objectlambda.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/transforming-objects.html">objectlambdaaccesspoint</a></td>
                    <td>arn:\${Partition}:s3-object-lambda:\${Region}:\${Account}:accesspoint/\${AccessPointName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Server Migration Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsservermigrationservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon S3 on Outposts</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3onoutposts.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html">accesspoint</a></td>
                    <td>arn:\${Partition}:s3-outposts:\${Region}:\${Account}:outpost/\${OutpostId}/accesspoint/\${AccessPointName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html">bucket</a></td>
                    <td>arn:\${Partition}:s3-outposts:\${Region}:\${Account}:outpost/\${OutpostId}/bucket/\${BucketName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/outposts-endpoints.html">endpoint</a></td>
                    <td>arn:\${Partition}:s3-outposts:\${Region}:\${Account}:outpost/\${OutpostId}/endpoint/\${EndpointId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingObjects.html">object</a></td>
                    <td>arn:\${Partition}:s3-outposts:\${Region}:\${Account}:outpost/\${OutpostId}/bucket/\${BucketName}/object/\${ObjectName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Secrets Manager</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssecretsmanager.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#iam-resources">Secret</a></td>
                    <td>arn:\${Partition}:secretsmanager:\${Region}:\${Account}:secret:\${SecretId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Security Token Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssecuritytokenservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html">role</a></td>
                    <td>arn:\${Partition}:iam::\${Account}:role/\${RoleNameWithPath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html">user</a></td>
                    <td>arn:\${Partition}:iam::\${Account}:user/\${UserNameWithPath}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns">self-session</a></td>
                    <td>arn:\${Partition}:sts::\${Account}:self</td>
                </tr>
            </tbody>
        </table>
        <h1>Service Quotas</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_servicequotas.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/identity-access-management.html#resources">quota</a></td>
                    <td>arn:\${Partition}:servicequotas:\${Region}:\${Account}:\${ServiceCode}/\${QuotaCode}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Security Hub</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssecurityhub.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-access.html#resources">hub</a></td>
                    <td>arn:\${Partition}:securityhub:\${Region}:\${Account}:hub/default</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-access.html#resources">product</a></td>
                    <td>arn:\${Partition}:securityhub:\${Region}:\${Account}:product/\${Company}/\${ProductId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-access.html#resources">finding-aggregator</a></td>
                    <td>arn:\${Partition}:securityhub:\${Region}:\${Account}:finding-aggregator/\${FindingAggregatorId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules">automation-rule</a></td>
                    <td>arn:\${Partition}:securityhub:\${Region}:\${Account}:automation-rule/\${AutomationRuleId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/securityhub/latest/userguide/central-configuration-intro.html">configuration-policy</a></td>
                    <td>arn:\${Partition}:securityhub:\${Region}:\${Account}:configuration-policy/\${ConfigurationPolicyId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon SES</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonses.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/ses/latest/APIReference/API_ConfigurationSet.html">configuration-set</a></td>
                    <td>arn:\${Partition}:ses:\${Region}:\${Account}:configuration-set/\${ConfigurationSetName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ses/latest/APIReference/API_CustomVerificationEmailTemplate.html">custom-verification-email-template</a></td>
                    <td>arn:\${Partition}:ses:\${Region}:\${Account}:custom-verification-email-template/\${TemplateName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_IdentityInfo.html">identity</a></td>
                    <td>arn:\${Partition}:ses:\${Region}:\${Account}:identity/\${IdentityName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ses/latest/APIReference/API_Template.html">template</a></td>
                    <td>arn:\${Partition}:ses:\${Region}:\${Account}:template/\${TemplateName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Serverless Application Repository</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsserverlessapplicationrepository.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications.html">applications</a></td>
                    <td>arn:\${Partition}:serverlessrepo:\${Region}:\${Account}:applications/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon SimpleDB</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsimpledb.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/DataModel.html">domain</a></td>
                    <td>arn:\${Partition}:sdb:\${Region}:\${Account}:domain/\${DomainName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Signer</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssigner.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/signer/latest/developerguide/gs-profile.html">signing-profile</a></td>
                    <td>arn:\${Partition}:signer:\${Region}:\${Account}:/signing-profiles/\${ProfileName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/signer/latest/developerguide/gs-job.html">signing-job</a></td>
                    <td>arn:\${Partition}:signer:\${Region}:\${Account}:/signing-jobs/\${JobId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Shield</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsshield.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_AttackDetail.html">attack</a></td>
                    <td>arn:\${Partition}:shield::\${Account}:attack/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_Protection.html">protection</a></td>
                    <td>arn:\${Partition}:shield::\${Account}:protection/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ProtectionGroup.html">protection-group</a></td>
                    <td>arn:\${Partition}:shield::\${Account}:protection-group/\${Id}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Snow Device Management</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssnowdevicemanagement.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/snowball/latest/snowcone-guide/aws-sdms.html">managed-device</a></td>
                    <td>arn:\${Partition}:snow-device-management:\${Region}:\${Account}:managed-device/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/snowball/latest/snowcone-guide/aws-sdms.html">task</a></td>
                    <td>arn:\${Partition}:snow-device-management:\${Region}:\${Account}:task/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS service providing managed private networks</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsserviceprovidingmanagedprivatenetworks.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/private-networks/latest/userguide/identity-access-management.html">network</a></td>
                    <td>arn:\${Partition}:private-networks:\${Region}:\${Account}:network/\${NetworkName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/private-networks/latest/userguide/identity-access-management.html">network-site</a></td>
                    <td>arn:\${Partition}:private-networks:\${Region}:\${Account}:network-site/\${NetworkName}/\${NetworkSiteName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/private-networks/latest/userguide/identity-access-management.html">network-resource</a></td>
                    <td>arn:\${Partition}:private-networks:\${Region}:\${Account}:network-resource/\${NetworkName}/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/private-networks/latest/userguide/identity-access-management.html">order</a></td>
                    <td>arn:\${Partition}:private-networks:\${Region}:\${Account}:order/\${NetworkName}/\${OrderId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/private-networks/latest/userguide/identity-access-management.html">device-identifier</a></td>
                    <td>arn:\${Partition}:private-networks:\${Region}:\${Account}:device-identifier/\${NetworkName}/\${DeviceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Signin</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssignin.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS SimSpace Weaver</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssimspaceweaver.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_configuring-simulation.html">Simulation</a></td>
                    <td>arn:\${Partition}:simspaceweaver:\${Region}:\${Account}:simulation/\${SimulationName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Simple Email Service v2</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsimpleemailservicev2.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/ses/latest/APIReference/API_ConfigurationSet.html">configuration-set</a></td>
                    <td>arn:\${Partition}:ses:\${Region}:\${Account}:configuration-set/\${ConfigurationSetName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ContactList.html">contact-list</a></td>
                    <td>arn:\${Partition}:ses:\${Region}:\${Account}:contact-list/\${ContactListName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_CustomVerificationEmailTemplateMetadata.html">custom-verification-email-template</a></td>
                    <td>arn:\${Partition}:ses:\${Region}:\${Account}:custom-verification-email-template/\${TemplateName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_DedicatedIp.html">dedicated-ip-pool</a></td>
                    <td>arn:\${Partition}:ses:\${Region}:\${Account}:dedicated-ip-pool/\${DedicatedIPPool}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_DeliverabilityTestReport.html">deliverability-test-report</a></td>
                    <td>arn:\${Partition}:ses:\${Region}:\${Account}:deliverability-test-report/\${ReportId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ExportJobSummary.html">export-job</a></td>
                    <td>arn:\${Partition}:ses:\${Region}:\${Account}:export-job/\${ExportJobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_IdentityInfo.html">identity</a></td>
                    <td>arn:\${Partition}:ses:\${Region}:\${Account}:identity/\${IdentityName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ImportJobSummary.html">import-job</a></td>
                    <td>arn:\${Partition}:ses:\${Region}:\${Account}:import-job/\${ImportJobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_Template.html">template</a></td>
                    <td>arn:\${Partition}:ses:\${Region}:\${Account}:template/\${TemplateName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS SQL Workbench</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssqlworkbench.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html">connection</a></td>
                    <td>arn:\${Partition}:sqlworkbench:\${Region}:\${Account}:connection/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html">query</a></td>
                    <td>arn:\${Partition}:sqlworkbench:\${Region}:\${Account}:query/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html">chart</a></td>
                    <td>arn:\${Partition}:sqlworkbench:\${Region}:\${Account}:chart/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html">notebook</a></td>
                    <td>arn:\${Partition}:sqlworkbench:\${Region}:\${Account}:notebook/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon SQS</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsqs.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-types.html">queue</a></td>
                    <td>arn:\${Partition}:sqs:\${Region}:\${Account}:\${QueueName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Service Catalog</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsservicecatalog.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_CreateApplication.html">Application</a></td>
                    <td>arn:\${Partition}:servicecatalog:\${Region}:\${Account}:/applications/\${ApplicationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_CreateAttributeGroup.html">AttributeGroup</a></td>
                    <td>arn:\${Partition}:servicecatalog:\${Region}:\${Account}:/attribute-groups/\${AttributeGroupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/servicecatalog/latest/dg/API_PortfolioDetail.html">Portfolio</a></td>
                    <td>arn:\${Partition}:catalog:\${Region}:\${Account}:portfolio/\${PortfolioId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ProductViewDetail.html">Product</a></td>
                    <td>arn:\${Partition}:catalog:\${Region}:\${Account}:product/\${ProductId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Simple Workflow Service</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsimpleworkflowservice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-domains.html">domain</a></td>
                    <td>arn:\${Partition}:swf::\${Account}:/domain/\${DomainName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Step Functions</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsstepfunctions.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-activities.html">activity</a></td>
                    <td>arn:\${Partition}:states:\${Region}:\${Account}:activity:\${ActivityName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-executions.html">execution</a></td>
                    <td>arn:\${Partition}:states:\${Region}:\${Account}:execution:\${StateMachineName}:\${ExecutionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-executions.html">express</a></td>
                    <td>arn:\${Partition}:states:\${Region}:\${Account}:express:\${StateMachineName}:\${ExecutionId}:\${ExpressId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html">statemachine</a></td>
                    <td>arn:\${Partition}:states:\${Region}:\${Account}:stateMachine:\${StateMachineName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-cd-aliasing-versioning.html">statemachineversion</a></td>
                    <td>arn:\${Partition}:states:\${Region}:\${Account}:stateMachine:\${StateMachineName}:\${StateMachineVersionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-cd-aliasing-versioning.html">statemachinealias</a></td>
                    <td>arn:\${Partition}:states:\${Region}:\${Account}:stateMachine:\${StateMachineName}:\${StateMachineAliasName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-examine-map-run.html">maprun</a></td>
                    <td>arn:\${Partition}:states:\${Region}:\${Account}:mapRun:\${StateMachineName}/\${MapRunLabel}:\${MapRunId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-examine-map-run.html">labelled execution</a></td>
                    <td>arn:\${Partition}:states:\${Region}:\${Account}:execution:\${StateMachineName}/\${MapRunLabel}:\${ExecutionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-examine-map-run.html">labelled express</a></td>
                    <td>arn:\${Partition}:states:\${Region}:\${Account}:express:\${StateMachineName}/\${MapRunLabel}:\${ExecutionId}:\${ExpressId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Snowball</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssnowball.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon SNS</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsns.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html">topic</a></td>
                    <td>arn:\${Partition}:sns:\${Region}:\${Account}:\${TopicName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Support App in Slack</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupportappinslack.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Support</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupport.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon S3</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html">accesspoint</a></td>
                    <td>arn:\${Partition}:s3:\${Region}:\${Account}:accesspoint/\${AccessPointName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html">bucket</a></td>
                    <td>arn:\${Partition}:s3:::\${BucketName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingObjects.html">object</a></td>
                    <td>arn:\${Partition}:s3:::\${BucketName}/\${ObjectName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-managing-jobs.html">job</a></td>
                    <td>arn:\${Partition}:s3:\${Region}:\${Account}:job/\${JobId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens.html">storagelensconfiguration</a></td>
                    <td>arn:\${Partition}:s3:\${Region}:\${Account}:storage-lens/\${ConfigId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_group.html">storagelensgroup</a></td>
                    <td>arn:\${Partition}:s3:\${Region}:\${Account}:storage-lens-group/\${Name}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/transforming-objects.html">objectlambdaaccesspoint</a></td>
                    <td>arn:\${Partition}:s3-object-lambda:\${Region}:\${Account}:accesspoint/\${AccessPointName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRequests.html">multiregionaccesspoint</a></td>
                    <td>arn:\${Partition}:s3::\${Account}:accesspoint/\${AccessPointAlias}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRequests.html">multiregionaccesspointrequestarn</a></td>
                    <td>arn:\${Partition}:s3:us-west-2:\${Account}:async-request/mrap/\${Operation}/\${Token}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-instance.html">accessgrantsinstance</a></td>
                    <td>arn:\${Partition}:s3:\${Region}:\${Account}:access-grants/default</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-location.html">accessgrantslocation</a></td>
                    <td>arn:\${Partition}:s3:\${Region}:\${Account}:access-grants/default/location/\${Token}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-grant.html">accessgrant</a></td>
                    <td>arn:\${Partition}:s3:\${Region}:\${Account}:access-grants/default/grant/\${Token}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Supply Chain</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html">instance</a></td>
                    <td>arn:\${Partition}:scn:\${Region}:\${Account}:instance/\${InstanceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html">bill-of-materials-import-job</a></td>
                    <td>arn:\${Partition}:scn:\${Region}:\${Account}:instance/\${InstanceId}/bill-of-materials-import-job/\${JobId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Systems Manager GUI Connect</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssystemsmanagerguiconnect.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Support Plans</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupportplans.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Sustainability</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssustainability.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Systems Manager for SAP</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssystemsmanagerforsap.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/systems-manager/index.html">application</a></td>
                    <td>arn:\${Partition}:ssm-sap:\${Region}:\${Account}:\${ApplicationType}/\${ApplicationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/systems-manager/index.html">component</a></td>
                    <td>arn:\${Partition}:ssm-sap:\${Region}:\${Account}:\${ApplicationType}/\${ApplicationId}/COMPONENT/\${ComponentId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/systems-manager/index.html">database</a></td>
                    <td>arn:\${Partition}:ssm-sap:\${Region}:\${Account}:\${ApplicationType}/\${ApplicationId}/DB/\${DatabaseId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Tag Editor</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_tageditor.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS Storage Gateway</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsstoragegateway.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/storagegateway/latest/userguide/resource_vtl-devices.html">device</a></td>
                    <td>arn:\${Partition}:storagegateway:\${Region}:\${Account}:gateway/\${GatewayId}/device/\${Vtldevice}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/storagegateway/latest/userguide/API_AssociateFileSystem.html">fs-association</a></td>
                    <td>arn:\${Partition}:storagegateway:\${Region}:\${Account}:fs-association/\${FsaId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/storagegateway/latest/userguide/StorageGatewayConcepts.html">gateway</a></td>
                    <td>arn:\${Partition}:storagegateway:\${Region}:\${Account}:gateway/\${GatewayId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/storagegateway/latest/userguide/GettingStartedCreateFileShare.html">share</a></td>
                    <td>arn:\${Partition}:storagegateway:\${Region}:\${Account}:share/\${ShareId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/storagegateway/latest/userguide/StorageGatewayConcepts.html#storage-gateway-vtl-concepts">tape</a></td>
                    <td>arn:\${Partition}:storagegateway:\${Region}:\${Account}:tape/\${TapeBarcode}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/storagegateway/latest/userguide/CreatingCustomTapePool.html">tapepool</a></td>
                    <td>arn:\${Partition}:storagegateway:\${Region}:\${Account}:tapepool/\${PoolId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/storagegateway/latest/userguide/GettingStartedCreateVolumes.html">target</a></td>
                    <td>arn:\${Partition}:storagegateway:\${Region}:\${Account}:gateway/\${GatewayId}/target/\${IscsiTarget}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/storagegateway/latest/userguide/StorageGatewayConcepts.html#volume-gateway-concepts">volume</a></td>
                    <td>arn:\${Partition}:storagegateway:\${Region}:\${Account}:gateway/\${GatewayId}/volume/\${VolumeId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Telco Network Builder</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awstelconetworkbuilder.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/tnb/latest/ug/function-packages.html">function-package</a></td>
                    <td>arn:\${Partition}:tnb:\${Region}:\${Account}:function-package/\${FunctionPackageId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/tnb/latest/ug/network-packages.html">network-package</a></td>
                    <td>arn:\${Partition}:tnb:\${Region}:\${Account}:network-package/\${NetworkPackageId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/tnb/latest/ug/network-instances.html">network-instance</a></td>
                    <td>arn:\${Partition}:tnb:\${Region}:\${Account}:network-instance/\${NetworkInstanceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/tnb/latest/ug/function-packages.html">function-instance</a></td>
                    <td>arn:\${Partition}:tnb:\${Region}:\${Account}:function-instance/\${FunctionInstanceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/tnb/latest/ug/network-operations.html">network-operation</a></td>
                    <td>arn:\${Partition}:tnb:\${Region}:\${Account}:network-operation/\${NetworkOperationId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Timestream</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazontimestream.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/timestream/latest/developerguide/API_Database.html">database</a></td>
                    <td>arn:\${Partition}:timestream:\${Region}:\${Account}:database/\${DatabaseName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/timestream/latest/developerguide/API_Table.html">table</a></td>
                    <td>arn:\${Partition}:timestream:\${Region}:\${Account}:database/\${DatabaseName}/table/\${TableName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/timestream/latest/developerguide/API_ScheduledQuery.html">scheduled-query</a></td>
                    <td>arn:\${Partition}:timestream:\${Region}:\${Account}:scheduled-query/\${ScheduledQueryName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Systems Manager Incident Manager</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssystemsmanagerincidentmanager.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/incident-manager/latest/userguide/response-plans.html">response-plan</a></td>
                    <td>arn:\${Partition}:ssm-incidents::\${Account}:response-plan/\${ResponsePlan}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/incident-manager/latest/userguide/tracking-details.html">incident-record</a></td>
                    <td>arn:\${Partition}:ssm-incidents::\${Account}:incident-record/\${ResponsePlan}/\${IncidentRecord}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/incident-manager/latest/userguide/disaster-recovery-resiliency.html#replication">replication-set</a></td>
                    <td>arn:\${Partition}:ssm-incidents::\${Account}:replication-set/\${ReplicationSet}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Systems Manager</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssystemsmanager.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html">association</a></td>
                    <td>arn:\${Partition}:ssm:\${Region}:\${Account}:association/\${AssociationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/running-automations.html">automation-execution</a></td>
                    <td>arn:\${Partition}:ssm:\${Region}:\${Account}:automation-execution/\${AutomationExecutionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html">automation-definition</a></td>
                    <td>arn:\${Partition}:ssm:\${Region}:\${Account}:automation-definition/\${AutomationDefinitionName}:\${VersionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html">bucket</a></td>
                    <td>arn:\${Partition}:s3:::\${BucketName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/documents.html">document</a></td>
                    <td>arn:\${Partition}:ssm:\${Region}:\${Account}:document/\${DocumentName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format">instance</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:instance/\${InstanceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-maintenance.html">maintenancewindow</a></td>
                    <td>arn:\${Partition}:ssm:\${Region}:\${Account}:maintenancewindow/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html">managed-instance</a></td>
                    <td>arn:\${Partition}:ssm:\${Region}:\${Account}:managed-instance/\${InstanceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-inventory-configuring.html">managed-instance-inventory</a></td>
                    <td>arn:\${Partition}:ssm:\${Region}:\${Account}:managed-instance-inventory/\${InstanceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems.html">opsitem</a></td>
                    <td>arn:\${Partition}:ssm:\${Region}:\${Account}:opsitem/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager.html">opsmetadata</a></td>
                    <td>arn:\${Partition}:ssm:\${Region}:\${Account}:opsmetadata/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html">parameter</a></td>
                    <td>arn:\${Partition}:ssm:\${Region}:\${Account}:parameter/\${ParameterNameWithoutLeadingSlash}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html">patchbaseline</a></td>
                    <td>arn:\${Partition}:ssm:\${Region}:\${Account}:patchbaseline/\${PatchBaselineIdResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems.html">resourcearn</a></td>
                    <td>arn:\${Partition}:ssm:\${Region}:\${Account}:opsitemgroup/default</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html">session</a></td>
                    <td>arn:\${Partition}:ssm:\${Region}:\${Account}:session/\${SessionId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-inventory-datasync.html">resourcedatasync</a></td>
                    <td>arn:\${Partition}:ssm:\${Region}:\${Account}:resource-data-sync/\${SyncName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html">servicesetting</a></td>
                    <td>arn:\${Partition}:ssm:\${Region}:\${Account}:servicesetting/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-assign-targets.html">windowtarget</a></td>
                    <td>arn:\${Partition}:ssm:\${Region}:\${Account}:windowtarget/\${WindowTargetId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-assign-tasks.html">windowtask</a></td>
                    <td>arn:\${Partition}:ssm:\${Region}:\${Account}:windowtask/\${WindowTaskId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html">task</a></td>
                    <td>arn:\${Partition}:ecs:\${Region}:\${Account}:task/\${TaskId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Textract</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazontextract.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/textract/latest/dg/API_AdapterOverview.html">adapter</a></td>
                    <td>arn:\${Partition}:textract:\${Region}:\${Account}:/adapters/\${AdapterId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/textract/latest/dg/API_AdapterVersionOverview.html">adapterversion</a></td>
                    <td>arn:\${Partition}:textract:\${Region}:\${Account}:/adapters/\${AdapterId}/versions/\${AdapterVersion}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Tax Settings</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awstaxsettings.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon SageMaker</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsagemaker.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/neo-edge-devices.html">device</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:device-fleet/\${DeviceFleetName}/device/\${DeviceName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/edge-device-fleet.html">device-fleet</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:device-fleet/\${DeviceFleetName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/edge-packaging-job.html">edge-packaging-job</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:edge-packaging-job/\${EdgePackagingJobName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/edge.html">edge-deployment-plan</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:edge-deployment/\${EdgeDeploymentPlanName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-start-human-loop.html">human-loop</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:human-loop/\${HumanLoopName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-create-flow-definition.html">flow-definition</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:flow-definition/\${FlowDefinitionName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-instructions-overview.html">human-task-ui</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:human-task-ui/\${HumanTaskUiName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-content-sharing.html">hub</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:hub/\${HubName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-content-sharing.html">hub-content</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:hub-content/\${HubName}/\${HubContentType}/\${HubContentName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender-recommendation-jobs.html">inference-recommendations-job</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:inference-recommendations-job/\${InferenceRecommendationsJobName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/inference-experiment.html">inference-experiment</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:inference-experiment/\${InferenceExperimentName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/sms.html">labeling-job</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:labeling-job/\${LabelingJobName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management.html">workteam</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:workteam/\${WorkteamName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management.html">workforce</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:workforce/\${WorkforceName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/studio-entity-status.html">domain</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:domain/\${DomainId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/studio-entity-status.html">user-profile</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:user-profile/\${DomainId}/\${UserProfileName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/studio-entity-status.html">space</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:space/\${DomainId}/\${SpaceName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/studio-entity-status.html">app</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:app/\${DomainId}/\${UserProfileName}/\${AppType}/\${AppName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi-create.html">app-image-config</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:app-image-config/\${AppImageConfigName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lcc.html">studio-lifecycle-config</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:studio-lifecycle-config/\${StudioLifecycleConfigName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html">notebook-instance</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:notebook-instance/\${NotebookInstanceName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html">notebook-instance-lifecycle-config</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:notebook-instance-lifecycle-config/\${NotebookInstanceLifecycleConfigName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html">code-repository</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:code-repository/\${CodeRepositoryName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi.html">image</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:image/\${ImageName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi.html">image-version</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:image-version/\${ImageName}/\${Version}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/algorithms-choose.html">algorithm</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:algorithm/\${AlgorithmName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-cluster.html">cluster</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:cluster/\${ClusterId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-training.html">training-job</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:training-job/\${TrainingJobName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html">processing-job</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:processing-job/\${ProcessingJobName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-how-it-works.html">hyper-parameter-tuning-job</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:hyper-parameter-tuning-job/\${HyperParameterTuningJobName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects-whatis.html">project</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:project/\${ProjectName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelPackage.html">model-package</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:model-package/\${ModelPackageName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-model-group.html">model-package-group</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:model-package-group/\${ModelPackageGroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html">model</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:model/\${ModelName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html">endpoint-config</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:endpoint-config/\${EndpointConfigName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html">endpoint</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:endpoint/\${EndpointName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html">inference-component</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:inference-component/\${InferenceComponentName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TransformJob.html.html">transform-job</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:transform-job/\${TransformJobName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CompilationJobSummary.html">compilation-job</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:compilation-job/\${CompilationJobName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html">automl-job</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:automl-job/\${AutoMLJobJobName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-scheduling.html">monitoring-schedule</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:monitoring-schedule/\${MonitoringScheduleName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-scheduling.html">monitoring-schedule-alert</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:monitoring-schedule/\${MonitoringScheduleName}/alert/\${MonitoringScheduleAlertName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-quality.html">data-quality-job-definition</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:data-quality-job-definition/\${DataQualityJobDefinitionName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality.html">model-quality-job-definition</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:model-quality-job-definition/\${ModelQualityJobDefinitionName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-detect-post-training-bias.html">model-bias-job-definition</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:model-bias-job-definition/\${ModelBiasJobDefinitionName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-explainability.html">model-explainability-job-definition</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:model-explainability-job-definition/\${ModelExplainabilityJobDefinitionName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Experiment.html">experiment</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:experiment/\${ExperimentName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Trial.html">experiment-trial</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:experiment-trial/\${TrialName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrialComponent.html">experiment-trial-component</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:experiment-trial-component/\${TrialComponentName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html">feature-group</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:feature-group/\${FeatureGroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Pipeline.html">pipeline</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:pipeline/\${PipelineName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PipelineExecution.html">pipeline-execution</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:pipeline/\${PipelineName}/execution/\${RandomString}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ArtifactSummary.html">artifact</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:artifact/\${HashOfArtifactSource}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContextSummary.html">context</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:context/\${ContextName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ActionSummary.html">action</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:action/\${ActionName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_LineageGroupSummary.html">lineage-group</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:lineage-group/\${LineageGroupName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelCard.html">model-card</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:model-card/\${ModelCardName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelCardExportJob.html">model-card-export-job</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:model-card/\${ModelCardName}/export-job/\${ExportJobName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-collaborate-permissions.html">shared-model</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:shared-model/\${SharedModelId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-collaborate-permissions.html">shared-model-event</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:shared-model-event/\${EventId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceCatalog.html">sagemaker-catalog</a></td>
                    <td>arn:\${Partition}:sagemaker:\${Region}:\${Account}:sagemaker-catalog/\${ResourceCatalogName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Tiros</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awstiros.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon Transcribe</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazontranscribe.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/transcribe/latest/dg/API_TranscriptionJob.html">transcriptionjob</a></td>
                    <td>arn:\${Partition}:transcribe:\${Region}:\${Account}:transcription-job/\${JobName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/transcribe/latest/dg/API_CreateVocabulary.html">vocabulary</a></td>
                    <td>arn:\${Partition}:transcribe:\${Region}:\${Account}:vocabulary/\${VocabularyName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/transcribe/latest/dg/API_CreateVocabularyFilter.html">vocabularyfilter</a></td>
                    <td>arn:\${Partition}:transcribe:\${Region}:\${Account}:vocabulary-filter/\${VocabularyFilterName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/transcribe/latest/dg/API_LanguageModel.html">languagemodel</a></td>
                    <td>arn:\${Partition}:transcribe:\${Region}:\${Account}:language-model/\${ModelName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/transcribe/latest/dg/API_MedicalTranscriptionJob.html">medicaltranscriptionjob</a></td>
                    <td>arn:\${Partition}:transcribe:\${Region}:\${Account}:medical-transcription-job/\${JobName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/transcribe/latest/dg/API_CreateMedicalVocabulary.html">medicalvocabulary</a></td>
                    <td>arn:\${Partition}:transcribe:\${Region}:\${Account}:medical-vocabulary/\${VocabularyName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/transcribe/latest/dg/API_CallAnalyticsJob.html">callanalyticsjob</a></td>
                    <td>arn:\${Partition}:transcribe:\${Region}:\${Account}:analytics-job/\${JobName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/transcribe/latest/dg/API_CreateCallAnalyticsCategory.html">callanalyticscategory</a></td>
                    <td>arn:\${Partition}:transcribe:\${Region}:\${Account}:analytics-category/\${CategoryName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/transcribe/latest/dg/API_MedicalScribeJob.html">medicalscribejob</a></td>
                    <td>arn:\${Partition}:transcribe:\${Region}:\${Account}:medical-scribe-job/\${JobName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Systems Manager Incident Manager Contacts</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssystemsmanagerincidentmanagercontacts.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html">contact</a></td>
                    <td>arn:\${Partition}:ssm-contacts:\${Region}:\${Account}:contact/\${ContactAlias}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html">contactchannel</a></td>
                    <td>arn:\${Partition}:ssm-contacts:\${Region}:\${Account}:contactchannel/\${ContactAlias}/\${ContactChannelId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/incident-manager/latest/userguide/escalation.html">engagement</a></td>
                    <td>arn:\${Partition}:ssm-contacts:\${Region}:\${Account}:engagement/\${ContactAlias}/\${EngagementId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/incident-manager/latest/userguide/escalation.html">page</a></td>
                    <td>arn:\${Partition}:ssm-contacts:\${Region}:\${Account}:page/\${ContactAlias}/\${PageId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-on-call-schedule.html">rotation</a></td>
                    <td>arn:\${Partition}:ssm-contacts:\${Region}:\${Account}:rotation/\${RotationId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Timestream InfluxDB</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazontimestreaminfluxdb.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_DbInstanceSummary.html">db-instance</a></td>
                    <td>arn:\${Partition}:timestream-influxdb:\${Region}:\${Account}:db-instance/\${DbInstanceIdentifier}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_DbParameterGroupSummary.html">db-parameter-group</a></td>
                    <td>arn:\${Partition}:timestream-influxdb:\${Region}:\${Account}:db-parameter-group/\${DbParameterGroupIdentifier}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Trusted Advisor</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awstrustedadvisor.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/awssupport/latest/APIReference/API_TrustedAdvisorCheckDescription.html">checks</a></td>
                    <td>arn:\${Partition}:trustedadvisor:\${Region}:\${Account}:checks/\${CategoryCode}/\${CheckId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Translate</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazontranslate.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/translate/latest/dg/how-custom-terminology.html">terminology</a></td>
                    <td>arn:\${Partition}:translate:\${Region}:\${Account}:terminology/\${ResourceName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/translate/latest/dg/customizing-translations-parallel-data.html">parallel-data</a></td>
                    <td>arn:\${Partition}:translate:\${Region}:\${Account}:parallel-data/\${ResourceName}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS User Notifications Contacts</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsusernotificationscontacts.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html">EmailContactResource</a></td>
                    <td>arn:\${Partition}:notifications-contacts::\${Account}:emailcontact/\${EmailContactId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Verified Access</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsverifiedaccess.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>AWS WAF</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awswaf.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ByteMatchSet.html">bytematchset</a></td>
                    <td>arn:\${Partition}:waf::\${Account}:bytematchset/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_IPSet.html">ipset</a></td>
                    <td>arn:\${Partition}:waf::\${Account}:ipset/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_RateBasedRule.html">ratebasedrule</a></td>
                    <td>arn:\${Partition}:waf::\${Account}:ratebasedrule/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_Rule.html">rule</a></td>
                    <td>arn:\${Partition}:waf::\${Account}:rule/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_SizeConstraintSet.html">sizeconstraintset</a></td>
                    <td>arn:\${Partition}:waf::\${Account}:sizeconstraintset/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_SqlInjectionMatchSet.html">sqlinjectionmatchset</a></td>
                    <td>arn:\${Partition}:waf::\${Account}:sqlinjectionset/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_WebACL.html">webacl</a></td>
                    <td>arn:\${Partition}:waf::\${Account}:webacl/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_XssMatchSet.html">xssmatchset</a></td>
                    <td>arn:\${Partition}:waf::\${Account}:xssmatchset/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_RegexMatchSet.html">regexmatchset</a></td>
                    <td>arn:\${Partition}:waf::\${Account}:regexmatch/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_RegexPatternSet.html">regexpatternset</a></td>
                    <td>arn:\${Partition}:waf::\${Account}:regexpatternset/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GeoMatchSet.html">geomatchset</a></td>
                    <td>arn:\${Partition}:waf::\${Account}:geomatchset/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_RuleGroup.html">rulegroup</a></td>
                    <td>arn:\${Partition}:waf::\${Account}:rulegroup/\${Id}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon VPC Lattice Services</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonvpclatticeservices.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html">Service</a></td>
                    <td>arn:\${Partition}:vpc-lattice:\${Region}:\${Account}:service/\${ServiceId}/\${RequestPath}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS User Notifications</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsusernotifications.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html">EventRule</a></td>
                    <td>arn:\${Partition}:notifications::\${Account}:configuration/\${NotificationConfigurationId}/rule/\${EventRuleId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html">NotificationConfiguration</a></td>
                    <td>arn:\${Partition}:notifications::\${Account}:configuration/\${NotificationConfigurationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html">NotificationEvent</a></td>
                    <td>arn:\${Partition}:notifications:\${Region}:\${Account}:configuration/\${NotificationConfigurationId}/event/\${NotificationEventId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon Verified Permissions</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonverifiedpermissions.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/policy-stores.html">policy-store</a></td>
                    <td>arn:\${Partition}:verifiedpermissions::\${Account}:policy-store/\${PolicyStoreId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon VPC Lattice</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonvpclattice.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html">ServiceNetwork</a></td>
                    <td>arn:\${Partition}:vpc-lattice:\${Region}:\${Account}:servicenetwork/\${ServiceNetworkId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html">Service</a></td>
                    <td>arn:\${Partition}:vpc-lattice:\${Region}:\${Account}:service/\${ServiceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-vpc-associations">ServiceNetworkVpcAssociation</a></td>
                    <td>arn:\${Partition}:vpc-lattice:\${Region}:\${Account}:servicenetworkvpcassociation/\${ServiceNetworkVpcAssociationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-service-associations">ServiceNetworkServiceAssociation</a></td>
                    <td>arn:\${Partition}:vpc-lattice:\${Region}:\${Account}:servicenetworkserviceassociation/\${ServiceNetworkServiceAssociationId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/target-groups.html">TargetGroup</a></td>
                    <td>arn:\${Partition}:vpc-lattice:\${Region}:\${Account}:targetgroup/\${TargetGroupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html">Listener</a></td>
                    <td>arn:\${Partition}:vpc-lattice:\${Region}:\${Account}:service/\${ServiceId}/listener/\${ListenerId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules">Rule</a></td>
                    <td>arn:\${Partition}:vpc-lattice:\${Region}:\${Account}:service/\${ServiceId}/listener/\${ListenerId}/rule/\${RuleId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/monitoring-access-logs.html">AccessLogSubscription</a></td>
                    <td>arn:\${Partition}:vpc-lattice:\${Region}:\${Account}:accesslogsubscription/\${AccessLogSubscriptionId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Transfer Family</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awstransferfamily.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/transfer/latest/userguide/create-user.html">user</a></td>
                    <td>arn:\${Partition}:transfer:\${Region}:\${Account}:user/\${ServerId}/\${UserName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/transfer/latest/userguide/configuring-servers.html">server</a></td>
                    <td>arn:\${Partition}:transfer:\${Region}:\${Account}:server/\${ServerId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/transfer/latest/userguide/transfer-workflows.html">workflow</a></td>
                    <td>arn:\${Partition}:transfer:\${Region}:\${Account}:workflow/\${WorkflowId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/transfer/latest/userguide/create-b2b-server.html">certificate</a></td>
                    <td>arn:\${Partition}:transfer:\${Region}:\${Account}:certificate/\${CertificateId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/transfer/latest/userguide/create-b2b-server.html">connector</a></td>
                    <td>arn:\${Partition}:transfer:\${Region}:\${Account}:connector/\${ConnectorId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/transfer/latest/userguide/create-b2b-server.html">profile</a></td>
                    <td>arn:\${Partition}:transfer:\${Region}:\${Account}:profile/\${ProfileId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/transfer/latest/userguide/create-b2b-server.html">agreement</a></td>
                    <td>arn:\${Partition}:transfer:\${Region}:\${Account}:agreement/\${AgreementId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/transfer/latest/userguide/edit-server-config.html">host-key</a></td>
                    <td>arn:\${Partition}:transfer:\${Region}:\${Account}:host-key/\${ServerId}/\${HostKeyId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Wickr</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awswickr.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/wickr/latest/adminguide/">network</a></td>
                    <td>arn:\${Partition}:wickr:\${Region}:\${Account}:network/\${NetworkId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon WorkLink</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonworklink.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/worklink/latest/api/API_CreateFleet.html">fleet</a></td>
                    <td>arn:\${Partition}:worklink::\${Account}:fleet/\${FleetName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon WorkDocs</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonworkdocs.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/workdocs/latest/adminguide/migration-tool.html">organization</a></td>
                    <td>arn:\${Partition}:workdocs:\${Region}:\${Account}:organization/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon WorkMail Message Flow</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonworkmailmessageflow.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/workmail/latest/adminguide/lambda-content.html">RawMessage</a></td>
                    <td>arn:\${Partition}:workmailmessageflow:\${Region}:\${Account}:message/\${OrganizationId}/\${Context}/\${MessageId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS Well-Architected Tool</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awswell-architectedtool.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_Workload.html">workload</a></td>
                    <td>arn:\${Partition}:wellarchitected:\${Region}:\${Account}:workload/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_Lens.html">lens</a></td>
                    <td>arn:\${Partition}:wellarchitected:\${Region}:\${Account}:lens/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_Profile.html">profile</a></td>
                    <td>arn:\${Partition}:wellarchitected:\${Region}:\${Account}:profile/\${ResourceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ReviewTemplate.html">review-template</a></td>
                    <td>arn:\${Partition}:wellarchitected:\${Region}:\${Account}:review-template/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS WAF Regional</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awswafregional.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ByteMatchSet.html">bytematchset</a></td>
                    <td>arn:\${Partition}:waf-regional:\${Region}:\${Account}:bytematchset/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_IPSet.html">ipset</a></td>
                    <td>arn:\${Partition}:waf-regional:\${Region}:\${Account}:ipset/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_WebACL.html">loadbalancer/app/</a></td>
                    <td>arn:\${Partition}:elasticloadbalancing:\${Region}:\${Account}:loadbalancer/app/\${LoadBalancerName}/\${LoadBalancerId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_RateBasedRule.html">ratebasedrule</a></td>
                    <td>arn:\${Partition}:waf-regional:\${Region}:\${Account}:ratebasedrule/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_Rule.html">rule</a></td>
                    <td>arn:\${Partition}:waf-regional:\${Region}:\${Account}:rule/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_SizeConstraintSet.html">sizeconstraintset</a></td>
                    <td>arn:\${Partition}:waf-regional:\${Region}:\${Account}:sizeconstraintset/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_SqlInjectionMatchSet.html">sqlinjectionmatchset</a></td>
                    <td>arn:\${Partition}:waf-regional:\${Region}:\${Account}:sqlinjectionset/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_WebACL.html">webacl</a></td>
                    <td>arn:\${Partition}:waf-regional:\${Region}:\${Account}:webacl/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_XssMatchSet.html">xssmatchset</a></td>
                    <td>arn:\${Partition}:waf-regional:\${Region}:\${Account}:xssmatchset/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_RegexMatchSet.html">regexmatchset</a></td>
                    <td>arn:\${Partition}:waf-regional:\${Region}:\${Account}:regexmatch/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_RegexPatternSet.html">regexpatternset</a></td>
                    <td>arn:\${Partition}:waf-regional:\${Region}:\${Account}:regexpatternset/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GeoMatchSet.html">geomatchset</a></td>
                    <td>arn:\${Partition}:waf-regional:\${Region}:\${Account}:geomatchset/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_RuleGroup.html">rulegroup</a></td>
                    <td>arn:\${Partition}:waf-regional:\${Region}:\${Account}:rulegroup/\${Id}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS WAF V2</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awswafv2.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_WebACL.html">webacl</a></td>
                    <td>arn:\${Partition}:wafv2:\${Region}:\${Account}:\${Scope}/webacl/\${Name}/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_IPSet.html">ipset</a></td>
                    <td>arn:\${Partition}:wafv2:\${Region}:\${Account}:\${Scope}/ipset/\${Name}/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_ManagedRuleSet.html">managedruleset</a></td>
                    <td>arn:\${Partition}:wafv2:\${Region}:\${Account}:\${Scope}/managedruleset/\${Name}/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html">rulegroup</a></td>
                    <td>arn:\${Partition}:wafv2:\${Region}:\${Account}:\${Scope}/rulegroup/\${Name}/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_RegexPatternSet.html">regexpatternset</a></td>
                    <td>arn:\${Partition}:wafv2:\${Region}:\${Account}:\${Scope}/regexpatternset/\${Name}/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_WebACL.html">loadbalancer/app/</a></td>
                    <td>arn:\${Partition}:elasticloadbalancing:\${Region}:\${Account}:loadbalancer/app/\${LoadBalancerName}/\${LoadBalancerId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_WebACL.html">apigateway</a></td>
                    <td>arn:\${Partition}:apigateway:\${Region}::/restapis/\${ApiId}/stages/\${StageName}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_WebACL.html">appsync</a></td>
                    <td>arn:\${Partition}:appsync:\${Region}:\${Account}:apis/\${GraphQLAPIId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_WebACL.html">userpool</a></td>
                    <td>arn:\${Partition}:cognito-idp:\${Region}:\${Account}:userpool/\${UserPoolId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_WebACL.html">apprunner</a></td>
                    <td>arn:\${Partition}:apprunner:\${Region}:\${Account}:service/\${ServiceName}/\${ServiceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/waf/latest/APIReference/API_WebACL.html">verified-access-instance</a></td>
                    <td>arn:\${Partition}:ec2:\${Region}:\${Account}:verified-access-instance/\${VerifiedAccessInstanceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon WorkMail</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonworkmail.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html">organization</a></td>
                    <td>arn:\${Partition}:workmail:\${Region}:\${Account}:organization/\${ResourceId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon WorkSpaces Application Manager</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonworkspacesapplicationmanager.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
        </tbody>
        </table>
        <h1>Amazon WorkSpaces Thin Client</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonworkspacesthinclient.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_Environment.html">environment</a></td>
                    <td>arn:\${Partition}:thinclient::\${Account}:environment/\${EnvironmentId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_Device.html">device</a></td>
                    <td>arn:\${Partition}:thinclient::\${Account}:device/\${DeviceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_SoftwareSet.html">softwareset</a></td>
                    <td>arn:\${Partition}:thinclient::\${Account}:softwareset/\${SoftwareSetId}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon WorkSpaces Web</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonworkspacesweb.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_CreateBrowserSettings.html">browserSettings</a></td>
                    <td>arn:\${Partition}:workspaces-web:\${Region}:\${Account}:browserSettings/\${BrowserSettingsId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_CreateIdentityProvider.html">identityProvider</a></td>
                    <td>arn:\${Partition}:workspaces-web:\${Region}:\${Account}:identityProvider/\${PortalId}/\${IdentityProviderId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_CreateNetworkSettings.html">networkSettings</a></td>
                    <td>arn:\${Partition}:workspaces-web:\${Region}:\${Account}:networkSettings/\${NetworkSettingsId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_CreatePortal.html">portal</a></td>
                    <td>arn:\${Partition}:workspaces-web:\${Region}:\${Account}:portal/\${PortalId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_CreateTrustStore.html">trustStore</a></td>
                    <td>arn:\${Partition}:workspaces-web:\${Region}:\${Account}:trustStore/\${TrustStoreId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_CreateUserSettings.html">userSettings</a></td>
                    <td>arn:\${Partition}:workspaces-web:\${Region}:\${Account}:userSettings/\${UserSettingsId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_CreateUserAccessLoggingSettings.html">userAccessLoggingSettings</a></td>
                    <td>arn:\${Partition}:workspaces-web:\${Region}:\${Account}:userAccessLoggingSettings/\${UserAccessLoggingSettingsId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_CreateIpAccessSettings.html">ipAccessSettings</a></td>
                    <td>arn:\${Partition}:workspaces-web:\${Region}:\${Account}:ipAccessSettings/\${IpAccessSettingsId}</td>
                </tr>
            </tbody>
        </table>
        <h1>AWS X-Ray</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsx-ray.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html#xray-concepts-groups">group</a></td>
                    <td>arn:\${Partition}:xray:\${Region}:\${Account}:group/\${GroupName}/\${Id}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html#xray-concepts-sampling">sampling-rule</a></td>
                    <td>arn:\${Partition}:xray:\${Region}:\${Account}:sampling-rule/\${SamplingRuleName}</td>
                </tr>
            </tbody>
        </table>
        <h1>Amazon WorkSpaces</h1>
        <p>Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonworkspaces.html</p>
        <table>
            <thead>
                <th width="300px">Service</th>
                <th width="600px">ARN</th> 
            </thead>
            <tbody>
           <tr>
                    <td><a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/manage-workspaces-directory.html">directoryid</a></td>
                    <td>arn:\${Partition}:workspaces:\${Region}:\${Account}:directory/\${DirectoryId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/bundles.html">workspacebundle</a></td>
                    <td>arn:\${Partition}:workspaces:\${Region}:\${Account}:workspacebundle/\${BundleId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp_workspace_management.html">workspaceid</a></td>
                    <td>arn:\${Partition}:workspaces:\${Region}:\${Account}:workspace/\${WorkspaceId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/bundles.html">workspaceimage</a></td>
                    <td>arn:\${Partition}:workspaces:\${Region}:\${Account}:workspaceimage/\${ImageId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-ip-access-control-groups.html">workspaceipgroup</a></td>
                    <td>arn:\${Partition}:workspaces:\${Region}:\${Account}:workspaceipgroup/\${GroupId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html">connectionalias</a></td>
                    <td>arn:\${Partition}:workspaces:\${Region}:\${Account}:connectionalias/\${ConnectionAliasId}</td>
                </tr>
               <tr>
                    <td><a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/application-bundle-management.html">workspaceapplication</a></td>
                    <td>arn:\${Partition}:workspaces:\${Region}:\${Account}:workspaceapplication/\${WorkSpaceApplicationId}</td>
                </tr>
            </tbody>
        </table>
        