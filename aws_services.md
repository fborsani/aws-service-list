# AWS App Runner
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsapprunner.html
| Service | ARN |
|---------|-----|
| [service](${UserGuideDocPage}architecture.html#architecture.resources) | arn:\${Partition}:apprunner:\${Region}:\${Account}:service/\${ServiceName}/\${ServiceId} |
| [connection](${UserGuideDocPage}architecture.html#architecture.resources) | arn:\${Partition}:apprunner:\${Region}:\${Account}:connection/\${ConnectionName}/\${ConnectionId} |
| [autoscalingconfiguration](${UserGuideDocPage}architecture.html#architecture.resources) | arn:\${Partition}:apprunner:\${Region}:\${Account}:autoscalingconfiguration/\${AutoscalingConfigurationName}/\${AutoscalingConfigurationVersion}/\${AutoscalingConfigurationId} |
| [observabilityconfiguration](${UserGuideDocPage}architecture.html#architecture.resources) | arn:\${Partition}:apprunner:\${Region}:\${Account}:observabilityconfiguration/\${ObservabilityConfigurationName}/\${ObservabilityConfigurationVersion}/\${ObservabilityConfigurationId} |
| [vpcconnector](${UserGuideDocPage}architecture.html#architecture.resources) | arn:\${Partition}:apprunner:\${Region}:\${Account}:vpcconnector/\${VpcConnectorName}/\${VpcConnectorVersion}/\${VpcConnectorId} |
| [vpcingressconnection](${UserGuideDocPage}architecture.html#architecture.resources) | arn:\${Partition}:apprunner:\${Region}:\${Account}:vpcingressconnection/\${VpcIngressConnectionName}/\${VpcIngressConnectionId} |
| [webacl](${UserGuideDocPage}waf.html) | arn:\${Partition}:wafv2:\${Region}:\${Account}:\${Scope}/webacl/\${Name}/\${Id} |
# AmazonMediaImport
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmediaimport.html
| Service | ARN |
|---------|-----|
# AWS Amplify
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsamplify.html
| Service | ARN |
|---------|-----|
| [apps](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html) | arn:\${Partition}:amplify:\${Region}:\${Account}:apps/\${AppId} |
| [branches](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html) | arn:\${Partition}:amplify:\${Region}:\${Account}:apps/\${AppId}/branches/\${BranchName} |
| [jobs](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html) | arn:\${Partition}:amplify:\${Region}:\${Account}:apps/\${AppId}/branches/\${BranchName}/jobs/\${JobId} |
| [domains](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html) | arn:\${Partition}:amplify:\${Region}:\${Account}:apps/\${AppId}/domains/\${DomainName} |
| [webhooks](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html) | arn:\${Partition}:amplify:\${Region}:\${Account}:webhooks/\${WebhookId} |
# Apache Kafka APIs for Amazon MSK clusters
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_apachekafkaapisforamazonmskclusters.html
| Service | ARN |
|---------|-----|
| [cluster](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#msk-iam-resources) | arn:\${Partition}:kafka:\${Region}:\${Account}:cluster/\${ClusterName}/\${ClusterUuid} |
| [topic](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#msk-iam-resources) | arn:\${Partition}:kafka:\${Region}:\${Account}:topic/\${ClusterName}/\${ClusterUuid}/\${TopicName} |
| [group](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#msk-iam-resources) | arn:\${Partition}:kafka:\${Region}:\${Account}:group/\${ClusterName}/\${ClusterUuid}/\${GroupName} |
| [transactional-id](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#msk-iam-resources) | arn:\${Partition}:kafka:\${Region}:\${Account}:transactional-id/\${ClusterName}/\${ClusterUuid}/\${TransactionalId} |
# Amazon API Gateway
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonapigateway.html
| Service | ARN |
|---------|-----|
| [execute-api-general](execute-api-general) | arn:\${Partition}:execute-api:\${Region}:\${Account}:\${ApiId}/\${Stage}/\${Method}/\${ApiSpecificResourcePath} |
# AWS App2Container
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsapp2container.html
| Service | ARN |
|---------|-----|
# Amazon API Gateway Management V2
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonapigatewaymanagementv2.html
| Service | ARN |
|---------|-----|
| [AccessLogSettings](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/stages/\${StageName}/accesslogsettings |
| [Api](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId} |
| [Apis](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/apis |
| [ApiMapping](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/domainnames/\${DomainName}/apimappings/\${ApiMappingId} |
| [ApiMappings](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/domainnames/\${DomainName}/apimappings |
| [Authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/authorizers/\${AuthorizerId} |
| [Authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/authorizers |
| [AuthorizersCache](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/stages/\${StageName}/cache/authorizers |
| [Cors](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/cors |
| [Deployment](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/deployments/\${DeploymentId} |
| [Deployments](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/deployments |
| [ExportedAPI](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/exports/\${Specification} |
| [Integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/integrations/\${IntegrationId} |
| [Integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/integrations |
| [IntegrationResponse](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/integrations/\${IntegrationId}/integrationresponses/\${IntegrationResponseId} |
| [IntegrationResponses](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/integrations/\${IntegrationId}/integrationresponses |
| [Model](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/models/\${ModelId} |
| [Models](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/models |
| [ModelTemplate](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/models/\${ModelId}/template |
| [Route](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/routes/\${RouteId} |
| [Routes](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/routes |
| [RouteResponse](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/routes/\${RouteId}/routeresponses/\${RouteResponseId} |
| [RouteResponses](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/routes/\${RouteId}/routeresponses |
| [RouteRequestParameter](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/routes/\${RouteId}/requestparameters/\${RequestParameterKey} |
| [RouteSettings](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/stages/\${StageName}/routesettings/\${RouteKey} |
| [Stage](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/stages/\${StageName} |
| [Stages](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/apis/\${ApiId}/stages |
| [VpcLink](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/vpclinks/\${VpcLinkId} |
| [VpcLinks](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/vpclinks |
# AWS Activate
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsactivate.html
| Service | ARN |
|---------|-----|
# AWS App Mesh
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsappmesh.html
| Service | ARN |
|---------|-----|
| [mesh](https://docs.aws.amazon.com/app-mesh/latest/userguide/meshes.html) | arn:\${Partition}:appmesh:\${Region}:\${Account}:mesh/\${MeshName} |
| [virtualService](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_services.html) | arn:\${Partition}:appmesh:\${Region}:\${Account}:mesh/\${MeshName}/virtualService/\${VirtualServiceName} |
| [virtualNode](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_nodes.html) | arn:\${Partition}:appmesh:\${Region}:\${Account}:mesh/\${MeshName}/virtualNode/\${VirtualNodeName} |
| [virtualRouter](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_routers.html) | arn:\${Partition}:appmesh:\${Region}:\${Account}:mesh/\${MeshName}/virtualRouter/\${VirtualRouterName} |
| [route](https://docs.aws.amazon.com/app-mesh/latest/userguide/routes.html) | arn:\${Partition}:appmesh:\${Region}:\${Account}:mesh/\${MeshName}/virtualRouter/\${VirtualRouterName}/route/\${RouteName} |
| [virtualGateway](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_gateways.html) | arn:\${Partition}:appmesh:\${Region}:\${Account}:mesh/\${MeshName}/virtualGateway/\${VirtualGatewayName} |
| [gatewayRoute](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_gateways.html) | arn:\${Partition}:appmesh:\${Region}:\${Account}:mesh/\${MeshName}/virtualGateway/\${VirtualGatewayName}/gatewayRoute/\${GatewayRouteName} |
# AWS Account Management
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsaccountmanagement.html
| Service | ARN |
|---------|-----|
| [account](https://docs.aws.amazon.com/accounts/latest/reference/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources) | arn:\${Partition}:account::\${Account}:account |
| [accountInOrganization](https://docs.aws.amazon.com/accounts/latest/reference/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources) | arn:\${Partition}:account::\${ManagementAccountId}:account/o-\${OrganizationId}/\${MemberAccountId} |
# AWS Amplify UI Builder
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsamplifyuibuilder.html
| Service | ARN |
|---------|-----|
| [CodegenJobResource](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CodegenJob.html) | arn:\${Partition}:amplifyuibuilder:\${Region}:\${Account}:app/\${AppId}/environment/\${EnvironmentName}/codegen-jobs/\${Id} |
| [ComponentResource](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_Component.html) | arn:\${Partition}:amplifyuibuilder:\${Region}:\${Account}:app/\${AppId}/environment/\${EnvironmentName}/components/\${Id} |
| [FormResource](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_Form.html) | arn:\${Partition}:amplifyuibuilder:\${Region}:\${Account}:app/\${AppId}/environment/\${EnvironmentName}/forms/\${Id} |
| [ThemeResource](https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_Theme.html) | arn:\${Partition}:amplifyuibuilder:\${Region}:\${Account}:app/\${AppId}/environment/\${EnvironmentName}/themes/\${Id} |
# AWS App Mesh Preview
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsappmeshpreview.html
| Service | ARN |
|---------|-----|
| [mesh](https://docs.aws.amazon.com/app-mesh/latest/userguide/meshes.html) | arn:\${Partition}:appmesh-preview:\${Region}:\${Account}:mesh/\${MeshName} |
| [virtualService](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_services.html) | arn:\${Partition}:appmesh-preview:\${Region}:\${Account}:mesh/\${MeshName}/virtualService/\${VirtualServiceName} |
| [virtualNode](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_nodes.html) | arn:\${Partition}:appmesh-preview:\${Region}:\${Account}:mesh/\${MeshName}/virtualNode/\${VirtualNodeName} |
| [virtualRouter](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_routers.html) | arn:\${Partition}:appmesh-preview:\${Region}:\${Account}:mesh/\${MeshName}/virtualRouter/\${VirtualRouterName} |
| [route](https://docs.aws.amazon.com/app-mesh/latest/userguide/routes.html) | arn:\${Partition}:appmesh-preview:\${Region}:\${Account}:mesh/\${MeshName}/virtualRouter/\${VirtualRouterName}/route/\${RouteName} |
| [virtualGateway](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_gateways.html) | arn:\${Partition}:appmesh-preview:\${Region}:\${Account}:mesh/\${MeshName}/virtualGateway/\${VirtualGatewayName} |
| [gatewayRoute](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_gateways.html) | arn:\${Partition}:appmesh-preview:\${Region}:\${Account}:mesh/\${MeshName}/virtualGateway/\${VirtualGatewayName}/gatewayRoute/\${GatewayRouteName} |
# Amazon API Gateway Management
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonapigatewaymanagement.html
| Service | ARN |
|---------|-----|
| [Account](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/account |
| [ApiKey](https://docs.aws.amazon.com/apigateway/latest/api/API_ApiKey.html) | arn:\${Partition}:apigateway:\${Region}::/apikeys/\${ApiKeyId} |
| [ApiKeys](https://docs.aws.amazon.com/apigateway/latest/api/API_ApiKey.html) | arn:\${Partition}:apigateway:\${Region}::/apikeys |
| [Authorizer](https://docs.aws.amazon.com/apigateway/latest/api/API_Authorizer.html) | arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/authorizers/\${AuthorizerId} |
| [Authorizers](https://docs.aws.amazon.com/apigateway/latest/api/API_Authorizer.html) | arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/authorizers |
| [BasePathMapping](https://docs.aws.amazon.com/apigateway/latest/api/API_BasePathMapping.html) | arn:\${Partition}:apigateway:\${Region}::/domainnames/\${DomainName}/basepathmappings/\${BasePath} |
| [BasePathMappings](https://docs.aws.amazon.com/apigateway/latest/api/API_BasePathMapping.html) | arn:\${Partition}:apigateway:\${Region}::/domainnames/\${DomainName}/basepathmappings |
| [ClientCertificate](https://docs.aws.amazon.com/apigateway/latest/api/API_ClientCertificate.html) | arn:\${Partition}:apigateway:\${Region}::/clientcertificates/\${ClientCertificateId} |
| [ClientCertificates](https://docs.aws.amazon.com/apigateway/latest/api/API_ClientCertificate.html) | arn:\${Partition}:apigateway:\${Region}::/clientcertificates |
| [Deployment](https://docs.aws.amazon.com/apigateway/latest/api/API_Deployment.html) | arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/deployments/\${DeploymentId} |
| [Deployments](https://docs.aws.amazon.com/apigateway/latest/api/API_Deployment.html) | arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/deployments |
| [DocumentationPart](https://docs.aws.amazon.com/apigateway/latest/api/API_DocumentationPart.html) | arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/documentation/parts/\${DocumentationPartId} |
| [DocumentationParts](https://docs.aws.amazon.com/apigateway/latest/api/API_DocumentationPart.html) | arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/documentation/parts |
| [DocumentationVersion](https://docs.aws.amazon.com/apigateway/latest/api/API_DocumentationVersion.html) | arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/documentation/versions/\${DocumentationVersionId} |
| [DocumentationVersions](https://docs.aws.amazon.com/apigateway/latest/api/API_DocumentationVersion.html) | arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/documentation/versions |
| [DomainName](https://docs.aws.amazon.com/apigateway/latest/api/API_DomainName.html) | arn:\${Partition}:apigateway:\${Region}::/domainnames/\${DomainName} |
| [DomainNames](https://docs.aws.amazon.com/apigateway/latest/api/API_DomainName.html) | arn:\${Partition}:apigateway:\${Region}::/domainnames |
| [GatewayResponse](https://docs.aws.amazon.com/apigateway/latest/api/API_GatewayResponse.html) | arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/gatewayresponses/\${ResponseType} |
| [GatewayResponses](https://docs.aws.amazon.com/apigateway/latest/api/API_GatewayResponse.html) | arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/gatewayresponses |
| [Integration](https://docs.aws.amazon.com/apigateway/latest/api/API_Integration.html) | arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/resources/\${ResourceId}/methods/\${HttpMethodType}/integration |
| [IntegrationResponse](https://docs.aws.amazon.com/apigateway/latest/api/API_IntegrationResponse.html) | arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/resources/\${ResourceId}/methods/\${HttpMethodType}/integration/responses/\${StatusCode} |
| [Method](https://docs.aws.amazon.com/apigateway/latest/api/API_Method.html) | arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/resources/\${ResourceId}/methods/\${HttpMethodType} |
| [MethodResponse](https://docs.aws.amazon.com/apigateway/latest/api/API_MethodResponse.html) | arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/resources/\${ResourceId}/methods/\${HttpMethodType}/responses/\${StatusCode} |
| [Model](https://docs.aws.amazon.com/apigateway/latest/api/API_Model.html) | arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/models/\${ModelName} |
| [Models](https://docs.aws.amazon.com/apigateway/latest/api/API_Model.html) | arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/models |
| [RequestValidator](https://docs.aws.amazon.com/apigateway/latest/api/API_RequestValidator.html) | arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/requestvalidators/\${RequestValidatorId} |
| [RequestValidators](https://docs.aws.amazon.com/apigateway/latest/api/API_RequestValidator.html) | arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/requestvalidators |
| [Resource](https://docs.aws.amazon.com/apigateway/latest/api/API_Resource.html) | arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/resources/\${ResourceId} |
| [Resources](https://docs.aws.amazon.com/apigateway/latest/api/API_Resource.html) | arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/resources |
| [RestApi](https://docs.aws.amazon.com/apigateway/latest/api/API_RestApi.html) | arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId} |
| [RestApis](https://docs.aws.amazon.com/apigateway/latest/api/API_RestApi.html) | arn:\${Partition}:apigateway:\${Region}::/restapis |
| [Sdk](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/stages/\${StageName}/sdks/\${SdkType} |
| [Stage](https://docs.aws.amazon.com/apigateway/latest/api/API_Stage.html) | arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/stages/\${StageName} |
| [Stages](https://docs.aws.amazon.com/apigateway/latest/api/API_Stage.html) | arn:\${Partition}:apigateway:\${Region}::/restapis/\${RestApiId}/stages |
| [Template](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | arn:\${Partition}:apigateway:\${Region}::/restapis/models/\${ModelName}/template |
| [UsagePlan](https://docs.aws.amazon.com/apigateway/latest/api/API_UsagePlan.html) | arn:\${Partition}:apigateway:\${Region}::/usageplans/\${UsagePlanId} |
| [UsagePlans](https://docs.aws.amazon.com/apigateway/latest/api/API_UsagePlan.html) | arn:\${Partition}:apigateway:\${Region}::/usageplans |
| [UsagePlanKey](https://docs.aws.amazon.com/apigateway/latest/api/API_UsagePlanKey.html) | arn:\${Partition}:apigateway:\${Region}::/usageplans/\${UsagePlanId}/keys/\${Id} |
| [UsagePlanKeys](https://docs.aws.amazon.com/apigateway/latest/api/API_UsagePlanKey.html) | arn:\${Partition}:apigateway:\${Region}::/usageplans/\${UsagePlanId}/keys |
| [VpcLink](https://docs.aws.amazon.com/apigateway/latest/api/API_VpcLink.html) | arn:\${Partition}:apigateway:\${Region}::/vpclinks/\${VpcLinkId} |
| [VpcLinks](https://docs.aws.amazon.com/apigateway/latest/api/API_VpcLink.html) | arn:\${Partition}:apigateway:\${Region}::/vpclinks |
| [Tags](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-tagging.html) | arn:\${Partition}:apigateway:\${Region}::/tags/\${UrlEncodedResourceARN} |
# AWS Amplify Admin
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsamplifyadmin.html
| Service | ARN |
|---------|-----|
| [created-backend](https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend.html) | arn:\${Partition}:amplifybackend:\${Region}:\${Account}:/backend/* |
| [backend](https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend.html) | arn:\${Partition}:amplifybackend:\${Region}:\${Account}:/backend/\${AppId}/* |
| [environment](https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-api-backendenvironmentname-details.html) | arn:\${Partition}:amplifybackend:\${Region}:\${Account}:/backend/\${AppId}/environments/* |
| [api](https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-api.html) | arn:\${Partition}:amplifybackend:\${Region}:\${Account}:/backend/\${AppId}/api/* |
| [auth](https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-auth.html) | arn:\${Partition}:amplifybackend:\${Region}:\${Account}:/backend/\${AppId}/auth/* |
| [job](https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-job-backendenvironmentname.html) | arn:\${Partition}:amplifybackend:\${Region}:\${Account}:/backend/\${AppId}/job/* |
| [config](https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-config.html) | arn:\${Partition}:amplifybackend:\${Region}:\${Account}:/backend/\${AppId}/config/* |
| [token](https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-token.html) | arn:\${Partition}:amplifybackend:\${Region}:\${Account}:/backend/\${AppId}/challenge/* |
| [storage](https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-storage.html) | arn:\${Partition}:amplifybackend:\${Region}:\${Account}:/backend/\${AppId}/storage/* |
# AWS Application Auto Scaling
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsapplicationautoscaling.html
| Service | ARN |
|---------|-----|
| [ScalableTarget](https://docs.aws.amazon.com/autoscaling/application/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources) | arn:\${Partition}:application-autoscaling:\${Region}:\${Account}:scalable-target/\${ResourceId} |
# Alexa for Business
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_alexaforbusiness.html
| Service | ARN |
|---------|-----|
| [profile](https://docs.aws.amazon.com/a4b/latest/APIReference/API_Profile.html) | arn:\${Partition}:a4b:\${Region}:\${Account}:profile/\${ResourceId} |
| [room](https://docs.aws.amazon.com/a4b/latest/APIReference/API_Room.html) | arn:\${Partition}:a4b:\${Region}:\${Account}:room/\${ResourceId} |
| [device](https://docs.aws.amazon.com/a4b/latest/APIReference/API_Device.html) | arn:\${Partition}:a4b:\${Region}:\${Account}:device/\${ResourceId} |
| [skillgroup](https://docs.aws.amazon.com/a4b/latest/APIReference/API_SkillGroup.html) | arn:\${Partition}:a4b:\${Region}:\${Account}:skill-group/\${ResourceId} |
| [user](https://docs.aws.amazon.com/a4b/latest/APIReference/API_UserData.html) | arn:\${Partition}:a4b:\${Region}:\${Account}:user/\${ResourceId} |
| [addressbook](https://docs.aws.amazon.com/a4b/latest/APIReference/API_AddressBook.html) | arn:\${Partition}:a4b:\${Region}:\${Account}:address-book/\${ResourceId} |
| [conferenceprovider](https://docs.aws.amazon.com/a4b/latest/APIReference/API_ConferenceProvider.html) | arn:\${Partition}:a4b:\${Region}:\${Account}:conference-provider/\${ResourceId} |
| [contact](https://docs.aws.amazon.com/a4b/latest/APIReference/API_Contact.html) | arn:\${Partition}:a4b:\${Region}:\${Account}:contact/\${ResourceId} |
| [schedule](https://docs.aws.amazon.com/a4b/latest/APIReference/API_BusinessReportSchedule.html) | arn:\${Partition}:a4b:\${Region}:\${Account}:schedule/\${ResourceId} |
| [networkprofile](https://docs.aws.amazon.com/a4b/latest/APIReference/API_NetworkProfile.html) | arn:\${Partition}:a4b:\${Region}:\${Account}:network-profile/\${ResourceId} |
| [gateway](https://docs.aws.amazon.com/a4b/latest/APIReference/API_Gateway.html) | arn:\${Partition}:a4b:\${Region}:\${Account}:gateway/\${ResourceId} |
| [gatewaygroup](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GatewayGroup.html) | arn:\${Partition}:a4b:\${Region}:\${Account}:gateway-group/\${ResourceId} |
# AWS Application Cost Profiler Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsapplicationcostprofilerservice.html
| Service | ARN |
|---------|-----|
# Application Discovery Arsenal
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_applicationdiscoveryarsenal.html
| Service | ARN |
|---------|-----|
# AWS Application Discovery Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsapplicationdiscoveryservice.html
| Service | ARN |
|---------|-----|
# AWS AppFabric
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsappfabric.html
| Service | ARN |
|---------|-----|
| [appbundle](https://docs.aws.amazon.com/appfabric/latest/api/API_AppBundle.html) | arn:\${Partition}:appfabric:\${Region}:\${Account}:appbundle/\${AppBundleIdentifier} |
| [appauthorization](https://docs.aws.amazon.com/appfabric/latest/api/API_AppAuthorization.html) | arn:\${Partition}:appfabric:\${Region}:\${Account}:appbundle/\${AppbundleId}/appauthorization/\${AppAuthorizationIdentifier} |
| [ingestion](https://docs.aws.amazon.com/appfabric/latest/api/API_Ingestion.html) | arn:\${Partition}:appfabric:\${Region}:\${Account}:appbundle/\${AppbundleId}/ingestion/\${IngestionIdentifier} |
| [ingestiondestination](https://docs.aws.amazon.com/appfabric/latest/api/API_IngestionDestination.html) | arn:\${Partition}:appfabric:\${Region}:\${Account}:appbundle/\${AppbundleId}/ingestion/\${IngestionIdentifier}/ingestiondestination/\${IngestionDestinationIdentifier} |
# Amazon AppIntegrations
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonappintegrations.html
| Service | ARN |
|---------|-----|
| [event-integration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_EventIntegration.html) | arn:\${Partition}:app-integrations:\${Region}:\${Account}:event-integration/\${EventIntegrationName} |
| [event-integration-association](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_EventIntegrationAssociation.html) | arn:\${Partition}:app-integrations:\${Region}:\${Account}:event-integration-association/\${EventIntegrationName}/\${ResourceId} |
| [data-integration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DataIntegrationSummary.html) | arn:\${Partition}:app-integrations:\${Region}:\${Account}:data-integration/\${DataIntegrationId} |
| [data-integration-association](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DataIntegrationAssociationSummary.html) | arn:\${Partition}:app-integrations:\${Region}:\${Account}:data-integration-association/\${DataIntegrationId}/\${ResourceId} |
| [application](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ApplicationSummary.html) | arn:\${Partition}:app-integrations:\${Region}:\${Account}:application/\${ApplicationId} |
| [application-association](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ApplicationAssociationSummary.html) | arn:\${Partition}:app-integrations:\${Region}:\${Account}:application-association/\${ApplicationId}/\${ApplicationAssociationId} |
# AWS Application Transformation Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsapplicationtransformationservice.html
| Service | ARN |
|---------|-----|
# Amazon AppFlow
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonappflow.html
| Service | ARN |
|---------|-----|
| [connectorprofile](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ConnectorProfile.html) | arn:\${Partition}:appflow:\${Region}:\${Account}:connectorprofile/\${ProfileName} |
| [flow](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_FlowDefinition.html) | arn:\${Partition}:appflow:\${Region}:\${Account}:flow/\${FlowName} |
| [connector](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ConnectorDetail.html) | arn:\${Partition}:appflow:\${Region}:\${Account}:connector/\${ConnectorLabel} |
# AWS Artifact
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsartifact.html
| Service | ARN |
|---------|-----|
| [report-package](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html) | arn:\${Partition}:artifact:::report-package/* |
| [customer-agreement](https://docs.aws.amazon.com/artifact/latest/ug/managing-agreements.html) | arn:\${Partition}:artifact::\${Account}:customer-agreement/* |
| [agreement](https://docs.aws.amazon.com/artifact/latest/ug/managing-agreements.html) | arn:\${Partition}:artifact:::agreement/* |
| [report](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html) | arn:\${Partition}:artifact:\${Region}::report/\${ReportId}:\${Version} |
# AWS AppConfig
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsappconfig.html
| Service | ARN |
|---------|-----|
| [application](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-application.html) | arn:\${Partition}:appconfig:\${Region}:\${Account}:application/\${ApplicationId} |
| [environment](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-environment.html) | arn:\${Partition}:appconfig:\${Region}:\${Account}:application/\${ApplicationId}/environment/\${EnvironmentId} |
| [configurationprofile](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile.html) | arn:\${Partition}:appconfig:\${Region}:\${Account}:application/\${ApplicationId}/configurationprofile/\${ConfigurationProfileId} |
| [deploymentstrategy](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy.html) | arn:\${Partition}:appconfig:\${Region}:\${Account}:deploymentstrategy/\${DeploymentStrategyId} |
| [deployment](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-deploying.html) | arn:\${Partition}:appconfig:\${Region}:\${Account}:application/\${ApplicationId}/environment/\${EnvironmentId}/deployment/\${DeploymentNumber} |
| [hostedconfigurationversion](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile.html) | arn:\${Partition}:appconfig:\${Region}:\${Account}:application/\${ApplicationId}/configurationprofile/\${ConfigurationProfileId}/hostedconfigurationversion/\${VersionNumber} |
| [configuration](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-retrieving-the-configuration.html) | arn:\${Partition}:appconfig:\${Region}:\${Account}:application/\${ApplicationId}/environment/\${EnvironmentId}/configuration/\${ConfigurationProfileId} |
| [extension](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html) | arn:\${Partition}:appconfig:\${Region}:\${Account}:extension/\${ExtensionId}/\${ExtensionVersionNumber} |
| [extensionassociation](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html) | arn:\${Partition}:appconfig:\${Region}:\${Account}:extensionassociation/\${ExtensionAssociationId} |
# AWS AppSync
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsappsync.html
| Service | ARN |
|---------|-----|
| [datasource](https://docs.aws.amazon.com/appsync/latest/devguide/attaching-a-data-source.html) | arn:\${Partition}:appsync:\${Region}:\${Account}:apis/\${GraphQLAPIId}/datasources/\${DatasourceName} |
| [domain](https://docs.aws.amazon.com/appsync/latest/devguide/custom-domain-name.html) | arn:\${Partition}:appsync:\${Region}:\${Account}:domainnames/\${DomainName} |
| [graphqlapi](https://docs.aws.amazon.com/appsync/latest/devguide/designing-a-graphql-api.html) | arn:\${Partition}:appsync:\${Region}:\${Account}:apis/\${GraphQLAPIId} |
| [field](https://docs.aws.amazon.com/appsync/latest/devguide/configuring-resolvers.html) | arn:\${Partition}:appsync:\${Region}:\${Account}:apis/\${GraphQLAPIId}/types/\${TypeName}/fields/\${FieldName} |
| [type](https://docs.aws.amazon.com/appsync/latest/devguide/designing-your-schema.html#adding-a-root-query-type) | arn:\${Partition}:appsync:\${Region}:\${Account}:apis/\${GraphQLAPIId}/types/\${TypeName} |
| [function](https://docs.aws.amazon.com/appsync/latest/devguide/pipeline-resolvers.html) | arn:\${Partition}:appsync:\${Region}:\${Account}:apis/\${GraphQLAPIId}/functions/\${FunctionId} |
| [sourceApiAssociation](https://docs.aws.amazon.com/appsync/latest/devguide/merged-api.html) | arn:\${Partition}:appsync:\${Region}:\${Account}:apis/\${MergedGraphQLAPIId}/sourceApiAssociations/\${Associationid} |
| [mergedApiAssociation](https://docs.aws.amazon.com/appsync/latest/devguide/merged-api.html) | arn:\${Partition}:appsync:\${Region}:\${Account}:apis/\${SourceGraphQLAPIId}/mergedApiAssociations/\${Associationid} |
# AWS Backup storage
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbackupstorage.html
| Service | ARN |
|---------|-----|
# AWS B2B Data Interchange
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsb2bdatainterchange.html
| Service | ARN |
|---------|-----|
| [profile](https://docs.aws.amazon.com/b2bi/latest/userguide/) | arn:\${Partition}:b2bi:\${Region}:\${Account}:profile/\${ResourceId} |
| [capability](https://docs.aws.amazon.com/b2bi/latest/userguide/) | arn:\${Partition}:b2bi:\${Region}:\${Account}:capability/\${ResourceId} |
| [partnership](https://docs.aws.amazon.com/b2bi/latest/userguide/) | arn:\${Partition}:b2bi:\${Region}:\${Account}:partnership/\${ResourceId} |
| [transformer](https://docs.aws.amazon.com/b2bi/latest/userguide/) | arn:\${Partition}:b2bi:\${Region}:\${Account}:transformer/\${ResourceId} |
# Amazon AppStream 2.0
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonappstream2.0.html
| Service | ARN |
|---------|-----|
| [fleet](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html#what-is-concepts) | arn:\${Partition}:appstream:\${Region}:\${Account}:fleet/\${FleetName} |
| [image](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html#what-is-concepts) | arn:\${Partition}:appstream:\${Region}:\${Account}:image/\${ImageName} |
| [image-builder](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html#what-is-concepts) | arn:\${Partition}:appstream:\${Region}:\${Account}:image-builder/\${ImageBuilderName} |
| [stack](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html#what-is-concepts) | arn:\${Partition}:appstream:\${Region}:\${Account}:stack/\${StackName} |
| [app-block](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html#what-is-concepts) | arn:\${Partition}:appstream:\${Region}:\${Account}:app-block/\${AppBlockName} |
| [application](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html#what-is-concepts) | arn:\${Partition}:appstream:\${Region}:\${Account}:application/\${ApplicationName} |
| [app-block-builder](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html#what-is-concepts) | arn:\${Partition}:appstream:\${Region}:\${Account}:app-block-builder/\${AppBlockBuilderName} |
# AWS Audit Manager
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsauditmanager.html
| Service | ARN |
|---------|-----|
| [assessment](https://docs.aws.amazon.com/audit-manager/latest/userguide/API_Assessment.html) | arn:\${Partition}:auditmanager:\${Region}:\${Account}:assessment/\${AssessmentId} |
| [assessmentFramework](https://docs.aws.amazon.com/audit-manager/latest/userguide/API_AssessmentFramework.html) | arn:\${Partition}:auditmanager:\${Region}:\${Account}:assessmentFramework/\${AssessmentFrameworkId} |
| [assessmentControlSet](https://docs.aws.amazon.com/audit-manager/latest/userguide/API_AssessmentControlSet.html) | arn:\${Partition}:auditmanager:\${Region}:\${Account}:assessment/\${AssessmentId}/controlSet/\${ControlSetId} |
| [control](https://docs.aws.amazon.com/audit-manager/latest/userguide/API_Control.html) | arn:\${Partition}:auditmanager:\${Region}:\${Account}:control/\${ControlId} |
# AWS Auto Scaling
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsautoscaling.html
| Service | ARN |
|---------|-----|
# Amazon Athena
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonathena.html
| Service | ARN |
|---------|-----|
| [datacatalog](https://docs.aws.amazon.com/athena/latest/ug/datacatalogs-example-policies.html) | arn:\${Partition}:athena:\${Region}:\${Account}:datacatalog/\${DataCatalogName} |
| [workgroup](https://docs.aws.amazon.com/athena/latest/ug/example-policies-workgroup.html) | arn:\${Partition}:athena:\${Region}:\${Account}:workgroup/\${WorkGroupName} |
| [capacity-reservation](https://docs.aws.amazon.com/athena/latest/ug/example-policies-capacity-reservations.html) | arn:\${Partition}:athena:\${Region}:\${Account}:capacity-reservation/\${CapacityReservationName} |
# AWS Application Migration Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsapplicationmigrationservice.html
| Service | ARN |
|---------|-----|
| [JobResource](https://docs.aws.amazon.com/mgn/latest/ug/launching-target-servers.html) | arn:\${Partition}:mgn:\${Region}:\${Account}:job/\${JobID} |
| [ReplicationConfigurationTemplateResource](https://docs.aws.amazon.com/mgn/latest/ug/replication-settings-template.html) | arn:\${Partition}:mgn:\${Region}:\${Account}:replication-configuration-template/\${ReplicationConfigurationTemplateID} |
| [LaunchConfigurationTemplateResource](https://docs.aws.amazon.com/mgn/latest/ug/post-launch-settings.html) | arn:\${Partition}:mgn:\${Region}:\${Account}:launch-configuration-template/\${LaunchConfigurationTemplateID} |
| [VcenterClientResource](https://docs.aws.amazon.com/mgn/latest/ug/agentless-mgn.html) | arn:\${Partition}:mgn:\${Region}:\${Account}:vcenter-client/\${VcenterClientID} |
| [SourceServerResource](https://docs.aws.amazon.com/mgn/latest/ug/source-servers.html) | arn:\${Partition}:mgn:\${Region}:\${Account}:source-server/\${SourceServerID} |
| [ApplicationResource](https://docs.aws.amazon.com/mgn/latest/ug/applications.html) | arn:\${Partition}:mgn:\${Region}:\${Account}:application/\${ApplicationID} |
| [WaveResource](https://docs.aws.amazon.com/mgn/latest/ug/waves.html) | arn:\${Partition}:mgn:\${Region}:\${Account}:wave/\${WaveID} |
| [ImportResource](https://docs.aws.amazon.com/mgn/latest/ug/imports.html) | arn:\${Partition}:mgn:\${Region}:\${Account}:import/\${ImportID} |
| [ExportResource](https://docs.aws.amazon.com/mgn/latest/ug/exports.html) | arn:\${Partition}:mgn:\${Region}:\${Account}:export/\${ExportID} |
| [ConnectorResource](https://docs.aws.amazon.com/mgn/latest/ug/connectors.html) | arn:\${Partition}:mgn:\${Region}:\${Account}:connector/\${ConnectorID} |
# AWS Backup Gateway
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbackupgateway.html
| Service | ARN |
|---------|-----|
| [gateway](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_Gateway.html) | arn:\${Partition}:backup-gateway::\${Account}:gateway/\${GatewayId} |
| [hypervisor](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_Hypervisor.html) | arn:\${Partition}:backup-gateway::\${Account}:hypervisor/\${HypervisorId} |
| [virtualmachine](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_VirtualMachine.html) | arn:\${Partition}:backup-gateway::\${Account}:vm/\${VirtualmachineId} |
# AWS Backup
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbackup.html
| Service | ARN |
|---------|-----|
| [backupVault](https://docs.aws.amazon.com/aws-backup/latest/devguide/vaults.html) | arn:\${Partition}:backup:\${Region}:\${Account}:backup-vault:\${BackupVaultName} |
| [backupPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/about-backup-plans.html) | arn:\${Partition}:backup:\${Region}:\${Account}:backup-plan:\${BackupPlanId} |
| [recoveryPoint](https://docs.aws.amazon.com/aws-backup/latest/devguide/recovery-points.html) | arn:\${Partition}:\${Vendor}:\${Region}:*:\${ResourceType}:\${RecoveryPointId} |
| [framework](https://docs.aws.amazon.com/aws-backup/latest/devguide/working-with-audit-frameworks.html) | arn:\${Partition}:backup:\${Region}:\${Account}:framework:\${FrameworkName}-\${FrameworkId} |
| [reportPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-report-plan-api.html) | arn:\${Partition}:backup:\${Region}:\${Account}:report-plan:\${ReportPlanName}-\${ReportPlanId} |
| [legalHold](https://docs.aws.amazon.com/aws-backup/latest/devguide/legalhold.html) | arn:\${Partition}:backup:\${Region}:\${Account}:legal-hold:\${LegalHoldId} |
| [restoreTestingPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing.html) | arn:\${Partition}:backup:\${Region}:\${Account}:restore-testing-plan:\${RestoreTestingPlanName}-\${RestoreTestingPlanId} |
# AWS Billing
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbilling.html
| Service | ARN |
|---------|-----|
# AWS Batch
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbatch.html
| Service | ARN |
|---------|-----|
| [compute-environment](https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html) | arn:\${Partition}:batch:\${Region}:\${Account}:compute-environment/\${ComputeEnvironmentName} |
| [job-queue](https://docs.aws.amazon.com/batch/latest/userguide/job_queues.html) | arn:\${Partition}:batch:\${Region}:\${Account}:job-queue/\${JobQueueName} |
| [job-definition](https://docs.aws.amazon.com/batch/latest/userguide/job_definitions.html) | arn:\${Partition}:batch:\${Region}:\${Account}:job-definition/\${JobDefinitionName} |
| [job-definition-revision](https://docs.aws.amazon.com/batch/latest/userguide/job_definitions.html) | arn:\${Partition}:batch:\${Region}:\${Account}:job-definition/\${JobDefinitionName}:\${Revision} |
| [job](https://docs.aws.amazon.com/batch/latest/userguide/jobs.html) | arn:\${Partition}:batch:\${Region}:\${Account}:job/\${JobId} |
| [scheduling-policy](https://docs.aws.amazon.com/batch/latest/userguide/scheduling-policies.html) | arn:\${Partition}:batch:\${Region}:\${Account}:scheduling-policy/\${SchedulingPolicyName} |
# AWS Billing Conductor
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbillingconductor.html
| Service | ARN |
|---------|-----|
| [billinggroup](https://docs.aws.amazon.com/billingconductor/latest/userguide/understanding-abc.html) | arn:\${Partition}:billingconductor::\${Account}:billinggroup/\${BillingGroupId} |
| [pricingplan](https://docs.aws.amazon.com/billingconductor/latest/userguide/understanding-abc.html) | arn:\${Partition}:billingconductor::\${Account}:pricingplan/\${PricingPlanId} |
| [pricingrule](https://docs.aws.amazon.com/billingconductor/latest/userguide/understanding-abc.html) | arn:\${Partition}:billingconductor::\${Account}:pricingrule/\${PricingRuleId} |
| [customlineitem](https://docs.aws.amazon.com/billingconductor/latest/userguide/understanding-abc.html) | arn:\${Partition}:billingconductor::\${Account}:customlineitem/\${CustomLineItemId} |
# Amazon Bedrock
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrock.html
| Service | ARN |
|---------|-----|
| [foundation-model](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html) | arn:\${Partition}:bedrock:\${Region}::foundation-model/\${ResourceId} |
| [custom-model](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html) | arn:\${Partition}:bedrock:\${Region}:\${Account}:custom-model/\${ResourceId} |
| [provisioned-model](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html) | arn:\${Partition}:bedrock:\${Region}:\${Account}:provisioned-model/\${ResourceId} |
| [model-customization-job](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html) | arn:\${Partition}:bedrock:\${Region}:\${Account}:model-customization-job/\${ResourceId} |
| [agent](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html) | arn:\${Partition}:bedrock:\${Region}:\${Account}:agent/\${AgentId} |
| [agent-alias](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html) | arn:\${Partition}:bedrock:\${Region}:\${Account}:agent-alias/\${AgentId}/\${AgentAliasId} |
| [knowledge-base](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html) | arn:\${Partition}:bedrock:\${Region}:\${Account}:knowledge-base/\${KnowledgeBaseId} |
| [model-evaluation-job](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html) | arn:\${Partition}:bedrock:\${Region}:\${Account}:model-evaluation-job/\${ResourceId} |
| [evaluation-job](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html) | arn:\${Partition}:bedrock:\${Region}:\${Account}:evaluation-job/\${ResourceId} |
| [model-invocation-job](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html) | arn:\${Partition}:bedrock:\${Region}:\${Account}:model-invocation-job/\${JobIdentifier} |
| [guardrail](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html) | arn:\${Partition}:bedrock:\${Region}:\${Account}:guardrail/\${GuardrailId} |
# AWS Billing And Cost Management Data Exports
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbillingandcostmanagementdataexports.html
| Service | ARN |
|---------|-----|
| [export](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Export.html) | arn:\${Partition}:bcm-data-exports:\${Region}:\${Account}:export/\${Identifier} |
| [table](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Table.html) | arn:\${Partition}:bcm-data-exports:\${Region}:\${Account}:table/\${Identifier} |
# Amazon Braket
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbraket.html
| Service | ARN |
|---------|-----|
| [quantum-task](https://docs.aws.amazon.com/braket/latest/developerguide/braket-manage-access.html#resources) | arn:\${Partition}:braket:\${Region}:\${Account}:quantum-task/\${RandomId} |
| [job](https://docs.aws.amazon.com/braket/latest/developerguide/braket-manage-access.html#resources) | arn:\${Partition}:braket:\${Region}:\${Account}:job/\${JobName} |
# AWS Billing Console
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbillingconsole.html
| Service | ARN |
|---------|-----|
# AWS BugBust
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbugbust.html
| Service | ARN |
|---------|-----|
| [Event](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/event-managing.html) | arn:\${Partition}:bugbust:\${Region}:\${Account}:events/\${EventId} |
# AWS Budget Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbudgetservice.html
| Service | ARN |
|---------|-----|
| [budget](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html) | arn:\${Partition}:budgets::\${Account}:budget/\${BudgetName} |
| [budgetAction](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html) | arn:\${Partition}:budgets::\${Account}:budget/\${BudgetName}/action/\${ActionId} |
# AWS Certificate Manager
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscertificatemanager.html
| Service | ARN |
|---------|-----|
| [certificate](https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html#concept-acm-cert) | arn:\${Partition}:acm:\${Region}:\${Account}:certificate/\${CertificateId} |
# AWS Chatbot
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awschatbot.html
| Service | ARN |
|---------|-----|
| [ChatbotConfiguration](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html) | arn:\${Partition}:chatbot::\${Account}:chat-configuration/\${ConfigurationType}/\${ChatbotConfigurationName} |
# AWS Cloud Control API
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscloudcontrolapi.html
| Service | ARN |
|---------|-----|
# Amazon Cloud Directory
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonclouddirectory.html
| Service | ARN |
|---------|-----|
| [appliedSchema](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/cd_key_concepts.html#whatisdirectory) | arn:\${Partition}:clouddirectory:\${Region}:\${Account}:directory/\${DirectoryId}/schema/\${SchemaName}/\${Version} |
| [developmentSchema](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/cd_key_concepts.html#whatisdirectory) | arn:\${Partition}:clouddirectory:\${Region}:\${Account}:schema/development/\${SchemaName} |
| [directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/cd_key_concepts.html#whatisdirectory) | arn:\${Partition}:clouddirectory:\${Region}:\${Account}:directory/\${DirectoryId} |
| [publishedSchema](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/cd_key_concepts.html#whatisdirectory) | arn:\${Partition}:clouddirectory:\${Region}:\${Account}:schema/published/\${SchemaName}/\${Version} |
# AWS Cloud9
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscloud9.html
| Service | ARN |
|---------|-----|
| [environment](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awscloud9.html##awscloud9-environment) | arn:\${Partition}:cloud9:\${Region}:\${Account}:environment:\${ResourceId} |
# Amazon CloudFront KeyValueStore
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudfrontkeyvaluestore.html
| Service | ARN |
|---------|-----|
| [key-value-store](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/kvs-with-functions.html) | arn:\${Partition}:cloudfront::\${Account}:key-value-store/\${ResourceId} |
# AWS Clean Rooms ML
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscleanroomsml.html
| Service | ARN |
|---------|-----|
| [trainingdataset](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_TrainingDatasetSummary.html) | arn:\${Partition}:cleanrooms-ml:\${Region}:\${Account}:training-dataset/\${ResourceId} |
| [audiencemodel](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_AudienceModelSummary.html) | arn:\${Partition}:cleanrooms-ml:\${Region}:\${Account}:audience-model/\${ResourceId} |
| [configuredaudiencemodel](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ConfiguredAudienceModelSummary.html) | arn:\${Partition}:cleanrooms-ml:\${Region}:\${Account}:configured-audience-model/\${ResourceId} |
| [audiencegenerationjob](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_AudienceGenerationJobSummary.html) | arn:\${Partition}:cleanrooms-ml:\${Region}:\${Account}:audience-generation-job/\${ResourceId} |
# Amazon CloudSearch
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudsearch.html
| Service | ARN |
|---------|-----|
| [domain](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/creating-domains.html) | arn:\${Partition}:cloudsearch:\${Region}:\${Account}:domain/\${DomainName} |
# AWS Cloud Map
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscloudmap.html
| Service | ARN |
|---------|-----|
| [namespace](https://docs.aws.amazon.com/cloud-map/latest/dg/API_Namespace.html) | arn:\${Partition}:servicediscovery:\${Region}:\${Account}:namespace/\${NamespaceId} |
| [service](https://docs.aws.amazon.com/cloud-map/latest/dg/API_Service.html) | arn:\${Partition}:servicediscovery:\${Region}:\${Account}:service/\${ServiceId} |
# AWS CloudHSM
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscloudhsm.html
| Service | ARN |
|---------|-----|
| [backup](https://docs.aws.amazon.com/cloudhsm/latest/userguide/backups.html) | arn:\${Partition}:cloudhsm:\${Region}:\${Account}:backup/\${CloudHsmBackupInstanceName} |
| [cluster](https://docs.aws.amazon.com/cloudhsm/latest/userguide/clusters.html) | arn:\${Partition}:cloudhsm:\${Region}:\${Account}:cluster/\${CloudHsmClusterInstanceName} |
# AWS Clean Rooms
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscleanrooms.html
| Service | ARN |
|---------|-----|
| [analysistemplate](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam.html) | arn:\${Partition}:cleanrooms:\${Region}:\${Account}:membership/\${MembershipId}/analysistemplate/\${AnalysisTemplateId} |
| [collaboration](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam.html) | arn:\${Partition}:cleanrooms:\${Region}:\${Account}:collaboration/\${CollaborationId} |
| [configuredaudiencemodelassociation](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam.html) | arn:\${Partition}:cleanrooms:\${Region}:\${Account}:membership/\${MembershipId}/configuredaudiencemodelassociation/\${ConfiguredAudienceModelAssociationId} |
| [configuredtable](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam.html) | arn:\${Partition}:cleanrooms:\${Region}:\${Account}:configuredtable/\${ConfiguredTableId} |
| [configuredtableassociation](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam.html) | arn:\${Partition}:cleanrooms:\${Region}:\${Account}:membership/\${MembershipId}/configuredtableassociation/\${ConfiguredTableAssociationId} |
| [membership](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam.html) | arn:\${Partition}:cleanrooms:\${Region}:\${Account}:membership/\${MembershipId} |
| [privacybudgettemplate](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam.html) | arn:\${Partition}:cleanrooms:\${Region}:\${Account}:membership/\${MembershipId}/privacybudgettemplate/\${PrivacyBudgetTemplateId} |
# AWS CloudShell
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscloudshell.html
| Service | ARN |
|---------|-----|
| [Environment](https://docs.aws.amazon.com/cloudshell/latest/userguide/sec-auth-with-identities.html#Environment) | arn:\${Partition}:cloudshell:\${Region}:\${Account}:environment/\${EnvironmentId} |
# AWS CloudTrail
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscloudtrail.html
| Service | ARN |
|---------|-----|
| [trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/how-cloudtrail-works.html#how-cloudtrail-works-trails) | arn:\${Partition}:cloudtrail:\${Region}:\${Account}:trail/\${TrailName} |
| [eventdatastore](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/how-cloudtrail-works.html#how-cloudtrail-works-lake) | arn:\${Partition}:cloudtrail:\${Region}:\${Account}:eventdatastore/\${EventDataStoreId} |
| [channel](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/how-cloudtrail-works.html#how-cloudtrail-works-channels) | arn:\${Partition}:cloudtrail:\${Region}:\${Account}:channel/\${ChannelId} |
# AWS CloudTrail Data
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscloudtraildata.html
| Service | ARN |
|---------|-----|
| [channel](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/how-cloudtrail-works.html#how-cloudtrail-works-channels) | arn:\${Partition}:cloudtrail:\${Region}:\${Account}:channel/\${ChannelId} |
# Amazon CloudFront
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudfront.html
| Service | ARN |
|---------|-----|
| [distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-working-with.html) | arn:\${Partition}:cloudfront::\${Account}:distribution/\${DistributionId} |
| [streaming-distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-working-with.html) | arn:\${Partition}:cloudfront::\${Account}:streaming-distribution/\${DistributionId} |
| [origin-access-identity](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html#private-content-restricting-access-to-s3-overview) | arn:\${Partition}:cloudfront::\${Account}:origin-access-identity/\${Id} |
| [field-level-encryption-config](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html) | arn:\${Partition}:cloudfront::\${Account}:field-level-encryption-config/\${Id} |
| [field-level-encryption-profile](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html) | arn:\${Partition}:cloudfront::\${Account}:field-level-encryption-profile/\${Id} |
| [cache-policy](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/working-with-policies.html) | arn:\${Partition}:cloudfront::\${Account}:cache-policy/\${Id} |
| [origin-request-policy](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/working-with-policies.html) | arn:\${Partition}:cloudfront::\${Account}:origin-request-policy/\${Id} |
| [realtime-log-config](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html) | arn:\${Partition}:cloudfront::\${Account}:realtime-log-config/\${Name} |
| [function](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.html) | arn:\${Partition}:cloudfront::\${Account}:function/\${Name} |
| [key-value-store](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/kvs-with-functions.html) | arn:\${Partition}:cloudfront::\${Account}:key-value-store/\${Name} |
| [response-headers-policy](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/working-with-policies.html) | arn:\${Partition}:cloudfront::\${Account}:response-headers-policy/\${Id} |
| [origin-access-control](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/working-with-policies.html) | arn:\${Partition}:cloudfront::\${Account}:origin-access-control/\${Id} |
| [continuous-deployment-policy](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/working-with-policies.html) | arn:\${Partition}:cloudfront::\${Account}:continuous-deployment-policy/\${Id} |
# AWS CloudFormation
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscloudformation.html
| Service | ARN |
|---------|-----|
| [changeset](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html#w2ab1b5c15c11) | arn:\${Partition}:cloudformation:\${Region}:\${Account}:changeSet/\${ChangeSetName}/\${Id} |
| [stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html#w2ab1b5c15b9) | arn:\${Partition}:cloudformation:\${Region}:\${Account}:stack/\${StackName}/\${Id} |
| [stackset](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stacksets-concepts-stackset) | arn:\${Partition}:cloudformation:\${Region}:\${Account}:stackset/\${StackSetName}:\${Id} |
| [stackset-target](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html) | arn:\${Partition}:cloudformation:\${Region}:\${Account}:stackset-target/\${StackSetTarget} |
| [type](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html) | arn:\${Partition}:cloudformation:\${Region}:\${Account}:type/resource/\${Type} |
| [generatedtemplate](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/generate-IaC.html) | arn:\${Partition}:cloudformation:\${Region}:\${Account}:generatedTemplate/\${Id} |
| [resourcescan](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/generate-IaC.html) | arn:\${Partition}:cloudformation:\${Region}:\${Account}:resourceScan/\${Id} |
# Amazon CloudWatch
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudwatch.html
| Service | ARN |
|---------|-----|
| [alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html) | arn:\${Partition}:cloudwatch:\${Region}:\${Account}:alarm:\${AlarmName} |
| [dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html) | arn:\${Partition}:cloudwatch::\${Account}:dashboard/\${DashboardName} |
| [insight-rule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html) | arn:\${Partition}:cloudwatch:\${Region}:\${Account}:insight-rule/\${InsightRuleName} |
| [metric-stream](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html) | arn:\${Partition}:cloudwatch:\${Region}:\${Account}:metric-stream/\${MetricStreamName} |
| [slo](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html) | arn:\${Partition}:cloudwatch:\${Region}:\${Account}:slo/\${SloName} |
| [service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html) | arn:\${Partition}:cloudwatch:\${Region}:\${Account}:service/\${ServiceName}-\${UniqueAttributesHex} |
# Amazon CloudWatch Network Monitor
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudwatchnetworkmonitor.html
| Service | ARN |
|---------|-----|
| [monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NM-components.html) | arn:\${Partition}:networkmonitor:\${Region}:\${Account}:monitor/\${MonitorName} |
| [probe](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NM-components.html) | arn:\${Partition}:networkmonitor:\${Region}:\${Account}:probe/\${ProbeId} |
# Amazon CloudWatch Internet Monitor
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudwatchinternetmonitor.html
| Service | ARN |
|---------|-----|
| [HealthEvent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-components.html) | arn:\${Partition}:internetmonitor:\${Region}:\${Account}:monitor/\${MonitorName}/health-event/\${EventId} |
| [Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-components.html) | arn:\${Partition}:internetmonitor:\${Region}:\${Account}:monitor/\${MonitorName} |
| [InternetEvent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-components.html) | arn:\${Partition}:internetmonitor::\${Account}:internet-event/\${InternetEventId} |
# Amazon CloudWatch Evidently
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudwatchevidently.html
| Service | ARN |
|---------|-----|
| [Project](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_Project.html) | arn:\${Partition}:evidently:\${Region}:\${Account}:project/\${ProjectName} |
| [Feature](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_Feature.html) | arn:\${Partition}:evidently:\${Region}:\${Account}:project/\${ProjectName}/feature/\${FeatureName} |
| [Experiment](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_Experiment.html) | arn:\${Partition}:evidently:\${Region}:\${Account}:project/\${ProjectName}/experiment/\${ExperimentName} |
| [Launch](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_Launch.html) | arn:\${Partition}:evidently:\${Region}:\${Account}:project/\${ProjectName}/launch/\${LaunchName} |
| [Segment](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_Segment.html) | arn:\${Partition}:evidently:\${Region}:\${Account}:segment/\${SegmentName} |
# Amazon CloudWatch Observability Access Manager
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudwatchobservabilityaccessmanager.html
| Service | ARN |
|---------|-----|
| [Link](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html) | arn:\${Partition}:oam:\${Region}:\${Account}:link/\${ResourceId} |
| [Sink](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html) | arn:\${Partition}:oam:\${Region}:\${Account}:sink/\${ResourceId} |
# Amazon CloudWatch Application Insights
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudwatchapplicationinsights.html
| Service | ARN |
|---------|-----|
# Amazon Chime
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonchime.html
| Service | ARN |
|---------|-----|
| [meeting](https://docs.aws.amazon.com/chime/latest/APIReference/API_Meeting.html) | arn:\${Partition}:chime::\${AccountId}:meeting/\${MeetingId} |
| [app-instance](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_AppInstance.html) | arn:\${Partition}:chime:\${Region}:\${AccountId}:app-instance/\${AppInstanceId} |
| [app-instance-user](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_AppInstanceUser.html) | arn:\${Partition}:chime:\${Region}:\${AccountId}:app-instance/\${AppInstanceId}/user/\${AppInstanceUserId} |
| [app-instance-bot](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_AppInstanceBot.html) | arn:\${Partition}:chime:\${Region}:\${AccountId}:app-instance/\${AppInstanceId}/bot/\${AppInstanceBotId} |
| [channel](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_Channel.html) | arn:\${Partition}:chime:\${Region}:\${AccountId}:app-instance/\${AppInstanceId}/channel/\${ChannelId} |
| [channel-flow](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelFlow.html) | arn:\${Partition}:chime:\${Region}:\${AccountId}:app-instance/\${AppInstanceId}/channel-flow/\${ChannelFlowId} |
| [media-pipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaPipeline.html) | arn:\${Partition}:chime:\${Region}:\${AccountId}:media-pipeline/\${MediaPipelineId} |
| [media-insights-pipeline-configuration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaInsightsPipelineConfiguration.html) | arn:\${Partition}:chime:\${Region}:\${AccountId}:media-insights-pipeline-configuration/\${ConfigurationName} |
| [media-pipeline-kinesis-video-stream-pool](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_KinesisVideoStreamPoolConfiguration.html) | arn:\${Partition}:chime:\${Region}:\${AccountId}:media-pipeline-kinesis-video-stream-pool/\${PoolName} |
| [voice-profile-domain](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceProfileDomain.html) | arn:\${Partition}:chime:\${Region}:\${AccountId}:voice-profile-domain/\${VoiceProfileDomainId} |
| [voice-profile](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceProfile.html) | arn:\${Partition}:chime:\${Region}:\${AccountId}:voice-profile/\${VoiceProfileId} |
| [voice-connector](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_VoiceConnector.html) | arn:\${Partition}:chime:\${Region}:\${AccountId}:vc/\${VoiceConnectorId} |
| [sip-media-application](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_SipMediaApplication.html) | arn:\${Partition}:chime:\${Region}:\${AccountId}:sma/\${SipMediaApplicationId} |
# Amazon CloudWatch Logs
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudwatchlogs.html
| Service | ARN |
|---------|-----|
| [log-group](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_LogGroup.html) | arn:\${Partition}:logs:\${Region}:\${Account}:log-group:\${LogGroupName} |
| [log-stream](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_LogStream.html) | arn:\${Partition}:logs:\${Region}:\${Account}:log-group:\${LogGroupName}:log-stream:\${LogStreamName} |
| [destination](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_Destination.html) | arn:\${Partition}:logs:\${Region}:\${Account}:destination:\${DestinationName} |
| [delivery-source](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeliverySource.html) | arn:\${Partition}:logs:\${Region}:\${Account}:delivery-source:\${DeliverySourceName} |
| [delivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_Delivery.html) | arn:\${Partition}:logs:\${Region}:\${Account}:delivery:\${DeliveryName} |
| [delivery-destination](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeliveryDestination.html) | arn:\${Partition}:logs:\${Region}:\${Account}:delivery-destination:\${DeliveryDestinationName} |
| [anomaly-detector](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_AnomalyDetector.html) | arn:\${Partition}:logs:\${Region}:\${Account}:anomaly-detector:\${DetectorId} |
# AWS CloudWatch RUM
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscloudwatchrum.html
| Service | ARN |
|---------|-----|
| [AppMonitorResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_AppMonitor.html) | arn:\${Partition}:rum:\${Region}:\${Account}:appmonitor/\${Name} |
# Amazon CodeCatalyst
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncodecatalyst.html
| Service | ARN |
|---------|-----|
| [connections](https://docs.aws.amazon.com/codecatalyst/latest/userguide/#) | arn:\${Partition}:codecatalyst:\${Region}:\${Account}:/connections/\${ConnectionId} |
| [identity-center-applications](https://docs.aws.amazon.com/codecatalyst/latest/userguide/#) | arn:\${Partition}:codecatalyst:\${Region}:\${Account}:/identity-center-applications/\${IdentityCenterApplicationId} |
| [space](https://docs.aws.amazon.com/codecatalyst/latest/userguide/#) | arn:\${Partition}:codecatalyst:::space/\${SpaceId} |
| [project](https://docs.aws.amazon.com/codecatalyst/latest/userguide/#) | arn:\${Partition}:codecatalyst:::space/\${SpaceId}/project/\${ProjectId} |
# Amazon CloudWatch Synthetics
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudwatchsynthetics.html
| Service | ARN |
|---------|-----|
| [canary](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) | arn:\${Partition}:synthetics:\${Region}:\${Account}:canary:\${CanaryName} |
| [group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Groups.html) | arn:\${Partition}:synthetics:\${Region}:\${Account}:group:\${GroupId} |
# AWS CodeCommit
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscodecommit.html
| Service | ARN |
|---------|-----|
| [repository](https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control.html#arn-formats) | arn:\${Partition}:codecommit:\${Region}:\${Account}:\${RepositoryName} |
# AWS CodeDeploy secure host commands service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscodedeploysecurehostcommandsservice.html
| Service | ARN |
|---------|-----|
# AWS CodeConnections
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscodeconnections.html
| Service | ARN |
|---------|-----|
| [Connection](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections.html) | arn:\${Partition}:codeconnections:\${Region}:\${Account}:connection/\${ConnectionId} |
| [Host](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-hosts.html) | arn:\${Partition}:codeconnections:\${Region}:\${Account}:host/\${HostId} |
| [RepositoryLink](https://docs.aws.amazon.com/dtconsole/latest/userguide/repositorylinks.html) | arn:\${Partition}:codeconnections:\${Region}:\${Account}:repository-link/\${RepositoryLinkId} |
# AWS CodeArtifact
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscodeartifact.html
| Service | ARN |
|---------|-----|
| [domain](https://docs.aws.amazon.com/codeartifact/latest/ug/domains.html) | arn:\${Partition}:codeartifact:\${Region}:\${Account}:domain/\${DomainName} |
| [repository](https://docs.aws.amazon.com/codeartifact/latest/ug/repos.html) | arn:\${Partition}:codeartifact:\${Region}:\${Account}:repository/\${DomainName}/\${RepositoryName} |
| [package-group](https://docs.aws.amazon.com/codeartifact/latest/ug/package-groups.html) | arn:\${Partition}:codeartifact:\${Region}:\${Account}:package-group/\${DomainName}\${EncodedPackageGroupPattern} |
| [package](https://docs.aws.amazon.com/codeartifact/latest/ug/packages.html) | arn:\${Partition}:codeartifact:\${Region}:\${Account}:package/\${DomainName}/\${RepositoryName}/\${PackageFormat}/\${PackageNamespace}/\${PackageName} |
# Amazon CodeGuru Profiler
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncodeguruprofiler.html
| Service | ARN |
|---------|-----|
| [ProfilingGroup](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-profiling-groups.html) | arn:\${Partition}:codeguru-profiler:\${Region}:\${Account}:profilingGroup/\${ProfilingGroupName} |
# Amazon CodeGuru Reviewer
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncodegurureviewer.html
| Service | ARN |
|---------|-----|
| [association](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/working-with-repositories.html) | arn:\${Partition}:codeguru-reviewer:\${Region}:\${Account}:association:\${ResourceId} |
| [codereview](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/code-reviews.html) | arn:\${Partition}:codeguru-reviewer:\${Region}:\${Account}:association:\${ResourceId}:codereview:\${CodeReviewId} |
# Amazon CodeGuru
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncodeguru.html
| Service | ARN |
|---------|-----|
# AWS CodeBuild
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscodebuild.html
| Service | ARN |
|---------|-----|
| [build](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats) | arn:\${Partition}:codebuild:\${Region}:\${Account}:build/\${BuildId} |
| [build-batch](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats) | arn:\${Partition}:codebuild:\${Region}:\${Account}:build-batch/\${BuildBatchId} |
| [project](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats) | arn:\${Partition}:codebuild:\${Region}:\${Account}:project/\${ProjectName} |
| [report-group](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats) | arn:\${Partition}:codebuild:\${Region}:\${Account}:report-group/\${ReportGroupName} |
| [report](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats) | arn:\${Partition}:codebuild:\${Region}:\${Account}:report/\${ReportGroupName}:\${ReportId} |
| [fleet](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats) | arn:\${Partition}:codebuild:\${Region}:\${Account}:fleet/\${FleetName}:\${FleetId} |
# AWS CodePipeline
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscodepipeline.html
| Service | ARN |
|---------|-----|
| [action](https://docs.aws.amazon.com/codepipeline/latest/userguide/iam-access-control-identity-based.html#ACP_ARN_Format) | arn:\${Partition}:codepipeline:\${Region}:\${Account}:\${PipelineName}/\${StageName}/\${ActionName} |
| [actiontype](https://docs.aws.amazon.com/codepipeline/latest/userguide/iam-access-control-identity-based.html#ACP_ARN_Format) | arn:\${Partition}:codepipeline:\${Region}:\${Account}:actiontype:\${Owner}/\${Category}/\${Provider}/\${Version} |
| [pipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/iam-access-control-identity-based.html#ACP_ARN_Format) | arn:\${Partition}:codepipeline:\${Region}:\${Account}:\${PipelineName} |
| [stage](https://docs.aws.amazon.com/codepipeline/latest/userguide/iam-access-control-identity-based.html#ACP_ARN_Format) | arn:\${Partition}:codepipeline:\${Region}:\${Account}:\${PipelineName}/\${StageName} |
| [webhook](https://docs.aws.amazon.com/codepipeline/latest/userguide/iam-access-control-identity-based.html#ACP_ARN_Format) | arn:\${Partition}:codepipeline:\${Region}:\${Account}:webhook:\${WebhookName} |
# Amazon CodeGuru Security
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncodegurusecurity.html
| Service | ARN |
|---------|-----|
| [ScanName](https://docs.aws.amazon.com/codeguru/latest/security-ug/working-with-code-scans.html) | arn:\${Partition}:codeguru-security:\${Region}:\${Account}:scans/\${ScanName} |
# AWS CodeStar Connections
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscodestarconnections.html
| Service | ARN |
|---------|-----|
| [Connection](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections.html) | arn:\${Partition}:codestar-connections:\${Region}:\${Account}:connection/\${ConnectionId} |
| [Host](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-hosts.html) | arn:\${Partition}:codestar-connections:\${Region}:\${Account}:host/\${HostId} |
| [RepositoryLink](https://docs.aws.amazon.com/dtconsole/latest/userguide/repositorylinks.html) | arn:\${Partition}:codestar-connections:\${Region}:\${Account}:repository-link/\${RepositoryLinkId} |
# AWS CodeDeploy
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscodedeploy.html
| Service | ARN |
|---------|-----|
| [application](https://docs.aws.amazon.com/codedeploy/latest/userguide/auth-and-access-control-permissions-reference.html) | arn:\${Partition}:codedeploy:\${Region}:\${Account}:application:\${ApplicationName} |
| [deploymentconfig](https://docs.aws.amazon.com/codedeploy/latest/userguide/auth-and-access-control-permissions-reference.html) | arn:\${Partition}:codedeploy:\${Region}:\${Account}:deploymentconfig:\${DeploymentConfigurationName} |
| [deploymentgroup](https://docs.aws.amazon.com/codedeploy/latest/userguide/auth-and-access-control-permissions-reference.html) | arn:\${Partition}:codedeploy:\${Region}:\${Account}:deploymentgroup:\${ApplicationName}/\${DeploymentGroupName} |
| [instance](https://docs.aws.amazon.com/codedeploy/latest/userguide/auth-and-access-control-permissions-reference.html) | arn:\${Partition}:codedeploy:\${Region}:\${Account}:instance:\${InstanceName} |
# Amazon Cognito Identity
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncognitoidentity.html
| Service | ARN |
|---------|-----|
| [identitypool](https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html) | arn:\${Partition}:cognito-identity:\${Region}:\${Account}:identitypool/\${IdentityPoolId} |
# AWS CodeStar
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscodestar.html
| Service | ARN |
|---------|-----|
| [project](https://docs.aws.amazon.com/codestar/latest/userguide/working-with-projects.html) | arn:\${Partition}:codestar:\${Region}:\${Account}:project/\${ProjectId} |
| [user](https://docs.aws.amazon.com/codestar/latest/userguide/working-with-user-info.html) | arn:\${Partition}:iam::\${Account}:user/\${AwsUserName} |
# Amazon CodeWhisperer
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncodewhisperer.html
| Service | ARN |
|---------|-----|
| [profile](https://docs.aws.amazon.com/codewhisperer/latest/userguide/as-whisper-admin.html#about-profiles) | arn:\${Partition}:codewhisperer::\${Account}:profile/\${Identifier} |
| [customization](https://docs.aws.amazon.com/codewhisperer/latest/userguide/as-whisper-admin.html#about-customizations) | arn:\${Partition}:codewhisperer::\${Account}:customization/\${Identifier} |
# AWS CodeStar Notifications
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscodestarnotifications.html
| Service | ARN |
|---------|-----|
| [notificationrule](https://docs.aws.amazon.com/codestar-notifications/latest/userguide/security_iam_service-with-iam.html) | arn:\${Partition}:codestar-notifications:\${Region}:\${Account}:notificationrule/\${NotificationRuleId} |
# Amazon Cognito Sync
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncognitosync.html
| Service | ARN |
|---------|-----|
| [dataset](https://docs.aws.amazon.com/cognito/latest/developerguide/synchronizing-data.html#understanding-datasets) | arn:\${Partition}:cognito-sync:\${Region}:\${Account}:identitypool/\${IdentityPoolId}/identity/\${IdentityId}/dataset/\${DatasetName} |
| [identity](https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html#authenticated-and-unauthenticated-identities) | arn:\${Partition}:cognito-sync:\${Region}:\${Account}:identitypool/\${IdentityPoolId}/identity/\${IdentityId} |
| [identitypool](https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html) | arn:\${Partition}:cognito-sync:\${Region}:\${Account}:identitypool/\${IdentityPoolId} |
# AWS Compute Optimizer
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscomputeoptimizer.html
| Service | ARN |
|---------|-----|
# AWS Consolidated Billing
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsconsolidatedbilling.html
| Service | ARN |
|---------|-----|
# Amazon Comprehend Medical
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncomprehendmedical.html
| Service | ARN |
|---------|-----|
# Amazon Connect Customer Profiles
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonconnectcustomerprofiles.html
| Service | ARN |
|---------|-----|
| [domains](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/) | arn:\${Partition}:profile:\${Region}:\${Account}:domains/\${DomainName} |
| [object-types](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/) | arn:\${Partition}:profile:\${Region}:\${Account}:domains/\${DomainName}/object-types/\${ObjectTypeName} |
| [integrations](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/) | arn:\${Partition}:profile:\${Region}:\${Account}:domains/\${DomainName}/integrations/\${Uri} |
| [event-streams](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/) | arn:\${Partition}:profile:\${Region}:\${Account}:domains/\${DomainName}/event-streams/\${EventStreamName} |
| [calculated-attributes](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/) | arn:\${Partition}:profile:\${Region}:\${Account}:domains/\${DomainName}/calculated-attributes/\${CalculatedAttributeName} |
# AWS Connector Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsconnectorservice.html
| Service | ARN |
|---------|-----|
# AWS Control Catalog
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscontrolcatalog.html
| Service | ARN |
|---------|-----|
| [common-control](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_CommonControlSummary.html) | arn:\${Partition}:controlcatalog:::common-control/\${CommonControlId} |
| [domain](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_DomainSummary.html) | arn:\${Partition}:controlcatalog:::domain/\${DomainId} |
| [objective](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ObjectiveSummary.html) | arn:\${Partition}:controlcatalog:::objective/\${ObjectiveId} |
# Amazon Connect Voice ID
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonconnectvoiceid.html
| Service | ARN |
|---------|-----|
| [domain](https://docs.aws.amazon.com/connect/latest/adminguide/enable-voiceid.html#voiceid-domain) | arn:\${Partition}:voiceid:\${Region}:\${Account}:domain/\${DomainId} |
# Amazon Comprehend
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncomprehend.html
| Service | ARN |
|---------|-----|
| [targeted-sentiment-detection-job](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartTargetedSentimentDetectionJob.html) | arn:\${Partition}:comprehend:\${Region}:\${Account}:targeted-sentiment-detection-job/\${JobId} |
| [document-classifier](https://docs.aws.amazon.com/comprehend/latest/dg/how-document-classification-training.html) | arn:\${Partition}:comprehend:\${Region}:\${Account}:document-classifier/\${DocumentClassifierName} |
| [document-classifier-endpoint](https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html) | arn:\${Partition}:comprehend:\${Region}:\${Account}:document-classifier-endpoint/\${DocumentClassifierEndpointName} |
| [entity-recognizer](https://docs.aws.amazon.com/comprehend/latest/dg/training-recognizers.html) | arn:\${Partition}:comprehend:\${Region}:\${Account}:entity-recognizer/\${EntityRecognizerName} |
| [entity-recognizer-endpoint](https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html) | arn:\${Partition}:comprehend:\${Region}:\${Account}:entity-recognizer-endpoint/\${EntityRecognizerEndpointName} |
| [dominant-language-detection-job](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartDominantLanguageDetectionJob.html) | arn:\${Partition}:comprehend:\${Region}:\${Account}:dominant-language-detection-job/\${JobId} |
| [entities-detection-job](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartEntitiesDetectionJob.html) | arn:\${Partition}:comprehend:\${Region}:\${Account}:entities-detection-job/\${JobId} |
| [pii-entities-detection-job](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartPiiEntitiesDetectionJob.html) | arn:\${Partition}:comprehend:\${Region}:\${Account}:pii-entities-detection-job/\${JobId} |
| [events-detection-job](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartEventsDetectionJob.html) | arn:\${Partition}:comprehend:\${Region}:\${Account}:events-detection-job/\${JobId} |
| [key-phrases-detection-job](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartKeyPhrasesDetectionJob.html) | arn:\${Partition}:comprehend:\${Region}:\${Account}:key-phrases-detection-job/\${JobId} |
| [sentiment-detection-job](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartSentimentDetectionJob.html) | arn:\${Partition}:comprehend:\${Region}:\${Account}:sentiment-detection-job/\${JobId} |
| [topics-detection-job](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartTopicsDetectionJob.html) | arn:\${Partition}:comprehend:\${Region}:\${Account}:topics-detection-job/\${JobId} |
| [document-classification-job](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartDocumentClassificationJob.html) | arn:\${Partition}:comprehend:\${Region}:\${Account}:document-classification-job/\${JobId} |
| [flywheel](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_CreateFlywheel.html) | arn:\${Partition}:comprehend:\${Region}:\${Account}:flywheel/\${FlywheelName} |
| [flywheel-dataset](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_CreateDataset.html) | arn:\${Partition}:comprehend:\${Region}:\${Account}:flywheel/\${FlywheelName}/dataset/\${DatasetName} |
# AWS Management Console Mobile App
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsconsolemobileapp.html
| Service | ARN |
|---------|-----|
| [DeviceIdentity](https://docs.aws.amazon.com/consolemobileapp/latest/userguide/permissions-policies.html) | arn:\${Partition}:consoleapp::\${Account}:device/\${DeviceId}/identity/\${IdentityId} |
# AWS Cost and Usage Report
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscostandusagereport.html
| Service | ARN |
|---------|-----|
| [cur](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) | arn:\${Partition}:cur:\${Region}:\${Account}:definition/\${ReportName} |
# Amazon Cognito User Pools
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncognitouserpools.html
| Service | ARN |
|---------|-----|
| [userpool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) | arn:\${Partition}:cognito-idp:\${Region}:\${Account}:userpool/\${UserPoolId} |
| [webacl](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-waf.html) | arn:\${Partition}:wafv2:\${Region}:\${Account}:\${Scope}/webacl/\${Name}/\${Id} |
# AWS Config
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsconfig.html
| Service | ARN |
|---------|-----|
| [AggregationAuthorization](https://docs.aws.amazon.com/config/latest/APIReference/API_AggregationAuthorization.html) | arn:\${Partition}:config:\${Region}:\${Account}:aggregation-authorization/\${AggregatorAccount}/\${AggregatorRegion} |
| [ConfigurationAggregator](https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigurationAggregator.html) | arn:\${Partition}:config:\${Region}:\${Account}:config-aggregator/\${AggregatorId} |
| [ConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigRule.html) | arn:\${Partition}:config:\${Region}:\${Account}:config-rule/\${ConfigRuleId} |
| [ConformancePack](https://docs.aws.amazon.com/config/latest/APIReference/API_ConformancePackDetail.html) | arn:\${Partition}:config:\${Region}:\${Account}:conformance-pack/\${ConformancePackName}/\${ConformancePackId} |
| [OrganizationConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_OrganizationConfigRule.html) | arn:\${Partition}:config:\${Region}:\${Account}:organization-config-rule/\${OrganizationConfigRuleId} |
| [OrganizationConformancePack](https://docs.aws.amazon.com/config/latest/APIReference/API_OrganizationConformancePack.html) | arn:\${Partition}:config:\${Region}:\${Account}:organization-conformance-pack/\${OrganizationConformancePackId} |
| [RemediationConfiguration](https://docs.aws.amazon.com/config/latest/APIReference/API_RemediationConfiguration.html) | arn:\${Partition}:config:\${Region}:\${Account}:remediation-configuration/\${RemediationConfigurationId} |
| [StoredQuery](https://docs.aws.amazon.com/config/latest/APIReference/API_StoredQuery.html) | arn:\${Partition}:config:\${Region}:\${Account}:stored-query/\${StoredQueryName}/\${StoredQueryId} |
# AWS Cost Explorer Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscostexplorerservice.html
| Service | ARN |
|---------|-----|
| [anomalysubscription](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalySubscription.html) | arn:\${Partition}:ce::\${Account}:anomalysubscription/\${Identifier} |
| [anomalymonitor](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalyMonitor.html) | arn:\${Partition}:ce::\${Account}:anomalymonitor/\${Identifier} |
| [costcategory](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategory.html) | arn:\${Partition}:ce::\${Account}:costcategory/\${Identifier} |
# AWS Control Tower
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscontroltower.html
| Service | ARN |
|---------|-----|
| [EnabledControl](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnableControl.html) | arn:\${Partition}:controltower:\${Region}:\${Account}:enabledcontrol/\${EnabledControlId} |
| [Baseline](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetBaseline.html) | arn:\${Partition}:controltower:\${Region}::baseline/\${BaselineId} |
| [EnabledBaseline](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnableBaseline.html) | arn:\${Partition}:controltower:\${Region}:\${Account}:enabledbaseline/\${EnabledBaselineId} |
| [LandingZone](https://docs.aws.amazon.com/controltower/latest/APIReference/API_CreateLandingZone.html) | arn:\${Partition}:controltower:\${Region}:\${Account}:landingzone/\${LandingZoneId} |
# Amazon Connect Cases
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonconnectcases.html
| Service | ARN |
|---------|-----|
| [Case](https://docs.aws.amazon.com/connect/latest/adminguide/cases.html) | arn:\${Partition}:cases:\${Region}:\${Account}:domain/\${DomainId}/case/\${CaseId} |
| [Domain](https://docs.aws.amazon.com/connect/latest/adminguide/cases.html) | arn:\${Partition}:cases:\${Region}:\${Account}:domain/\${DomainId} |
| [Field](https://docs.aws.amazon.com/connect/latest/adminguide/case-fields.html) | arn:\${Partition}:cases:\${Region}:\${Account}:domain/\${DomainId}/field/\${FieldId} |
| [Layout](https://docs.aws.amazon.com/connect/latest/adminguide/case-layouts.html) | arn:\${Partition}:cases:\${Region}:\${Account}:domain/\${DomainId}/layout/\${LayoutId} |
| [RelatedItem](https://docs.aws.amazon.com/connect/latest/adminguide/associatecontactandcase.html) | arn:\${Partition}:cases:\${Region}:\${Account}:domain/\${DomainId}/case/\${CaseId}/related-item/\${RelatedItemId} |
| [Template](https://docs.aws.amazon.com/connect/latest/adminguide/case-templates.html) | arn:\${Partition}:cases:\${Region}:\${Account}:domain/\${DomainId}/template/\${TemplateId} |
# AWS Customer Verification Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscustomerverificationservice.html
| Service | ARN |
|---------|-----|
# AWS Cost Optimization Hub
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscostoptimizationhub.html
| Service | ARN |
|---------|-----|
# Amazon Data Lifecycle Manager
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazondatalifecyclemanager.html
| Service | ARN |
|---------|-----|
| [policy](https://docs.aws.amazon.com/dlm/latest/APIReference/API_LifecyclePolicy.html) | arn:\${Partition}:dlm:\${Region}:\${Account}:policy/\${ResourceName} |
# AWS Data Exchange
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdataexchange.html
| Service | ARN |
|---------|-----|
| [jobs](https://docs.aws.amazon.com/data-exchange/latest/userguide/jobs.html) | arn:\${Partition}:dataexchange:\${Region}:\${Account}:jobs/\${JobId} |
| [data-sets](https://docs.aws.amazon.com/data-exchange/latest/userguide/data-sets.html) | arn:\${Partition}:dataexchange:\${Region}:\${Account}:data-sets/\${DataSetId} |
| [entitled-data-sets](https://docs.aws.amazon.com/data-exchange/latest/userguide/data-sets.html) | arn:\${Partition}:dataexchange:\${Region}::data-sets/\${DataSetId} |
| [revisions](https://docs.aws.amazon.com/data-exchange/latest/userguide/data-sets.html#revisions) | arn:\${Partition}:dataexchange:\${Region}:\${Account}:data-sets/\${DataSetId}/revisions/\${RevisionId} |
| [entitled-revisions](https://docs.aws.amazon.com/data-exchange/latest/userguide/data-sets.html#revisions) | arn:\${Partition}:dataexchange:\${Region}::data-sets/\${DataSetId}/revisions/\${RevisionId} |
| [assets](https://docs.aws.amazon.com/data-exchange/latest/userguide/data-sets.html#assets) | arn:\${Partition}:dataexchange:\${Region}:\${Account}:data-sets/\${DataSetId}/revisions/\${RevisionId}/assets/\${AssetId} |
| [entitled-assets](https://docs.aws.amazon.com/data-exchange/latest/userguide/data-sets.html#assets) | arn:\${Partition}:dataexchange:\${Region}::data-sets/\${DataSetId}/revisions/\${RevisionId}/assets/\${AssetId} |
| [event-actions](https://docs.aws.amazon.com/data-exchange/latest/userguide/data-sets.html) | arn:\${Partition}:dataexchange:\${Region}:\${Account}:event-actions/\${EventActionId} |
# AWS DeepComposer
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdeepcomposer.html
| Service | ARN |
|---------|-----|
| [model](https://docs.aws.amazon.com/deepcomposer/latest/devguide/get-started-custom-model.html) | arn:\${Partition}:deepcomposer:\${Region}:\${Account}:model/\${ModelId} |
| [composition](https://docs.aws.amazon.com/deepcomposer/latest/devguide/get-started-learn-from-pre-trained-models.html) | arn:\${Partition}:deepcomposer:\${Region}:\${Account}:composition/\${CompositionId} |
| [audio](https://docs.aws.amazon.com/deepcomposer/latest/devguide/get-started-learn-from-pre-trained-models.html) | arn:\${Partition}:deepcomposer:\${Region}:\${Account}:audio/\${AudioId} |
# AWS Data Pipeline
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatapipeline.html
| Service | ARN |
|---------|-----|
| [pipeline](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatapipeline.html) | arn:\${Partition}:datapipeline:\${Region}:\${Account}:pipeline/\${PipelineId} |
# Database Query Metadata Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_databasequerymetadataservice.html
| Service | ARN |
|---------|-----|
# AWS DeepLens
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdeeplens.html
| Service | ARN |
|---------|-----|
| [device](device) | arn:\${Partition}:deeplens:\${Region}:\${Account}:device/\${DeviceName} |
| [project](project) | arn:\${Partition}:deeplens:\${Region}:\${Account}:project/\${ProjectName} |
| [model](model) | arn:\${Partition}:deeplens:\${Region}:\${Account}:model/\${ModelName} |
# AWS Diagnostic tools
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdiagnostictools.html
| Service | ARN |
|---------|-----|
| [execution](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_Execution.html) | arn:\${Partition}:ts::\${Account}:execution/\${UserId}/\${ToolId}/\${ExecutionId} |
| [tool](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_Tool.html) | arn:\${Partition}:ts::aws:tool/\${ToolId} |
# Amazon DevOps Guru
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazondevopsguru.html
| Service | ARN |
|---------|-----|
| [topic](https://docs.aws.amazon.com/devops-guru/latest/userguide/setting-up.html#setting-up-notifications) | arn:\${Partition}:sns:\${Region}:\${Account}:\${TopicName} |
# Amazon DataZone
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazondatazone.html
| Service | ARN |
|---------|-----|
| [domain](https://docs.aws.amazon.com/datazone/latest/userguide/create-domain.html) | arn:\${Partition}:datazone:\${Region}:\${Account}:domain/\${DomainId} |
# Amazon Detective
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazondetective.html
| Service | ARN |
|---------|-----|
| [Graph](https://docs.aws.amazon.com/detective/latest/adminguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources) | arn:\${Partition}:detective:\${Region}:\${Account}:graph:\${ResourceId} |
# AWS DataSync
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatasync.html
| Service | ARN |
|---------|-----|
| [agent](https://docs.aws.amazon.com/datasync/latest/userguide/working-with-agents.html) | arn:\${Partition}:datasync:\${Region}:\${AccountId}:agent/\${AgentId} |
| [location](https://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html) | arn:\${Partition}:datasync:\${Region}:\${AccountId}:location/\${LocationId} |
| [task](https://docs.aws.amazon.com/datasync/latest/userguide/working-with-tasks.html) | arn:\${Partition}:datasync:\${Region}:\${AccountId}:task/\${TaskId} |
| [taskexecution](https://docs.aws.amazon.com/datasync/latest/userguide/working-with-task-executions.html) | arn:\${Partition}:datasync:\${Region}:\${AccountId}:task/\${TaskId}/execution/\${ExecutionId} |
| [storagesystem](https://docs.aws.amazon.com/datasync/latest/userguide/discovery-configure-storage.html) | arn:\${Partition}:datasync:\${Region}:\${AccountId}:system/\${StorageSystemId} |
| [discoveryjob](https://docs.aws.amazon.com/datasync/latest/userguide/discovery-job-create.html) | arn:\${Partition}:datasync:\${Region}:\${AccountId}:system/\${StorageSystemId}/job/\${DiscoveryJobId} |
# AWS Device Farm
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdevicefarm.html
| Service | ARN |
|---------|-----|
| [project](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Project.html) | arn:\${Partition}:devicefarm:\${Region}:\${Account}:project:\${ResourceId} |
| [run](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Run.html) | arn:\${Partition}:devicefarm:\${Region}:\${Account}:run:\${ResourceId} |
| [job](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Job.html) | arn:\${Partition}:devicefarm:\${Region}:\${Account}:job:\${ResourceId} |
| [suite](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Suite.html) | arn:\${Partition}:devicefarm:\${Region}:\${Account}:suite:\${ResourceId} |
| [test](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Test.html) | arn:\${Partition}:devicefarm:\${Region}:\${Account}:test:\${ResourceId} |
| [upload](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Upload.html) | arn:\${Partition}:devicefarm:\${Region}:\${Account}:upload:\${ResourceId} |
| [artifact](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Artifact.html) | arn:\${Partition}:devicefarm:\${Region}:\${Account}:artifact:\${ResourceId} |
| [sample](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Sample.html) | arn:\${Partition}:devicefarm:\${Region}:\${Account}:sample:\${ResourceId} |
| [networkprofile](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_NetworkProfile.html) | arn:\${Partition}:devicefarm:\${Region}:\${Account}:networkprofile:\${ResourceId} |
| [deviceinstance](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_DeviceInstance.html) | arn:\${Partition}:devicefarm:\${Region}::deviceinstance:\${ResourceId} |
| [session](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_RemoteAccessSession.html) | arn:\${Partition}:devicefarm:\${Region}:\${Account}:session:\${ResourceId} |
| [devicepool](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_DevicePool.html) | arn:\${Partition}:devicefarm:\${Region}:\${Account}:devicepool:\${ResourceId} |
| [device](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Device.html) | arn:\${Partition}:devicefarm:\${Region}::device:\${ResourceId} |
| [instanceprofile](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_InstanceProfile.html) | arn:\${Partition}:devicefarm:\${Region}:\${Account}:instanceprofile:\${ResourceId} |
| [vpceconfiguration](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_VPCEConfiguration.html) | arn:\${Partition}:devicefarm:\${Region}:\${Account}:vpceconfiguration:\${ResourceId} |
| [testgrid-project](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_TestGridProject.html) | arn:\${Partition}:devicefarm:\${Region}:\${Account}:testgrid-project:\${ResourceId} |
| [testgrid-session](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_TestGridSession.html) | arn:\${Partition}:devicefarm:\${Region}:\${Account}:testgrid-session:\${ResourceId} |
# AWS DeepRacer
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdeepracer.html
| Service | ARN |
|---------|-----|
| [car](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-choose-race-type.html) | arn:\${Partition}:deepracer:\${Region}:\${Account}:car/\${ResourceId} |
| [evaluation_job](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-get-started-test-in-simulator.html) | arn:\${Partition}:deepracer:\${Region}:\${Account}:evaluation_job/\${ResourceId} |
| [leaderboard](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-submit-model-to-leaderboard.html) | arn:\${Partition}:deepracer:\${Region}::leaderboard/\${ResourceId} |
| [leaderboard_evaluation_job](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-submit-model-to-leaderboard.html) | arn:\${Partition}:deepracer:\${Region}:\${Account}:leaderboard_evaluation_job/\${ResourceId} |
| [reinforcement_learning_model](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-get-started-training-model.html) | arn:\${Partition}:deepracer:\${Region}:\${Account}:model/reinforcement_learning/\${ResourceId} |
| [track](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-console-train-evaluate-models.html) | arn:\${Partition}:deepracer:\${Region}::track/\${ResourceId} |
| [training_job](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-get-started-training-model.html) | arn:\${Partition}:deepracer:\${Region}:\${Account}:training_job/\${ResourceId} |
# AWS Deadline Cloud
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdeadlinecloud.html
| Service | ARN |
|---------|-----|
| [budget](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_Budget.html) | arn:\${Partition}:deadline:\${Region}:\${Account}:farm/\${FarmId}/budget/\${BudgetId} |
| [farm](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_Farm.html) | arn:\${Partition}:deadline:\${Region}:\${Account}:farm/\${FarmId} |
| [fleet](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_Fleet.html) | arn:\${Partition}:deadline:\${Region}:\${Account}:farm/\${FarmId}/fleet/\${FleetId} |
| [job](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_Job.html) | arn:\${Partition}:deadline:\${Region}:\${Account}:farm/\${FarmId}/queue/\${QueueId}/job/\${JobId} |
| [license-endpoint](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_LicenseEndpoint.html) | arn:\${Partition}:deadline:\${Region}:\${Account}:license-endpoint/\${LicenseEndpointId} |
| [metered-product](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_MeteredProduct.html) | arn:\${Partition}:deadline:\${Region}:\${Account}:license-endpoint/\${LicenseEndpointId}/metered-product/\${ProductId} |
| [monitor](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_Monitor.html) | arn:\${Partition}:deadline:\${Region}:\${Account}:monitor/\${MonitorId} |
| [queue](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_Queue.html) | arn:\${Partition}:deadline:\${Region}:\${Account}:farm/\${FarmId}/queue/\${QueueId} |
| [worker](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_Worker.html) | arn:\${Partition}:deadline:\${Region}:\${Account}:farm/\${FarmId}/fleet/\${FleetId}/worker/\${WorkerId} |
# AWS Database Migration Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html
| Service | ARN |
|---------|-----|
| [Certificate](https://docs.aws.amazon.com/dms/latest/APIReference/API_Certificate.html) | arn:\${Partition}:dms:\${Region}:\${Account}:cert:* |
| [DataProvider](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html) | arn:\${Partition}:dms:\${Region}:\${Account}:data-provider:* |
| [DataMigration](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html) | arn:\${Partition}:dms:\${Region}:\${Account}:data-migration:* |
| [Endpoint](https://docs.aws.amazon.com/dms/latest/APIReference/API_Endpoint.html) | arn:\${Partition}:dms:\${Region}:\${Account}:endpoint:* |
| [EventSubscription](https://docs.aws.amazon.com/dms/latest/APIReference/API_EventSubscription.html) | arn:\${Partition}:dms:\${Region}:\${Account}:es:* |
| [InstanceProfile](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html) | arn:\${Partition}:dms:\${Region}:\${Account}:instance-profile:* |
| [MigrationProject](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html) | arn:\${Partition}:dms:\${Region}:\${Account}:migration-project:* |
| [ReplicationConfig](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html) | arn:\${Partition}:dms:\${Region}:\${Account}:replication-config:* |
| [ReplicationInstance](https://docs.aws.amazon.com/dms/latest/APIReference/API_ReplicationInstance.html) | arn:\${Partition}:dms:\${Region}:\${Account}:rep:* |
| [ReplicationSubnetGroup](https://docs.aws.amazon.com/dms/latest/APIReference/API_ReplicationSubnetGroup.html) | arn:\${Partition}:dms:\${Region}:\${Account}:subgrp:* |
| [ReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_ReplicationTask.html) | arn:\${Partition}:dms:\${Region}:\${Account}:task:* |
| [ReplicationTaskAssessmentRun](https://docs.aws.amazon.com/dms/latest/APIReference/API_ReplicationTaskAssessmentRun.html) | arn:\${Partition}:dms:\${Region}:\${Account}:assessment-run:* |
| [ReplicationTaskIndividualAssessment](https://docs.aws.amazon.com/dms/latest/APIReference/API_ReplicationTaskIndividualAssessment.html) | arn:\${Partition}:dms:\${Region}:\${Account}:individual-assessment:* |
# Amazon Connect
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonconnect.html
| Service | ARN |
|---------|-----|
| [instance](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-instances.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId} |
| [contact](https://docs.aws.amazon.com/connect/latest/adminguide/connect-contact-attributes.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/contact/\${ContactId} |
| [user](https://docs.aws.amazon.com/connect/latest/adminguide/connect-agents.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/agent/\${UserId} |
| [routing-profile](https://docs.aws.amazon.com/connect/latest/adminguide/routing-profiles.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/routing-profile/\${RoutingProfileId} |
| [security-profile](https://docs.aws.amazon.com/connect/latest/adminguide/connect-security-profiles.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/security-profile/\${SecurityProfileId} |
| [hierarchy-group](https://docs.aws.amazon.com/connect/latest/adminguide/agent-hierarchy.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/agent-group/\${HierarchyGroupId} |
| [queue](https://docs.aws.amazon.com/connect/latest/adminguide/create-queue.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/queue/\${QueueId} |
| [wildcard-queue](https://docs.aws.amazon.com/connect/latest/adminguide/create-queue.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/queue/* |
| [quick-connect](https://docs.aws.amazon.com/connect/latest/adminguide/quick-connects.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/transfer-destination/\${QuickConnectId} |
| [wildcard-quick-connect](https://docs.aws.amazon.com/connect/latest/adminguide/quick-connects.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/transfer-destination/* |
| [contact-flow](https://docs.aws.amazon.com/connect/latest/adminguide/connect-contact-flows.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/contact-flow/\${ContactFlowId} |
| [task-template](https://docs.aws.amazon.com/connect/latest/adminguide/task-templates.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/task-template/\${TaskTemplateId} |
| [contact-flow-module](https://docs.aws.amazon.com/connect/latest/adminguide/contact-flow-modules.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/flow-module/\${ContactFlowModuleId} |
| [wildcard-contact-flow](https://docs.aws.amazon.com/connect/latest/adminguide/connect-contact-flows.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/contact-flow/* |
| [hours-of-operation](https://docs.aws.amazon.com/connect/latest/adminguide/set-hours-operation.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/operating-hours/\${HoursOfOperationId} |
| [agent-status](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-agent-status.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/agent-state/\${AgentStatusId} |
| [wildcard-agent-status](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-agent-status.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/agent-state/* |
| [legacy-phone-number](https://docs.aws.amazon.com/connect/latest/adminguide/ag-overview-numbers.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/phone-number/\${PhoneNumberId} |
| [wildcard-legacy-phone-number](https://docs.aws.amazon.com/connect/latest/adminguide/ag-overview-numbers.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/phone-number/* |
| [phone-number](https://docs.aws.amazon.com/connect/latest/adminguide/ag-overview-numbers.html) | arn:\${Partition}:connect:\${Region}:\${Account}:phone-number/\${PhoneNumberId} |
| [wildcard-phone-number](https://docs.aws.amazon.com/connect/latest/adminguide/ag-overview-numbers.html) | arn:\${Partition}:connect:\${Region}:\${Account}:phone-number/* |
| [integration-association](https://docs.aws.amazon.com/connect/latest/adminguide/connect-rules.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/integration-association/\${IntegrationAssociationId} |
| [use-case](https://docs.aws.amazon.com/connect/latest/adminguide/add-rules-task-creation.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/use-case/\${UseCaseId} |
| [vocabulary](https://docs.aws.amazon.com/connect/latest/adminguide/add-custom-vocabulary.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/vocabulary/\${VocabularyId} |
| [traffic-distribution-group](https://docs.aws.amazon.com/connect/latest/adminguide/setup-traffic-distribution-groups.html) | arn:\${Partition}:connect:\${Region}:\${Account}:traffic-distribution-group/\${TrafficDistributionGroupId} |
| [rule](https://docs.aws.amazon.com/connect/latest/adminguide/connect-rules.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/rule/\${RuleId} |
| [evaluation-form](https://docs.aws.amazon.com/connect/latest/adminguide/create-evaluation-forms.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/evaluation-form/\${FormId} |
| [contact-evaluation](https://docs.aws.amazon.com/connect/latest/adminguide/evaluations.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/contact-evaluation/\${EvaluationId} |
| [prompt](https://docs.aws.amazon.com/connect/latest/adminguide/prompts.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/prompt/\${PromptId} |
| [customer-managed-view](https://docs.aws.amazon.com/connect/latest/adminguide/view-resources-sg.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/view/\${ViewId} |
| [aws-managed-view](https://docs.aws.amazon.com/connect/latest/adminguide/view-resources-sg.html) | arn:\${Partition}:connect:\${Region}:aws:view/\${ViewId} |
| [qualified-customer-managed-view](https://docs.aws.amazon.com/connect/latest/adminguide/view-resources-sg.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/view/\${ViewId}:\${ViewQualifier} |
| [qualified-aws-managed-view](https://docs.aws.amazon.com/connect/latest/adminguide/view-resources-sg.html) | arn:\${Partition}:connect:\${Region}:aws:view/\${ViewId}:\${ViewQualifier} |
| [customer-managed-view-version](https://docs.aws.amazon.com/connect/latest/adminguide/view-resources-sg.html) | arn:\${Partition}:connect:\${Region}:\${Account}:instance/\${InstanceId}/view/\${ViewId}:\${ViewVersion} |
# Amazon DynamoDB Accelerator (DAX)
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazondynamodbacceleratordax.html
| Service | ARN |
|---------|-----|
| [application](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.access-control.html) | arn:\${Partition}:dax:\${Region}:\${Account}:cache/\${ClusterName} |
# AWS Directory Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdirectoryservice.html
| Service | ARN |
|---------|-----|
| [directory](https://docs.aws.amazon.com/directoryservice/latest/devguide/welcome.html) | arn:\${Partition}:ds:\${Region}:\${Account}:directory/\${DirectoryId} |
# Amazon DocumentDB Elastic Clusters
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazondocumentdbelasticclusters.html
| Service | ARN |
|---------|-----|
| [cluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/elastic-managing.html) | arn:\${Partition}:docdb-elastic:\${Region}:\${Account}:cluster/\${ResourceId} |
| [cluster-snapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/elastic-managing.html#elastic-manage-snapshots) | arn:\${Partition}:docdb-elastic:\${Region}:\${Account}:cluster-snapshot/\${ResourceId} |
# AWS Direct Connect
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdirectconnect.html
| Service | ARN |
|---------|-----|
| [dxcon](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_Connection.html) | arn:\${Partition}:directconnect:\${Region}:\${Account}:dxcon/\${ConnectionId} |
| [dxlag](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_Lag.html) | arn:\${Partition}:directconnect:\${Region}:\${Account}:dxlag/\${LagId} |
| [dxvif](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_VirtualInterface.html) | arn:\${Partition}:directconnect:\${Region}:\${Account}:dxvif/\${VirtualInterfaceId} |
| [dx-gateway](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DirectConnectGateway.html) | arn:\${Partition}:directconnect::\${Account}:dx-gateway/\${DirectConnectGatewayId} |
# Amazon DynamoDB
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazondynamodb.html
| Service | ARN |
|---------|-----|
| [index](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.PrimaryKey) | arn:\${Partition}:dynamodb:\${Region}:\${Account}:table/\${TableName}/index/\${IndexName} |
| [stream](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.Streams) | arn:\${Partition}:dynamodb:\${Region}:\${Account}:table/\${TableName}/stream/\${StreamLabel} |
| [table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.TablesItemsAttributes) | arn:\${Partition}:dynamodb:\${Region}:\${Account}:table/\${TableName} |
| [backup](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/backuprestore_HowItWorks.html) | arn:\${Partition}:dynamodb:\${Region}:\${Account}:table/\${TableName}/backup/\${BackupName} |
| [export](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/S3DataExport.HowItWorks.html) | arn:\${Partition}:dynamodb:\${Region}:\${Account}:table/\${TableName}/export/\${ExportName} |
| [global-table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_HowItWorks.html) | arn:\${Partition}:dynamodb::\${Account}:global-table/\${GlobalTableName} |
| [import](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/S3DataImport.HowItWorks.html) | arn:\${Partition}:dynamodb:\${Region}:\${Account}:table/\${TableName}/import/\${ImportName} |
# Amazon EKS Auth
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoneksauth.html
| Service | ARN |
|---------|-----|
| [cluster](https://docs.aws.amazon.com/eks/latest/userguide/clusters.html) | arn:\${Partition}:eks:\${Region}:\${Account}:cluster/\${ClusterName} |
# Amazon EC2 Auto Scaling
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2autoscaling.html
| Service | ARN |
|---------|-----|
| [autoScalingGroup](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-resources) | arn:\${Partition}:autoscaling:\${Region}:\${Account}:autoScalingGroup:\${GroupId}:autoScalingGroupName/\${GroupFriendlyName} |
| [launchConfiguration](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-resources) | arn:\${Partition}:autoscaling:\${Region}:\${Account}:launchConfiguration:\${Id}:launchConfigurationName/\${LaunchConfigurationName} |
# Amazon EC2 Instance Connect
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2instanceconnect.html
| Service | ARN |
|---------|-----|
| [instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format) | arn:\${Partition}:ec2:\${Region}:\${Account}:instance/\${InstanceId} |
| [instance-connect-endpoint](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/permissions-for-ec2-instance-connect-endpoint.html#iam-CreateInstanceConnectEndpoint) | arn:\${Partition}:ec2:\${Region}:\${Account}:instance-connect-endpoint/\${InstanceConnectEndpointId} |
# Amazon Elastic Block Store
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelasticblockstore.html
| Service | ARN |
|---------|-----|
| [snapshot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html) | arn:\${Partition}:ec2:\${Region}::snapshot/\${SnapshotId} |
# Amazon EC2 Image Builder
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2imagebuilder.html
| Service | ARN |
|---------|-----|
| [component](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_Component.html) | arn:\${Partition}:imagebuilder:\${Region}:\${Account}:component/\${ComponentName}/\${ComponentVersion}/\${ComponentBuildVersion} |
| [componentVersion](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ComponentVersion.html) | arn:\${Partition}:imagebuilder:\${Region}:\${Account}:component/\${ComponentName}/\${ComponentVersion} |
| [distributionConfiguration](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_DistributionConfiguration.html) | arn:\${Partition}:imagebuilder:\${Region}:\${Account}:distribution-configuration/\${DistributionConfigurationName} |
| [image](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_Image.html) | arn:\${Partition}:imagebuilder:\${Region}:\${Account}:image/\${ImageName}/\${ImageVersion}/\${ImageBuildVersion} |
| [imageVersion](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImageVersion.html) | arn:\${Partition}:imagebuilder:\${Region}:\${Account}:image/\${ImageName}/\${ImageVersion} |
| [imageRecipe](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImageRecipe.html) | arn:\${Partition}:imagebuilder:\${Region}:\${Account}:image-recipe/\${ImageRecipeName}/\${ImageRecipeVersion} |
| [containerRecipe](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ContainerRecipe.html) | arn:\${Partition}:imagebuilder:\${Region}:\${Account}:container-recipe/\${ContainerRecipeName}/\${ContainerRecipeVersion} |
| [imagePipeline](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImagePipeline.html) | arn:\${Partition}:imagebuilder:\${Region}:\${Account}:image-pipeline/\${ImagePipelineName} |
| [infrastructureConfiguration](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_InfrastructureConfiguration.html) | arn:\${Partition}:imagebuilder:\${Region}:\${Account}:infrastructure-configuration/\${ResourceId} |
| [kmsKey](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys) | arn:\${Partition}:kms:\${Region}:\${Account}:key/\${KeyId} |
| [lifecycleExecution](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_LifecycleExecution.html) | arn:\${Partition}:imagebuilder:\${Region}:\${Account}:lifecycle-execution/\${LifecycleExecutionId} |
| [lifecyclePolicy](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_LifecyclePolicy.html) | arn:\${Partition}:imagebuilder:\${Region}:\${Account}:lifecycle-policy/\${LifecyclePolicyName} |
| [workflow](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_Workflow.html) | arn:\${Partition}:imagebuilder:\${Region}:\${Account}:workflow/\${WorkflowType}/\${WorkflowName}/\${WorkflowVersion}/\${WorkflowBuildVersion} |
| [workflowVersion](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_WorkflowVersion.html) | arn:\${Partition}:imagebuilder:\${Region}:\${Account}:workflow/\${WorkflowType}/\${WorkflowName}/\${WorkflowVersion} |
| [workflowExecution](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_WorkflowExecutionMetadata.html) | arn:\${Partition}:imagebuilder:\${Region}:\${Account}:workflow-execution/\${WorkflowExecutionId} |
| [workflowStepExecution](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_WorkflowStepMetadata.html) | arn:\${Partition}:imagebuilder:\${Region}:\${Account}:workflow-step-execution/\${WorkflowStepExecutionId} |
# Amazon Elastic Container Registry Public
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelasticcontainerregistrypublic.html
| Service | ARN |
|---------|-----|
| [repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/iam-policy-structure.html#ECR-Public_ARN_Format) | arn:\${Partition}:ecr-public::\${Account}:repository/\${RepositoryName} |
| [registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/iam-policy-structure.html#ECR-Public_ARN_Format) | arn:\${Partition}:ecr-public::\${Account}:registry/\${RegistryId} |
# Amazon Elastic Container Registry
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelasticcontainerregistry.html
| Service | ARN |
|---------|-----|
| [repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/Repositories.html) | arn:\${Partition}:ecr:\${Region}:\${Account}:repository/\${RepositoryName} |
# AWS Elastic Beanstalk
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselasticbeanstalk.html
| Service | ARN |
|---------|-----|
| [application](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.arn.html) | arn:\${Partition}:elasticbeanstalk:\${Region}:\${Account}:application/\${ApplicationName} |
| [applicationversion](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.arn.html) | arn:\${Partition}:elasticbeanstalk:\${Region}:\${Account}:applicationversion/\${ApplicationName}/\${VersionLabel} |
| [configurationtemplate](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.arn.html) | arn:\${Partition}:elasticbeanstalk:\${Region}:\${Account}:configurationtemplate/\${ApplicationName}/\${TemplateName} |
| [environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.arn.html) | arn:\${Partition}:elasticbeanstalk:\${Region}:\${Account}:environment/\${ApplicationName}/\${EnvironmentName} |
| [solutionstack](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.arn.html) | arn:\${Partition}:elasticbeanstalk:\${Region}::solutionstack/\${SolutionStackName} |
| [platform](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.arn.html) | arn:\${Partition}:elasticbeanstalk:\${Region}::platform/\${PlatformNameWithVersion} |
# Amazon Elastic Inference
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelasticinference.html
| Service | ARN |
|---------|-----|
| [accelerator](accelerator) | arn:\${Partition}:elastic-inference:\${Region}:\${Account}:elastic-inference-accelerator/\${AcceleratorId} |
# Amazon Elastic File System
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelasticfilesystem.html
| Service | ARN |
|---------|-----|
| [file-system](https://docs.aws.amazon.com/efs/latest/ug/access-control-overview.html#access-control-resources) | arn:\${Partition}:elasticfilesystem:\${Region}:\${Account}:file-system/\${FileSystemId} |
| [access-point](https://docs.aws.amazon.com/efs/latest/ug/access-control-overview.html#access-control-resources) | arn:\${Partition}:elasticfilesystem:\${Region}:\${Account}:access-point/\${AccessPointId} |
# Amazon Elastic Container Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelasticcontainerservice.html
| Service | ARN |
|---------|-----|
| [cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/clusters.html) | arn:\${Partition}:ecs:\${Region}:\${Account}:cluster/\${ClusterName} |
| [container-instance](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/manage-capacity.html) | arn:\${Partition}:ecs:\${Region}:\${Account}:container-instance/\${ClusterName}/\${ContainerInstanceId} |
| [service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html) | arn:\${Partition}:ecs:\${Region}:\${Account}:service/\${ClusterName}/\${ServiceName} |
| [task](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html) | arn:\${Partition}:ecs:\${Region}:\${Account}:task/\${ClusterName}/\${TaskId} |
| [task-definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html) | arn:\${Partition}:ecs:\${Region}:\${Account}:task-definition/\${TaskDefinitionFamilyName}:\${TaskDefinitionRevisionNumber} |
| [capacity-provider](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-capacity-providers.html) | arn:\${Partition}:ecs:\${Region}:\${Account}:capacity-provider/\${CapacityProviderName} |
| [task-set](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-external.html) | arn:\${Partition}:ecs:\${Region}:\${Account}:task-set/\${ClusterName}/\${ServiceName}/\${TaskSetId} |
# AWS Elastic Load Balancing
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselasticloadbalancing.html
| Service | ARN |
|---------|-----|
| [loadbalancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) | arn:\${Partition}:elasticloadbalancing:\${Region}:\${Account}:loadbalancer/\${LoadBalancerName} |
# AWS Elemental Appliances and Software
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselementalappliancesandsoftware.html
| Service | ARN |
|---------|-----|
| [quote](https://docs.aws.amazon.com/elemental-appliances-software) | arn:\${Partition}:elemental-appliances-software:\${Region}:\${Account}:quote/\${ResourceId} |
# Amazon Elastic Transcoder
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelastictranscoder.html
| Service | ARN |
|---------|-----|
| [job](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/operations-jobs.html) | arn:\${Partition}:elastictranscoder:\${Region}:\${Account}:job/\${JobId} |
| [pipeline](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/operations-pipelines.html) | arn:\${Partition}:elastictranscoder:\${Region}:\${Account}:pipeline/\${PipelineId} |
| [preset](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/operations-presets.html) | arn:\${Partition}:elastictranscoder:\${Region}:\${Account}:preset/\${PresetId} |
# Amazon Elastic Kubernetes Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelastickubernetesservice.html
| Service | ARN |
|---------|-----|
| [cluster](https://docs.aws.amazon.com/eks/latest/userguide/clusters.html) | arn:\${Partition}:eks:\${Region}:\${Account}:cluster/\${ClusterName} |
| [nodegroup](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html) | arn:\${Partition}:eks:\${Region}:\${Account}:nodegroup/\${ClusterName}/\${NodegroupName}/\${UUID} |
| [addon](https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html) | arn:\${Partition}:eks:\${Region}:\${Account}:addon/\${ClusterName}/\${AddonName}/\${UUID} |
| [fargateprofile](https://docs.aws.amazon.com/eks/latest/userguide/fargate-profile.html) | arn:\${Partition}:eks:\${Region}:\${Account}:fargateprofile/\${ClusterName}/\${FargateProfileName}/\${UUID} |
| [identityproviderconfig](https://docs.aws.amazon.com/eks/latest/userguide/authenticate-oidc-identity-provider.html) | arn:\${Partition}:eks:\${Region}:\${Account}:identityproviderconfig/\${ClusterName}/\${IdentityProviderType}/\${IdentityProviderConfigName}/\${UUID} |
| [eks-anywhere-subscription](https://anywhere.eks.amazonaws.com/docs/clustermgmt/support/cluster-license/) | arn:\${Partition}:eks:\${Region}:\${Account}:eks-anywhere-subscription/\${UUID} |
| [podidentityassociation](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html) | arn:\${Partition}:eks:\${Region}:\${Account}:podidentityassociation/\${ClusterName}/\${UUID} |
| [access-entry](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html) | arn:\${Partition}:eks:\${Region}:\${Account}:access-entry/\${ClusterName}/\${IamIdentityType}/\${IamIdentityAccountID}/\${IamIdentityName}/\${UUID} |
| [access-policy](https://docs.aws.amazon.com/eks/latest/userguide/access-policies.html) | arn:\${Partition}:eks::aws:cluster-access-policy/\${AccessPolicyName} |
# AWS Elastic Load Balancing V2
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselasticloadbalancingv2.html
| Service | ARN |
|---------|-----|
| [listener/app](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html) | arn:\${Partition}:elasticloadbalancing:\${Region}:\${Account}:listener/app/\${LoadBalancerName}/\${LoadBalancerId}/\${ListenerId} |
| [listener-rule/app](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-update-rules.html) | arn:\${Partition}:elasticloadbalancing:\${Region}:\${Account}:listener-rule/app/\${LoadBalancerName}/\${LoadBalancerId}/\${ListenerId}/\${ListenerRuleId} |
| [listener/net](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html) | arn:\${Partition}:elasticloadbalancing:\${Region}:\${Account}:listener/net/\${LoadBalancerName}/\${LoadBalancerId}/\${ListenerId} |
| [listener-rule/net](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-update-rules.html) | arn:\${Partition}:elasticloadbalancing:\${Region}:\${Account}:listener-rule/net/\${LoadBalancerName}/\${LoadBalancerId}/\${ListenerId}/\${ListenerRuleId} |
| [loadbalancer/app/](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html#application-load-balancer-overview) | arn:\${Partition}:elasticloadbalancing:\${Region}:\${Account}:loadbalancer/app/\${LoadBalancerName}/\${LoadBalancerId} |
| [loadbalancer/net/](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html#network-load-balancer-overview) | arn:\${Partition}:elasticloadbalancing:\${Region}:\${Account}:loadbalancer/net/\${LoadBalancerName}/\${LoadBalancerId} |
| [targetgroup](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html) | arn:\${Partition}:elasticloadbalancing:\${Region}:\${Account}:targetgroup/\${TargetGroupName}/\${TargetGroupId} |
| [truststore](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/trust-store.html) | arn:\${Partition}:elasticloadbalancing:\${Region}:\${Account}:truststore/\${TrustStoreName}/\${TrustStoreId} |
# AWS Elemental Appliances and Software Activation Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselementalappliancesandsoftwareactivationservice.html
| Service | ARN |
|---------|-----|
| [activation](https://docs.aws.amazon.com/elemental-appliances-software/) | arn:\${Partition}:elemental-activations:\${Region}:\${Account}:activation/\${ResourceId} |
# AWS Elastic Disaster Recovery
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselasticdisasterrecovery.html
| Service | ARN |
|---------|-----|
| [JobResource](https://docs.aws.amazon.com/drs/latest/userguide/failback-overview.html) | arn:\${Partition}:drs:\${Region}:\${Account}:job/\${JobID} |
| [RecoveryInstanceResource](https://docs.aws.amazon.com/drs/latest/userguide/recovery-instances.html) | arn:\${Partition}:drs:\${Region}:\${Account}:recovery-instance/\${RecoveryInstanceID} |
| [ReplicationConfigurationTemplateResource](https://docs.aws.amazon.com/drs/latest/userguide/replication-settings-template.html) | arn:\${Partition}:drs:\${Region}:\${Account}:replication-configuration-template/\${ReplicationConfigurationTemplateID} |
| [LaunchConfigurationTemplateResource](https://docs.aws.amazon.com/drs/latest/userguide/default-drs-launch-settings.html) | arn:\${Partition}:drs:\${Region}:\${Account}:launch-configuration-template/\${LaunchConfigurationTemplateID} |
| [SourceServerResource](https://docs.aws.amazon.com/drs/latest/userguide/source-servers.html) | arn:\${Partition}:drs:\${Region}:\${Account}:source-server/\${SourceServerID} |
| [SourceNetworkResource](https://docs.aws.amazon.com/drs/latest/userguide/source-networks.html) | arn:\${Partition}:drs:\${Region}:\${Account}:source-network/\${SourceNetworkID} |
# AWS Elemental MediaConnect
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselementalmediaconnect.html
| Service | ARN |
|---------|-----|
| [Entitlement](https://docs.aws.amazon.com/mediaconnect/latest/ug/entitlements.html) | arn:\${Partition}:mediaconnect:\${Region}:\${Account}:entitlement:\${FlowId}:\${EntitlementName} |
| [Flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows.html) | arn:\${Partition}:mediaconnect:\${Region}:\${Account}:flow:\${FlowId}:\${FlowName} |
| [Output](https://docs.aws.amazon.com/mediaconnect/latest/ug/outputs.html) | arn:\${Partition}:mediaconnect:\${Region}:\${Account}:output:\${OutputId}:\${OutputName} |
| [Source](https://docs.aws.amazon.com/mediaconnect/latest/ug/sources.html) | arn:\${Partition}:mediaconnect:\${Region}:\${Account}:source:\${SourceId}:\${SourceName} |
| [Gateway](https://docs.aws.amazon.com/mediaconnect/latest/ug/gateway.html) | arn:\${Partition}:mediaconnect:\${Region}:\${Account}:gateway:\${GatewayId}:\${GatewayName} |
| [Bridge](https://docs.aws.amazon.com/mediaconnect/latest/ug/gateway-components-bridges.html) | arn:\${Partition}:mediaconnect:\${Region}:\${Account}:bridge:\${FlowId}:\${FlowName} |
| [GatewayInstance](https://docs.aws.amazon.com/mediaconnect/latest/ug/gateway-components-instances.html) | arn:\${Partition}:mediaconnect:\${Region}:\${Account}:gateway:\${GatewayId}:\${GatewayName}:instance:\${InstanceId} |
# AWS Elemental MediaPackage
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselementalmediapackage.html
| Service | ARN |
|---------|-----|
| [channels](https://docs.aws.amazon.com/mediapackage/latest/ug/channels.html) | arn:\${Partition}:mediapackage:\${Region}:\${Account}:channels/\${ChannelIdentifier} |
| [origin_endpoints](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints.html) | arn:\${Partition}:mediapackage:\${Region}:\${Account}:origin_endpoints/\${OriginEndpointIdentifier} |
| [harvest_jobs](https://docs.aws.amazon.com/mediapackage/latest/ug/harvest-jobs.html) | arn:\${Partition}:mediapackage:\${Region}:\${Account}:harvest_jobs/\${HarvestJobIdentifier} |
# Amazon ElastiCache
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelasticache.html
| Service | ARN |
|---------|-----|
| [parametergroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.Components.html#WhatIs.Components.ParameterGroups) | arn:\${Partition}:elasticache:\${Region}:\${Account}:parametergroup:\${CacheParameterGroupName} |
| [securitygroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.Components.html#WhatIs.Components.SecurityGroups) | arn:\${Partition}:elasticache:\${Region}:\${Account}:securitygroup:\${CacheSecurityGroupName} |
| [subnetgroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.Components.html#WhatIs.Components.SubnetGroups) | arn:\${Partition}:elasticache:\${Region}:\${Account}:subnetgroup:\${CacheSubnetGroupName} |
| [replicationgroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.Components.html#WhatIs.Components.ReplicationGroups) | arn:\${Partition}:elasticache:\${Region}:\${Account}:replicationgroup:\${ReplicationGroupId} |
| [cluster](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.Components.html#WhatIs.Components.Clusters) | arn:\${Partition}:elasticache:\${Region}:\${Account}:cluster:\${CacheClusterId} |
| [reserved-instance](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/reserved-nodes.html) | arn:\${Partition}:elasticache:\${Region}:\${Account}:reserved-instance:\${ReservedCacheNodeId} |
| [snapshot](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.Components.html#WhatIs.Components.Snapshots) | arn:\${Partition}:elasticache:\${Region}:\${Account}:snapshot:\${SnapshotName} |
| [globalreplicationgroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Redis-Global-Datastore.html) | arn:\${Partition}:elasticache::\${Account}:globalreplicationgroup:\${GlobalReplicationGroupId} |
| [user](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.RBAC.html) | arn:\${Partition}:elasticache:\${Region}:\${Account}:user:\${UserId} |
| [usergroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.RBAC.html) | arn:\${Partition}:elasticache:\${Region}:\${Account}:usergroup:\${UserGroupId} |
| [serverlesscache](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html) | arn:\${Partition}:elasticache:\${Region}:\${Account}:serverlesscache:\${ServerlessCacheName} |
| [serverlesscachesnapshot](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html) | arn:\${Partition}:elasticache:\${Region}:\${Account}:serverlesscachesnapshot:\${ServerlessCacheSnapshotName} |
# Amazon Elastic MapReduce
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelasticmapreduce.html
| Service | ARN |
|---------|-----|
| [cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-overview.html) | arn:\${Partition}:elasticmapreduce:\${Region}:\${Account}:cluster/\${ClusterId} |
| [editor](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks.html) | arn:\${Partition}:elasticmapreduce:\${Region}:\${Account}:editor/\${EditorId} |
| [notebook-execution](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-headless.html) | arn:\${Partition}:elasticmapreduce:\${Region}:\${Account}:notebook-execution/\${NotebookExecutionId} |
| [studio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio.html) | arn:\${Partition}:elasticmapreduce:\${Region}:\${Account}:studio/\${StudioId} |
# AWS Elemental MediaConvert
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselementalmediaconvert.html
| Service | ARN |
|---------|-----|
| [Job](https://docs.aws.amazon.com/mediaconvert/latest/apireference/jobs.html) | arn:\${Partition}:mediaconvert:\${Region}:\${Account}:jobs/\${JobId} |
| [Queue](https://docs.aws.amazon.com/mediaconvert/latest/apireference/queues.html) | arn:\${Partition}:mediaconvert:\${Region}:\${Account}:queues/\${QueueName} |
| [Preset](https://docs.aws.amazon.com/mediaconvert/latest/apireference/presets.html) | arn:\${Partition}:mediaconvert:\${Region}:\${Account}:presets/\${PresetName} |
| [JobTemplate](https://docs.aws.amazon.com/mediaconvert/latest/apireference/jobtemplates.html) | arn:\${Partition}:mediaconvert:\${Region}:\${Account}:jobTemplates/\${JobTemplateName} |
| [CertificateAssociation](https://docs.aws.amazon.com/mediaconvert/latest/apireference/certificates.html) | arn:\${Partition}:mediaconvert:\${Region}:\${Account}:certificates/\${CertificateArn} |
# AWS Elemental MediaPackage V2
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselementalmediapackagev2.html
| Service | ARN |
|---------|-----|
| [ChannelGroup](https://docs.aws.amazon.com/mediapackage/latest/userguide/channel-groups.html) | arn:\${Partition}:mediapackagev2:\${Region}:\${Account}:channelGroup/\${ChannelGroupName} |
| [Channel](https://docs.aws.amazon.com/mediapackage/latest/userguide/channels.html) | arn:\${Partition}:mediapackagev2:\${Region}:\${Account}:channelGroup/\${ChannelGroupName}/channel/\${ChannelName} |
| [OriginEndpoint](https://docs.aws.amazon.com/mediapackage/latest/userguide/endpoints.html) | arn:\${Partition}:mediapackagev2:\${Region}:\${Account}:channelGroup/\${ChannelGroupName}/channel/\${ChannelName}/originEndpoint/\${OriginEndpointName} |
# AWS Elemental MediaLive
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselementalmedialive.html
| Service | ARN |
|---------|-----|
| [channel](https://docs.aws.amazon.com/medialive/latest/ug/container-channel.html) | arn:\${Partition}:medialive:\${Region}:\${Account}:channel:\${ChannelId} |
| [input](https://docs.aws.amazon.com/medialive/latest/ug/creating-input.html) | arn:\${Partition}:medialive:\${Region}:\${Account}:input:\${InputId} |
| [input-device](https://docs.aws.amazon.com/medialive/latest/ug/eml-devices.html) | arn:\${Partition}:medialive:\${Region}:\${Account}:inputDevice:\${DeviceId} |
| [input-security-group](https://docs.aws.amazon.com/medialive/latest/ug/working-with-input-security-groups.html) | arn:\${Partition}:medialive:\${Region}:\${Account}:inputSecurityGroup:\${InputSecurityGroupId} |
| [multiplex](https://docs.aws.amazon.com/medialive/latest/ug/eml-multiplex.html) | arn:\${Partition}:medialive:\${Region}:\${Account}:multiplex:\${MultiplexId} |
| [reservation](https://docs.aws.amazon.com/medialive/latest/ug/reservations.html) | arn:\${Partition}:medialive:\${Region}:\${Account}:reservation:\${ReservationId} |
| [offering](https://docs.aws.amazon.com/medialive/latest/ug/input-output-reservations.html) | arn:\${Partition}:medialive:\${Region}:\${Account}:offering:\${OfferingId} |
| [signal-map](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-create.html) | arn:\${Partition}:medialive:\${Region}:\${Account}:signal-map:\${SignalMapId} |
| [cloudwatch-alarm-template-group](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-alarms-templates-create.html) | arn:\${Partition}:medialive:\${Region}:\${Account}:cloudwatch-alarm-template-group:\${CloudWatchAlarmTemplateGroupId} |
| [cloudwatch-alarm-template](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-alarms-templates-create.html) | arn:\${Partition}:medialive:\${Region}:\${Account}:cloudwatch-alarm-template:\${CloudWatchAlarmTemplateId} |
| [eventbridge-rule-template-group](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-notifications-template-create.html) | arn:\${Partition}:medialive:\${Region}:\${Account}:eventbridge-rule-template-group:\${EventBridgeRuleTemplateGroupId} |
| [eventbridge-rule-template](https://docs.aws.amazon.com/medialive/latest/ug/monitor-with-workflow-monitor-configure-notifications-template-create.html) | arn:\${Partition}:medialive:\${Region}:\${Account}:eventbridge-rule-template:\${EventBridgeRuleTemplateId} |
# AWS Elemental MediaPackage VOD
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselementalmediapackagevod.html
| Service | ARN |
|---------|-----|
| [assets](https://docs.aws.amazon.com/mediapackage/latest/ug/asset.html) | arn:\${Partition}:mediapackage-vod:\${Region}:\${Account}:assets/\${AssetIdentifier} |
| [packaging-configurations](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-cfig.html) | arn:\${Partition}:mediapackage-vod:\${Region}:\${Account}:packaging-configurations/\${PackagingConfigurationIdentifier} |
| [packaging-groups](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-group.html) | arn:\${Partition}:mediapackage-vod:\${Region}:\${Account}:packaging-groups/\${PackagingGroupIdentifier} |
# AWS Elemental MediaStore
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselementalmediastore.html
| Service | ARN |
|---------|-----|
| [container](https://docs.aws.amazon.com/mediastore/latest/ug/containers.html) | arn:\${Partition}:mediastore:\${Region}:\${Account}:container/\${ContainerName} |
| [object](https://docs.aws.amazon.com/mediastore/latest/ug/objects.html) | arn:\${Partition}:mediastore:\${Region}:\${Account}:container/\${ContainerName}/\${ObjectPath} |
| [folder](https://docs.aws.amazon.com/mediastore/latest/ug/folders.html) | arn:\${Partition}:mediastore:\${Region}:\${Account}:container/\${ContainerName}/\${FolderPath} |
# Amazon EMR on EKS (EMR Containers)
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonemroneksemrcontainers.html
| Service | ARN |
|---------|-----|
| [virtualCluster](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/virtual-cluster.html) | arn:\${Partition}:emr-containers:\${Region}:\${Account}:/virtualclusters/\${VirtualClusterId} |
| [jobRun](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/job-runs.html) | arn:\${Partition}:emr-containers:\${Region}:\${Account}:/virtualclusters/\${VirtualClusterId}/jobruns/\${JobRunId} |
| [jobTemplate](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/job-templates.html) | arn:\${Partition}:emr-containers:\${Region}:\${Account}:/jobtemplates/\${JobTemplateId} |
| [managedEndpoint](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-create-eks-cluster.html#emr-studio-create-managed-endpoint) | arn:\${Partition}:emr-containers:\${Region}:\${Account}:/virtualclusters/\${VirtualClusterId}/endpoints/\${EndpointId} |
| [securityConfiguration](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/security-configurations.html) | arn:\${Partition}:emr-containers:\${Region}:\${Account}:/securityconfigurations/\${SecurityConfigurationId} |
# AWS Elemental MediaTailor
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselementalmediatailor.html
| Service | ARN |
|---------|-----|
| [playbackConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/playbackconfiguration.html) | arn:\${Partition}:mediatailor:\${Region}:\${Account}:playbackConfiguration/\${ResourceId} |
| [prefetchSchedule](https://docs.aws.amazon.com/mediatailor/latest/apireference/prefetchschedule-playbackconfigurationname-name.html) | arn:\${Partition}:mediatailor:\${Region}:\${Account}:prefetchSchedule/\${ResourceId} |
| [channel](https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname.html) | arn:\${Partition}:mediatailor:\${Region}:\${Account}:channel/\${ChannelName} |
| [program](https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname-program-programname.html) | arn:\${Partition}:mediatailor:\${Region}:\${Account}:program/\${ChannelName}/\${ProgramName} |
| [sourceLocation](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname.html) | arn:\${Partition}:mediatailor:\${Region}:\${Account}:sourceLocation/\${SourceLocationName} |
| [vodSource](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-vodsource-vodsourcename.html) | arn:\${Partition}:mediatailor:\${Region}:\${Account}:vodSource/\${SourceLocationName}/\${VodSourceName} |
| [liveSource](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-livesource-livesourcename.html) | arn:\${Partition}:mediatailor:\${Region}:\${Account}:liveSource/\${SourceLocationName}/\${LiveSourceName} |
# AWS Entity Resolution
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsentityresolution.html
| Service | ARN |
|---------|-----|
| [MatchingWorkflow](https://docs.aws.amazon.com/entityresolution/latest/userguide/) | arn:\${Partition}:entityresolution::\${Account}:matchingworkflow/\${WorkflowName} |
| [SchemaMapping](https://docs.aws.amazon.com/entityresolution/latest/userguide/) | arn:\${Partition}:entityresolution::\${Account}:schemamapping/\${SchemaName} |
| [IdMappingWorkflow](https://docs.aws.amazon.com/entityresolution/latest/userguide/) | arn:\${Partition}:entityresolution::\${Account}:idmappingworkflow/\${WorkflowName} |
| [ProviderService](https://docs.aws.amazon.com/entityresolution/latest/userguide/) | arn:\${Partition}:entityresolution::\${Account}:providerservice/\${ProviderName}/\${ProviderServiceName} |
| [IdNamespace](https://docs.aws.amazon.com/entityresolution/latest/userguide/) | arn:\${Partition}:entityresolution::\${Account}:idnamespace/\${IdNamespaceName} |
# AWS Elemental Support Cases
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselementalsupportcases.html
| Service | ARN |
|---------|-----|
# AWS Elemental Support Content
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselementalsupportcontent.html
| Service | ARN |
|---------|-----|
# Amazon EMR Serverless
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonemrserverless.html
| Service | ARN |
|---------|-----|
| [application](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless.html) | arn:\${Partition}:emr-serverless:\${Region}:\${Account}:/applications/\${ApplicationId} |
| [jobRun](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless.html) | arn:\${Partition}:emr-serverless:\${Region}:\${Account}:/applications/\${ApplicationId}/jobruns/\${JobRunId} |
# Amazon EventBridge Pipes
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoneventbridgepipes.html
| Service | ARN |
|---------|-----|
| [pipe](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html) | arn:\${Partition}:pipes:\${Region}:\${Account}:pipe/\${Name} |
# Amazon EventBridge Scheduler
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoneventbridgescheduler.html
| Service | ARN |
|---------|-----|
| [schedule-group](https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-schedule-group.html) | arn:\${Partition}:scheduler:\${Region}:\${Account}:schedule-group/\${GroupName} |
| [schedule](https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-schedule.html) | arn:\${Partition}:scheduler:\${Region}:\${Account}:schedule/\${GroupName}/\${ScheduleName} |
# AWS Fault Injection Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsfaultinjectionservice.html
| Service | ARN |
|---------|-----|
| [action](https://docs.aws.amazon.com/fis/latest/userguide/actions.html) | arn:\${Partition}:fis:\${Region}:\${Account}:action/\${Id} |
| [experiment](https://docs.aws.amazon.com/fis/latest/userguide/experiments.html) | arn:\${Partition}:fis:\${Region}:\${Account}:experiment/\${Id} |
| [experiment-template](https://docs.aws.amazon.com/fis/latest/userguide/working-with-templates.html) | arn:\${Partition}:fis:\${Region}:\${Account}:experiment-template/\${Id} |
# Amazon EventBridge
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoneventbridge.html
| Service | ARN |
|---------|-----|
| [event-source](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format) | arn:\${Partition}:events:\${Region}::event-source/\${EventSourceName} |
| [event-bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format) | arn:\${Partition}:events:\${Region}:\${Account}:event-bus/\${EventBusName} |
| [rule-on-default-event-bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format) | arn:\${Partition}:events:\${Region}:\${Account}:rule/\${RuleName} |
| [rule-on-custom-event-bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format) | arn:\${Partition}:events:\${Region}:\${Account}:rule/\${EventBusName}/\${RuleName} |
| [archive](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format) | arn:\${Partition}:events:\${Region}:\${Account}:archive/\${ArchiveName} |
| [replay](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format) | arn:\${Partition}:events:\${Region}:\${Account}:replay/\${ReplayName} |
| [connection](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format) | arn:\${Partition}:events:\${Region}:\${Account}:connection/\${ConnectionName} |
| [api-destination](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format) | arn:\${Partition}:events:\${Region}:\${Account}:api-destination/\${ApiDestinationName} |
| [endpoint](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html#eventbridge-arn-format) | arn:\${Partition}:events:\${Region}:\${Account}:endpoint/\${EndpointName} |
# AWS Free Tier
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsfreetier.html
| Service | ARN |
|---------|-----|
# Amazon EventBridge Schemas
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoneventbridgeschemas.html
| Service | ARN |
|---------|-----|
| [discoverer](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-schema.html) | arn:\${Partition}:schemas:\${Region}:\${Account}:discoverer/\${DiscovererId} |
| [registry](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-schema.html) | arn:\${Partition}:schemas:\${Region}:\${Account}:registry/\${RegistryName} |
| [schema](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-schema.html) | arn:\${Partition}:schemas:\${Region}:\${Account}:schema/\${RegistryName}/\${SchemaName} |
# Amazon FinSpace API
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfinspaceapi.html
| Service | ARN |
|---------|-----|
| [credential](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html) | arn:\${Partition}:finspace-api:\${Region}:\${Account}:/credentials/programmatic |
# Amazon FreeRTOS
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfreertos.html
| Service | ARN |
|---------|-----|
| [configuration](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-ocw.html) | arn:\${Partition}:freertos:\${Region}:\${Account}:configuration/\${ConfigurationName} |
| [subscription](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-getting-started-emp.html) | arn:\${Partition}:freertos:\${Region}:\${Account}:subscription/\${SubscriptionID} |
# Amazon FSx
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfsx.html
| Service | ARN |
|---------|-----|
| [file-system](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/access-control-overview.html#access-control-resources) | arn:\${Partition}:fsx:\${Region}:\${Account}:file-system/\${FileSystemId} |
| [file-cache](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/security-iam.html) | arn:\${Partition}:fsx:\${Region}:\${Account}:file-cache/\${FileCacheId} |
| [backup](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/access-control-overview.html#access-control-resources) | arn:\${Partition}:fsx:\${Region}:\${Account}:backup/\${BackupId} |
| [storage-virtual-machine](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/security-iam.html) | arn:\${Partition}:fsx:\${Region}:\${Account}:storage-virtual-machine/\${FileSystemId}/\${StorageVirtualMachineId} |
| [task](https://docs.aws.amazon.com/fsx/latest/LustreGuide/access-control-overview.html#access-control-resources) | arn:\${Partition}:fsx:\${Region}:\${Account}:task/\${TaskId} |
| [association](https://docs.aws.amazon.com/fsx/latest/LustreGuide/access-control-overview.html#access-control-resources) | arn:\${Partition}:fsx:\${Region}:\${Account}:association/\${FileSystemIdOrFileCacheId}/\${DataRepositoryAssociationId} |
| [volume](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/security-iam.html) | arn:\${Partition}:fsx:\${Region}:\${Account}:volume/\${FileSystemId}/\${VolumeId} |
| [snapshot](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/access-control-overview.html#access-control-resources) | arn:\${Partition}:fsx:\${Region}:\${Account}:snapshot/\${VolumeId}/\${SnapshotId} |
# Amazon Fraud Detector
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html
| Service | ARN |
|---------|-----|
| [batch-prediction](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies) | arn:\${Partition}:frauddetector:\${Region}:\${Account}:batch-prediction/\${ResourcePath} |
| [detector](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies) | arn:\${Partition}:frauddetector:\${Region}:\${Account}:detector/\${ResourcePath} |
| [detector-version](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies) | arn:\${Partition}:frauddetector:\${Region}:\${Account}:detector-version/\${ResourcePath} |
| [entity-type](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies) | arn:\${Partition}:frauddetector:\${Region}:\${Account}:entity-type/\${ResourcePath} |
| [external-model](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies) | arn:\${Partition}:frauddetector:\${Region}:\${Account}:external-model/\${ResourcePath} |
| [event-type](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies) | arn:\${Partition}:frauddetector:\${Region}:\${Account}:event-type/\${ResourcePath} |
| [label](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies) | arn:\${Partition}:frauddetector:\${Region}:\${Account}:label/\${ResourcePath} |
| [model](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies) | arn:\${Partition}:frauddetector:\${Region}:\${Account}:model/\${ResourcePath} |
| [model-version](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies) | arn:\${Partition}:frauddetector:\${Region}:\${Account}:model-version/\${ResourcePath} |
| [outcome](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies) | arn:\${Partition}:frauddetector:\${Region}:\${Account}:outcome/\${ResourcePath} |
| [rule](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies) | arn:\${Partition}:frauddetector:\${Region}:\${Account}:rule/\${ResourcePath} |
| [variable](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies) | arn:\${Partition}:frauddetector:\${Region}:\${Account}:variable/\${ResourcePath} |
| [batch-import](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies) | arn:\${Partition}:frauddetector:\${Region}:\${Account}:batch-import/\${ResourcePath} |
| [list](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies) | arn:\${Partition}:frauddetector:\${Region}:\${Account}:list/\${ResourcePath} |
# AWS Glue DataBrew
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsgluedatabrew.html
| Service | ARN |
|---------|-----|
| [Project](https://docs.aws.amazon.com/databrew/latest/dg/projects.html) | arn:\${Partition}:databrew:\${Region}:\${Account}:project/\${ResourceId} |
| [Dataset](https://docs.aws.amazon.com/databrew/latest/dg/datasets.html) | arn:\${Partition}:databrew:\${Region}:\${Account}:dataset/\${ResourceId} |
| [Ruleset](https://docs.aws.amazon.com/databrew/latest/dg/rulesets.html) | arn:\${Partition}:databrew:\${Region}:\${Account}:ruleset/\${ResourceId} |
| [Recipe](https://docs.aws.amazon.com/databrew/latest/dg/recipes.html) | arn:\${Partition}:databrew:\${Region}:\${Account}:recipe/\${ResourceId} |
| [Job](https://docs.aws.amazon.com/databrew/latest/dg/jobs.html) | arn:\${Partition}:databrew:\${Region}:\${Account}:job/\${ResourceId} |
| [Schedule](https://docs.aws.amazon.com/databrew/latest/dg/jobs.html#jobs.scheduling) | arn:\${Partition}:databrew:\${Region}:\${Account}:schedule/\${ResourceId} |
# Amazon FinSpace
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfinspace.html
| Service | ARN |
|---------|-----|
| [environment](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html) | arn:\${Partition}:finspace:\${Region}:\${Account}:environment/\${EnvironmentId} |
| [user](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html) | arn:\${Partition}:finspace:\${Region}:\${Account}:user/\${UserId} |
| [kxEnvironment](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html) | arn:\${Partition}:finspace:\${Region}:\${Account}:kxEnvironment/\${EnvironmentId} |
| [kxUser](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html) | arn:\${Partition}:finspace:\${Region}:\${Account}:kxEnvironment/\${EnvironmentId}/kxUser/\${UserName} |
| [kxCluster](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html) | arn:\${Partition}:finspace:\${Region}:\${Account}:kxEnvironment/\${EnvironmentId}/kxCluster/\${KxCluster} |
| [kxDatabase](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html) | arn:\${Partition}:finspace:\${Region}:\${Account}:kxEnvironment/\${EnvironmentId}/kxDatabase/\${KxDatabase} |
| [kxScalingGroup](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html) | arn:\${Partition}:finspace:\${Region}:\${Account}:kxEnvironment/\${EnvironmentId}/kxScalingGroup/\${KxScalingGroup} |
| [kxDataview](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html) | arn:\${Partition}:finspace:\${Region}:\${Account}:kxEnvironment/\${EnvironmentId}/kxDatabase/\${KxDatabase}/kxDataview/\${KxDataview} |
| [kxVolume](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html) | arn:\${Partition}:finspace:\${Region}:\${Account}:kxEnvironment/\${EnvironmentId}/kxVolume/\${KxVolume} |
# AWS Global Accelerator
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsglobalaccelerator.html
| Service | ARN |
|---------|-----|
| [accelerator](https://docs.aws.amazon.com/global-accelerator/latest/api/API_Accelerator.html) | arn:\${Partition}:globalaccelerator::\${Account}:accelerator/\${ResourceId} |
| [listener](https://docs.aws.amazon.com/global-accelerator/latest/api/API_Listener.html) | arn:\${Partition}:globalaccelerator::\${Account}:accelerator/\${ResourceId}/listener/\${ListenerId} |
| [endpointgroup](https://docs.aws.amazon.com/global-accelerator/latest/api/API_EndpointGroup.html) | arn:\${Partition}:globalaccelerator::\${Account}:accelerator/\${ResourceId}/listener/\${ListenerId}/endpoint-group/\${EndpointGroupId} |
| [attachment](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CrossAccountAttachment.html) | arn:\${Partition}:globalaccelerator::\${Account}:attachment/\${ResourceId} |
# AWS Firewall Manager
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsfirewallmanager.html
| Service | ARN |
|---------|-----|
| [policy](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_Policy.html) | arn:\${Partition}:fms:\${Region}:\${Account}:policy/\${Id} |
| [applications-list](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_AppsListData.html) | arn:\${Partition}:fms:\${Region}:\${Account}:applications-list/\${Id} |
| [protocols-list](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ProtocolsListData.html) | arn:\${Partition}:fms:\${Region}:\${Account}:protocols-list/\${Id} |
| [resource-set](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ResourceSet.html) | arn:\${Partition}:fms:\${Region}:\${Account}:resource-set/\${Id} |
# AWS HealthImaging
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awshealthimaging.html
| Service | ARN |
|---------|-----|
| [datastore](https://docs.aws.amazon.com/healthimaging/latest/devguide/API_DatastoreProperties.html) | arn:\${Partition}:medical-imaging:\${Region}:\${Account}:datastore/\${DatastoreId} |
| [imageset](https://docs.aws.amazon.com/healthimaging/latest/devguide/API_ImageSetProperties.html) | arn:\${Partition}:medical-imaging:\${Region}:\${Account}:datastore/\${DatastoreId}/imageset/\${ImageSetId} |
# Amazon Forecast
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonforecast.html
| Service | ARN |
|---------|-----|
| [dataset](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html) | arn:\${Partition}:forecast:\${Region}:\${Account}:dataset/\${ResourceId} |
| [datasetGroup](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetGroup.html) | arn:\${Partition}:forecast:\${Region}:\${Account}:dataset-group/\${ResourceId} |
| [datasetImportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetImportJob.html) | arn:\${Partition}:forecast:\${Region}:\${Account}:dataset-import-job/\${ResourceId} |
| [algorithm](https://docs.aws.amazon.com/forecast/latest/dg/aws-forecast-choosing-recipes.html) | arn:\${Partition}:forecast:::algorithm/\${ResourceId} |
| [predictor](https://docs.aws.amazon.com/forecast/latest/dg/API_CreatePredictor.html) | arn:\${Partition}:forecast:\${Region}:\${Account}:predictor/\${ResourceId} |
| [predictorBacktestExportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_CreatePredictorBacktestExportJob.html) | arn:\${Partition}:forecast:\${Region}:\${Account}:predictor-backtest-export-job/\${ResourceId} |
| [forecast](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateForecast.html) | arn:\${Partition}:forecast:\${Region}:\${Account}:forecast/\${ResourceId} |
| [forecastExport](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateForecastExportJob.html) | arn:\${Partition}:forecast:\${Region}:\${Account}:forecast-export-job/\${ResourceId} |
| [explainability](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateExplainability.html) | arn:\${Partition}:forecast:\${Region}:\${Account}:explainability/\${ResourceId} |
| [explainabilityExport](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateExplainabilityExport.html) | arn:\${Partition}:forecast:\${Region}:\${Account}:explainability-export/\${ResourceId} |
| [monitor](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateMonitor.html) | arn:\${Partition}:forecast:\${Region}:\${Account}:monitor/\${ResourceId} |
| [whatIfAnalysis](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateWhatIfAnalysis.html) | arn:\${Partition}:forecast:\${Region}:\${Account}:what-if-analysis/\${ResourceId} |
| [whatIfForecast](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateWhatIfForecast.html) | arn:\${Partition}:forecast:\${Region}:\${Account}:what-if-forecast/\${ResourceId} |
| [whatIfForecastExport](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateWhatIfForecastExport.html) | arn:\${Partition}:forecast:\${Region}:\${Account}:what-if-forecast-export/\${ResourceId} |
| [endpoint](https://docs.aws.amazon.com/forecast/latest/dg/what-is-forecast.html) | arn:\${Partition}:forecast:\${Region}:\${Account}:forecast-endpoint/\${ResourceId} |
# Amazon GroundTruth Labeling
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazongroundtruthlabeling.html
| Service | ARN |
|---------|-----|
# AWS Ground Station
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsgroundstation.html
| Service | ARN |
|---------|-----|
| [Config](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ConfigListItem.html) | arn:\${Partition}:groundstation:\${Region}:\${Account}:config/\${ConfigType}/\${ConfigId} |
| [Contact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ContactData.html) | arn:\${Partition}:groundstation:\${Region}:\${Account}:contact/\${ContactId} |
| [DataflowEndpointGroup](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DataflowEndpoint.html) | arn:\${Partition}:groundstation:\${Region}:\${Account}:dataflow-endpoint-group/\${DataflowEndpointGroupId} |
| [EphemerisItem](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_EphemerisItem.html) | arn:\${Partition}:groundstation:\${Region}:\${Account}:ephemeris/\${EphemerisId} |
| [GroundStationResource](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GroundStationData.html) | arn:\${Partition}:groundstation:\${Region}:\${Account}:groundstation:\${GroundStationId} |
| [MissionProfile](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_MissionProfileListItem.html) | arn:\${Partition}:groundstation:\${Region}:\${Account}:mission-profile/\${MissionProfileId} |
| [Satellite](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_SatelliteListItem.html) | arn:\${Partition}:groundstation:\${Region}:\${Account}:satellite/\${SatelliteId} |
| [Agent](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AgentDetails.html) | arn:\${Partition}:groundstation:\${Region}:\${Account}:agent/\${AgentId} |
# AWS HealthLake
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awshealthlake.html
| Service | ARN |
|---------|-----|
| [datastore](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DatastoreProperties.html) | arn:\${Partition}:healthlake:\${Region}:\${Account}:datastore/fhir/\${DatastoreId} |
# AWS Health APIs and Notifications
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awshealthapisandnotifications.html
| Service | ARN |
|---------|-----|
| [event](https://docs.aws.amazon.com/health/latest/ug/supported-operations.html) | arn:\${Partition}:health:*::event/\${Service}/\${EventTypeCode}/* |
# Amazon Honeycode
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonhoneycode.html
| Service | ARN |
|---------|-----|
| [workbook](https://docs.aws.amazon.com/honeycode/latest/UserGuide/resource-workbook.html) | arn:\${Partition}:honeycode:\${Region}:\${Account}:workbook:workbook/\${WorkbookId} |
| [table](https://docs.aws.amazon.com/honeycode/latest/UserGuide/resource-table.html) | arn:\${Partition}:honeycode:\${Region}:\${Account}:table:workbook/\${WorkbookId}/table/\${TableId} |
| [screen](https://docs.aws.amazon.com/honeycode/latest/UserGuide/resource-screen.html) | arn:\${Partition}:honeycode:\${Region}:\${Account}:screen:workbook/\${WorkbookId}/app/\${AppId}/screen/\${ScreenId} |
| [screen-automation](https://docs.aws.amazon.com/honeycode/latest/UserGuide/resource-screen-automation.html) | arn:\${Partition}:honeycode:\${Region}:\${Account}:screen-automation:workbook/\${WorkbookId}/app/\${AppId}/screen/\${ScreenId}/automation/\${AutomationId} |
# Amazon GameLift
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazongamelift.html
| Service | ARN |
|---------|-----|
| [alias](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-console-aliases.html) | arn:\${Partition}:gamelift:\${Region}::alias/\${AliasId} |
| [build](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-console-builds.html) | arn:\${Partition}:gamelift:\${Region}:\${Account}:build/\${BuildId} |
| [containerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/developerguide/containers-create-groups.html) | arn:\${Partition}:gamelift:\${Region}:\${Account}:containergroupdefinition/\${Name} |
| [fleet](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-console-fleets.html) | arn:\${Partition}:gamelift:\${Region}:\${Account}:fleet/\${FleetId} |
| [gameServerGroup](https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-integrate-gameservergroup.html) | arn:\${Partition}:gamelift:\${Region}:\${Account}:gameservergroup/\${GameServerGroupName} |
| [gameSessionQueue](https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-console.html) | arn:\${Partition}:gamelift:\${Region}:\${Account}:gamesessionqueue/\${GameSessionQueueName} |
| [location](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-anywhere.html#fleet-anywhere-location) | arn:\${Partition}:gamelift:\${Region}:\${Account}:location/\${LocationId} |
| [matchmakingConfiguration](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-create-configuration.html) | arn:\${Partition}:gamelift:\${Region}:\${Account}:matchmakingconfiguration/\${MatchmakingConfigurationName} |
| [matchmakingRuleSet](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-rulesets.html) | arn:\${Partition}:gamelift:\${Region}:\${Account}:matchmakingruleset/\${MatchmakingRuleSetName} |
| [script](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-console-scripts.html) | arn:\${Partition}:gamelift:\${Region}:\${Account}:script/\${ScriptId} |
# Amazon GuardDuty
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonguardduty.html
| Service | ARN |
|---------|-----|
| [detector](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_managing_access.html#guardduty-resources) | arn:\${Partition}:guardduty:\${Region}:\${Account}:detector/\${DetectorId} |
| [filter](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_managing_access.html#guardduty-resources) | arn:\${Partition}:guardduty:\${Region}:\${Account}:detector/\${DetectorId}/filter/\${FilterName} |
| [ipset](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_managing_access.html#guardduty-resources) | arn:\${Partition}:guardduty:\${Region}:\${Account}:detector/\${DetectorId}/ipset/\${IPSetId} |
| [threatintelset](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_managing_access.html#guardduty-resources) | arn:\${Partition}:guardduty:\${Region}:\${Account}:detector/\${DetectorId}/threatintelset/\${ThreatIntelSetId} |
| [publishingDestination](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_managing_access.html#guardduty-resources) | arn:\${Partition}:guardduty:\${Region}:\${Account}:detector/\${DetectorId}/publishingDestination/\${PublishingDestinationId} |
# AWS IAM Access Analyzer
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiamaccessanalyzer.html
| Service | ARN |
|---------|-----|
| [Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources) | arn:\${Partition}:access-analyzer:\${Region}:\${Account}:analyzer/\${AnalyzerName} |
| [ArchiveRule](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources) | arn:\${Partition}:access-analyzer:\${Region}:\${Account}:analyzer/\${AnalyzerName}/archive-rule/\${RuleName} |
# AWS IAM Identity Center OIDC service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiamidentitycenteroidcservice.html
| Service | ARN |
|---------|-----|
| [Application](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-started-enable-identity-center.html) | arn:\${Partition}:sso::\${AccountId}:application/\${InstanceId}/\${ApplicationId} |
# AWS Identity Store Auth
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsidentitystoreauth.html
| Service | ARN |
|---------|-----|
# AWS HealthOmics
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awshealthomics.html
| Service | ARN |
|---------|-----|
| [AnnotationImportJob](https://docs.aws.amazon.com/omics/latest/api/API_AnnotationImportJobItem.html) | arn:\${Partition}:omics:\${Region}:\${Account}:annotationImportJob/\${AnnotationImportJobId} |
| [AnnotationStore](https://docs.aws.amazon.com/omics/latest/api/API_AnnotationStoreItem.html) | arn:\${Partition}:omics:\${Region}:\${Account}:annotationStore/\${AnnotationStoreId} |
| [AnnotationStoreVersion](https://docs.aws.amazon.com/omics/latest/api/API_AnnotationStoreVersionItem.html) | arn:\${Partition}:omics:\${Region}:\${Account}:annotationStore/\${AnnotationStoreName}/version/\${AnnotationStoreVersionName} |
| [readSet](https://docs.aws.amazon.com/omics/latest/api/API_ReadSetFiles.html) | arn:\${Partition}:omics:\${Region}:\${Account}:sequenceStore/\${SequenceStoreId}/readSet/\${ReadSetId} |
| [reference](https://docs.aws.amazon.com/omics/latest/api/API_ReferenceFiles.html) | arn:\${Partition}:omics:\${Region}:\${Account}:referenceStore/\${ReferenceStoreId}/reference/\${ReferenceId} |
| [referenceStore](https://docs.aws.amazon.com/omics/latest/api/API_ReferenceStoreDetail.html) | arn:\${Partition}:omics:\${Region}:\${Account}:referenceStore/\${ReferenceStoreId} |
| [run](https://docs.aws.amazon.com/omics/latest/api/API_RunListItem.html) | arn:\${Partition}:omics:\${Region}:\${Account}:run/\${Id} |
| [runGroup](https://docs.aws.amazon.com/omics/latest/api/API_RunGroupListItem.html) | arn:\${Partition}:omics:\${Region}:\${Account}:runGroup/\${Id} |
| [sequenceStore](https://docs.aws.amazon.com/omics/latest/api/API_SequenceStoreDetail.html) | arn:\${Partition}:omics:\${Region}:\${Account}:sequenceStore/\${SequenceStoreId} |
| [TaggingResource](https://docs.aws.amazon.com/omics/latest/api/API_TagResource.html) | arn:\${Partition}:omics:\${Region}:\${Account}:tag/\${TagKey} |
| [TaskResource](https://docs.aws.amazon.com/omics/latest/api/API_TaskListItem.html) | arn:\${Partition}:omics:\${Region}:\${Account}:task/\${Id} |
| [VariantImportJob](https://docs.aws.amazon.com/omics/latest/api/API_VariantImportJobItem.html) | arn:\${Partition}:omics:\${Region}:\${Account}:variantImportJob/\${VariantImportJobId} |
| [VariantStore](https://docs.aws.amazon.com/omics/latest/api/API_VariantStoreItem.html) | arn:\${Partition}:omics:\${Region}:\${Account}:variantStore/\${VariantStoreId} |
| [workflow](https://docs.aws.amazon.com/omics/latest/api/API_WorkflowListItem.html) | arn:\${Partition}:omics:\${Region}:\${Account}:workflow/\${Id} |
# High-volume outbound communications
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_high-volumeoutboundcommunications.html
| Service | ARN |
|---------|-----|
| [campaign](https://docs.aws.amazon.com/connect/latest/adminguide/enable-high-volume-outbound-communications.html) | arn:\${Partition}:connect-campaigns:\${Region}:\${Account}:campaign/\${CampaignId} |
# AWS Glue
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsglue.html
| Service | ARN |
|---------|-----|
| [catalog](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html) | arn:\${Partition}:glue:\${Region}:\${Account}:catalog |
| [database](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html) | arn:\${Partition}:glue:\${Region}:\${Account}:database/\${DatabaseName} |
| [table](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html) | arn:\${Partition}:glue:\${Region}:\${Account}:table/\${DatabaseName}/\${TableName} |
| [tableversion](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html) | arn:\${Partition}:glue:\${Region}:\${Account}:tableVersion/\${DatabaseName}/\${TableName}/\${TableVersionName} |
| [connection](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html) | arn:\${Partition}:glue:\${Region}:\${Account}:connection/\${ConnectionName} |
| [userdefinedfunction](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html) | arn:\${Partition}:glue:\${Region}:\${Account}:userDefinedFunction/\${DatabaseName}/\${UserDefinedFunctionName} |
| [devendpoint](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html) | arn:\${Partition}:glue:\${Region}:\${Account}:devEndpoint/\${DevEndpointName} |
| [job](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html) | arn:\${Partition}:glue:\${Region}:\${Account}:job/\${JobName} |
| [trigger](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html) | arn:\${Partition}:glue:\${Region}:\${Account}:trigger/\${TriggerName} |
| [crawler](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html) | arn:\${Partition}:glue:\${Region}:\${Account}:crawler/\${CrawlerName} |
| [workflow](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html) | arn:\${Partition}:glue:\${Region}:\${Account}:workflow/\${WorkflowName} |
| [blueprint](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html) | arn:\${Partition}:glue:\${Region}:\${Account}:blueprint/\${BlueprintName} |
| [mlTransform](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html) | arn:\${Partition}:glue:\${Region}:\${Account}:mlTransform/\${TransformId} |
| [registry](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html) | arn:\${Partition}:glue:\${Region}:\${Account}:registry/\${RegistryName} |
| [schema](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html) | arn:\${Partition}:glue:\${Region}:\${Account}:schema/\${SchemaName} |
| [session](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html) | arn:\${Partition}:glue:\${Region}:\${Account}:session/\${SessionId} |
| [dataQualityRuleset](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html) | arn:\${Partition}:glue:\${Region}:\${Account}:dataQualityRuleset/\${RulesetName} |
| [customEntityType](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html) | arn:\${Partition}:glue:\${Region}:\${Account}:customEntityType/\${CustomEntityTypeId} |
| [completion](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html) | arn:\${Partition}:glue:\${Region}:\${Account}:completion/\${CompletionId} |
# AWS IAM Identity Center (successor to AWS Single Sign-On) directory
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiamidentitycentersuccessortoawssinglesign-ondirectory.html
| Service | ARN |
|---------|-----|
# AWS Identity Sync
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsidentitysync.html
| Service | ARN |
|---------|-----|
| [SyncProfileResource](https://docs.aws.amazon.com/singlesignon/latest/userguide/security-iam-awsmanpol.html) | arn:\${Partition}:identity-sync:\${Region}:\${Account}:profile/\${SyncProfileName} |
| [SyncTargetResource](https://docs.aws.amazon.com/singlesignon/latest/userguide/security-iam-awsmanpol.html) | arn:\${Partition}:identity-sync:\${Region}:\${Account}:target/\${SyncProfileName}/\${SyncTargetName} |
# Amazon Inspector
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoninspector.html
| Service | ARN |
|---------|-----|
# AWS Identity Store
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsidentitystore.html
| Service | ARN |
|---------|-----|
| [Identitystore](https://docs.aws.amazon.com/singlesignon/latest/) | arn:\${Partition}:identitystore::\${Account}:identitystore/\${IdentityStoreId} |
| [User](https://docs.aws.amazon.com/singlesignon/latest/) | arn:\${Partition}:identitystore:::user/\${UserId} |
| [Group](https://docs.aws.amazon.com/singlesignon/latest/) | arn:\${Partition}:identitystore:::group/\${GroupId} |
| [GroupMembership](https://docs.aws.amazon.com/singlesignon/latest/) | arn:\${Partition}:identitystore:::membership/\${MembershipId} |
| [AllUsers](https://docs.aws.amazon.com/singlesignon/latest/) | arn:\${Partition}:identitystore:::user/* |
| [AllGroups](https://docs.aws.amazon.com/singlesignon/latest/) | arn:\${Partition}:identitystore:::group/* |
| [AllGroupMemberships](https://docs.aws.amazon.com/singlesignon/latest/) | arn:\${Partition}:identitystore:::membership/* |
# AWS Import Export Disk Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsimportexportdiskservice.html
| Service | ARN |
|---------|-----|
# Amazon InspectorScan
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoninspectorscan.html
| Service | ARN |
|---------|-----|
# Amazon Interactive Video Service Chat
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoninteractivevideoservicechat.html
| Service | ARN |
|---------|-----|
| [Room](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_Room.html) | arn:\${Partition}:ivschat:\${Region}:\${Account}:room/\${ResourceId} |
| [Logging-Configuration](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_LoggingConfiguration.html) | arn:\${Partition}:ivschat:\${Region}:\${Account}:logging-configuration/\${ResourceId} |
# AWS Identity and Access Management (IAM)
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsidentityandaccessmanagementiam.html
| Service | ARN |
|---------|-----|
| [access-report](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor-view-data-orgs.html) | arn:\${Partition}:iam::\${Account}:access-report/\${EntityPath} |
| [assumed-role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) | arn:\${Partition}:iam::\${Account}:assumed-role/\${RoleName}/\${RoleSessionName} |
| [federated-user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html) | arn:\${Partition}:iam::\${Account}:federated-user/\${UserName} |
| [group](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html) | arn:\${Partition}:iam::\${Account}:group/\${GroupNameWithPath} |
| [instance-profile](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) | arn:\${Partition}:iam::\${Account}:instance-profile/\${InstanceProfileNameWithPath} |
| [mfa](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html) | arn:\${Partition}:iam::\${Account}:mfa/\${MfaTokenIdWithPath} |
| [oidc-provider](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html) | arn:\${Partition}:iam::\${Account}:oidc-provider/\${OidcProviderName} |
| [policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html) | arn:\${Partition}:iam::\${Account}:policy/\${PolicyNameWithPath} |
| [role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) | arn:\${Partition}:iam::\${Account}:role/\${RoleNameWithPath} |
| [saml-provider](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html) | arn:\${Partition}:iam::\${Account}:saml-provider/\${SamlProviderName} |
| [server-certificate](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html) | arn:\${Partition}:iam::\${Account}:server-certificate/\${CertificateNameWithPath} |
| [sms-mfa](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html) | arn:\${Partition}:iam::\${Account}:sms-mfa/\${MfaTokenIdWithPath} |
| [user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html) | arn:\${Partition}:iam::\${Account}:user/\${UserNameWithPath} |
# Amazon Interactive Video Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoninteractivevideoservice.html
| Service | ARN |
|---------|-----|
| [Channel](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_Channel.html) | arn:\${Partition}:ivs:\${Region}:\${Account}:channel/\${ResourceId} |
| [Stream-Key](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_StreamKey.html) | arn:\${Partition}:ivs:\${Region}:\${Account}:stream-key/\${ResourceId} |
| [Playback-Key-Pair](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_PlaybackKeyPair.html) | arn:\${Partition}:ivs:\${Region}:\${Account}:playback-key/\${ResourceId} |
| [Playback-Restriction-Policy](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_PlaybackRestrictionPolicy.html) | arn:\${Partition}:ivs:\${Region}:\${Account}:playback-restriction-policy/\${ResourceId} |
| [Recording-Configuration](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_RecordingConfiguration.html) | arn:\${Partition}:ivs:\${Region}:\${Account}:recording-configuration/\${ResourceId} |
| [Stage](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_Stage.html) | arn:\${Partition}:ivs:\${Region}:\${Account}:stage/\${ResourceId} |
| [Composition](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_Composition.html) | arn:\${Partition}:ivs:\${Region}:\${Account}:composition/\${ResourceId} |
| [Encoder-Configuration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_EncoderConfiguration.html) | arn:\${Partition}:ivs:\${Region}:\${Account}:encoder-configuration/\${ResourceId} |
| [Storage-Configuration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_StorageConfiguration.html) | arn:\${Partition}:ivs:\${Region}:\${Account}:storage-configuration/\${ResourceId} |
# AWS IoT Device Tester
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotdevicetester.html
| Service | ARN |
|---------|-----|
# AWS Identity and Access Management Roles Anywhere
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsidentityandaccessmanagementrolesanywhere.html
| Service | ARN |
|---------|-----|
| [trust-anchor](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html#first-time-user) | arn:\${Partition}:rolesanywhere:\${Region}:\${Account}:trust-anchor/\${TrustAnchorId} |
| [profile](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html#first-time-user) | arn:\${Partition}:rolesanywhere:\${Region}:\${Account}:profile/\${ProfileId} |
| [subject](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html#first-time-user) | arn:\${Partition}:rolesanywhere:\${Region}:\${Account}:subject/\${SubjectId} |
| [crl](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html#first-time-user) | arn:\${Partition}:rolesanywhere:\${Region}:\${Account}:crl/\${CrlId} |
# AWS IAM Identity Center (successor to AWS Single Sign-On)
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiamidentitycentersuccessortoawssinglesign-on.html
| Service | ARN |
|---------|-----|
| [PermissionSet](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html) | arn:\${Partition}:sso:::permissionSet/\${InstanceId}/\${PermissionSetId} |
| [Account](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html) | arn:\${Partition}:sso:::account/\${AccountId} |
| [Instance](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_InstanceMetadata.html) | arn:\${Partition}:sso:::instance/\${InstanceId} |
| [Application](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_Application.html) | arn:\${Partition}:sso::\${AccountId}:application/\${InstanceId}/\${ApplicationId} |
| [TrustedTokenIssuer](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_TrustedTokenIssuerMetadata.html) | arn:\${Partition}:sso::\${AccountId}:trustedTokenIssuer/\${InstanceId}/\${TrustedTokenIssuerId} |
| [ApplicationProvider](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ApplicationProvider.html) | arn:\${Partition}:sso::aws:applicationProvider/\${ApplicationProviderId} |
# AWS Invoicing Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsinvoicingservice.html
| Service | ARN |
|---------|-----|
# AWS IoT 1-Click
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot1-click.html
| Service | ARN |
|---------|-----|
| [device](https://docs.aws.amazon.com/iot-1-click/1.0/devices-apireference/resources.html) | arn:\${Partition}:iot1click:\${Region}:\${Account}:devices/\${DeviceId} |
| [project](https://docs.aws.amazon.com/iot-1-click/latest/projects-apireference/API_Operations.html) | arn:\${Partition}:iot1click:\${Region}:\${Account}:projects/\${ProjectName} |
# Amazon Inspector2
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoninspector2.html
| Service | ARN |
|---------|-----|
| [Filter](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html) | arn:\${Partition}:inspector2:\${Region}:\${Account}:owner/\${OwnerId}/filter/\${FilterId} |
| [Finding](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html) | arn:\${Partition}:inspector2:\${Region}:\${Account}:finding/\${FindingId} |
| [CIS Scan Configuration](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html) | arn:\${Partition}:inspector2:\${Region}:\${Account}:owner/\${OwnerId}/cis-configuration/\${CISScanConfigurationId} |
# AWS IoT Core Device Advisor
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotcoredeviceadvisor.html
| Service | ARN |
|---------|-----|
| [Suitedefinition](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-workflow.html#device-advisor-workflow-create-suite-definition) | arn:\${Partition}:iotdeviceadvisor:\${Region}:\${Account}:suitedefinition/\${SuiteDefinitionId} |
| [Suiterun](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-workflow.html#device-advisor-workflow-start-suite-run) | arn:\${Partition}:iotdeviceadvisor:\${Region}:\${Account}:suiterun/\${SuiteDefinitionId}/\${SuiteRunId} |
# AWS IoT Fleet Hub for Device Management
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotfleethubfordevicemanagement.html
| Service | ARN |
|---------|-----|
| [application](https://docs.aws.amazon.com/iot/latest/apireference/API_iotfleethub_ApplicationSummary.html) | arn:\${Partition}:iotfleethub:\${Region}:\${Account}:application/\${ApplicationId} |
# AWS IoT Events
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotevents.html
| Service | ARN |
|---------|-----|
| [detectorModel](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-getting-started.html) | arn:\${Partition}:iotevents:\${Region}:\${Account}:detectorModel/\${DetectorModelName} |
| [alarmModel](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-getting-started.html) | arn:\${Partition}:iotevents:\${Region}:\${Account}:alarmModel/\${AlarmModelName} |
| [input](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-getting-started.html) | arn:\${Partition}:iotevents:\${Region}:\${Account}:input/\${InputName} |
# AWS IoT
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html
| Service | ARN |
|---------|-----|
| [client](https://docs.aws.amazon.com/iot/latest/developerguide/iot-message-broker.html) | arn:\${Partition}:iot:\${Region}:\${Account}:client/\${ClientId} |
| [index](https://docs.aws.amazon.com/iot/latest/developerguide/iot-indexing.html) | arn:\${Partition}:iot:\${Region}:\${Account}:index/\${IndexName} |
| [fleetmetric](https://docs.aws.amazon.com/iot/latest/developerguide/iot-indexing.html) | arn:\${Partition}:iot:\${Region}:\${Account}:fleetmetric/\${FleetMetricName} |
| [job](https://docs.aws.amazon.com/iot/latest/developerguide/iot-jobs.html) | arn:\${Partition}:iot:\${Region}:\${Account}:job/\${JobId} |
| [jobtemplate](https://docs.aws.amazon.com/iot/latest/developerguide/job-templates.html) | arn:\${Partition}:iot:\${Region}:\${Account}:jobtemplate/\${JobTemplateId} |
| [tunnel](https://docs.aws.amazon.com/iot/latest/developerguide/iot-tunnels.html) | arn:\${Partition}:iot:\${Region}:\${Account}:tunnel/\${TunnelId} |
| [thing](https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html) | arn:\${Partition}:iot:\${Region}:\${Account}:thing/\${ThingName} |
| [thinggroup](https://docs.aws.amazon.com/iot/latest/developerguide/thing-groups.html) | arn:\${Partition}:iot:\${Region}:\${Account}:thinggroup/\${ThingGroupName} |
| [billinggroup](https://docs.aws.amazon.com/iot/latest/developerguide/billing-groups.html) | arn:\${Partition}:iot:\${Region}:\${Account}:billinggroup/\${BillingGroupName} |
| [dynamicthinggroup](https://docs.aws.amazon.com/iot/latest/developerguide/dynamic-thing-groups.html) | arn:\${Partition}:iot:\${Region}:\${Account}:thinggroup/\${ThingGroupName} |
| [thingtype](https://docs.aws.amazon.com/iot/latest/developerguide/thing-types.html) | arn:\${Partition}:iot:\${Region}:\${Account}:thingtype/\${ThingTypeName} |
| [topic](https://docs.aws.amazon.com/iot/latest/developerguide/iot-message-broker.html) | arn:\${Partition}:iot:\${Region}:\${Account}:topic/\${TopicName} |
| [topicfilter](https://docs.aws.amazon.com/iot/latest/developerguide/topics.html) | arn:\${Partition}:iot:\${Region}:\${Account}:topicfilter/\${TopicFilter} |
| [rolealias](https://docs.aws.amazon.com/iot/latest/developerguide/authorizing-direct-aws.html) | arn:\${Partition}:iot:\${Region}:\${Account}:rolealias/\${RoleAlias} |
| [authorizer](https://docs.aws.amazon.com/iot/latest/developerguide/custom-authorizer.html) | arn:\${Partition}:iot:\${Region}:\${Account}:authorizer/\${AuthorizerName} |
| [policy](https://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html) | arn:\${Partition}:iot:\${Region}:\${Account}:policy/\${PolicyName} |
| [cert](https://docs.aws.amazon.com/iot/latest/developerguide/x509-certs.html) | arn:\${Partition}:iot:\${Region}:\${Account}:cert/\${Certificate} |
| [cacert](https://docs.aws.amazon.com/iot/latest/developerguide/x509-certs.html) | arn:\${Partition}:iot:\${Region}:\${Account}:cacert/\${CACertificate} |
| [stream](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-ota-dev.html) | arn:\${Partition}:iot:\${Region}:\${Account}:stream/\${StreamId} |
| [otaupdate](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-ota-dev.html) | arn:\${Partition}:iot:\${Region}:\${Account}:otaupdate/\${OtaUpdateId} |
| [scheduledaudit](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-audit.html) | arn:\${Partition}:iot:\${Region}:\${Account}:scheduledaudit/\${ScheduleName} |
| [mitigationaction](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-mitigation-actions.html) | arn:\${Partition}:iot:\${Region}:\${Account}:mitigationaction/\${MitigationActionName} |
| [securityprofile](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-detect.html) | arn:\${Partition}:iot:\${Region}:\${Account}:securityprofile/\${SecurityProfileName} |
| [custommetric](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-detect.html) | arn:\${Partition}:iot:\${Region}:\${Account}:custommetric/\${MetricName} |
| [dimension](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-detect.html) | arn:\${Partition}:iot:\${Region}:\${Account}:dimension/\${DimensionName} |
| [rule](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html) | arn:\${Partition}:iot:\${Region}:\${Account}:rule/\${RuleName} |
| [destination](https://docs.aws.amazon.com/iot/latest/developerguide/rule-destination.html) | arn:\${Partition}:iot:\${Region}:\${Account}:destination/\${DestinationType}/\${Uuid} |
| [provisioningtemplate](https://docs.aws.amazon.com/iot/latest/developerguide/provision-template.html) | arn:\${Partition}:iot:\${Region}:\${Account}:provisioningtemplate/\${ProvisioningTemplate} |
| [domainconfiguration](https://docs.aws.amazon.com/iot/latest/developerguide/domain-configuration.html) | arn:\${Partition}:iot:\${Region}:\${Account}:domainconfiguration/\${DomainConfigurationName}/\${Id} |
| [package](https://docs.aws.amazon.com/iot/latest/developerguide/software-package-catalog.html) | arn:\${Partition}:iot:\${Region}:\${Account}:package/\${PackageName} |
| [packageversion](https://docs.aws.amazon.com/iot/latest/developerguide/software-package-catalog.html) | arn:\${Partition}:iot:\${Region}:\${Account}:package/\${PackageName}/version/\${VersionName} |
| [certificateprovider](https://docs.aws.amazon.com/iot/latest/developerguide/provisioning-cert-provider.html) | arn:\${Partition}:iot:\${Region}:\${Account}:certificateprovider/\${CertificateProviderName} |
# AWS IoT Analytics
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotanalytics.html
| Service | ARN |
|---------|-----|
| [channel](https://docs.aws.amazon.com/iotanalytics/latest/userguide/welcome.html#aws-iot-analytics-how) | arn:\${Partition}:iotanalytics:\${Region}:\${Account}:channel/\${ChannelName} |
| [dataset](https://docs.aws.amazon.com/iotanalytics/latest/userguide/welcome.html#aws-iot-analytics-how) | arn:\${Partition}:iotanalytics:\${Region}:\${Account}:dataset/\${DatasetName} |
| [datastore](https://docs.aws.amazon.com/iotanalytics/latest/userguide/welcome.html#aws-iot-analytics-how) | arn:\${Partition}:iotanalytics:\${Region}:\${Account}:datastore/\${DatastoreName} |
| [pipeline](https://docs.aws.amazon.com/iotanalytics/latest/userguide/welcome.html#aws-iot-analytics-how) | arn:\${Partition}:iotanalytics:\${Region}:\${Account}:pipeline/\${PipelineName} |
# AWS IoT RoboRunner
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotroborunner.html
| Service | ARN |
|---------|-----|
| [DestinationResource](https://docs.aws.amazon.com/iotroborunner/latest/api/) | arn:\${Partition}:iotroborunner:\${Region}:\${Account}:site/\${SiteId}/destination/\${DestinationId} |
| [SiteResource](https://docs.aws.amazon.com/iotroborunner/latest/api/) | arn:\${Partition}:iotroborunner:\${Region}:\${Account}:site/\${SiteId} |
| [WorkerFleetResource](https://docs.aws.amazon.com/iotroborunner/latest/api/) | arn:\${Partition}:iotroborunner:\${Region}:\${Account}:site/\${SiteId}/worker-fleet/\${WorkerFleetId} |
| [WorkerResource](https://docs.aws.amazon.com/iotroborunner/latest/api/) | arn:\${Partition}:iotroborunner:\${Region}:\${Account}:site/\${SiteId}/worker-fleet/\${WorkerFleetId}/worker/\${WorkerId} |
# AWS IQ Permissions
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiqpermissions.html
| Service | ARN |
|---------|-----|
| [permission](https://aws.amazon.com/iq/) | arn:\${Partition}:iq-permission:\${Region}::permission/\${PermissionRequestId} |
# AWS IoT TwinMaker
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiottwinmaker.html
| Service | ARN |
|---------|-----|
| [workspace](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CreateWorkspace.html) | arn:\${Partition}:iottwinmaker:\${Region}:\${Account}:workspace/\${WorkspaceId} |
| [entity](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CreateEntity.html) | arn:\${Partition}:iottwinmaker:\${Region}:\${Account}:workspace/\${WorkspaceId}/entity/\${EntityId} |
| [componentType](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CreateComponentType.html) | arn:\${Partition}:iottwinmaker:\${Region}:\${Account}:workspace/\${WorkspaceId}/component-type/\${ComponentTypeId} |
| [scene](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CreateScene.html) | arn:\${Partition}:iottwinmaker:\${Region}:\${Account}:workspace/\${WorkspaceId}/scene/\${SceneId} |
| [syncJob](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CreateSyncJob.html) | arn:\${Partition}:iottwinmaker:\${Region}:\${Account}:workspace/\${WorkspaceId}/sync-job/\${SyncJobId} |
| [metadataTransferJob](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CreateMetadataTransferJob.html) | arn:\${Partition}:iottwinmaker:\${Region}:\${Account}:metadata-transfer-job/\${MetadataTransferJobId} |
# AWS IoT Greengrass
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotgreengrass.html
| Service | ARN |
|---------|-----|
| [connectivityInfo](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-connectivityinfo.html) | arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/things/\${ThingName}/connectivityInfo |
| [certificateAuthority](https://docs.aws.amazon.com/greengrass/latest/developerguide/gg-sec.html) | arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/groups/\${GroupId}/certificateauthorities/\${CertificateAuthorityId} |
| [deployment](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-createdeploymentrequest.html) | arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/groups/\${GroupId}/deployments/\${DeploymentId} |
| [bulkDeployment](https://docs.aws.amazon.com/greengrass/latest/developerguide/bulk-deploy-cli.html) | arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/bulk/deployments/\${BulkDeploymentId} |
| [group](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-groupinformation.html) | arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/groups/\${GroupId} |
| [groupVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-groupversion.html) | arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/groups/\${GroupId}/versions/\${VersionId} |
| [coreDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-core.html) | arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/cores/\${CoreDefinitionId} |
| [coreDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-coredefinitionversion.html) | arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/cores/\${CoreDefinitionId}/versions/\${VersionId} |
| [deviceDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-device.html) | arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/devices/\${DeviceDefinitionId} |
| [deviceDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-devicedefinitionversion.html) | arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/devices/\${DeviceDefinitionId}/versions/\${VersionId} |
| [functionDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-function.html) | arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/functions/\${FunctionDefinitionId} |
| [functionDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-functiondefinitionversion.html) | arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/functions/\${FunctionDefinitionId}/versions/\${VersionId} |
| [subscriptionDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-subscription.html) | arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/subscriptions/\${SubscriptionDefinitionId} |
| [subscriptionDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-subscriptiondefinitionversion.html) | arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/subscriptions/\${SubscriptionDefinitionId}/versions/\${VersionId} |
| [loggerDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-logger.html) | arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/loggers/\${LoggerDefinitionId} |
| [loggerDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-loggerdefinitionversion.html) | arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/loggers/\${LoggerDefinitionId}/versions/\${VersionId} |
| [resourceDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-resource.html) | arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/resources/\${ResourceDefinitionId} |
| [resourceDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-resourcedefinitionversion.html) | arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/resources/\${ResourceDefinitionId}/versions/\${VersionId} |
| [connectorDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-connector.html) | arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/connectors/\${ConnectorDefinitionId} |
| [connectorDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-connectordefinitionversion.html) | arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/definition/connectors/\${ConnectorDefinitionId}/versions/\${VersionId} |
| [thing](https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html) | arn:\${Partition}:iot:\${Region}:\${Account}:thing/\${ThingName} |
| [thingRuntimeConfig](https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html) | arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/things/\${ThingName}/runtimeconfig |
# AWS IoT Jobs DataPlane
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotjobsdataplane.html
| Service | ARN |
|---------|-----|
| [thing](https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html) | arn:\${Partition}:iot:\${Region}:\${Account}:thing/\${ThingName} |
# AWS IoT FleetWise
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotfleetwise.html
| Service | ARN |
|---------|-----|
| [campaign](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/campaigns.html) | arn:\${Partition}:iotfleetwise:\${Region}:\${Account}:campaign/\${CampaignName} |
| [decodermanifest](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/decoder-manifests.html) | arn:\${Partition}:iotfleetwise:\${Region}:\${Account}:decoder-manifest/\${Name} |
| [fleet](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleets.html) | arn:\${Partition}:iotfleetwise:\${Region}:\${Account}:fleet/\${FleetId} |
| [modelmanifest](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/vehicle-models.html) | arn:\${Partition}:iotfleetwise:\${Region}:\${Account}:model-manifest/\${Name} |
| [signalcatalog](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/signal-catalogs.html) | arn:\${Partition}:iotfleetwise:\${Region}:\${Account}:signal-catalog/\${Name} |
| [vehicle](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/vehicles.html) | arn:\${Partition}:iotfleetwise:\${Region}:\${Account}:vehicle/\${VehicleId} |
# AWS IoT SiteWise
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotsitewise.html
| Service | ARN |
|---------|-----|
| [asset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAsset.html) | arn:\${Partition}:iotsitewise:\${Region}:\${Account}:asset/\${AssetId} |
| [asset-model](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModel.html) | arn:\${Partition}:iotsitewise:\${Region}:\${Account}:asset-model/\${AssetModelId} |
| [time-series](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeTimeSeries.html) | arn:\${Partition}:iotsitewise:\${Region}:\${Account}:time-series/\${TimeSeriesId} |
| [gateway](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateGateway.html) | arn:\${Partition}:iotsitewise:\${Region}:\${Account}:gateway/\${GatewayId} |
| [portal](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreatePortal.html) | arn:\${Partition}:iotsitewise:\${Region}:\${Account}:portal/\${PortalId} |
| [project](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateProject.html) | arn:\${Partition}:iotsitewise:\${Region}:\${Account}:project/\${ProjectId} |
| [dashboard](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateDashboard.html) | arn:\${Partition}:iotsitewise:\${Region}:\${Account}:dashboard/\${DashboardId} |
| [access-policy](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAccessPolicy.html) | arn:\${Partition}:iotsitewise:\${Region}:\${Account}:access-policy/\${AccessPolicyId} |
# AWS IoT Wireless
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotwireless.html
| Service | ARN |
|---------|-----|
| [WirelessDevice](https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_CreateWirelessDevice.html) | arn:\${Partition}:iotwireless:\${Region}:\${Account}:WirelessDevice/\${WirelessDeviceId} |
| [WirelessGateway](https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_CreateWirelessGateway.html) | arn:\${Partition}:iotwireless:\${Region}:\${Account}:WirelessGateway/\${WirelessGatewayId} |
| [DeviceProfile](https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_CreateDeviceProfile.html) | arn:\${Partition}:iotwireless:\${Region}:\${Account}:DeviceProfile/\${DeviceProfileId} |
| [ServiceProfile](https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_CreateServiceProfile.html) | arn:\${Partition}:iotwireless:\${Region}:\${Account}:ServiceProfile/\${ServiceProfileId} |
| [Destination](https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_CreateDestination.html) | arn:\${Partition}:iotwireless:\${Region}:\${Account}:Destination/\${DestinationName} |
| [SidewalkAccount](https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_AssociateAwsAccountWithPartnerAccount.html) | arn:\${Partition}:iotwireless:\${Region}:\${Account}:SidewalkAccount/\${SidewalkAccountId} |
| [WirelessGatewayTaskDefinition](https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_CreateWirelessGatewayTaskDefinition.html) | arn:\${Partition}:iotwireless:\${Region}:\${Account}:WirelessGatewayTaskDefinition/\${WirelessGatewayTaskDefinitionId} |
| [FuotaTask](https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_CreateFuotaTask.html) | arn:\${Partition}:iotwireless:\${Region}:\${Account}:FuotaTask/\${FuotaTaskId} |
| [MulticastGroup](https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_CreateMulticastGroup.html) | arn:\${Partition}:iotwireless:\${Region}:\${Account}:MulticastGroup/\${MulticastGroupId} |
| [NetworkAnalyzerConfiguration](https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_CreateNetworkAnalyzerConfiguration.html) | arn:\${Partition}:iotwireless:\${Region}:\${Account}:NetworkAnalyzerConfiguration/\${NetworkAnalyzerConfigurationName} |
| [thing](https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html) | arn:\${Partition}:iot:\${Region}:\${Account}:thing/\${ThingName} |
| [cert](https://docs.aws.amazon.com/iot/latest/developerguide/x509-client-certs.html) | arn:\${Partition}:iot:\${Region}:\${Account}:cert/\${Certificate} |
| [ImportTask](https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_StartWirelessDeviceImportTask.html) | arn:\${Partition}:iotwireless:\${Region}:\${Account}:ImportTask/\${ImportTaskId} |
# AWS IoT Greengrass V2
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotgreengrassv2.html
| Service | ARN |
|---------|-----|
| [connectivityInfo](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ConnectivityInfo.html) | arn:\${Partition}:greengrass:\${Region}:\${Account}:/greengrass/things/\${ThingName}/connectivityInfo |
| [component](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_Component.html) | arn:\${Partition}:greengrass:\${Region}:\${Account}:components:\${ComponentName} |
| [componentVersion](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_Component.html) | arn:\${Partition}:greengrass:\${Region}:\${Account}:components:\${ComponentName}:versions:\${ComponentVersion} |
| [coreDevice](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_CoreDevice.html) | arn:\${Partition}:greengrass:\${Region}:\${Account}:coreDevices:\${CoreDeviceThingName} |
| [deployment](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_Deployment.html) | arn:\${Partition}:greengrass:\${Region}:\${Account}:deployments:\${DeploymentId} |
# AWS IQ
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiq.html
| Service | ARN |
|---------|-----|
| [conversation](https://aws.amazon.com/iq/) | arn:\${Partition}:iq:\${Region}::conversation/\${ConversationId} |
| [buyer](https://aws.amazon.com/iq/) | arn:\${Partition}:iq:\${Region}::buyer/\${BuyerId} |
| [expert](https://aws.amazon.com/iq/) | arn:\${Partition}:iq:\${Region}::expert/\${ExpertId} |
| [call](https://aws.amazon.com/iq/) | arn:\${Partition}:iq:\${Region}::call/\${CallId} |
| [token](https://aws.amazon.com/iq/) | arn:\${Partition}:iq:\${Region}::token/\${TokenId} |
| [proposal](https://aws.amazon.com/iq/) | arn:\${Partition}:iq:\${Region}::proposal/\${ConversationId}/\${ProposalId} |
| [paymentRequest](https://aws.amazon.com/iq/) | arn:\${Partition}:iq:\${Region}::paymentRequest/\${ConversationId}/\${ProposalId}/\${PaymentRequestId} |
| [paymentSchedule](https://aws.amazon.com/iq/) | arn:\${Partition}:iq:\${Region}::paymentSchedule/\${ConversationId}/\${ProposalId}/\${VersionId} |
| [seller](https://aws.amazon.com/iq/) | arn:\${Partition}:iq:\${Region}::seller/\${SellerAwsAccountId} |
| [company](https://aws.amazon.com/iq/) | arn:\${Partition}:iq:\${Region}::company/\${CompanyId} |
| [request](https://aws.amazon.com/iq/) | arn:\${Partition}:iq:\${Region}::request/\${RequestId} |
| [listing](https://aws.amazon.com/iq/) | arn:\${Partition}:iq:\${Region}::listing/\${ListingId} |
| [attachment](https://aws.amazon.com/iq/) | arn:\${Partition}:iq:\${Region}::attachment/\${AttachmentId} |
| [permission](https://aws.amazon.com/iq/) | arn:\${Partition}:iq-permission:\${Region}::permission/\${PermissionRequestId} |
# Amazon Kendra Intelligent Ranking
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkendraintelligentranking.html
| Service | ARN |
|---------|-----|
| [rescore-execution-plan](https://docs.aws.amazon.com/kendra/latest/dg/search-service-rerank.html) | arn:\${Partition}:kendra-ranking:\${Region}:\${Account}:rescore-execution-plan/\${RescoreExecutionPlanId} |
# Amazon Kendra
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkendra.html
| Service | ARN |
|---------|-----|
| [index](https://docs.aws.amazon.com/kendra/latest/dg/index.html) | arn:\${Partition}:kendra:\${Region}:\${Account}:index/\${IndexId} |
| [data-source](https://docs.aws.amazon.com/kendra/latest/dg/data-source.html) | arn:\${Partition}:kendra:\${Region}:\${Account}:index/\${IndexId}/data-source/\${DataSourceId} |
| [faq](https://docs.aws.amazon.com/kendra/latest/dg/faq.html) | arn:\${Partition}:kendra:\${Region}:\${Account}:index/\${IndexId}/faq/\${FaqId} |
| [experience](https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html) | arn:\${Partition}:kendra:\${Region}:\${Account}:index/\${IndexId}/experience/\${ExperienceId} |
| [thesaurus](https://docs.aws.amazon.com/kendra/latest/dg/thesaurus.html) | arn:\${Partition}:kendra:\${Region}:\${Account}:index/\${IndexId}/thesaurus/\${ThesaurusId} |
| [query-suggestions-block-list](https://docs.aws.amazon.com/kendra/latest/dg/query-suggestions-block-list.html) | arn:\${Partition}:kendra:\${Region}:\${Account}:index/\${IndexId}/query-suggestions-block-list/\${QuerySuggestionsBlockListId} |
| [featured-results-set](https://docs.aws.amazon.com/kendra/latest/dg/featured-results.html) | arn:\${Partition}:kendra:\${Region}:\${Account}:index/\${IndexId}/featured-results-set/\${FeaturedResultsSetId} |
| [access-control-configuration](https://docs.aws.amazon.com/kendra/latest/dg/API_CreateAccessControlConfiguration.html) | arn:\${Partition}:kendra:\${Region}:\${Account}:index/\${IndexId}/access-control-configuration/\${AccessControlConfigurationId} |
# Amazon Kinesis Firehose
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkinesisfirehose.html
| Service | ARN |
|---------|-----|
| [deliverystream](https://docs.aws.amazon.com/firehose/latest/dev/basic-create.html) | arn:\${Partition}:firehose:\${Region}:\${Account}:deliverystream/\${DeliveryStreamName} |
# Amazon Kinesis Analytics V2
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkinesisanalyticsv2.html
| Service | ARN |
|---------|-----|
| [application](https://docs.aws.amazon.com/kinesisanalytics/latest/java/how-it-works.html) | arn:\${Partition}:kinesisanalytics:\${Region}:\${Account}:application/\${ApplicationName} |
# Amazon Kinesis Data Streams
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkinesisdatastreams.html
| Service | ARN |
|---------|-----|
| [stream](https://docs.aws.amazon.com/kinesis/latest/dev/amazon-kinesis-streams.html) | arn:\${Partition}:kinesis:\${Region}:\${Account}:stream/\${StreamName} |
| [consumer](https://docs.aws.amazon.com/kinesis/latest/dev/amazon-kinesis-consumers.html) | arn:\${Partition}:kinesis:\${Region}:\${Account}:\${StreamType}/\${StreamName}/consumer/\${ConsumerName}:\${ConsumerCreationTimpstamp} |
| [kmsKey](https://docs.aws.amazon.com/kinesis/latest/dev/concepts.html#kms_keys) | arn:\${Partition}:kms:\${Region}:\${Account}:key/\${KeyId} |
# Amazon Keyspaces (for Apache Cassandra)
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkeyspacesforapachecassandra.html
| Service | ARN |
|---------|-----|
| [keyspace](https://docs.aws.amazon.com/keyspaces/latest/devguide/what-is.html) | arn:\${Partition}:cassandra:\${Region}:\${Account}:/keyspace/\${KeyspaceName}/ |
| [table](https://docs.aws.amazon.com/keyspaces/latest/devguide/what-is.html) | arn:\${Partition}:cassandra:\${Region}:\${Account}:/keyspace/\${KeyspaceName}/table/\${TableName} |
# Amazon Kinesis Analytics
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkinesisanalytics.html
| Service | ARN |
|---------|-----|
| [application](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works.html) | arn:\${Partition}:kinesisanalytics:\${Region}:\${Account}:application/\${ApplicationName} |
# Amazon Kinesis Video Streams
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkinesisvideostreams.html
| Service | ARN |
|---------|-----|
| [stream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-it-works.html) | arn:\${Partition}:kinesisvideo:\${Region}:\${Account}:stream/\${StreamName}/\${CreationTime} |
| [channel](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-how-it-works.html) | arn:\${Partition}:kinesisvideo:\${Region}:\${Account}:channel/\${ChannelName}/\${CreationTime} |
# AWS Lake Formation
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awslakeformation.html
| Service | ARN |
|---------|-----|
# AWS Key Management Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awskeymanagementservice.html
| Service | ARN |
|---------|-----|
| [alias](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#alias-concept) | arn:\${Partition}:kms:\${Region}:\${Account}:alias/\${Alias} |
| [key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms_keys) | arn:\${Partition}:kms:\${Region}:\${Account}:key/\${KeyId} |
# AWS License Manager Linux Subscriptions Manager
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awslicensemanagerlinuxsubscriptionsmanager.html
| Service | ARN |
|---------|-----|
# AWS Launch Wizard
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awslaunchwizard.html
| Service | ARN |
|---------|-----|
# Amazon Lex
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonlex.html
| Service | ARN |
|---------|-----|
| [bot](https://docs.aws.amazon.com/lex/latest/dg/API_BotMetadata.html) | arn:\${Partition}:lex:\${Region}:\${Account}:bot:\${BotName} |
| [bot version](https://docs.aws.amazon.com/lex/latest/dg/API_BotMetadata.html) | arn:\${Partition}:lex:\${Region}:\${Account}:bot:\${BotName}:\${BotVersion} |
| [bot alias](https://docs.aws.amazon.com/lex/latest/dg/API_BotAliasMetadata.html) | arn:\${Partition}:lex:\${Region}:\${Account}:bot:\${BotName}:\${BotAlias} |
| [channel](https://docs.aws.amazon.com/lex/latest/dg/API_BotChannelAssociation.html) | arn:\${Partition}:lex:\${Region}:\${Account}:bot-channel:\${BotName}:\${BotAlias}:\${ChannelName} |
| [intent version](https://docs.aws.amazon.com/lex/latest/dg/API_Intent.html) | arn:\${Partition}:lex:\${Region}:\${Account}:intent:\${IntentName}:\${IntentVersion} |
| [slottype version](https://docs.aws.amazon.com/lex/latest/dg/API_SlotTypeMetadata.html) | arn:\${Partition}:lex:\${Region}:\${Account}:slottype:\${SlotName}:\${SlotVersion} |
# AWS License Manager
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awslicensemanager.html
| Service | ARN |
|---------|-----|
| [license-configuration](https://docs.aws.amazon.com/license-manager/latest/userguide/license-configurations.html) | arn:\${Partition}:license-manager:\${Region}:\${Account}:license-configuration:\${LicenseConfigurationId} |
| [license](https://docs.aws.amazon.com/license-manager/latest/userguide/seller-issued-licenses.html) | arn:\${Partition}:license-manager::\${Account}:license:\${LicenseId} |
| [grant](https://docs.aws.amazon.com/license-manager/latest/userguide/granted-licenses.html) | arn:\${Partition}:license-manager::\${Account}:grant:\${GrantId} |
| [report-generator](https://docs.aws.amazon.com/license-manager/latest/userguide/report-generators.html) | arn:\${Partition}:license-manager:\${Region}:\${Account}:report-generator:\${ReportGeneratorId} |
# Amazon EC2
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html
| Service | ARN |
|---------|-----|
| [elastic-ip](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:elastic-ip/\${AllocationId} |
| [capacity-reservation-fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format) | arn:\${Partition}:ec2:\${Region}:\${Account}:capacity-reservation-fleet/\${CapacityReservationFleetId} |
| [capacity-reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:capacity-reservation/\${CapacityReservationId} |
| [carrier-gateway](https://docs.aws.amazon.com/vpc/latest/userguide/Carrier_Gateway.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:carrier-gateway/\${CarrierGatewayId} |
| [certificate](https://docs.aws.amazon.com/acm/latest/userguide/authen-overview.html#acm-resources-operations) | arn:\${Partition}:acm:\${Region}:\${Account}:certificate/\${CertificateId} |
| [client-vpn-endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:client-vpn-endpoint/\${ClientVpnEndpointId} |
| [customer-gateway](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:customer-gateway/\${CustomerGatewayId} |
| [dedicated-host](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-overview.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:dedicated-host/\${DedicatedHostId} |
| [dhcp-options](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:dhcp-options/\${DhcpOptionsId} |
| [egress-only-internet-gateway](https://docs.aws.amazon.com/vpc/latest/userguide/egress-only-internet-gateway.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:egress-only-internet-gateway/\${EgressOnlyInternetGatewayId} |
| [elastic-gpu](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/elastic-gpus.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:elastic-gpu/\${ElasticGpuId} |
| [elastic-inference](https://docs.aws.amazon.com/elastic-inference/latest/developerguide/what-is-ei.html) | arn:\${Partition}:elastic-inference:\${Region}:\${Account}:elastic-inference-accelerator/\${AcceleratorId} |
| [export-image-task](https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-image-import.html#export-vm-image) | arn:\${Partition}:ec2:\${Region}:\${Account}:export-image-task/\${ExportImageTaskId} |
| [export-instance-task](https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:export-instance-task/\${ExportTaskId} |
| [fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:fleet/\${FleetId} |
| [fpga-image](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format) | arn:\${Partition}:ec2:\${Region}:\${Account}:fpga-image/\${FpgaImageId} |
| [host-reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format) | arn:\${Partition}:ec2:\${Region}:\${Account}:host-reservation/\${HostReservationId} |
| [image](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) | arn:\${Partition}:ec2:\${Region}::image/\${ImageId} |
| [import-image-task](https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-image-import.html#import-vm-image) | arn:\${Partition}:ec2:\${Region}:\${Account}:import-image-task/\${ImportImageTaskId} |
| [import-snapshot-task](https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-import-snapshot.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:import-snapshot-task/\${ImportSnapshotTaskId} |
| [instance-connect-endpoint](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format) | arn:\${Partition}:ec2:\${Region}:\${Account}:instance-connect-endpoint/\${InstanceConnectEndpointId} |
| [instance-event-window](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format) | arn:\${Partition}:ec2:\${Region}:\${Account}:instance-event-window/\${InstanceEventWindowId} |
| [instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Instances.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:instance/\${InstanceId} |
| [internet-gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:internet-gateway/\${InternetGatewayId} |
| [ipam](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format) | arn:\${Partition}:ec2::\${Account}:ipam/\${IpamId} |
| [ipam-pool](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format) | arn:\${Partition}:ec2::\${Account}:ipam-pool/\${IpamPoolId} |
| [ipam-resource-discovery-association](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format) | arn:\${Partition}:ec2::\${Account}:ipam-resource-discovery-association/\${IpamResourceDiscoveryAssociationId} |
| [ipam-resource-discovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format) | arn:\${Partition}:ec2::\${Account}:ipam-resource-discovery/\${IpamResourceDiscoveryId} |
| [ipam-scope](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format) | arn:\${Partition}:ec2::\${Account}:ipam-scope/\${IpamScopeId} |
| [coip-pool](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format) | arn:\${Partition}:ec2:\${Region}:\${Account}:coip-pool/\${Ipv4PoolCoipId} |
| [ipv4pool-ec2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#ip-addressing-eips) | arn:\${Partition}:ec2:\${Region}:\${Account}:ipv4pool-ec2/\${Ipv4PoolEc2Id} |
| [ipv6pool-ec2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#ipv6-addressing) | arn:\${Partition}:ec2:\${Region}:\${Account}:ipv6pool-ec2/\${Ipv6PoolEc2Id} |
| [key-pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:key-pair/\${KeyPairName} |
| [launch-template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:launch-template/\${LaunchTemplateId} |
| [license-configuration](https://docs.aws.amazon.com/license-manager/latest/userguide/create-license-configuration.html) | arn:\${Partition}:license-manager:\${Region}:\${Account}:license-configuration:\${LicenseConfigurationId} |
| [local-gateway](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html#lgw) | arn:\${Partition}:ec2:\${Region}:\${Account}:local-gateway/\${LocalGatewayId} |
| [local-gateway-route-table-virtual-interface-group-association](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:local-gateway-route-table-virtual-interface-group-association/\${LocalGatewayRouteTableVirtualInterfaceGroupAssociationId} |
| [local-gateway-route-table-vpc-association](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html#vpc-associations) | arn:\${Partition}:ec2:\${Region}:\${Account}:local-gateway-route-table-vpc-association/\${LocalGatewayRouteTableVpcAssociationId} |
| [local-gateway-route-table](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html#route-tables) | arn:\${Partition}:ec2:\${Region}:\${Account}:local-gateway-route-table/\${LocalGatewayRoutetableId} |
| [local-gateway-virtual-interface-group](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:local-gateway-virtual-interface-group/\${LocalGatewayVirtualInterfaceGroupId} |
| [local-gateway-virtual-interface](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:local-gateway-virtual-interface/\${LocalGatewayVirtualInterfaceId} |
| [natgateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:natgateway/\${NatGatewayId} |
| [network-acl](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:network-acl/\${NaclId} |
| [network-insights-access-scope-analysis](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format) | arn:\${Partition}:ec2:\${Region}:\${Account}:network-insights-access-scope-analysis/\${NetworkInsightsAccessScopeAnalysisId} |
| [network-insights-access-scope](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format) | arn:\${Partition}:ec2:\${Region}:\${Account}:network-insights-access-scope/\${NetworkInsightsAccessScopeId} |
| [network-insights-analysis](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format) | arn:\${Partition}:ec2:\${Region}:\${Account}:network-insights-analysis/\${NetworkInsightsAnalysisId} |
| [network-insights-path](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format) | arn:\${Partition}:ec2:\${Region}:\${Account}:network-insights-path/\${NetworkInsightsPathId} |
| [network-interface](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:network-interface/\${NetworkInterfaceId} |
| [placement-group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:placement-group/\${PlacementGroupName} |
| [prefix-list](https://docs.aws.amazon.com/vpc/latest/userguide/managed-prefix-lists.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:prefix-list/\${PrefixListId} |
| [replace-root-volume-task](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/replace-root.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:replace-root-volume-task/\${ReplaceRootVolumeTaskId} |
| [reserved-instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:reserved-instances/\${ReservationId} |
| [group](https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html) | arn:\${Partition}:resource-groups:\${Region}:\${Account}:group/\${GroupName} |
| [role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) | arn:\${Partition}:iam::\${Account}:role/\${RoleNameWithPath} |
| [route-table](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:route-table/\${RouteTableId} |
| [security-group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:security-group/\${SecurityGroupId} |
| [security-group-rule](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format) | arn:\${Partition}:ec2:\${Region}:\${Account}:security-group-rule/\${SecurityGroupRuleId} |
| [snapshot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html) | arn:\${Partition}:ec2:\${Region}::snapshot/\${SnapshotId} |
| [spot-fleet-request](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format) | arn:\${Partition}:ec2:\${Region}:\${Account}:spot-fleet-request/\${SpotFleetRequestId} |
| [spot-instances-request](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:spot-instances-request/\${SpotInstanceRequestId} |
| [subnet-cidr-reservation](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-cidr-reservation.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:subnet-cidr-reservation/\${SubnetCidrReservationId} |
| [subnet](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:subnet/\${SubnetId} |
| [traffic-mirror-filter](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-filter.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:traffic-mirror-filter/\${TrafficMirrorFilterId} |
| [traffic-mirror-filter-rule](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-filter.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:traffic-mirror-filter-rule/\${TrafficMirrorFilterRuleId} |
| [traffic-mirror-session](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-session.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:traffic-mirror-session/\${TrafficMirrorSessionId} |
| [traffic-mirror-target](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-target.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:traffic-mirror-target/\${TrafficMirrorTargetId} |
| [transit-gateway-attachment](https://docs.aws.amazon.com/vpc/latest/tgw/how-transit-gateways-work.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:transit-gateway-attachment/\${TransitGatewayAttachmentId} |
| [transit-gateway-connect-peer](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format) | arn:\${Partition}:ec2:\${Region}:\${Account}:transit-gateway-connect-peer/\${TransitGatewayConnectPeerId} |
| [transit-gateway](https://docs.aws.amazon.com/vpc/latest/tgw/how-transit-gateways-work.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:transit-gateway/\${TransitGatewayId} |
| [transit-gateway-multicast-domain](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-multicast-overview.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:transit-gateway-multicast-domain/\${TransitGatewayMulticastDomainId} |
| [transit-gateway-policy-table](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format) | arn:\${Partition}:ec2:\${Region}:\${Account}:transit-gateway-policy-table/\${TransitGatewayPolicyTableId} |
| [transit-gateway-route-table-announcement](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format) | arn:\${Partition}:ec2:\${Region}:\${Account}:transit-gateway-route-table-announcement/\${TransitGatewayRouteTableAnnouncementId} |
| [transit-gateway-route-table](https://docs.aws.amazon.com/vpc/latest/tgw/how-transit-gateways-work.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:transit-gateway-route-table/\${TransitGatewayRouteTableId} |
| [verified-access-endpoint](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format) | arn:\${Partition}:ec2:\${Region}:\${Account}:verified-access-endpoint/\${VerifiedAccessEndpointId} |
| [verified-access-group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format) | arn:\${Partition}:ec2:\${Region}:\${Account}:verified-access-group/\${VerifiedAccessGroupId} |
| [verified-access-instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format) | arn:\${Partition}:ec2:\${Region}:\${Account}:verified-access-instance/\${VerifiedAccessInstanceId} |
| [verified-access-policy](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format) | arn:\${Partition}:ec2:\${Region}:\${Account}:verified-access-policy/\${VerifiedAccessPolicyId} |
| [verified-access-trust-provider](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format) | arn:\${Partition}:ec2:\${Region}:\${Account}:verified-access-trust-provider/\${VerifiedAccessTrustProviderId} |
| [volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volumes.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:volume/\${VolumeId} |
| [vpc-endpoint-connection](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-services-overview.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:vpc-endpoint-connection/\${VpcEndpointConnectionId} |
| [vpc-endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-services-overview.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:vpc-endpoint/\${VpcEndpointId} |
| [vpc-endpoint-service](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-services-overview.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:vpc-endpoint-service/\${VpcEndpointServiceId} |
| [vpc-endpoint-service-permission](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html#vpc-endpoint-policies) | arn:\${Partition}:ec2:\${Region}:\${Account}:vpc-endpoint-service-permission/\${VpcEndpointServicePermissionId} |
| [vpc-flow-log](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:vpc-flow-log/\${VpcFlowLogId} |
| [vpc](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:vpc/\${VpcId} |
| [vpc-peering-connection](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:vpc-peering-connection/\${VpcPeeringConnectionId} |
| [vpn-connection-device-type](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:vpn-connection-device-type/\${VpnConnectionDeviceTypeId} |
| [vpn-connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:vpn-connection/\${VpnConnectionId} |
| [vpn-gateway](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:vpn-gateway/\${VpnGatewayId} |
# AWS License Manager User Subscriptions
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awslicensemanagerusersubscriptions.html
| Service | ARN |
|---------|-----|
# AWS Lambda
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awslambda.html
| Service | ARN |
|---------|-----|
| [code signing config](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html) | arn:\${Partition}:lambda:\${Region}:\${Account}:code-signing-config:\${CodeSigningConfigId} |
| [eventSourceMapping](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html) | arn:\${Partition}:lambda:\${Region}:\${Account}:event-source-mapping:\${UUID} |
| [function](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html) | arn:\${Partition}:lambda:\${Region}:\${Account}:function:\${FunctionName} |
| [function alias](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html) | arn:\${Partition}:lambda:\${Region}:\${Account}:function:\${FunctionName}:\${Alias} |
| [function version](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html) | arn:\${Partition}:lambda:\${Region}:\${Account}:function:\${FunctionName}:\${Version} |
| [layer](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html) | arn:\${Partition}:lambda:\${Region}:\${Account}:layer:\${LayerName} |
| [layerVersion](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html) | arn:\${Partition}:lambda:\${Region}:\${Account}:layer:\${LayerName}:\${LayerVersion} |
# Amazon Lookout for Metrics
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonlookoutformetrics.html
| Service | ARN |
|---------|-----|
| [AnomalyDetector](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_AnomalyDetectorSummary.html) | arn:\${Partition}:lookoutmetrics:\${Region}:\${Account}:AnomalyDetector:\${AnomalyDetectorName} |
| [MetricSet](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_MetricSetSummary.html) | arn:\${Partition}:lookoutmetrics:\${Region}:\${Account}:MetricSet/\${AnomalyDetectorName}/\${MetricSetName} |
| [Alert](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_AlertSummary.html) | arn:\${Partition}:lookoutmetrics:\${Region}:\${Account}:Alert:\${AlertName} |
# Amazon Machine Learning
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmachinelearning.html
| Service | ARN |
|---------|-----|
| [batchprediction](https://docs.aws.amazon.com/machine-learning/latest/dg/amazon-machine-learning-key-concepts.html#batch-predictions) | arn:\${Partition}:machinelearning:\${Region}:\${Account}:batchprediction/\${BatchPredictionId} |
| [datasource](https://docs.aws.amazon.com/machine-learning/latest/dg/amazon-machine-learning-key-concepts.html#datasources) | arn:\${Partition}:machinelearning:\${Region}:\${Account}:datasource/\${DatasourceId} |
| [evaluation](https://docs.aws.amazon.com/machine-learning/latest/dg/amazon-machine-learning-key-concepts.html#evaluations) | arn:\${Partition}:machinelearning:\${Region}:\${Account}:evaluation/\${EvaluationId} |
| [mlmodel](https://docs.aws.amazon.com/machine-learning/latest/dg/amazon-machine-learning-key-concepts.html#ml-models) | arn:\${Partition}:machinelearning:\${Region}:\${Account}:mlmodel/\${MlModelId} |
# Amazon Location
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonlocation.html
| Service | ARN |
|---------|-----|
| [api-key](https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html) | arn:\${Partition}:geo:\${Region}:\${Account}:api-key/\${KeyName} |
| [geofence-collection](https://docs.aws.amazon.com/location/latest/developerguide/geofence-tracker-concepts.html) | arn:\${Partition}:geo:\${Region}:\${Account}:geofence-collection/\${GeofenceCollectionName} |
| [map](https://docs.aws.amazon.com/location/latest/developerguide/map-concepts.html) | arn:\${Partition}:geo:\${Region}:\${Account}:map/\${MapName} |
| [place-index](https://docs.aws.amazon.com/location/latest/developerguide/places-concepts.html) | arn:\${Partition}:geo:\${Region}:\${Account}:place-index/\${IndexName} |
| [route-calculator](https://docs.aws.amazon.com/location/latest/developerguide/route-concepts.html) | arn:\${Partition}:geo:\${Region}:\${Account}:route-calculator/\${CalculatorName} |
| [tracker](https://docs.aws.amazon.com/location/latest/developerguide/geofence-tracker-concepts.html) | arn:\${Partition}:geo:\${Region}:\${Account}:tracker/\${TrackerName} |
# Amazon Managed Blockchain Query
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmanagedblockchainquery.html
| Service | ARN |
|---------|-----|
# Amazon Lookout for Equipment
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonlookoutforequipment.html
| Service | ARN |
|---------|-----|
| [dataset](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/dataset.html) | arn:\${Partition}:lookoutequipment:\${Region}:\${Account}:dataset/\${DatasetName}/\${DatasetId} |
| [model](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/model.html) | arn:\${Partition}:lookoutequipment:\${Region}:\${Account}:model/\${ModelName}/\${ModelId} |
| [model-version](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/model-version.html) | arn:\${Partition}:lookoutequipment:\${Region}:\${Account}:model/\${ModelName}/\${ModelId}/model-version/\${ModelVersionNumber} |
| [inference-scheduler](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/inference-scheduler.html) | arn:\${Partition}:lookoutequipment:\${Region}:\${Account}:inference-scheduler/\${InferenceSchedulerName}/\${InferenceSchedulerId} |
| [label-group](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/label-group.html) | arn:\${Partition}:lookoutequipment:\${Region}:\${Account}:label-group/\${LabelGroupName}/\${LabelGroupId} |
# Amazon Macie
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmacie.html
| Service | ARN |
|---------|-----|
| [AllowList](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html) | arn:\${Partition}:macie2:\${Region}:\${Account}:allow-list/\${ResourceId} |
| [ClassificationJob](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html) | arn:\${Partition}:macie2:\${Region}:\${Account}:classification-job/\${ResourceId} |
| [CustomDataIdentifier](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html.html) | arn:\${Partition}:macie2:\${Region}:\${Account}:custom-data-identifier/\${ResourceId} |
| [FindingsFilter](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html) | arn:\${Partition}:macie2:\${Region}:\${Account}:findings-filter/\${ResourceId} |
| [Member](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html) | arn:\${Partition}:macie2:\${Region}:\${Account}:member/\${ResourceId} |
# Amazon Lex V2
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonlexv2.html
| Service | ARN |
|---------|-----|
| [bot](https://docs.aws.amazon.com/lexv2/latest/dg/how-it-works.html) | arn:\${Partition}:lex:\${Region}:\${Account}:bot/\${BotId} |
| [bot alias](https://docs.aws.amazon.com/lexv2/latest/dg/how-it-works.html) | arn:\${Partition}:lex:\${Region}:\${Account}:bot-alias/\${BotId}/\${BotAliasId} |
| [test set](https://docs.aws.amazon.com/lexv2/latest/dg/test-workbench.html) | arn:\${Partition}:lex:\${Region}:\${Account}:test-set/\${TestSetId} |
# Amazon Managed Grafana
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmanagedgrafana.html
| Service | ARN |
|---------|-----|
| [workspace](https://docs.aws.amazon.com/grafana/latest/userguide/security-iam.html) | arn:\${Partition}:grafana:\${Region}:\${Account}:/workspaces/\${ResourceId} |
# AWS Mainframe Modernization Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmainframemodernizationservice.html
| Service | ARN |
|---------|-----|
| [Application](https://docs.aws.amazon.com/m2/latest/userguide/concept-m2.html#application-concept) | arn:\${Partition}:m2:\${Region}:\${Account}:app/\${ApplicationId} |
| [Environment](https://docs.aws.amazon.com/m2/latest/userguide/concept-m2.html#environment-concept) | arn:\${Partition}:m2:\${Region}:\${Account}:env/\${EnvironmentId} |
# Amazon Lookout for Vision
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonlookoutforvision.html
| Service | ARN |
|---------|-----|
| [model](https://docs.aws.amazon.com/lookout-for-vision/latest/developer-guide/model-create-project.html) | arn:\${Partition}:lookoutvision:\${Region}:\${Account}:model/\${ProjectName}/\${ModelVersion} |
| [project](https://docs.aws.amazon.com/lookout-for-vision/latest/developer-guide/model-create-project.html) | arn:\${Partition}:lookoutvision:\${Region}:\${Account}:project/\${ProjectName} |
# Amazon Managed Blockchain
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmanagedblockchain.html
| Service | ARN |
|---------|-----|
| [network](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_Network.html) | arn:\${Partition}:managedblockchain:\${Region}::networks/\${NetworkId} |
| [member](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_Member.html) | arn:\${Partition}:managedblockchain:\${Region}:\${Account}:members/\${MemberId} |
| [node](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_Node.html) | arn:\${Partition}:managedblockchain:\${Region}:\${Account}:nodes/\${NodeId} |
| [proposal](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_Proposal.html) | arn:\${Partition}:managedblockchain:\${Region}::proposals/\${ProposalId} |
| [invitation](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_Invitation.html) | arn:\${Partition}:managedblockchain:\${Region}:\${Account}:invitations/\${InvitationId} |
| [accessor](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_Accessor.html) | arn:\${Partition}:managedblockchain:\${Region}:\${Account}:accessors/\${AccessorId} |
# AWS Marketplace
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplace.html
| Service | ARN |
|---------|-----|
# Amazon Managed Streaming for Kafka Connect
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmanagedstreamingforkafkaconnect.html
| Service | ARN |
|---------|-----|
| [connector](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ConnectorSummary.html) | arn:\${Partition}:kafkaconnect:\${Region}:\${Account}:connector/\${ConnectorName}/\${UUID} |
| [custom plugin](https://docs.aws.amazon.com/MSKC/latest/mskc/API_CustomPlugin.html) | arn:\${Partition}:kafkaconnect:\${Region}:\${Account}:custom-plugin/\${CustomPluginName}/\${UUID} |
| [worker configuration](https://docs.aws.amazon.com/MSKC/latest/mskc/API_WorkerConfiguration.html) | arn:\${Partition}:kafkaconnect:\${Region}:\${Account}:worker-configuration/\${WorkerConfigurationName}/\${UUID} |
# Amazon Managed Workflows for Apache Airflow
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmanagedworkflowsforapacheairflow.html
| Service | ARN |
|---------|-----|
| [environment](https://docs.aws.amazon.com/mwaa/latest/userguide/using-mwaa.html) | arn:\${Partition}:airflow:\${Region}:\${Account}:environment/\${EnvironmentName} |
| [rbac-role](https://docs.aws.amazon.com/mwaa/latest/userguide/access-policies.html) | arn:\${Partition}:airflow:\${Region}:\${Account}:role/\${EnvironmentName}/\${RoleName} |
# AWS Marketplace Deployment Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacedeploymentservice.html
| Service | ARN |
|---------|-----|
| [DeploymentParameter](https://docs.aws.amazon.com/marketplace-deployment/latest/api-reference/API_DeploymentParameterInput.html) | arn:\${Partition}:aws-marketplace:\${Region}:\${Account}:DeploymentParameter:catalogs/\${CatalogName}/products/\${ProductId}/\${ResourceId} |
# Amazon Managed Service for Prometheus
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmanagedserviceforprometheus.html
| Service | ARN |
|---------|-----|
| [workspace](https://docs.aws.amazon.com/prometheus/latest/userguide/security-iam.html) | arn:\${Partition}:aps:\${Region}:\${Account}:workspace/\${WorkspaceId} |
| [rulegroupsnamespace](https://docs.aws.amazon.com/prometheus/latest/userguide/security-iam.html) | arn:\${Partition}:aps:\${Region}:\${Account}:rulegroupsnamespace/\${WorkspaceId}/\${Namespace} |
| [scraper](https://docs.aws.amazon.com/prometheus/latest/userguide/security-iam.html) | arn:\${Partition}:aps:\${Region}:\${Account}:scraper/\${ScraperId} |
| [cluster](https://docs.aws.amazon.com/eks/latest/userguide/clusters.html) | arn:\${Partition}:eks:\${Region}:\${Account}:cluster/\${ClusterName} |
# AWS Marketplace Management Portal
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacemanagementportal.html
| Service | ARN |
|---------|-----|
# Amazon Managed Streaming for Apache Kafka
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmanagedstreamingforapachekafka.html
| Service | ARN |
|---------|-----|
| [cluster](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn.html) | arn:\${Partition}:kafka:\${Region}:\${Account}:cluster/\${ClusterName}/\${Uuid} |
| [configuration](https://docs.aws.amazon.com/msk/1.0/apireference/configurations-arn.html) | arn:\${Partition}:kafka:\${Region}:\${Account}:configuration/\${ConfigurationName}/\${Uuid} |
| [vpc-connection](https://docs.aws.amazon.com/msk/1.0/apireference/vpc-connections-arn.html) | arn:\${Partition}:kafka:\${Region}:\${VpcOwnerAccount}:vpc-connection/\${ClusterOwnerAccount}/\${ClusterName}/\${Uuid} |
| [replicator](https://docs.aws.amazon.com/msk/latest/developerguide/v1-replicators.html) | arn:\${Partition}:kafka:\${Region}:\${Account}:replicator/\${ReplicatorName}/\${Uuid} |
| [topic](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#msk-iam-resources) | arn:\${Partition}:kafka:\${Region}:\${Account}:topic/\${ClusterName}/\${ClusterUuid}/\${TopicName} |
| [group](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#msk-iam-resources) | arn:\${Partition}:kafka:\${Region}:\${Account}:group/\${ClusterName}/\${ClusterUuid}/\${GroupName} |
| [transactional-id](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html#msk-iam-resources) | arn:\${Partition}:kafka:\${Region}:\${Account}:transactional-id/\${ClusterName}/\${ClusterUuid}/\${TransactionalId} |
# Amazon Lightsail
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonlightsail.html
| Service | ARN |
|---------|-----|
| [Domain](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_Domain.html) | arn:\${Partition}:lightsail:\${Region}:\${Account}:Domain/\${Id} |
| [Instance](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_Instance.html) | arn:\${Partition}:lightsail:\${Region}:\${Account}:Instance/\${Id} |
| [InstanceSnapshot](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_InstanceSnapshot.html) | arn:\${Partition}:lightsail:\${Region}:\${Account}:InstanceSnapshot/\${Id} |
| [KeyPair](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_KeyPair.html) | arn:\${Partition}:lightsail:\${Region}:\${Account}:KeyPair/\${Id} |
| [StaticIp](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_StaticIp.html) | arn:\${Partition}:lightsail:\${Region}:\${Account}:StaticIp/\${Id} |
| [Disk](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_Disk.html) | arn:\${Partition}:lightsail:\${Region}:\${Account}:Disk/\${Id} |
| [DiskSnapshot](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_DiskSnapshot.html) | arn:\${Partition}:lightsail:\${Region}:\${Account}:DiskSnapshot/\${Id} |
| [LoadBalancer](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_LoadBalancer.html) | arn:\${Partition}:lightsail:\${Region}:\${Account}:LoadBalancer/\${Id} |
| [LoadBalancerTlsCertificate](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_LoadBalancerTlsCertificate.html) | arn:\${Partition}:lightsail:\${Region}:\${Account}:LoadBalancerTlsCertificate/\${Id} |
| [ExportSnapshotRecord](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_ExportSnapshotRecord.html) | arn:\${Partition}:lightsail:\${Region}:\${Account}:ExportSnapshotRecord/\${Id} |
| [CloudFormationStackRecord](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CloudFormationStackRecord.html) | arn:\${Partition}:lightsail:\${Region}:\${Account}:CloudFormationStackRecord/\${Id} |
| [RelationalDatabase](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_RelationalDatabase.html) | arn:\${Partition}:lightsail:\${Region}:\${Account}:RelationalDatabase/\${Id} |
| [RelationalDatabaseSnapshot](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_RelationalDatabaseSnapshot.html) | arn:\${Partition}:lightsail:\${Region}:\${Account}:RelationalDatabaseSnapshot/\${Id} |
| [Alarm](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_Alarm.html) | arn:\${Partition}:lightsail:\${Region}:\${Account}:Alarm/\${Id} |
| [Certificate](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_Certificate.html) | arn:\${Partition}:lightsail:\${Region}:\${Account}:Certificate/\${Id} |
| [ContactMethod](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_ContactMethod.html) | arn:\${Partition}:lightsail:\${Region}:\${Account}:ContactMethod/\${Id} |
| [ContainerService](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_ContainerService.html) | arn:\${Partition}:lightsail:\${Region}:\${Account}:ContainerService/\${Id} |
| [Distribution](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_LightsailDistribution.html) | arn:\${Partition}:lightsail:\${Region}:\${Account}:Distribution/\${Id} |
| [Bucket](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_Bucket.html) | arn:\${Partition}:lightsail:\${Region}:\${Account}:Bucket/\${Id} |
# AWS Marketplace Commerce Analytics Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacecommerceanalyticsservice.html
| Service | ARN |
|---------|-----|
# AWS Marketplace Catalog
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacecatalog.html
| Service | ARN |
|---------|-----|
| [Entity](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeEntity.html#API_DescribeEntity_ResponseSyntax) | arn:\${Partition}:aws-marketplace:\${Region}:\${Account}:\${Catalog}/\${EntityType}/\${ResourceId} |
| [ChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_StartChangeSet.html#API_StartChangeSet_ResponseSyntax) | arn:\${Partition}:aws-marketplace:\${Region}:\${Account}:\${Catalog}/ChangeSet/\${ResourceId} |
# AWS Marketplace Entitlement Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplaceentitlementservice.html
| Service | ARN |
|---------|-----|
# AWS Marketplace Image Building Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplaceimagebuildingservice.html
| Service | ARN |
|---------|-----|
# AWS Marketplace Discovery
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacediscovery.html
| Service | ARN |
|---------|-----|
# AWS Marketplace Private Marketplace
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplaceprivatemarketplace.html
| Service | ARN |
|---------|-----|
# AWS Marketplace Procurement Systems Integration
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplaceprocurementsystemsintegration.html
| Service | ARN |
|---------|-----|
# AWS Marketplace Seller Reporting
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacesellerreporting.html
| Service | ARN |
|---------|-----|
| [SellerDashboard](https://docs.aws.amazon.com/marketplace/latest/userguide/dashboards.html#reports-accessing) | arn:\${Partition}:aws-marketplace::\${Account}:\${Catalog}/ReportingData/\${FactTable}/Dashboard/\${DashboardName} |
# AWS Marketplace Metering Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacemeteringservice.html
| Service | ARN |
|---------|-----|
# AWS Marketplace Vendor Insights
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacevendorinsights.html
| Service | ARN |
|---------|-----|
| [DataSource](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacevendorinsights.html#awsmarketplacevendorinsights-resources-for-iam-policies) | arn:\${Partition}:vendor-insights:::data-source:\${ResourceId} |
| [SecurityProfile](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacevendorinsights.html#awsmarketplacevendorinsights-resources-for-iam-policies) | arn:\${Partition}:vendor-insights:::security-profile:\${ResourceId} |
# AWS Migration Hub
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmigrationhub.html
| Service | ARN |
|---------|-----|
| [progressUpdateStream](https://docs.aws.amazon.com/migrationhub/latest/ug/API_ProgressUpdateStreamSummary.html) | arn:\${Partition}:mgh:\${Region}:\${Account}:progressUpdateStream/\${Stream} |
| [migrationTask](https://docs.aws.amazon.com/migrationhub/latest/ug/API_MigrationTask.html) | arn:\${Partition}:mgh:\${Region}:\${Account}:progressUpdateStream/\${Stream}/migrationTask/\${Task} |
# Amazon Message Delivery Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmessagedeliveryservice.html
| Service | ARN |
|---------|-----|
# Amazon Message Gateway Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmessagegatewayservice.html
| Service | ARN |
|---------|-----|
# AWS Microservice Extractor for .NET
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmicroserviceextractorfor.net.html
| Service | ARN |
|---------|-----|
# Amazon Mechanical Turk
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmechanicalturk.html
| Service | ARN |
|---------|-----|
# AWS Migration Hub Orchestrator
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmigrationhuborchestrator.html
| Service | ARN |
|---------|-----|
| [workflow](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/workflow.html) | arn:\${Partition}:migrationhub-orchestrator:\${Region}:\${Account}:workflow/\${ResourceId} |
| [template](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/templates.html) | arn:\${Partition}:migrationhub-orchestrator:\${Region}:\${Account}:template/\${ResourceId} |
# AWS Migration Acceleration Program Credits
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmigrationaccelerationprogramcredits.html
| Service | ARN |
|---------|-----|
| [agreement](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html) | arn:\${Partition}:mapcredits:::\${Agreement}/\${AgreementId} |
# Amazon MemoryDB
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmemorydb.html
| Service | ARN |
|---------|-----|
| [parametergroup](https://docs.aws.amazon.com/memorydb/latest/devguide/WhatIs.Components.html) | arn:\${Partition}:memorydb:\${Region}:\${Account}:parametergroup/\${ParameterGroupName} |
| [subnetgroup](https://docs.aws.amazon.com/memorydb/latest/devguide/WhatIs.Components.html) | arn:\${Partition}:memorydb:\${Region}:\${Account}:subnetgroup/\${SubnetGroupName} |
| [cluster](https://docs.aws.amazon.com/memorydb/latest/devguide/WhatIs.Components.html) | arn:\${Partition}:memorydb:\${Region}:\${Account}:cluster/\${ClusterName} |
| [snapshot](https://docs.aws.amazon.com/memorydb/latest/devguide/WhatIs.Components.html) | arn:\${Partition}:memorydb:\${Region}:\${Account}:snapshot/\${SnapshotName} |
| [user](https://docs.aws.amazon.com/memorydb/latest/devguide/WhatIs.Components.html) | arn:\${Partition}:memorydb:\${Region}:\${Account}:user/\${UserName} |
| [acl](https://docs.aws.amazon.com/memorydb/latest/devguide/WhatIs.Components.html) | arn:\${Partition}:memorydb:\${Region}:\${Account}:acl/\${AclName} |
| [reservednode](https://docs.aws.amazon.com/memorydb/latest/devguide/WhatIs.Components.html) | arn:\${Partition}:memorydb:\${Region}:\${Account}:reservednode/\${ReservationID} |
# Amazon Mobile Analytics
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmobileanalytics.html
| Service | ARN |
|---------|-----|
# AWS Migration Hub Strategy Recommendations
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmigrationhubstrategyrecommendations.html
| Service | ARN |
|---------|-----|
# AWS Migration Hub Refactor Spaces
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmigrationhubrefactorspaces.html
| Service | ARN |
|---------|-----|
| [environment](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources) | arn:\${Partition}:refactor-spaces:\${Region}:\${Account}:environment/\${EnvironmentId} |
| [application](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources) | arn:\${Partition}:refactor-spaces:\${Region}:\${Account}:environment/\${EnvironmentId}/application/\${ApplicationId} |
| [service](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources) | arn:\${Partition}:refactor-spaces:\${Region}:\${Account}:environment/\${EnvironmentId}/application/\${ApplicationId}/service/\${ServiceId} |
| [route](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources) | arn:\${Partition}:refactor-spaces:\${Region}:\${Account}:environment/\${EnvironmentId}/application/\${ApplicationId}/route/\${RouteId} |
# Amazon Monitron
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmonitron.html
| Service | ARN |
|---------|-----|
| [project](https://docs.aws.amazon.com/Monitron/latest/user-guide/projects-chapter.html) | arn:\${Partition}:monitron:\${Region}:\${Account}:project/\${ResourceId} |
# Amazon MQ
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmq.html
| Service | ARN |
|---------|-----|
| [brokers](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-how-it-works.html) | arn:\${Partition}:mq:\${Region}:\${Account}:broker:\${BrokerName}:\${BrokerId} |
| [configurations](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-how-it-works.html) | arn:\${Partition}:mq:\${Region}:\${Account}:configuration:\${ConfigurationId} |
# Amazon Neptune
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonneptune.html
| Service | ARN |
|---------|-----|
| [database](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-resources.html) | arn:\${Partition}:neptune-db:\${Region}:\${Account}:\${RelativeId}/database |
# AWS Network Manager Chat
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsnetworkmanagerchat.html
| Service | ARN |
|---------|-----|
# Amazon Neptune Analytics
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonneptuneanalytics.html
| Service | ARN |
|---------|-----|
| [graph](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/iam-resources.html#graph) | arn:\${Partition}:neptune-graph:\${Region}:\${Account}:graph/\${ResourceId} |
| [graph-snapshot](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/iam-resources.html#graph-snapshot) | arn:\${Partition}:neptune-graph:\${Region}:\${Account}:graph-snapshot/\${ResourceId} |
| [import-task](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/iam-resources.html#import-task) | arn:\${Partition}:neptune-graph:\${Region}:\${Account}:import-task/\${ResourceId} |
# AWS Network Firewall
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsnetworkfirewall.html
| Service | ARN |
|---------|-----|
| [Firewall](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_Firewall.html) | arn:\${Partition}:network-firewall:\${Region}:\${Account}:firewall/\${Name} |
| [FirewallPolicy](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_FirewallPolicyResponse.html) | arn:\${Partition}:network-firewall:\${Region}:\${Account}:firewall-policy/\${Name} |
| [StatefulRuleGroup](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_RuleGroupResponse.html) | arn:\${Partition}:network-firewall:\${Region}:\${Account}:stateful-rulegroup/\${Name} |
| [StatelessRuleGroup](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_RuleGroupResponse.html) | arn:\${Partition}:network-firewall:\${Region}:\${Account}:stateless-rulegroup/\${Name} |
| [TLSInspectionConfiguration](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_TLSInspectionConfigurationResponse.html) | arn:\${Partition}:network-firewall:\${Region}:\${Account}:tls-configuration/\${Name} |
# Amazon One Enterprise
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazononeenterprise.html
| Service | ARN |
|---------|-----|
| [device-instance](https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-device-instance.html) | arn:\${Partition}:one:\${Region}:\${Account}:device-instance/\${DeviceInstanceId} |
| [configuration](https://docs.aws.amazon.com/one-enterprise/latest/userguide/configure-instance.html) | arn:\${Partition}:one:\${Region}:\${Account}:device-instance/\${DeviceInstanceId}/configuration/\${Version} |
| [device-configuration-template](https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-config-template.html) | arn:\${Partition}:one:\${Region}:\${Account}:device-configuration-template/\${TemplateId} |
| [site](https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-sites.html) | arn:\${Partition}:one:\${Region}:\${Account}:site/\${SiteId} |
| [user](https://docs.aws.amazon.com/one-enterprise/latest/userguide/enrollment-entry.html) | arn:\${Partition}:one:\${Region}:\${Account}:user/\${UserId} |
# AWS OpsWorks Configuration Management
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsopsworksconfigurationmanagement.html
| Service | ARN |
|---------|-----|
| [server](server) | arn:\${Partition}:opsworks-cm::\${Account}:server/\${ServerName}/\${UniqueId} |
| [backup](backup) | arn:\${Partition}:opsworks-cm::\${Account}:backup/\${ServerName}-{Date-and-Time-Stamp-of-Backup} |
# Amazon OpenSearch Serverless
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonopensearchserverless.html
| Service | ARN |
|---------|-----|
| [Collection](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-overview.html) | arn:\${Partition}:aoss:\${Region}:\${Account}:collection/\${CollectionId} |
| [Dashboards](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-overview.html) | arn:\${Partition}:aoss:\${Region}:\${Account}:dashboards/default |
# Amazon Nimble Studio
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonnimblestudio.html
| Service | ARN |
|---------|-----|
| [studio](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_Studio.html) | arn:\${Partition}:nimble:\${Region}:\${Account}:studio/\${StudioId} |
| [streaming-image](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_StreamingImage.html) | arn:\${Partition}:nimble:\${Region}:\${Account}:streaming-image/\${StreamingImageId} |
| [studio-component](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_StudioComponent.html) | arn:\${Partition}:nimble:\${Region}:\${Account}:studio-component/\${StudioComponentId} |
| [launch-profile](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_LaunchProfile.html) | arn:\${Partition}:nimble:\${Region}:\${Account}:launch-profile/\${LaunchProfileId} |
| [streaming-session](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_StreamingSession.html) | arn:\${Partition}:nimble:\${Region}:\${Account}:streaming-session/\${StreamingSessionId} |
| [streaming-session-backup](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_StreamingSessionBackup.html) | arn:\${Partition}:nimble:\${Region}:\${Account}:streaming-session-backup/\${StreamingSessionBackupId} |
| [eula](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_Eula.html) | arn:\${Partition}:nimble:\${Region}:\${Account}:eula/\${EulaId} |
| [eula-acceptance](https://docs.aws.amazon.com/nimble-studio/latest/APIReference/API_EulaAcceptance.html) | arn:\${Partition}:nimble:\${Region}:\${Account}:eula-acceptance/\${EulaAcceptanceId} |
# AWS Organizations
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html
| Service | ARN |
|---------|-----|
| [account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_arn-formats.html) | arn:\${Partition}:organizations::\${Account}:account/o-\${OrganizationId}/\${AccountId} |
| [handshake](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_arn-formats.html) | arn:\${Partition}:organizations::\${Account}:handshake/o-\${OrganizationId}/\${HandshakeType}/h-\${HandshakeId} |
| [organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_arn-formats.html) | arn:\${Partition}:organizations::\${Account}:organization/o-\${OrganizationId} |
| [organizationalunit](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_arn-formats.html) | arn:\${Partition}:organizations::\${Account}:ou/o-\${OrganizationId}/ou-\${OrganizationalUnitId} |
| [policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_arn-formats.html) | arn:\${Partition}:organizations::\${Account}:policy/o-\${OrganizationId}/\${PolicyType}/p-\${PolicyId} |
| [resourcepolicy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_arn-formats.html) | arn:\${Partition}:organizations::\${Account}:resourcepolicy/o-\${OrganizationId}/rp-\${ResourcePolicyId} |
| [awspolicy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_arn-formats.html) | arn:\${Partition}:organizations::aws:policy/\${PolicyType}/p-\${PolicyId} |
| [root](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_arn-formats.html) | arn:\${Partition}:organizations::\${Account}:root/o-\${OrganizationId}/r-\${RootId} |
# AWS Outposts
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsoutposts.html
| Service | ARN |
|---------|-----|
| [outpost](https://docs.aws.amazon.com/outposts/latest/userguide/work-with-outposts.html) | arn:\${Partition}:outposts:\${Region}:\${Account}:outpost/\${OutpostId} |
| [site](https://docs.aws.amazon.com/outposts/latest/userguide/work-with-outposts.html) | arn:\${Partition}:outposts:\${Region}:\${Account}:site/\${SiteId} |
# Amazon OpenSearch Ingestion
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonopensearchingestion.html
| Service | ARN |
|---------|-----|
| [pipeline](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_Pipeline.html) | arn:\${Partition}:osis:\${Region}:\${Account}:pipeline/\${PipelineName} |
| [pipeline-blueprint](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_PipelineBlueprint.html) | arn:\${Partition}:osis:\${Region}:\${Account}:blueprint/\${BlueprintName} |
# AWS Network Manager
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsnetworkmanager.html
| Service | ARN |
|---------|-----|
| [global-network](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-network-manager.html) | arn:\${Partition}:networkmanager::\${Account}:global-network/\${ResourceId} |
| [site](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-network-manager.html) | arn:\${Partition}:networkmanager::\${Account}:site/\${GlobalNetworkId}/\${ResourceId} |
| [link](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-network-manager.html) | arn:\${Partition}:networkmanager::\${Account}:link/\${GlobalNetworkId}/\${ResourceId} |
| [device](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-network-manager.html) | arn:\${Partition}:networkmanager::\${Account}:device/\${GlobalNetworkId}/\${ResourceId} |
| [connection](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-network-manager.html) | arn:\${Partition}:networkmanager::\${Account}:connection/\${GlobalNetworkId}/\${ResourceId} |
| [core-network](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-network-manager.html) | arn:\${Partition}:networkmanager::\${Account}:core-network/\${ResourceId} |
| [attachment](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-network-manager.html) | arn:\${Partition}:networkmanager::\${Account}:attachment/\${ResourceId} |
| [connect-peer](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-network-manager.html) | arn:\${Partition}:networkmanager::\${Account}:connect-peer/\${ResourceId} |
| [peering](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-network-manager.html) | arn:\${Partition}:networkmanager::\${Account}:peering/\${ResourceId} |
# AWS Partner central account management
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awspartnercentralaccountmanagement.html
| Service | ARN |
|---------|-----|
# AWS OpsWorks
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsopsworks.html
| Service | ARN |
|---------|-----|
| [stack](https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks.html) | arn:\${Partition}:opsworks:\${Region}:\${Account}:stack/\${StackId}/ |
# AWS Payments
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awspayments.html
| Service | ARN |
|---------|-----|
# AWS Panorama
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awspanorama.html
| Service | ARN |
|---------|-----|
| [device](https://docs.aws.amazon.com/panorama/latest/dev/gettingstarted-concepts.html#gettingstarted-concepts-appliance) | arn:\${Partition}:panorama:\${Region}:\${Account}:device/\${DeviceId} |
| [package](https://docs.aws.amazon.com/panorama/latest/dev/gettingstarted-concepts.html#gettingstarted-concepts-node) | arn:\${Partition}:panorama:\${Region}:\${Account}:package/\${PackageId} |
| [applicationInstance](https://docs.aws.amazon.com/panorama/latest/dev/gettingstarted-concepts.html#gettingstarted-concepts-application) | arn:\${Partition}:panorama:\${Region}:\${Account}:applicationInstance/\${ApplicationInstanceId} |
# Amazon OpenSearch Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonopensearchservice.html
| Service | ARN |
|---------|-----|
| [domain](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac.html) | arn:\${Partition}:es:\${Region}:\${Account}:domain/\${DomainName} |
| [es_role](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/slr.html) | arn:\${Partition}:iam::\${Account}:role/aws-service-role/es.amazonaws.com/AWSServiceRoleForAmazonOpenSearchService |
| [opensearchservice_role](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/slr.html) | arn:\${Partition}:iam::\${Account}:role/aws-service-role/opensearchservice.amazonaws.com/AWSServiceRoleForAmazonOpenSearchService |
# AWS Performance Insights
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsperformanceinsights.html
| Service | ARN |
|---------|-----|
| [metric-resource](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.access-control.html) | arn:\${Partition}:pi:\${Region}:\${Account}:metrics/\${ServiceType}/\${Identifier} |
| [perf-reports-resource](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.access-control.html) | arn:\${Partition}:pi:\${Region}:\${Account}:perf-reports/\${ServiceType}/\${Identifier}/\${ReportId} |
# Amazon Pinpoint SMS and Voice Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonpinpointsmsandvoiceservice.html
| Service | ARN |
|---------|-----|
# AWS Payment Cryptography
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awspaymentcryptography.html
| Service | ARN |
|---------|-----|
| [key](${APIReferenceDocPage}API_Key.html) | arn:\${Partition}:payment-cryptography:\${Region}:\${Account}:key/\${KeyId} |
| [alias](${APIReferenceDocPage}API_Alias.html) | arn:\${Partition}:payment-cryptography:\${Region}:\${Account}:alias/\${Alias} |
# Amazon Personalize
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonpersonalize.html
| Service | ARN |
|---------|-----|
| [schema](https://docs.aws.amazon.com/personalize/latest/dg/how-it-works-dataset-schema.html#schema-examples) | arn:\${Partition}:personalize:\${Region}:\${Account}:schema/\${ResourceId} |
| [featureTransformation](https://docs.aws.amazon.com/personalize/latest/dg/API_FeatureTransformation.html) | arn:\${Partition}:personalize:\${Region}:\${Account}:feature-transformation/\${ResourceId} |
| [dataset](https://docs.aws.amazon.com/personalize/latest/dg/API_Dataset.html) | arn:\${Partition}:personalize:\${Region}:\${Account}:dataset/\${ResourceId} |
| [datasetGroup](https://docs.aws.amazon.com/personalize/latest/dg/API_DatasetGroup.html) | arn:\${Partition}:personalize:\${Region}:\${Account}:dataset-group/\${ResourceId} |
| [datasetImportJob](https://docs.aws.amazon.com/personalize/latest/dg/API_DatasetImportJob.html) | arn:\${Partition}:personalize:\${Region}:\${Account}:dataset-import-job/\${ResourceId} |
| [dataInsightsJob](https://docs.aws.amazon.com/personalize/latest/dg/analyzing-data.html) | arn:\${Partition}:personalize:\${Region}:\${Account}:data-insights-job/\${ResourceId} |
| [datasetExportJob](https://docs.aws.amazon.com/personalize/latest/dg/API_DatasetExportJob.html) | arn:\${Partition}:personalize:\${Region}:\${Account}:dataset-export-job/\${ResourceId} |
| [solution](https://docs.aws.amazon.com/personalize/latest/dg/API_Solution.html) | arn:\${Partition}:personalize:\${Region}:\${Account}:solution/\${ResourceId} |
| [campaign](https://docs.aws.amazon.com/personalize/latest/dg/API_Campaign.html) | arn:\${Partition}:personalize:\${Region}:\${Account}:campaign/\${ResourceId} |
| [eventTracker](https://docs.aws.amazon.com/personalize/latest/dg/API_EventTracker.html) | arn:\${Partition}:personalize:\${Region}:\${Account}:event-tracker/\${ResourceId} |
| [recipe](https://docs.aws.amazon.com/personalize/latest/dg/API_Recipe.html) | arn:\${Partition}:personalize:\${Region}:\${Account}:recipe/\${ResourceId} |
| [algorithm](https://docs.aws.amazon.com/personalize/latest/dg/API_Algorithm.html) | arn:\${Partition}:personalize:\${Region}:\${Account}:algorithm/\${ResourceId} |
| [batchInferenceJob](https://docs.aws.amazon.com/personalize/latest/dg/API_BatchInferenceJob.html) | arn:\${Partition}:personalize:\${Region}:\${Account}:batch-inference-job/\${ResourceId} |
| [filter](https://docs.aws.amazon.com/personalize/latest/dg/API_Filter.html) | arn:\${Partition}:personalize:\${Region}:\${Account}:filter/\${ResourceId} |
| [recommender](https://docs.aws.amazon.com/personalize/latest/dg/API_Recommender.html) | arn:\${Partition}:personalize:\${Region}:\${Account}:recommender/\${ResourceId} |
| [batchSegmentJob](https://docs.aws.amazon.com/personalize/latest/dg/API_BatchSegmentJob.html) | arn:\${Partition}:personalize:\${Region}:\${Account}:batch-segment-job/\${ResourceId} |
| [metricAttribution](https://docs.aws.amazon.com/personalize/latest/dg/API_MetricAttribution.html) | arn:\${Partition}:personalize:\${Region}:\${Account}:metric-attribution/\${ResourceId} |
# AWS Price List
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awspricelist.html
| Service | ARN |
|---------|-----|
# AWS Private Certificate Authority
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsprivatecertificateauthority.html
| Service | ARN |
|---------|-----|
| [certificate-authority](https://docs.aws.amazon.com/privateca/latest/userguide/api-permissions.html) | arn:\${Partition}:acm-pca:\${Region}:\${Account}:certificate-authority/\${CertificateAuthorityId} |
# AWS Private CA Connector for Active Directory
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsprivatecaconnectorforactivedirectory.html
| Service | ARN |
|---------|-----|
| [Connector](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_Connector.html) | arn:\${Partition}:pca-connector-ad:\${Region}:\${Account}:connector/\${ConnectorId} |
| [DirectoryRegistration](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_DirectoryRegistration.html) | arn:\${Partition}:pca-connector-ad:\${Region}:\${Account}:directory-registration/\${DirectoryId} |
| [ServicePrincipalName](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ServicePrincipalName.html) | arn:\${Partition}:pca-connector-ad:\${Region}:\${Account}:directory-registration/\${DirectoryId} |
| [Template](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_Template.html) | arn:\${Partition}:pca-connector-ad:\${Region}:\${Account}:connector/\${ConnectorId}/template/\${TemplateId} |
| [TemplateGroupAccessControlEntry](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_AccessControlEntry.html) | arn:\${Partition}:pca-connector-ad:\${Region}:\${Account}:connector/\${ConnectorId}/template/\${TemplateId} |
# Amazon Polly
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonpolly.html
| Service | ARN |
|---------|-----|
| [lexicon](https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html) | arn:\${Partition}:polly:\${Region}:\${Account}:lexicon/\${LexiconName} |
# AWS Purchase Orders Console
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awspurchaseordersconsole.html
| Service | ARN |
|---------|-----|
| [purchase-order](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions) | arn:\${Partition}:purchase-orders::\${Account}:purchase-order/\${ResourceName} |
# Amazon Q
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonq.html
| Service | ARN |
|---------|-----|
# Amazon Pinpoint SMS Voice V2
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonpinpointsmsvoicev2.html
| Service | ARN |
|---------|-----|
| [ConfigurationSet](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateConfigurationSet.html) | arn:\${Partition}:sms-voice:\${Region}:\${Account}:configuration-set/\${ConfigurationSetName} |
| [OptOutList](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateOptOutList.html) | arn:\${Partition}:sms-voice:\${Region}:\${Account}:opt-out-list/\${OptOutListName} |
| [PhoneNumber](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RequestPhoneNumber.html) | arn:\${Partition}:sms-voice:\${Region}:\${Account}:phone-number/\${PhoneNumberId} |
| [Pool](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreatePool.html) | arn:\${Partition}:sms-voice:\${Region}:\${Account}:pool/\${PoolId} |
| [ProtectConfiguration](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_ProtectConfiguration.html) | arn:\${Partition}:sms-voice:\${Region}:\${Account}:protect-configuration/\${ProtectConfigurationId} |
| [SenderId](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeSenderIds.html) | arn:\${Partition}:sms-voice:\${Region}:\${Account}:sender-id/\${SenderId}/\${IsoCountryCode} |
| [Registration](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeRegistrations.html) | arn:\${Partition}:sms-voice:\${Region}:\${Account}:registration/\${RegistrationId} |
| [RegistrationAttachment](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeRegistrationAttachments.html) | arn:\${Partition}:sms-voice:\${Region}:\${Account}:registration-attachment/\${RegistrationAttachmentId} |
| [VerifiedDestinationNumber](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeVerifiedDestinationNumbers.html) | arn:\${Partition}:sms-voice:\${Region}:\${Account}:verified-destination-number/\${VerifiedDestinationNumberId} |
# Amazon Pinpoint Email Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonpinpointemailservice.html
| Service | ARN |
|---------|-----|
| [configuration-set](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_CreateConfigurationSet.html) | arn:\${Partition}:ses:\${Region}:\${Account}:configuration-set/\${ConfigurationSetName} |
| [dedicated-ip-pool](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DedicatedIp.html) | arn:\${Partition}:ses:\${Region}:\${Account}:dedicated-ip-pool/\${DedicatedIPPool} |
| [deliverability-test-report](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DeliverabilityTestReport.html) | arn:\${Partition}:ses:\${Region}:\${Account}:deliverability-test-report/\${ReportId} |
| [identity](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_IdentityInfo.html) | arn:\${Partition}:ses:\${Region}:\${Account}:identity/\${IdentityName} |
# Amazon Q Business Q Apps
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonqbusinessqapps.html
| Service | ARN |
|---------|-----|
| [application](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-app.html) | arn:\${Partition}:qbusiness:\${Region}:\${Account}:application/\${ApplicationId} |
# Amazon Pinpoint
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonpinpoint.html
| Service | ARN |
|---------|-----|
| [app](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId} |
| [apps](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/* |
| [campaign](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-campaigns-campaign-id.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/campaigns/\${CampaignId} |
| [journey](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys-journey-id.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/journeys/\${JourneyId} |
| [journeys](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/journeys |
| [segment](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-segments-segment-id.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/segments/\${SegmentId} |
| [template](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:templates/\${TemplateName}/\${TemplateType} |
| [templates](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:templates |
| [recommender](https://docs.aws.amazon.com/pinpoint/latest/apireference/recommenders.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:recommenders/\${RecommenderId} |
| [recommenders](https://docs.aws.amazon.com/pinpoint/latest/apireference/recommenders.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:recommenders/* |
| [phone-number-validate](https://docs.aws.amazon.com/pinpoint/latest/apireference/phone-number-validate.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:phone/number/validate |
| [channels](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/channels |
| [channel](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/channels/\${ChannelType} |
| [event-stream](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-eventstream.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/eventstream |
| [events](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-events.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/events |
| [messages](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/messages |
| [verify-otp](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-verify-otp.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/verify-otp |
| [otp](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-verify-otp.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/otp |
| [attribute](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-attributes-attribute-type.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/attributes/\${AttributeType} |
| [user](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-users-user-id.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/users/\${UserId} |
| [endpoint](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-endpoints-endpoint-id.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/endpoints/\${EndpointId} |
| [import-job](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-jobs-import-job-id.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/jobs/import/\${JobId} |
| [export-job](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-jobs-export-job-id.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/jobs/export/\${JobId} |
| [application-metrics](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-kpis-daterange-kpi-name.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/kpis/daterange/\${KpiName} |
| [campaign-metrics](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-campaigns-campaign-id-kpis-daterange-kpi-name.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/campaigns/\${CampaignId}/kpis/daterange/\${KpiName} |
| [journey-metrics](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys-journey-id-kpis-daterange-kpi-name.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/journeys/\${JourneyId}/kpis/daterange/\${KpiName} |
| [journey-execution-metrics](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys-journey-id-execution-metrics.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/journeys/\${JourneyId}/execution-metrics |
| [journey-execution-activity-metrics](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys-journey-id-activities-journey-activity-id-execution-metrics.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:apps/\${AppId}/journeys/\${JourneyId}/activities/\${JourneyActivityId}/execution-metrics |
| [reports](https://docs.aws.amazon.com/pinpoint/latest/apireference/reports.html) | arn:\${Partition}:mobiletargeting:\${Region}:\${Account}:reports |
# Amazon Q Business
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonqbusiness.html
| Service | ARN |
|---------|-----|
| [application](${UserGuideDocPage}create-application.html) | arn:\${Partition}:qbusiness:\${Region}:\${Account}:application/\${ApplicationId} |
| [retriever](${UserGuideDocPage}select-retriever.html) | arn:\${Partition}:qbusiness:\${Region}:\${Account}:application/\${ApplicationId}/retriever/\${RetrieverId} |
| [index](${UserGuideDocPage}select-retriever.html) | arn:\${Partition}:qbusiness:\${Region}:\${Account}:application/\${ApplicationId}/index/\${IndexId} |
| [data-source](${UserGuideDocPage}connect-data.html) | arn:\${Partition}:qbusiness:\${Region}:\${Account}:application/\${ApplicationId}/index/\${IndexId}/data-source/\${DataSourceId} |
| [plugin](${UserGuideDocPage}plugins.html) | arn:\${Partition}:qbusiness:\${Region}:\${Account}:application/\${ApplicationId}/plugin/\${PluginId} |
| [web-experience](${UserGuideDocPage}using-web-experience.html) | arn:\${Partition}:qbusiness:\${Region}:\${Account}:application/\${ApplicationId}/web-experience/\${WebExperienceId} |
| [user-license](${UserGuideDocPage}provisioning.html) | arn:\${Partition}:qbusiness:\${Region}:\${Account}:application/\${ApplicationId}/user-license/\${UserLicenseId} |
| [subscription](${UserGuideDocPage}subscriptions.html) | arn:\${Partition}:qbusiness:\${Region}:\${Account}:application/\${ApplicationId}/subscription/\${SubscriptionId} |
# AWS Proton
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsproton.html
| Service | ARN |
|---------|-----|
| [environment-template](https://docs.aws.amazon.com/proton/latest/adminguide/ag-env-templates.html) | arn:\${Partition}:proton:\${Region}:\${Account}:environment-template/\${Name} |
| [environment-template-version](https://docs.aws.amazon.com/proton/latest/adminguide/ag-env-templates.html) | arn:\${Partition}:proton:\${Region}:\${Account}:environment-template/\${TemplateName}:\${MajorVersion}.\${MinorVersion} |
| [environment-template-major-version](https://docs.aws.amazon.com/proton/latest/adminguide/ag-env-templates.html) | arn:\${Partition}:proton:\${Region}:\${Account}:environment-template/\${TemplateName}:\${MajorVersionId} |
| [environment-template-minor-version](https://docs.aws.amazon.com/proton/latest/adminguide/ag-env-templates.html) | arn:\${Partition}:proton:\${Region}:\${Account}:environment-template/\${TemplateName}:\${MajorVersionId}.\${MinorVersionId} |
| [service-template](https://docs.aws.amazon.com/proton/latest/adminguide/managing-svc-templates.html) | arn:\${Partition}:proton:\${Region}:\${Account}:service-template/\${Name} |
| [service-template-version](https://docs.aws.amazon.com/proton/latest/adminguide/managing-svc-templates.html) | arn:\${Partition}:proton:\${Region}:\${Account}:service-template/\${TemplateName}:\${MajorVersion}.\${MinorVersion} |
| [service-template-major-version](https://docs.aws.amazon.com/proton/latest/adminguide/managing-svc-templates.html) | arn:\${Partition}:proton:\${Region}:\${Account}:service-template/\${TemplateName}:\${MajorVersionId} |
| [service-template-minor-version](https://docs.aws.amazon.com/proton/latest/adminguide/managing-svc-templates.html) | arn:\${Partition}:proton:\${Region}:\${Account}:service-template/\${TemplateName}:\${MajorVersionId}.\${MinorVersionId} |
| [environment](https://docs.aws.amazon.com/proton/latest/adminguide/ag-environments.html) | arn:\${Partition}:proton:\${Region}:\${Account}:environment/\${Name} |
| [service](https://docs.aws.amazon.com/proton/latest/adminguide/ag-services.html) | arn:\${Partition}:proton:\${Region}:\${Account}:service/\${Name} |
| [service-instance](https://docs.aws.amazon.com/proton/latest/adminguide/ag-services.html) | arn:\${Partition}:proton:\${Region}:\${Account}:service/\${ServiceName}/service-instance/\${Name} |
| [environment-account-connection](https://docs.aws.amazon.com/proton/latest/adminguide/ag-env-account-connections.html) | arn:\${Partition}:proton:\${Region}:\${Account}:environment-account-connection/\${Id} |
| [repository](https://docs.aws.amazon.com/proton/latest/adminguide/ag-repositories.html) | arn:\${Partition}:proton:\${Region}:\${Account}:repository/\${Provider}:\${Name} |
| [component](https://docs.aws.amazon.com/proton/latest/adminguide/ag-components.html) | arn:\${Partition}:proton:\${Region}:\${Account}:component/\${Id} |
| [deployment](https://docs.aws.amazon.com/proton/latest/adminguide/ag-deployments.html) | arn:\${Partition}:proton:\${Region}:\${Account}:deployment/\${Id} |
# Amazon RDS Data API
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonrdsdataapi.html
| Service | ARN |
|---------|-----|
| [cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Aurora.Managing.html) | arn:\${Partition}:rds:\${Region}:\${Account}:cluster:\${DbClusterInstanceName} |
# AWS re:Post Private
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsre_postprivate.html
| Service | ARN |
|---------|-----|
| [space](https://docs.aws.amazon.com/repostprivate/latest/UserGuide/) | arn:\${Partition}:repostspace:\${Region}:\${Account}:space/\${ResourceId} |
# Amazon RDS IAM Authentication
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonrdsiamauthentication.html
| Service | ARN |
|---------|-----|
| [db-user](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.DBAccounts.html) | arn:\${Partition}:rds-db:\${Region}:\${Account}:dbuser:\${DbiResourceId}/\${DbUserName} |
# AWS Recycle Bin
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsrecyclebin.html
| Service | ARN |
|---------|-----|
| [rule](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-recycle-bin.html#recycle-bin-concepts) | arn:\${Partition}:rbin:\${Region}:\${Account}:rule/\${ResourceName} |
# Amazon Q in Connect
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonqinconnect.html
| Service | ARN |
|---------|-----|
| [Assistant](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_AssistantData.html) | arn:\${Partition}:wisdom:\${Region}:\${Account}:assistant/\${AssistantId} |
| [AssistantAssociation](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_AssistantAssociationData.html) | arn:\${Partition}:wisdom:\${Region}:\${Account}:association/\${AssistantId}/\${AssistantAssociationId} |
| [Content](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_ContentData.html) | arn:\${Partition}:wisdom:\${Region}:\${Account}:content/\${KnowledgeBaseId}/\${ContentId} |
| [KnowledgeBase](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_KnowledgeBaseData.html) | arn:\${Partition}:wisdom:\${Region}:\${Account}:knowledge-base/\${KnowledgeBaseId} |
| [Session](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_SessionData.html) | arn:\${Partition}:wisdom:\${Region}:\${Account}:session/\${AssistantId}/\${SessionId} |
| [QuickResponse](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_QuickResponseData.html) | arn:\${Partition}:wisdom:\${Region}:\${Account}:quick-response/\${KnowledgeBaseId}/\${QuickResponseId} |
# Amazon QLDB
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonqldb.html
| Service | ARN |
|---------|-----|
| [ledger](https://docs.aws.amazon.com/qldb/latest/developerguide/ledger-structure.html) | arn:\${Partition}:qldb:\${Region}:\${Account}:ledger/\${LedgerName} |
| [stream](https://docs.aws.amazon.com/qldb/latest/developerguide/streams.html) | arn:\${Partition}:qldb:\${Region}:\${Account}:stream/\${LedgerName}/\${StreamId} |
| [table](https://docs.aws.amazon.com/qldb/latest/developerguide/working.manage-tables.html) | arn:\${Partition}:qldb:\${Region}:\${Account}:ledger/\${LedgerName}/table/\${TableId} |
| [catalog](https://docs.aws.amazon.com/qldb/latest/developerguide/working.catalog.html) | arn:\${Partition}:qldb:\${Region}:\${Account}:ledger/\${LedgerName}/information_schema/user_tables |
# Amazon Redshift Data API
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonredshiftdataapi.html
| Service | ARN |
|---------|-----|
| [cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html) | arn:\${Partition}:redshift:\${Region}:\${Account}:cluster:\${ClusterName} |
| [workgroup](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-serverless.html) | arn:\${Partition}:redshift-serverless:\${Region}:\${Account}:workgroup/\${WorkgroupId} |
# Amazon QuickSight
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonquicksight.html
| Service | ARN |
|---------|-----|
| [account](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AccountInfo.html) | arn:\${Partition}:quicksight:\${Region}:\${Account}:account/\${ResourceId} |
| [user](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_User.html) | arn:\${Partition}:quicksight:\${Region}:\${Account}:user/\${ResourceId} |
| [group](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Group.html) | arn:\${Partition}:quicksight:\${Region}:\${Account}:group/\${ResourceId} |
| [analysis](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Analysis.html) | arn:\${Partition}:quicksight:\${Region}:\${Account}:analysis/\${ResourceId} |
| [dashboard](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Dashboard.html) | arn:\${Partition}:quicksight:\${Region}:\${Account}:dashboard/\${ResourceId} |
| [template](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Template.html) | arn:\${Partition}:quicksight:\${Region}:\${Account}:template/\${ResourceId} |
| [vpcconnection](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_VPCConnection.html) | arn:\${Partition}:quicksight:\${Region}:\${Account}:vpcConnection/\${ResourceId} |
| [assetBundleExportJob](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AssetBundleExportJob.html) | arn:\${Partition}:quicksight:\${Region}:\${Account}:asset-bundle-export-job/\${ResourceId} |
| [assetBundleImportJob](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AssetBundleImportJob.html) | arn:\${Partition}:quicksight:\${Region}:\${Account}:asset-bundle-import-job/\${ResourceId} |
| [datasource](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataSource.html) | arn:\${Partition}:quicksight:\${Region}:\${Account}:datasource/\${ResourceId} |
| [dataset](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataSet.html) | arn:\${Partition}:quicksight:\${Region}:\${Account}:dataset/\${ResourceId} |
| [ingestion](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Ingestion.html) | arn:\${Partition}:quicksight:\${Region}:\${Account}:dataset/\${DatasetId}/ingestion/\${ResourceId} |
| [refreshschedule](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RefreshSchedule.html) | arn:\${Partition}:quicksight:\${Region}:\${Account}:dataset/\${DatasetId}/refresh-schedule/\${ResourceId} |
| [theme](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Theme.html) | arn:\${Partition}:quicksight:\${Region}:\${Account}:theme/\${ResourceId} |
| [assignment](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_IAMPolicyAssignment.html) | arn:\${Partition}:quicksight::\${Account}:assignment/\${ResourceId} |
| [customization](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AccountCustomization.html) | arn:\${Partition}:quicksight:\${Region}:\${Account}:customization/\${ResourceId} |
| [namespace](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_NamespaceInfoV2.html) | arn:\${Partition}:quicksight:\${Region}:\${Account}:namespace/\${ResourceId} |
| [folder](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Folder.html) | arn:\${Partition}:quicksight:\${Region}:\${Account}:folder/\${ResourceId} |
| [emailCustomizationTemplate](https://docs.aws.amazon.com/quicksight/latest/user/customizing-quicksight-email-templates.html) | arn:\${Partition}:quicksight:\${Region}:\${Account}:email-customization-template/\${ResourceId} |
| [topic](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicDetails.html) | arn:\${Partition}:quicksight:\${Region}:\${Account}:topic/\${ResourceId} |
| [dashboardSnapshotJob](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DashboardSnapshotJob.html) | arn:\${Partition}:quicksight:\${Region}:\${Account}:dashboard/\${DashboardId}/snapshot-job/\${ResourceId} |
# AWS Resource Explorer
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsresourceexplorer.html
| Service | ARN |
|---------|-----|
| [view](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_View.html) | arn:\${Partition}:resource-explorer-2:\${Region}:\${Account}:view/\${ViewName}/\${ViewUuid} |
| [index](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_Index.html) | arn:\${Partition}:resource-explorer-2:\${Region}:\${Account}:index/\${IndexUuid} |
# Amazon Resource Group Tagging API
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonresourcegrouptaggingapi.html
| Service | ARN |
|---------|-----|
# Amazon Redshift Serverless
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonredshiftserverless.html
| Service | ARN |
|---------|-----|
| [namespace](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-workgroup-namespace.html) | arn:\${Partition}:redshift-serverless:\${Region}:\${Account}:namespace/\${NamespaceId} |
| [snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-snapshots-recovery.html) | arn:\${Partition}:redshift-serverless:\${Region}:\${Account}:snapshot/\${SnapshotId} |
| [workgroup](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-workgroup-namespace.html) | arn:\${Partition}:redshift-serverless:\${Region}:\${Account}:workgroup/\${WorkgroupId} |
| [recoveryPoint](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-snapshots-recovery.html) | arn:\${Partition}:redshift-serverless:\${Region}:\${Account}:recoverypoint/\${RecoveryPointId} |
| [endpointAccess](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-connecting.html) | arn:\${Partition}:redshift-serverless:\${Region}:\${Account}:managedvpcendpoint/\${EndpointAccessId} |
# AWS Resource Access Manager (RAM)
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsresourceaccessmanagerram.html
| Service | ARN |
|---------|-----|
| [resource-share](https://docs.aws.amazon.com/ram/latest/APIReference/API_ResourceShare.html) | arn:\${Partition}:ram:\${Region}:\${Account}:resource-share/\${ResourcePath} |
| [resource-share-invitation](https://docs.aws.amazon.com/ram/latest/APIReference/API_ResourceShareInvitation.html) | arn:\${Partition}:ram:\${Region}:\${Account}:resource-share-invitation/\${ResourcePath} |
| [permission](https://docs.aws.amazon.com/ram/latest/APIReference/API_ResourceSharePermissionDetail.html) | arn:\${Partition}:ram::\${Account}:permission/\${ResourcePath} |
| [customer-managed-permission](https://docs.aws.amazon.com/ram/latest/APIReference/API_ResourceSharePermissionDetail.html) | arn:\${Partition}:ram:\${Region}:\${Account}:permission/\${ResourcePath} |
# AWS Resource Groups
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsresourcegroups.html
| Service | ARN |
|---------|-----|
| [group](https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html) | arn:\${Partition}:resource-groups:\${Region}:\${Account}:group/\${GroupName} |
# Amazon Rekognition
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonrekognition.html
| Service | ARN |
|---------|-----|
| [collection](https://docs.aws.amazon.com/rekognition/latest/dg/collections.html) | arn:\${Partition}:rekognition:\${Region}:\${Account}:collection/\${CollectionId} |
| [streamprocessor](https://docs.aws.amazon.com/rekognition/latest/dg/streaming-video.html) | arn:\${Partition}:rekognition:\${Region}:\${Account}:streamprocessor/\${StreamprocessorId} |
| [project](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/mp-create-project.html) | arn:\${Partition}:rekognition:\${Region}:\${Account}:project/\${ProjectName}/\${CreationTimestamp} |
| [projectversion](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/training-model.html) | arn:\${Partition}:rekognition:\${Region}:\${Account}:project/\${ProjectName}/version/\${VersionName}/\${CreationTimestamp} |
| [dataset](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/creating-datasets.html) | arn:\${Partition}:rekognition:\${Region}:\${Account}:project/\${ProjectName}/dataset/\${DatasetType}/\${CreationTimestamp} |
# Amazon RHEL Knowledgebase Portal
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonrhelknowledgebaseportal.html
| Service | ARN |
|---------|-----|
# Amazon Redshift
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonredshift.html
| Service | ARN |
|---------|-----|
| [cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html) | arn:\${Partition}:redshift:\${Region}:\${Account}:cluster:\${ClusterName} |
| [datashare](https://docs.aws.amazon.com/redshift/latest/dg/datashare-overview.html) | arn:\${Partition}:redshift:\${Region}:\${Account}:datashare:\${ProducerClusterNamespace}/\${DataShareName} |
| [dbgroup](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_GROUP.html) | arn:\${Partition}:redshift:\${Region}:\${Account}:dbgroup:\${ClusterName}/\${DbGroup} |
| [dbname](https://docs.aws.amazon.com/redshift/latest/dg/t_creating_database.html) | arn:\${Partition}:redshift:\${Region}:\${Account}:dbname:\${ClusterName}/\${DbName} |
| [dbuser](https://docs.aws.amazon.com/redshift/latest/dg/r_Users.html) | arn:\${Partition}:redshift:\${Region}:\${Account}:dbuser:\${ClusterName}/\${DbUser} |
| [eventsubscription](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-events.html) | arn:\${Partition}:redshift:\${Region}:\${Account}:eventsubscription:\${EventSubscriptionName} |
| [hsmclientcertificate](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html#working-with-HSM) | arn:\${Partition}:redshift:\${Region}:\${Account}:hsmclientcertificate:\${HSMClientCertificateId} |
| [hsmconfiguration](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html#working-with-HSM) | arn:\${Partition}:redshift:\${Region}:\${Account}:hsmconfiguration:\${HSMConfigurationId} |
| [namespace](https://docs.aws.amazon.com/redshift/latest/dg/concepts.html) | arn:\${Partition}:redshift:\${Region}:\${Account}:namespace:\${ClusterNamespace} |
| [parametergroup](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html) | arn:\${Partition}:redshift:\${Region}:\${Account}:parametergroup:\${ParameterGroupName} |
| [securitygroup](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html) | arn:\${Partition}:redshift:\${Region}:\${Account}:securitygroup:\${SecurityGroupName}/ec2securitygroup/\${Owner}/\${Ec2SecurityGroupId} |
| [securitygroupingress-cidr](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html) | arn:\${Partition}:redshift:\${Region}:\${Account}:securitygroupingress:\${SecurityGroupName}/cidrip/\${IpRange} |
| [securitygroupingress-ec2securitygroup](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html) | arn:\${Partition}:redshift:\${Region}:\${Account}:securitygroupingress:\${SecurityGroupName}/ec2securitygroup/\${Owner}/\${Ece2SecuritygroupId} |
| [snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html) | arn:\${Partition}:redshift:\${Region}:\${Account}:snapshot:\${ClusterName}/\${SnapshotName} |
| [snapshotcopygrant](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html#configure-snapshot-copy-grant) | arn:\${Partition}:redshift:\${Region}:\${Account}:snapshotcopygrant:\${SnapshotCopyGrantName} |
| [snapshotschedule](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html) | arn:\${Partition}:redshift:\${Region}:\${Account}:snapshotschedule:\${ParameterGroupName} |
| [subnetgroup](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-cluster-subnet-groups.html) | arn:\${Partition}:redshift:\${Region}:\${Account}:subnetgroup:\${SubnetGroupName} |
| [usagelimit](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-usage-limits.html) | arn:\${Partition}:redshift:\${Region}:\${Account}:usagelimit:\${UsageLimitId} |
| [redshiftidcapplication](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-idp-connect.html) | arn:\${Partition}:redshift:\${Region}:\${Account}:redshiftidcapplication:\${RedshiftIdcApplicationId} |
| [qev2idcapplication](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-idp-connect.html) | arn:\${Partition}:redshift:\${Region}:\${Account}:qev2idcapplication:\${Qev2IdcApplicationId} |
# Amazon Route 53 Application Recovery Controller - Zonal Shift
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53applicationrecoverycontroller-zonalshift.html
| Service | ARN |
|---------|-----|
| [ALB](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.html) | arn:\${Partition}:elasticloadbalancing:\${Region}:\${Account}:loadbalancer/app/\${LoadBalancerName}/\${LoadBalancerId} |
| [NLB](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.html) | arn:\${Partition}:elasticloadbalancing:\${Region}:\${Account}:loadbalancer/net/\${LoadBalancerName}/\${LoadBalancerId} |
# AWS Resilience Hub
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsresiliencehub.html
| Service | ARN |
|---------|-----|
| [resiliency-policy](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ResiliencyPolicy.html) | arn:\${Partition}:resiliencehub:\${Region}:\${Account}:resiliency-policy/\${ResiliencyPolicyId} |
| [application](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_App.html) | arn:\${Partition}:resiliencehub:\${Region}:\${Account}:app/\${AppId} |
| [app-assessment](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_AppAssessment.html) | arn:\${Partition}:resiliencehub:\${Region}:\${Account}:app-assessment/\${AppAssessmentId} |
| [recommendation-template](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_RecommendationTemplate.html) | arn:\${Partition}:resiliencehub:\${Region}:\${Account}:recommendation-template/\${RecommendationTemplateId} |
# Amazon RDS
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonrds.html
| Service | ARN |
|---------|-----|
| [cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Aurora.html) | arn:\${Partition}:rds:\${Region}:\${Account}:cluster:\${DbClusterInstanceName} |
| [shardgrp](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.DBShardGroup.html) | arn:\${Partition}:rds:\${Region}:\${Account}:shard-group:\${DbShardGroupResourceId} |
| [cluster-auto-backup](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html) | arn:\${Partition}:rds:\${Region}:\${Account}:cluster-auto-backup:\${DbClusterAutomatedBackupId} |
| [auto-backup](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html) | arn:\${Partition}:rds:\${Region}:\${Account}:auto-backup:\${DbInstanceAutomatedBackupId} |
| [cluster-endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.Endpoints.html) | arn:\${Partition}:rds:\${Region}:\${Account}:cluster-endpoint:\${DbClusterEndpoint} |
| [cluster-pg](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html) | arn:\${Partition}:rds:\${Region}:\${Account}:cluster-pg:\${ClusterParameterGroupName} |
| [cluster-snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html) | arn:\${Partition}:rds:\${Region}:\${Account}:cluster-snapshot:\${ClusterSnapshotName} |
| [db](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.html) | arn:\${Partition}:rds:\${Region}:\${Account}:db:\${DbInstanceName} |
| [es](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html) | arn:\${Partition}:rds:\${Region}:\${Account}:es:\${SubscriptionName} |
| [global-cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html) | arn:\${Partition}:rds::\${Account}:global-cluster:\${GlobalCluster} |
| [og](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.html) | arn:\${Partition}:rds:\${Region}:\${Account}:og:\${OptionGroupName} |
| [pg](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html) | arn:\${Partition}:rds:\${Region}:\${Account}:pg:\${ParameterGroupName} |
| [proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html) | arn:\${Partition}:rds:\${Region}:\${Account}:db-proxy:\${DbProxyId} |
| [proxy-endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html) | arn:\${Partition}:rds:\${Region}:\${Account}:db-proxy-endpoint:\${DbProxyEndpointId} |
| [ri](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html) | arn:\${Partition}:rds:\${Region}:\${Account}:ri:\${ReservedDbInstanceName} |
| [secgrp](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html) | arn:\${Partition}:rds:\${Region}:\${Account}:secgrp:\${SecurityGroupName} |
| [snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html) | arn:\${Partition}:rds:\${Region}:\${Account}:snapshot:\${SnapshotName} |
| [subgrp](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Scenarios.html#USER_VPC.Scenario1) | arn:\${Partition}:rds:\${Region}:\${Account}:subgrp:\${SubnetGroupName} |
| [target-group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html) | arn:\${Partition}:rds:\${Region}:\${Account}:target-group:\${TargetGroupId} |
| [cev](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev.html) | arn:\${Partition}:rds:\${Region}:\${Account}:cev:\${Engine}/\${EngineVersion}/\${CustomDbEngineVersionId} |
| [deployment](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html) | arn:\${Partition}:rds:\${Region}:\${Account}:deployment:\${BlueGreenDeploymentIdentifier} |
| [integration](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.html) | arn:\${Partition}:rds:\${Region}:\${Account}:integration:\${IntegrationIdentifier} |
| [snapshot-tenant-database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.single-tenant.snapshots.html#br-cdb.db-snapshots) | arn:\${Partition}:rds:\${Region}:\${Account}:snapshot-tenant-database:\${SnapshotName}:\${TenantResourceId} |
| [tenant-database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.CDBs.html#multi-tenant-configuration) | arn:\${Partition}:rds:\${Region}:\${Account}:tenant-database:\${TenantResourceId} |
# Amazon Route 53 Domains
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53domains.html
| Service | ARN |
|---------|-----|
# Amazon Route 53
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53.html
| Service | ARN |
|---------|-----|
| [cidrcollection](API_CidrCollection.html) | arn:\${Partition}:route53:::cidrcollection/\${Id} |
| [change](https://docs.aws.amazon.com/Route53/latest/APIReference/API_Change.html) | arn:\${Partition}:route53:::change/\${Id} |
| [delegationset](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-concepts.html#route-53-concepts-reusable-delegation-set) | arn:\${Partition}:route53:::delegationset/\${Id} |
| [healthcheck](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-concepts.html#route-53-concepts-health-check) | arn:\${Partition}:route53:::healthcheck/\${Id} |
| [hostedzone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-concepts.html#route-53-concepts-hosted-zone) | arn:\${Partition}:route53:::hostedzone/\${Id} |
| [trafficpolicy](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/traffic-policies.html) | arn:\${Partition}:route53:::trafficpolicy/\${Id} |
| [trafficpolicyinstance](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/traffic-policy-records.html) | arn:\${Partition}:route53:::trafficpolicyinstance/\${Id} |
| [queryloggingconfig](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html) | arn:\${Partition}:route53:::queryloggingconfig/\${Id} |
| [vpc](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:vpc/\${VpcId} |
# AWS RoboMaker
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsrobomaker.html
| Service | ARN |
|---------|-----|
| [robotApplication](https://docs.aws.amazon.com/robomaker/latest/dg/managing-robot-applications.html) | arn:\${Partition}:robomaker:\${Region}:\${Account}:robot-application/\${ApplicationName}/\${CreatedOnEpoch} |
| [simulationApplication](https://docs.aws.amazon.com/robomaker/latest/dg/managing-simulation-applications.html) | arn:\${Partition}:robomaker:\${Region}:\${Account}:simulation-application/\${ApplicationName}/\${CreatedOnEpoch} |
| [simulationJob](https://docs.aws.amazon.com/robomaker/latest/dg/simulation.html) | arn:\${Partition}:robomaker:\${Region}:\${Account}:simulation-job/\${SimulationJobId} |
| [simulationJobBatch](https://docs.aws.amazon.com/robomaker/latest/dg/simulation-job-batch.html) | arn:\${Partition}:robomaker:\${Region}:\${Account}:simulation-job-batch/\${SimulationJobBatchId} |
| [deploymentJob](https://docs.aws.amazon.com/robomaker/latest/dg/deployment.html) | arn:\${Partition}:robomaker:\${Region}:\${Account}:deployment-job/\${DeploymentJobId} |
| [robot](https://docs.aws.amazon.com/robomaker/latest/dg/fleets.html) | arn:\${Partition}:robomaker:\${Region}:\${Account}:robot/\${RobotName}/\${CreatedOnEpoch} |
| [deploymentFleet](https://docs.aws.amazon.com/robomaker/latest/dg/managing-simulation-applications.html) | arn:\${Partition}:robomaker:\${Region}:\${Account}:deployment-fleet/\${FleetName}/\${CreatedOnEpoch} |
| [worldGenerationJob](https://docs.aws.amazon.com/robomaker/latest/dg/worlds-managing-generation-jobs.html) | arn:\${Partition}:robomaker:\${Region}:\${Account}:world-generation-job/\${WorldGenerationJobId} |
| [worldExportJob](https://docs.aws.amazon.com/robomaker/latest/dg/worlds-managing-export-jobs.html) | arn:\${Partition}:robomaker:\${Region}:\${Account}:world-export-job/\${WorldExportJobId} |
| [worldTemplate](https://docs.aws.amazon.com/robomaker/latest/dg/worlds-managing-simworld-templates.html) | arn:\${Partition}:robomaker:\${Region}:\${Account}:world-template/\${WorldTemplateJobId} |
| [world](https://docs.aws.amazon.com/robomaker/latest/dg/worlds-managing-generated-worlds.html) | arn:\${Partition}:robomaker:\${Region}:\${Account}:world/\${WorldId} |
# Amazon Route 53 Recovery Cluster
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycluster.html
| Service | ARN |
|---------|-----|
| [routingcontrol](https://docs.aws.amazon.com/recovery-cluster/latest/api/routingcontrol.html) | arn:\${Partition}:route53-recovery-control::\${Account}:controlpanel/\${ControlPanelId}/routingcontrol/\${RoutingControlId} |
# Amazon S3 Glacier
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3glacier.html
| Service | ARN |
|---------|-----|
| [vault](https://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-vaults.html) | arn:\${Partition}:glacier:\${Region}:\${Account}:vaults/\${VaultName} |
# Amazon Route 53 Recovery Controls
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoverycontrols.html
| Service | ARN |
|---------|-----|
| [cluster](https://docs.aws.amazon.com/recovery-cluster/latest/api/cluster.html) | arn:\${Partition}:route53-recovery-control::\${Account}:cluster/\${ResourceId} |
| [controlpanel](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel.html) | arn:\${Partition}:route53-recovery-control::\${Account}:controlpanel/\${ControlPanelId} |
| [routingcontrol](https://docs.aws.amazon.com/recovery-cluster/latest/api/routingcontrol.html) | arn:\${Partition}:route53-recovery-control::\${Account}:controlpanel/\${ControlPanelId}/routingcontrol/\${RoutingControlId} |
| [safetyrule](https://docs.aws.amazon.com/recovery-cluster/latest/api/safetyrule.html) | arn:\${Partition}:route53-recovery-control::\${Account}:controlpanel/\${ControlPanelId}/safetyrule/\${SafetyRuleId} |
# Amazon Route 53 Resolver
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53resolver.html
| Service | ARN |
|---------|-----|
| [resolver-dnssec-config](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/access-control-overview.html#access-control-resources) | arn:\${Partition}:route53resolver:\${Region}:\${Account}:resolver-dnssec-config/\${ResourceId} |
| [resolver-query-log-config](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/access-control-overview.html#access-control-resources) | arn:\${Partition}:route53resolver:\${Region}:\${Account}:resolver-query-log-config/\${ResourceId} |
| [resolver-rule](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/access-control-overview.html#access-control-resources) | arn:\${Partition}:route53resolver:\${Region}:\${Account}:resolver-rule/\${ResourceId} |
| [resolver-endpoint](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/access-control-overview.html#access-control-resources) | arn:\${Partition}:route53resolver:\${Region}:\${Account}:resolver-endpoint/\${ResourceId} |
| [firewall-rule-group](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/access-control-overview.html#access-control-resources) | arn:\${Partition}:route53resolver:\${Region}:\${Account}:firewall-rule-group/\${ResourceId} |
| [firewall-rule-group-association](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/access-control-overview.html#access-control-resources) | arn:\${Partition}:route53resolver:\${Region}:\${Account}:firewall-rule-group-association/\${ResourceId} |
| [firewall-domain-list](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/access-control-overview.html#access-control-resources) | arn:\${Partition}:route53resolver:\${Region}:\${Account}:firewall-domain-list/\${ResourceId} |
| [firewall-config](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/access-control-overview.html#access-control-resources) | arn:\${Partition}:route53resolver:\${Region}:\${Account}:firewall-config/\${ResourceId} |
| [resolver-config](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/access-control-overview.html#access-control-resources) | arn:\${Partition}:route53resolver:\${Region}:\${Account}:resolver-config/\${ResourceId} |
| [outpost-resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/access-control-overview.html#access-control-resources) | arn:\${Partition}:route53resolver:\${Region}:\${Account}:outpost-resolver/\${ResourceId} |
# Amazon Route 53 Profiles enables sharing DNS settings with VPCs
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53profilesenablessharingdnssettingswithvpcs.html
| Service | ARN |
|---------|-----|
| [profile](https://docs.aws.amazon.com/Route53/latest/APIReference/#access-control-resources) | arn:\${Partition}:route53profiles:\${Region}:\${Account}:profile/\${ResourceId} |
| [profile-association](https://docs.aws.amazon.com/Route53/latest/APIReference/#access-control-resources) | arn:\${Partition}:route53profiles:\${Region}:\${Account}:profile-association/\${ResourceId} |
# Amazon S3 Express
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3express.html
| Service | ARN |
|---------|-----|
| [bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-zonal-buckets.html) | arn:\${Partition}:s3express:\${Region}:\${Account}:bucket/\${BucketName} |
# Amazon Route 53 Recovery Readiness
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53recoveryreadiness.html
| Service | ARN |
|---------|-----|
| [readinesscheck](https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.readiness-checks.html) | arn:\${Partition}:route53-recovery-readiness::\${Account}:readiness-check/\${ResourceId} |
| [resourceset](https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.readiness-checks.html) | arn:\${Partition}:route53-recovery-readiness::\${Account}:resource-set/\${ResourceId} |
| [cell](https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.recovery-groups.html) | arn:\${Partition}:route53-recovery-readiness::\${Account}:cell/\${ResourceId} |
| [recoverygroup](https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.recovery-groups.html) | arn:\${Partition}:route53-recovery-readiness::\${Account}:recovery-group/\${ResourceId} |
# AWS Savings Plans
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssavingsplans.html
| Service | ARN |
|---------|-----|
| [savingsplan](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html) | arn:\${Partition}:savingsplans::\${Account}:savingsplan/\${ResourceId} |
# Amazon S3 Object Lambda
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3objectlambda.html
| Service | ARN |
|---------|-----|
| [objectlambdaaccesspoint](https://docs.aws.amazon.com/AmazonS3/latest/dev/transforming-objects.html) | arn:\${Partition}:s3-object-lambda:\${Region}:\${Account}:accesspoint/\${AccessPointName} |
# Amazon S3 on Outposts
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3onoutposts.html
| Service | ARN |
|---------|-----|
| [accesspoint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html) | arn:\${Partition}:s3-outposts:\${Region}:\${Account}:outpost/\${OutpostId}/accesspoint/\${AccessPointName} |
| [bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html) | arn:\${Partition}:s3-outposts:\${Region}:\${Account}:outpost/\${OutpostId}/bucket/\${BucketName} |
| [endpoint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/outposts-endpoints.html) | arn:\${Partition}:s3-outposts:\${Region}:\${Account}:outpost/\${OutpostId}/endpoint/\${EndpointId} |
| [object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingObjects.html) | arn:\${Partition}:s3-outposts:\${Region}:\${Account}:outpost/\${OutpostId}/bucket/\${BucketName}/object/\${ObjectName} |
# AWS Secrets Manager
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssecretsmanager.html
| Service | ARN |
|---------|-----|
| [Secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#iam-resources) | arn:\${Partition}:secretsmanager:\${Region}:\${Account}:secret:\${SecretId} |
# AWS Server Migration Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsservermigrationservice.html
| Service | ARN |
|---------|-----|
# Amazon SageMaker Ground Truth Synthetic
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsagemakergroundtruthsynthetic.html
| Service | ARN |
|---------|-----|
# Amazon Security Lake
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsecuritylake.html
| Service | ARN |
|---------|-----|
| [data-lake](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DataLakeResource.html) | arn:\${Partition}:securitylake:\${Region}:\${Account}:data-lake/default |
| [subscriber](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_SubscriberResource.html) | arn:\${Partition}:securitylake:\${Region}:\${Account}:subscriber/\${SubscriberId} |
# Amazon SageMaker geospatial capabilities
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsagemakergeospatialcapabilities.html
| Service | ARN |
|---------|-----|
| [EarthObservationJob](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-eoj.html) | arn:\${Partition}:sagemaker-geospatial:\${Region}:\${Account}:earth-observation-job/\${JobID} |
| [RasterDataCollection](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-data-collections.html) | arn:\${Partition}:sagemaker-geospatial:\${Region}:\${Account}:raster-data-collection/\${CollectionID} |
| [VectorEnrichmentJob](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-vej.html) | arn:\${Partition}:sagemaker-geospatial:\${Region}:\${Account}:vector-enrichment-job/\${JobID} |
# AWS Security Hub
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssecurityhub.html
| Service | ARN |
|---------|-----|
| [hub](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-access.html#resources) | arn:\${Partition}:securityhub:\${Region}:\${Account}:hub/default |
| [product](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-access.html#resources) | arn:\${Partition}:securityhub:\${Region}:\${Account}:product/\${Company}/\${ProductId} |
| [finding-aggregator](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-access.html#resources) | arn:\${Partition}:securityhub:\${Region}:\${Account}:finding-aggregator/\${FindingAggregatorId} |
| [automation-rule](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules) | arn:\${Partition}:securityhub:\${Region}:\${Account}:automation-rule/\${AutomationRuleId} |
| [configuration-policy](https://docs.aws.amazon.com/securityhub/latest/userguide/central-configuration-intro.html) | arn:\${Partition}:securityhub:\${Region}:\${Account}:configuration-policy/\${ConfigurationPolicyId} |
# AWS Serverless Application Repository
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsserverlessapplicationrepository.html
| Service | ARN |
|---------|-----|
| [applications](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications.html) | arn:\${Partition}:serverlessrepo:\${Region}:\${Account}:applications/\${ResourceId} |
# AWS Security Token Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssecuritytokenservice.html
| Service | ARN |
|---------|-----|
| [role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) | arn:\${Partition}:iam::\${Account}:role/\${RoleNameWithPath} |
| [user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html) | arn:\${Partition}:iam::\${Account}:user/\${UserNameWithPath} |
| [self-session](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns) | arn:\${Partition}:sts::\${Account}:self |
# AWS service providing managed private networks
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsserviceprovidingmanagedprivatenetworks.html
| Service | ARN |
|---------|-----|
| [network](https://docs.aws.amazon.com/private-networks/latest/userguide/identity-access-management.html) | arn:\${Partition}:private-networks:\${Region}:\${Account}:network/\${NetworkName} |
| [network-site](https://docs.aws.amazon.com/private-networks/latest/userguide/identity-access-management.html) | arn:\${Partition}:private-networks:\${Region}:\${Account}:network-site/\${NetworkName}/\${NetworkSiteName} |
| [network-resource](https://docs.aws.amazon.com/private-networks/latest/userguide/identity-access-management.html) | arn:\${Partition}:private-networks:\${Region}:\${Account}:network-resource/\${NetworkName}/\${ResourceId} |
| [order](https://docs.aws.amazon.com/private-networks/latest/userguide/identity-access-management.html) | arn:\${Partition}:private-networks:\${Region}:\${Account}:order/\${NetworkName}/\${OrderId} |
| [device-identifier](https://docs.aws.amazon.com/private-networks/latest/userguide/identity-access-management.html) | arn:\${Partition}:private-networks:\${Region}:\${Account}:device-identifier/\${NetworkName}/\${DeviceId} |
# AWS Signin
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssignin.html
| Service | ARN |
|---------|-----|
# AWS Signer
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssigner.html
| Service | ARN |
|---------|-----|
| [signing-profile](https://docs.aws.amazon.com/signer/latest/developerguide/gs-profile.html) | arn:\${Partition}:signer:\${Region}:\${Account}:/signing-profiles/\${ProfileName} |
| [signing-job](https://docs.aws.amazon.com/signer/latest/developerguide/gs-job.html) | arn:\${Partition}:signer:\${Region}:\${Account}:/signing-jobs/\${JobId} |
# Amazon SimpleDB
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsimpledb.html
| Service | ARN |
|---------|-----|
| [domain](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/DataModel.html) | arn:\${Partition}:sdb:\${Region}:\${Account}:domain/\${DomainName} |
# AWS SimSpace Weaver
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssimspaceweaver.html
| Service | ARN |
|---------|-----|
| [Simulation](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_configuring-simulation.html) | arn:\${Partition}:simspaceweaver:\${Region}:\${Account}:simulation/\${SimulationName} |
# AWS Service Catalog
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsservicecatalog.html
| Service | ARN |
|---------|-----|
| [Application](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_CreateApplication.html) | arn:\${Partition}:servicecatalog:\${Region}:\${Account}:/applications/\${ApplicationId} |
| [AttributeGroup](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_CreateAttributeGroup.html) | arn:\${Partition}:servicecatalog:\${Region}:\${Account}:/attribute-groups/\${AttributeGroupId} |
| [Portfolio](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_PortfolioDetail.html) | arn:\${Partition}:catalog:\${Region}:\${Account}:portfolio/\${PortfolioId} |
| [Product](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ProductViewDetail.html) | arn:\${Partition}:catalog:\${Region}:\${Account}:product/\${ProductId} |
# AWS Shield
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsshield.html
| Service | ARN |
|---------|-----|
| [attack](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_AttackDetail.html) | arn:\${Partition}:shield::\${Account}:attack/\${Id} |
| [protection](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_Protection.html) | arn:\${Partition}:shield::\${Account}:protection/\${Id} |
| [protection-group](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ProtectionGroup.html) | arn:\${Partition}:shield::\${Account}:protection-group/\${Id} |
# Amazon SES
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonses.html
| Service | ARN |
|---------|-----|
| [configuration-set](https://docs.aws.amazon.com/ses/latest/APIReference/API_ConfigurationSet.html) | arn:\${Partition}:ses:\${Region}:\${Account}:configuration-set/\${ConfigurationSetName} |
| [custom-verification-email-template](https://docs.aws.amazon.com/ses/latest/APIReference/API_CustomVerificationEmailTemplate.html) | arn:\${Partition}:ses:\${Region}:\${Account}:custom-verification-email-template/\${TemplateName} |
| [identity](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_IdentityInfo.html) | arn:\${Partition}:ses:\${Region}:\${Account}:identity/\${IdentityName} |
| [template](https://docs.aws.amazon.com/ses/latest/APIReference/API_Template.html) | arn:\${Partition}:ses:\${Region}:\${Account}:template/\${TemplateName} |
# AWS Snow Device Management
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssnowdevicemanagement.html
| Service | ARN |
|---------|-----|
| [managed-device](https://docs.aws.amazon.com/snowball/latest/snowcone-guide/aws-sdms.html) | arn:\${Partition}:snow-device-management:\${Region}:\${Account}:managed-device/\${ResourceId} |
| [task](https://docs.aws.amazon.com/snowball/latest/snowcone-guide/aws-sdms.html) | arn:\${Partition}:snow-device-management:\${Region}:\${Account}:task/\${ResourceId} |
# AWS Snowball
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssnowball.html
| Service | ARN |
|---------|-----|
# Service Quotas
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_servicequotas.html
| Service | ARN |
|---------|-----|
| [quota](https://docs.aws.amazon.com/servicequotas/latest/userguide/identity-access-management.html#resources) | arn:\${Partition}:servicequotas:\${Region}:\${Account}:\${ServiceCode}/\${QuotaCode} |
# Amazon Simple Email Service v2
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsimpleemailservicev2.html
| Service | ARN |
|---------|-----|
| [configuration-set](https://docs.aws.amazon.com/ses/latest/APIReference/API_ConfigurationSet.html) | arn:\${Partition}:ses:\${Region}:\${Account}:configuration-set/\${ConfigurationSetName} |
| [contact-list](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ContactList.html) | arn:\${Partition}:ses:\${Region}:\${Account}:contact-list/\${ContactListName} |
| [custom-verification-email-template](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_CustomVerificationEmailTemplateMetadata.html) | arn:\${Partition}:ses:\${Region}:\${Account}:custom-verification-email-template/\${TemplateName} |
| [dedicated-ip-pool](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_DedicatedIp.html) | arn:\${Partition}:ses:\${Region}:\${Account}:dedicated-ip-pool/\${DedicatedIPPool} |
| [deliverability-test-report](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_DeliverabilityTestReport.html) | arn:\${Partition}:ses:\${Region}:\${Account}:deliverability-test-report/\${ReportId} |
| [export-job](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ExportJobSummary.html) | arn:\${Partition}:ses:\${Region}:\${Account}:export-job/\${ExportJobId} |
| [identity](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_IdentityInfo.html) | arn:\${Partition}:ses:\${Region}:\${Account}:identity/\${IdentityName} |
| [import-job](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ImportJobSummary.html) | arn:\${Partition}:ses:\${Region}:\${Account}:import-job/\${ImportJobId} |
| [template](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_Template.html) | arn:\${Partition}:ses:\${Region}:\${Account}:template/\${TemplateName} |
# Amazon Simple Workflow Service
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsimpleworkflowservice.html
| Service | ARN |
|---------|-----|
| [domain](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-domains.html) | arn:\${Partition}:swf::\${Account}:/domain/\${DomainName} |
# Amazon S3
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html
| Service | ARN |
|---------|-----|
| [accesspoint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html) | arn:\${Partition}:s3:\${Region}:\${Account}:accesspoint/\${AccessPointName} |
| [bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html) | arn:\${Partition}:s3:::\${BucketName} |
| [object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingObjects.html) | arn:\${Partition}:s3:::\${BucketName}/\${ObjectName} |
| [job](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-managing-jobs.html) | arn:\${Partition}:s3:\${Region}:\${Account}:job/\${JobId} |
| [storagelensconfiguration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens.html) | arn:\${Partition}:s3:\${Region}:\${Account}:storage-lens/\${ConfigId} |
| [storagelensgroup](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_group.html) | arn:\${Partition}:s3:\${Region}:\${Account}:storage-lens-group/\${Name} |
| [objectlambdaaccesspoint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transforming-objects.html) | arn:\${Partition}:s3-object-lambda:\${Region}:\${Account}:accesspoint/\${AccessPointName} |
| [multiregionaccesspoint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRequests.html) | arn:\${Partition}:s3::\${Account}:accesspoint/\${AccessPointAlias} |
| [multiregionaccesspointrequestarn](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRequests.html) | arn:\${Partition}:s3:us-west-2:\${Account}:async-request/mrap/\${Operation}/\${Token} |
| [accessgrantsinstance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-instance.html) | arn:\${Partition}:s3:\${Region}:\${Account}:access-grants/default |
| [accessgrantslocation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-location.html) | arn:\${Partition}:s3:\${Region}:\${Account}:access-grants/default/location/\${Token} |
| [accessgrant](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-grant.html) | arn:\${Partition}:s3:\${Region}:\${Account}:access-grants/default/grant/\${Token} |
# Amazon SNS
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsns.html
| Service | ARN |
|---------|-----|
| [topic](https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html) | arn:\${Partition}:sns:\${Region}:\${Account}:\${TopicName} |
# AWS Support
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupport.html
| Service | ARN |
|---------|-----|
# Amazon SQS
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsqs.html
| Service | ARN |
|---------|-----|
| [queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-types.html) | arn:\${Partition}:sqs:\${Region}:\${Account}:\${QueueName} |
# AWS Step Functions
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsstepfunctions.html
| Service | ARN |
|---------|-----|
| [activity](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-activities.html) | arn:\${Partition}:states:\${Region}:\${Account}:activity:\${ActivityName} |
| [execution](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-executions.html) | arn:\${Partition}:states:\${Region}:\${Account}:execution:\${StateMachineName}:\${ExecutionId} |
| [express](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-executions.html) | arn:\${Partition}:states:\${Region}:\${Account}:express:\${StateMachineName}:\${ExecutionId}:\${ExpressId} |
| [statemachine](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html) | arn:\${Partition}:states:\${Region}:\${Account}:stateMachine:\${StateMachineName} |
| [statemachineversion](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-cd-aliasing-versioning.html) | arn:\${Partition}:states:\${Region}:\${Account}:stateMachine:\${StateMachineName}:\${StateMachineVersionId} |
| [statemachinealias](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-cd-aliasing-versioning.html) | arn:\${Partition}:states:\${Region}:\${Account}:stateMachine:\${StateMachineName}:\${StateMachineAliasName} |
| [maprun](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-examine-map-run.html) | arn:\${Partition}:states:\${Region}:\${Account}:mapRun:\${StateMachineName}/\${MapRunLabel}:\${MapRunId} |
| [labelled execution](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-examine-map-run.html) | arn:\${Partition}:states:\${Region}:\${Account}:execution:\${StateMachineName}/\${MapRunLabel}:\${ExecutionId} |
| [labelled express](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-examine-map-run.html) | arn:\${Partition}:states:\${Region}:\${Account}:express:\${StateMachineName}/\${MapRunLabel}:\${ExecutionId}:\${ExpressId} |
# AWS Sustainability
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssustainability.html
| Service | ARN |
|---------|-----|
# AWS Support Plans
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupportplans.html
| Service | ARN |
|---------|-----|
# AWS Support App in Slack
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupportappinslack.html
| Service | ARN |
|---------|-----|
# AWS SQL Workbench
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssqlworkbench.html
| Service | ARN |
|---------|-----|
| [connection](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html) | arn:\${Partition}:sqlworkbench:\${Region}:\${Account}:connection/\${ResourceId} |
| [query](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html) | arn:\${Partition}:sqlworkbench:\${Region}:\${Account}:query/\${ResourceId} |
| [chart](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html) | arn:\${Partition}:sqlworkbench:\${Region}:\${Account}:chart/\${ResourceId} |
| [notebook](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html) | arn:\${Partition}:sqlworkbench:\${Region}:\${Account}:notebook/\${ResourceId} |
# AWS Supply Chain
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html
| Service | ARN |
|---------|-----|
| [instance](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html) | arn:\${Partition}:scn:\${Region}:\${Account}:instance/\${InstanceId} |
| [bill-of-materials-import-job](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html) | arn:\${Partition}:scn:\${Region}:\${Account}:instance/\${InstanceId}/bill-of-materials-import-job/\${JobId} |
# AWS Systems Manager GUI Connect
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssystemsmanagerguiconnect.html
| Service | ARN |
|---------|-----|
# AWS Systems Manager for SAP
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssystemsmanagerforsap.html
| Service | ARN |
|---------|-----|
| [application](https://docs.aws.amazon.com/systems-manager/index.html) | arn:\${Partition}:ssm-sap:\${Region}:\${Account}:\${ApplicationType}/\${ApplicationId} |
| [component](https://docs.aws.amazon.com/systems-manager/index.html) | arn:\${Partition}:ssm-sap:\${Region}:\${Account}:\${ApplicationType}/\${ApplicationId}/COMPONENT/\${ComponentId} |
| [database](https://docs.aws.amazon.com/systems-manager/index.html) | arn:\${Partition}:ssm-sap:\${Region}:\${Account}:\${ApplicationType}/\${ApplicationId}/DB/\${DatabaseId} |
# Tag Editor
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_tageditor.html
| Service | ARN |
|---------|-----|
# AWS Storage Gateway
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsstoragegateway.html
| Service | ARN |
|---------|-----|
| [device](https://docs.aws.amazon.com/storagegateway/latest/userguide/resource_vtl-devices.html) | arn:\${Partition}:storagegateway:\${Region}:\${Account}:gateway/\${GatewayId}/device/\${Vtldevice} |
| [fs-association](https://docs.aws.amazon.com/storagegateway/latest/userguide/API_AssociateFileSystem.html) | arn:\${Partition}:storagegateway:\${Region}:\${Account}:fs-association/\${FsaId} |
| [gateway](https://docs.aws.amazon.com/storagegateway/latest/userguide/StorageGatewayConcepts.html) | arn:\${Partition}:storagegateway:\${Region}:\${Account}:gateway/\${GatewayId} |
| [share](https://docs.aws.amazon.com/storagegateway/latest/userguide/GettingStartedCreateFileShare.html) | arn:\${Partition}:storagegateway:\${Region}:\${Account}:share/\${ShareId} |
| [tape](https://docs.aws.amazon.com/storagegateway/latest/userguide/StorageGatewayConcepts.html#storage-gateway-vtl-concepts) | arn:\${Partition}:storagegateway:\${Region}:\${Account}:tape/\${TapeBarcode} |
| [tapepool](https://docs.aws.amazon.com/storagegateway/latest/userguide/CreatingCustomTapePool.html) | arn:\${Partition}:storagegateway:\${Region}:\${Account}:tapepool/\${PoolId} |
| [target](https://docs.aws.amazon.com/storagegateway/latest/userguide/GettingStartedCreateVolumes.html) | arn:\${Partition}:storagegateway:\${Region}:\${Account}:gateway/\${GatewayId}/target/\${IscsiTarget} |
| [volume](https://docs.aws.amazon.com/storagegateway/latest/userguide/StorageGatewayConcepts.html#volume-gateway-concepts) | arn:\${Partition}:storagegateway:\${Region}:\${Account}:gateway/\${GatewayId}/volume/\${VolumeId} |
# Amazon SageMaker
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsagemaker.html
| Service | ARN |
|---------|-----|
| [device](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-edge-devices.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:device-fleet/\${DeviceFleetName}/device/\${DeviceName} |
| [device-fleet](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-device-fleet.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:device-fleet/\${DeviceFleetName} |
| [edge-packaging-job](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-packaging-job.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:edge-packaging-job/\${EdgePackagingJobName} |
| [edge-deployment-plan](https://docs.aws.amazon.com/sagemaker/latest/dg/edge.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:edge-deployment/\${EdgeDeploymentPlanName} |
| [human-loop](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-start-human-loop.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:human-loop/\${HumanLoopName} |
| [flow-definition](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-create-flow-definition.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:flow-definition/\${FlowDefinitionName} |
| [human-task-ui](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-instructions-overview.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:human-task-ui/\${HumanTaskUiName} |
| [hub](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-content-sharing.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:hub/\${HubName} |
| [hub-content](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-content-sharing.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:hub-content/\${HubName}/\${HubContentType}/\${HubContentName} |
| [inference-recommendations-job](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender-recommendation-jobs.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:inference-recommendations-job/\${InferenceRecommendationsJobName} |
| [inference-experiment](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-experiment.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:inference-experiment/\${InferenceExperimentName} |
| [labeling-job](https://docs.aws.amazon.com/sagemaker/latest/dg/sms.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:labeling-job/\${LabelingJobName} |
| [workteam](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:workteam/\${WorkteamName} |
| [workforce](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:workforce/\${WorkforceName} |
| [domain](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-entity-status.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:domain/\${DomainId} |
| [user-profile](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-entity-status.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:user-profile/\${DomainId}/\${UserProfileName} |
| [space](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-entity-status.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:space/\${DomainId}/\${SpaceName} |
| [app](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-entity-status.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:app/\${DomainId}/\${UserProfileName}/\${AppType}/\${AppName} |
| [app-image-config](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi-create.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:app-image-config/\${AppImageConfigName} |
| [studio-lifecycle-config](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lcc.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:studio-lifecycle-config/\${StudioLifecycleConfigName} |
| [notebook-instance](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:notebook-instance/\${NotebookInstanceName} |
| [notebook-instance-lifecycle-config](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:notebook-instance-lifecycle-config/\${NotebookInstanceLifecycleConfigName} |
| [code-repository](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:code-repository/\${CodeRepositoryName} |
| [image](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:image/\${ImageName} |
| [image-version](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:image-version/\${ImageName}/\${Version} |
| [algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/algorithms-choose.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:algorithm/\${AlgorithmName} |
| [cluster](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-cluster.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:cluster/\${ClusterId} |
| [training-job](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-training.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:training-job/\${TrainingJobName} |
| [processing-job](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:processing-job/\${ProcessingJobName} |
| [hyper-parameter-tuning-job](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-how-it-works.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:hyper-parameter-tuning-job/\${HyperParameterTuningJobName} |
| [project](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects-whatis.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:project/\${ProjectName} |
| [model-package](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelPackage.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:model-package/\${ModelPackageName} |
| [model-package-group](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-model-group.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:model-package-group/\${ModelPackageGroupName} |
| [model](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:model/\${ModelName} |
| [endpoint-config](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:endpoint-config/\${EndpointConfigName} |
| [endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:endpoint/\${EndpointName} |
| [inference-component](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:inference-component/\${InferenceComponentName} |
| [transform-job](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TransformJob.html.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:transform-job/\${TransformJobName} |
| [compilation-job](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CompilationJobSummary.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:compilation-job/\${CompilationJobName} |
| [automl-job](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:automl-job/\${AutoMLJobJobName} |
| [monitoring-schedule](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-scheduling.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:monitoring-schedule/\${MonitoringScheduleName} |
| [monitoring-schedule-alert](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-scheduling.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:monitoring-schedule/\${MonitoringScheduleName}/alert/\${MonitoringScheduleAlertName} |
| [data-quality-job-definition](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-quality.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:data-quality-job-definition/\${DataQualityJobDefinitionName} |
| [model-quality-job-definition](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:model-quality-job-definition/\${ModelQualityJobDefinitionName} |
| [model-bias-job-definition](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-detect-post-training-bias.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:model-bias-job-definition/\${ModelBiasJobDefinitionName} |
| [model-explainability-job-definition](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-explainability.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:model-explainability-job-definition/\${ModelExplainabilityJobDefinitionName} |
| [experiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Experiment.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:experiment/\${ExperimentName} |
| [experiment-trial](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Trial.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:experiment-trial/\${TrialName} |
| [experiment-trial-component](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrialComponent.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:experiment-trial-component/\${TrialComponentName} |
| [feature-group](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:feature-group/\${FeatureGroupName} |
| [pipeline](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Pipeline.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:pipeline/\${PipelineName} |
| [pipeline-execution](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PipelineExecution.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:pipeline/\${PipelineName}/execution/\${RandomString} |
| [artifact](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ArtifactSummary.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:artifact/\${HashOfArtifactSource} |
| [context](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContextSummary.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:context/\${ContextName} |
| [action](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ActionSummary.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:action/\${ActionName} |
| [lineage-group](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_LineageGroupSummary.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:lineage-group/\${LineageGroupName} |
| [model-card](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelCard.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:model-card/\${ModelCardName} |
| [model-card-export-job](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelCardExportJob.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:model-card/\${ModelCardName}/export-job/\${ExportJobName} |
| [shared-model](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-collaborate-permissions.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:shared-model/\${SharedModelId} |
| [shared-model-event](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-collaborate-permissions.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:shared-model-event/\${EventId} |
| [sagemaker-catalog](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceCatalog.html) | arn:\${Partition}:sagemaker:\${Region}:\${Account}:sagemaker-catalog/\${ResourceCatalogName} |
# AWS Tax Settings
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awstaxsettings.html
| Service | ARN |
|---------|-----|
# AWS Systems Manager Incident Manager
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssystemsmanagerincidentmanager.html
| Service | ARN |
|---------|-----|
| [response-plan](https://docs.aws.amazon.com/incident-manager/latest/userguide/response-plans.html) | arn:\${Partition}:ssm-incidents::\${Account}:response-plan/\${ResponsePlan} |
| [incident-record](https://docs.aws.amazon.com/incident-manager/latest/userguide/tracking-details.html) | arn:\${Partition}:ssm-incidents::\${Account}:incident-record/\${ResponsePlan}/\${IncidentRecord} |
| [replication-set](https://docs.aws.amazon.com/incident-manager/latest/userguide/disaster-recovery-resiliency.html#replication) | arn:\${Partition}:ssm-incidents::\${Account}:replication-set/\${ReplicationSet} |
# Amazon Timestream InfluxDB
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazontimestreaminfluxdb.html
| Service | ARN |
|---------|-----|
| [db-instance](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_DbInstanceSummary.html) | arn:\${Partition}:timestream-influxdb:\${Region}:\${Account}:db-instance/\${DbInstanceIdentifier} |
| [db-parameter-group](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_DbParameterGroupSummary.html) | arn:\${Partition}:timestream-influxdb:\${Region}:\${Account}:db-parameter-group/\${DbParameterGroupIdentifier} |
# AWS Tiros
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awstiros.html
| Service | ARN |
|---------|-----|
# AWS Telco Network Builder
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awstelconetworkbuilder.html
| Service | ARN |
|---------|-----|
| [function-package](https://docs.aws.amazon.com/tnb/latest/ug/function-packages.html) | arn:\${Partition}:tnb:\${Region}:\${Account}:function-package/\${FunctionPackageId} |
| [network-package](https://docs.aws.amazon.com/tnb/latest/ug/network-packages.html) | arn:\${Partition}:tnb:\${Region}:\${Account}:network-package/\${NetworkPackageId} |
| [network-instance](https://docs.aws.amazon.com/tnb/latest/ug/network-instances.html) | arn:\${Partition}:tnb:\${Region}:\${Account}:network-instance/\${NetworkInstanceId} |
| [function-instance](https://docs.aws.amazon.com/tnb/latest/ug/function-packages.html) | arn:\${Partition}:tnb:\${Region}:\${Account}:function-instance/\${FunctionInstanceId} |
| [network-operation](https://docs.aws.amazon.com/tnb/latest/ug/network-operations.html) | arn:\${Partition}:tnb:\${Region}:\${Account}:network-operation/\${NetworkOperationId} |
# AWS Systems Manager Incident Manager Contacts
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssystemsmanagerincidentmanagercontacts.html
| Service | ARN |
|---------|-----|
| [contact](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html) | arn:\${Partition}:ssm-contacts:\${Region}:\${Account}:contact/\${ContactAlias} |
| [contactchannel](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html) | arn:\${Partition}:ssm-contacts:\${Region}:\${Account}:contactchannel/\${ContactAlias}/\${ContactChannelId} |
| [engagement](https://docs.aws.amazon.com/incident-manager/latest/userguide/escalation.html) | arn:\${Partition}:ssm-contacts:\${Region}:\${Account}:engagement/\${ContactAlias}/\${EngagementId} |
| [page](https://docs.aws.amazon.com/incident-manager/latest/userguide/escalation.html) | arn:\${Partition}:ssm-contacts:\${Region}:\${Account}:page/\${ContactAlias}/\${PageId} |
| [rotation](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-on-call-schedule.html) | arn:\${Partition}:ssm-contacts:\${Region}:\${Account}:rotation/\${RotationId} |
# Amazon Transcribe
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazontranscribe.html
| Service | ARN |
|---------|-----|
| [transcriptionjob](https://docs.aws.amazon.com/transcribe/latest/dg/API_TranscriptionJob.html) | arn:\${Partition}:transcribe:\${Region}:\${Account}:transcription-job/\${JobName} |
| [vocabulary](https://docs.aws.amazon.com/transcribe/latest/dg/API_CreateVocabulary.html) | arn:\${Partition}:transcribe:\${Region}:\${Account}:vocabulary/\${VocabularyName} |
| [vocabularyfilter](https://docs.aws.amazon.com/transcribe/latest/dg/API_CreateVocabularyFilter.html) | arn:\${Partition}:transcribe:\${Region}:\${Account}:vocabulary-filter/\${VocabularyFilterName} |
| [languagemodel](https://docs.aws.amazon.com/transcribe/latest/dg/API_LanguageModel.html) | arn:\${Partition}:transcribe:\${Region}:\${Account}:language-model/\${ModelName} |
| [medicaltranscriptionjob](https://docs.aws.amazon.com/transcribe/latest/dg/API_MedicalTranscriptionJob.html) | arn:\${Partition}:transcribe:\${Region}:\${Account}:medical-transcription-job/\${JobName} |
| [medicalvocabulary](https://docs.aws.amazon.com/transcribe/latest/dg/API_CreateMedicalVocabulary.html) | arn:\${Partition}:transcribe:\${Region}:\${Account}:medical-vocabulary/\${VocabularyName} |
| [callanalyticsjob](https://docs.aws.amazon.com/transcribe/latest/dg/API_CallAnalyticsJob.html) | arn:\${Partition}:transcribe:\${Region}:\${Account}:analytics-job/\${JobName} |
| [callanalyticscategory](https://docs.aws.amazon.com/transcribe/latest/dg/API_CreateCallAnalyticsCategory.html) | arn:\${Partition}:transcribe:\${Region}:\${Account}:analytics-category/\${CategoryName} |
| [medicalscribejob](https://docs.aws.amazon.com/transcribe/latest/dg/API_MedicalScribeJob.html) | arn:\${Partition}:transcribe:\${Region}:\${Account}:medical-scribe-job/\${JobName} |
# Amazon Translate
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazontranslate.html
| Service | ARN |
|---------|-----|
| [terminology](https://docs.aws.amazon.com/translate/latest/dg/how-custom-terminology.html) | arn:\${Partition}:translate:\${Region}:\${Account}:terminology/\${ResourceName} |
| [parallel-data](https://docs.aws.amazon.com/translate/latest/dg/customizing-translations-parallel-data.html) | arn:\${Partition}:translate:\${Region}:\${Account}:parallel-data/\${ResourceName} |
# Amazon Textract
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazontextract.html
| Service | ARN |
|---------|-----|
| [adapter](https://docs.aws.amazon.com/textract/latest/dg/API_AdapterOverview.html) | arn:\${Partition}:textract:\${Region}:\${Account}:/adapters/\${AdapterId} |
| [adapterversion](https://docs.aws.amazon.com/textract/latest/dg/API_AdapterVersionOverview.html) | arn:\${Partition}:textract:\${Region}:\${Account}:/adapters/\${AdapterId}/versions/\${AdapterVersion} |
# AWS User Notifications Contacts
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsusernotificationscontacts.html
| Service | ARN |
|---------|-----|
| [EmailContactResource](https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html) | arn:\${Partition}:notifications-contacts::\${Account}:emailcontact/\${EmailContactId} |
# Amazon Timestream
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazontimestream.html
| Service | ARN |
|---------|-----|
| [database](https://docs.aws.amazon.com/timestream/latest/developerguide/API_Database.html) | arn:\${Partition}:timestream:\${Region}:\${Account}:database/\${DatabaseName} |
| [table](https://docs.aws.amazon.com/timestream/latest/developerguide/API_Table.html) | arn:\${Partition}:timestream:\${Region}:\${Account}:database/\${DatabaseName}/table/\${TableName} |
| [scheduled-query](https://docs.aws.amazon.com/timestream/latest/developerguide/API_ScheduledQuery.html) | arn:\${Partition}:timestream:\${Region}:\${Account}:scheduled-query/\${ScheduledQueryName} |
# AWS Verified Access
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsverifiedaccess.html
| Service | ARN |
|---------|-----|
# AWS Trusted Advisor
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awstrustedadvisor.html
| Service | ARN |
|---------|-----|
| [checks](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_TrustedAdvisorCheckDescription.html) | arn:\${Partition}:trustedadvisor:\${Region}:\${Account}:checks/\${CategoryCode}/\${CheckId} |
# AWS User Notifications
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsusernotifications.html
| Service | ARN |
|---------|-----|
| [EventRule](https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html) | arn:\${Partition}:notifications::\${Account}:configuration/\${NotificationConfigurationId}/rule/\${EventRuleId} |
| [NotificationConfiguration](https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html) | arn:\${Partition}:notifications::\${Account}:configuration/\${NotificationConfigurationId} |
| [NotificationEvent](https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html) | arn:\${Partition}:notifications:\${Region}:\${Account}:configuration/\${NotificationConfigurationId}/event/\${NotificationEventId} |
# AWS Transfer Family
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awstransferfamily.html
| Service | ARN |
|---------|-----|
| [user](https://docs.aws.amazon.com/transfer/latest/userguide/create-user.html) | arn:\${Partition}:transfer:\${Region}:\${Account}:user/\${ServerId}/\${UserName} |
| [server](https://docs.aws.amazon.com/transfer/latest/userguide/configuring-servers.html) | arn:\${Partition}:transfer:\${Region}:\${Account}:server/\${ServerId} |
| [workflow](https://docs.aws.amazon.com/transfer/latest/userguide/transfer-workflows.html) | arn:\${Partition}:transfer:\${Region}:\${Account}:workflow/\${WorkflowId} |
| [certificate](https://docs.aws.amazon.com/transfer/latest/userguide/create-b2b-server.html) | arn:\${Partition}:transfer:\${Region}:\${Account}:certificate/\${CertificateId} |
| [connector](https://docs.aws.amazon.com/transfer/latest/userguide/create-b2b-server.html) | arn:\${Partition}:transfer:\${Region}:\${Account}:connector/\${ConnectorId} |
| [profile](https://docs.aws.amazon.com/transfer/latest/userguide/create-b2b-server.html) | arn:\${Partition}:transfer:\${Region}:\${Account}:profile/\${ProfileId} |
| [agreement](https://docs.aws.amazon.com/transfer/latest/userguide/create-b2b-server.html) | arn:\${Partition}:transfer:\${Region}:\${Account}:agreement/\${AgreementId} |
| [host-key](https://docs.aws.amazon.com/transfer/latest/userguide/edit-server-config.html) | arn:\${Partition}:transfer:\${Region}:\${Account}:host-key/\${ServerId}/\${HostKeyId} |
# Amazon Verified Permissions
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonverifiedpermissions.html
| Service | ARN |
|---------|-----|
| [policy-store](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/policy-stores.html) | arn:\${Partition}:verifiedpermissions::\${Account}:policy-store/\${PolicyStoreId} |
# Amazon VPC Lattice Services
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonvpclatticeservices.html
| Service | ARN |
|---------|-----|
| [Service](https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html) | arn:\${Partition}:vpc-lattice:\${Region}:\${Account}:service/\${ServiceId}/\${RequestPath} |
# AWS WAF
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awswaf.html
| Service | ARN |
|---------|-----|
| [bytematchset](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ByteMatchSet.html) | arn:\${Partition}:waf::\${Account}:bytematchset/\${Id} |
| [ipset](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_IPSet.html) | arn:\${Partition}:waf::\${Account}:ipset/\${Id} |
| [ratebasedrule](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_RateBasedRule.html) | arn:\${Partition}:waf::\${Account}:ratebasedrule/\${Id} |
| [rule](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_Rule.html) | arn:\${Partition}:waf::\${Account}:rule/\${Id} |
| [sizeconstraintset](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_SizeConstraintSet.html) | arn:\${Partition}:waf::\${Account}:sizeconstraintset/\${Id} |
| [sqlinjectionmatchset](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_SqlInjectionMatchSet.html) | arn:\${Partition}:waf::\${Account}:sqlinjectionset/\${Id} |
| [webacl](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_WebACL.html) | arn:\${Partition}:waf::\${Account}:webacl/\${Id} |
| [xssmatchset](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_XssMatchSet.html) | arn:\${Partition}:waf::\${Account}:xssmatchset/\${Id} |
| [regexmatchset](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_RegexMatchSet.html) | arn:\${Partition}:waf::\${Account}:regexmatch/\${Id} |
| [regexpatternset](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_RegexPatternSet.html) | arn:\${Partition}:waf::\${Account}:regexpatternset/\${Id} |
| [geomatchset](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GeoMatchSet.html) | arn:\${Partition}:waf::\${Account}:geomatchset/\${Id} |
| [rulegroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_RuleGroup.html) | arn:\${Partition}:waf::\${Account}:rulegroup/\${Id} |
# AWS WAF Regional
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awswafregional.html
| Service | ARN |
|---------|-----|
| [bytematchset](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ByteMatchSet.html) | arn:\${Partition}:waf-regional:\${Region}:\${Account}:bytematchset/\${Id} |
| [ipset](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_IPSet.html) | arn:\${Partition}:waf-regional:\${Region}:\${Account}:ipset/\${Id} |
| [loadbalancer/app/](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_WebACL.html) | arn:\${Partition}:elasticloadbalancing:\${Region}:\${Account}:loadbalancer/app/\${LoadBalancerName}/\${LoadBalancerId} |
| [ratebasedrule](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_RateBasedRule.html) | arn:\${Partition}:waf-regional:\${Region}:\${Account}:ratebasedrule/\${Id} |
| [rule](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_Rule.html) | arn:\${Partition}:waf-regional:\${Region}:\${Account}:rule/\${Id} |
| [sizeconstraintset](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_SizeConstraintSet.html) | arn:\${Partition}:waf-regional:\${Region}:\${Account}:sizeconstraintset/\${Id} |
| [sqlinjectionmatchset](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_SqlInjectionMatchSet.html) | arn:\${Partition}:waf-regional:\${Region}:\${Account}:sqlinjectionset/\${Id} |
| [webacl](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_WebACL.html) | arn:\${Partition}:waf-regional:\${Region}:\${Account}:webacl/\${Id} |
| [xssmatchset](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_XssMatchSet.html) | arn:\${Partition}:waf-regional:\${Region}:\${Account}:xssmatchset/\${Id} |
| [regexmatchset](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_RegexMatchSet.html) | arn:\${Partition}:waf-regional:\${Region}:\${Account}:regexmatch/\${Id} |
| [regexpatternset](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_RegexPatternSet.html) | arn:\${Partition}:waf-regional:\${Region}:\${Account}:regexpatternset/\${Id} |
| [geomatchset](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GeoMatchSet.html) | arn:\${Partition}:waf-regional:\${Region}:\${Account}:geomatchset/\${Id} |
| [rulegroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_RuleGroup.html) | arn:\${Partition}:waf-regional:\${Region}:\${Account}:rulegroup/\${Id} |
# Amazon WorkLink
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonworklink.html
| Service | ARN |
|---------|-----|
| [fleet](https://docs.aws.amazon.com/worklink/latest/api/API_CreateFleet.html) | arn:\${Partition}:worklink::\${Account}:fleet/\${FleetName} |
# AWS Wickr
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awswickr.html
| Service | ARN |
|---------|-----|
| [network](https://docs.aws.amazon.com/wickr/latest/adminguide/) | arn:\${Partition}:wickr:\${Region}:\${Account}:network/\${NetworkId} |
# Amazon WorkDocs
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonworkdocs.html
| Service | ARN |
|---------|-----|
| [organization](https://docs.aws.amazon.com/workdocs/latest/adminguide/migration-tool.html) | arn:\${Partition}:workdocs:\${Region}:\${Account}:organization/\${ResourceId} |
# Amazon VPC Lattice
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonvpclattice.html
| Service | ARN |
|---------|-----|
| [ServiceNetwork](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html) | arn:\${Partition}:vpc-lattice:\${Region}:\${Account}:servicenetwork/\${ServiceNetworkId} |
| [Service](https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html) | arn:\${Partition}:vpc-lattice:\${Region}:\${Account}:service/\${ServiceId} |
| [ServiceNetworkVpcAssociation](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-vpc-associations) | arn:\${Partition}:vpc-lattice:\${Region}:\${Account}:servicenetworkvpcassociation/\${ServiceNetworkVpcAssociationId} |
| [ServiceNetworkServiceAssociation](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-service-associations) | arn:\${Partition}:vpc-lattice:\${Region}:\${Account}:servicenetworkserviceassociation/\${ServiceNetworkServiceAssociationId} |
| [TargetGroup](https://docs.aws.amazon.com/vpc-lattice/latest/ug/target-groups.html) | arn:\${Partition}:vpc-lattice:\${Region}:\${Account}:targetgroup/\${TargetGroupId} |
| [Listener](https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html) | arn:\${Partition}:vpc-lattice:\${Region}:\${Account}:service/\${ServiceId}/listener/\${ListenerId} |
| [Rule](https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules) | arn:\${Partition}:vpc-lattice:\${Region}:\${Account}:service/\${ServiceId}/listener/\${ListenerId}/rule/\${RuleId} |
| [AccessLogSubscription](https://docs.aws.amazon.com/vpc-lattice/latest/ug/monitoring-access-logs.html) | arn:\${Partition}:vpc-lattice:\${Region}:\${Account}:accesslogsubscription/\${AccessLogSubscriptionId} |
# Amazon WorkMail Message Flow
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonworkmailmessageflow.html
| Service | ARN |
|---------|-----|
| [RawMessage](https://docs.aws.amazon.com/workmail/latest/adminguide/lambda-content.html) | arn:\${Partition}:workmailmessageflow:\${Region}:\${Account}:message/\${OrganizationId}/\${Context}/\${MessageId} |
# AWS Systems Manager
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssystemsmanager.html
| Service | ARN |
|---------|-----|
| [association](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) | arn:\${Partition}:ssm:\${Region}:\${Account}:association/\${AssociationId} |
| [automation-execution](https://docs.aws.amazon.com/systems-manager/latest/userguide/running-automations.html) | arn:\${Partition}:ssm:\${Region}:\${Account}:automation-execution/\${AutomationExecutionId} |
| [automation-definition](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html) | arn:\${Partition}:ssm:\${Region}:\${Account}:automation-definition/\${AutomationDefinitionName}:\${VersionId} |
| [bucket](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html) | arn:\${Partition}:s3:::\${BucketName} |
| [document](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents.html) | arn:\${Partition}:ssm:\${Region}:\${Account}:document/\${DocumentName} |
| [instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format) | arn:\${Partition}:ec2:\${Region}:\${Account}:instance/\${InstanceId} |
| [maintenancewindow](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-maintenance.html) | arn:\${Partition}:ssm:\${Region}:\${Account}:maintenancewindow/\${ResourceId} |
| [managed-instance](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) | arn:\${Partition}:ssm:\${Region}:\${Account}:managed-instance/\${InstanceId} |
| [managed-instance-inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-inventory-configuring.html) | arn:\${Partition}:ssm:\${Region}:\${Account}:managed-instance-inventory/\${InstanceId} |
| [opsitem](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems.html) | arn:\${Partition}:ssm:\${Region}:\${Account}:opsitem/\${ResourceId} |
| [opsmetadata](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager.html) | arn:\${Partition}:ssm:\${Region}:\${Account}:opsmetadata/\${ResourceId} |
| [parameter](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) | arn:\${Partition}:ssm:\${Region}:\${Account}:parameter/\${ParameterNameWithoutLeadingSlash} |
| [patchbaseline](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) | arn:\${Partition}:ssm:\${Region}:\${Account}:patchbaseline/\${PatchBaselineIdResourceId} |
| [resourcearn](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems.html) | arn:\${Partition}:ssm:\${Region}:\${Account}:opsitemgroup/default |
| [session](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) | arn:\${Partition}:ssm:\${Region}:\${Account}:session/\${SessionId} |
| [resourcedatasync](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-inventory-datasync.html) | arn:\${Partition}:ssm:\${Region}:\${Account}:resource-data-sync/\${SyncName} |
| [servicesetting](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) | arn:\${Partition}:ssm:\${Region}:\${Account}:servicesetting/\${ResourceId} |
| [windowtarget](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-assign-targets.html) | arn:\${Partition}:ssm:\${Region}:\${Account}:windowtarget/\${WindowTargetId} |
| [windowtask](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-assign-tasks.html) | arn:\${Partition}:ssm:\${Region}:\${Account}:windowtask/\${WindowTaskId} |
| [task](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html) | arn:\${Partition}:ecs:\${Region}:\${Account}:task/\${TaskId} |
# AWS Well-Architected Tool
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awswell-architectedtool.html
| Service | ARN |
|---------|-----|
| [workload](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_Workload.html) | arn:\${Partition}:wellarchitected:\${Region}:\${Account}:workload/\${ResourceId} |
| [lens](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_Lens.html) | arn:\${Partition}:wellarchitected:\${Region}:\${Account}:lens/\${ResourceId} |
| [profile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_Profile.html) | arn:\${Partition}:wellarchitected:\${Region}:\${Account}:profile/\${ResourceId} |
| [review-template](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ReviewTemplate.html) | arn:\${Partition}:wellarchitected:\${Region}:\${Account}:review-template/\${ResourceId} |
# AWS WAF V2
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awswafv2.html
| Service | ARN |
|---------|-----|
| [webacl](https://docs.aws.amazon.com/waf/latest/APIReference/API_WebACL.html) | arn:\${Partition}:wafv2:\${Region}:\${Account}:\${Scope}/webacl/\${Name}/\${Id} |
| [ipset](https://docs.aws.amazon.com/waf/latest/APIReference/API_IPSet.html) | arn:\${Partition}:wafv2:\${Region}:\${Account}:\${Scope}/ipset/\${Name}/\${Id} |
| [managedruleset](https://docs.aws.amazon.com/waf/latest/APIReference/API_ManagedRuleSet.html) | arn:\${Partition}:wafv2:\${Region}:\${Account}:\${Scope}/managedruleset/\${Name}/\${Id} |
| [rulegroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html) | arn:\${Partition}:wafv2:\${Region}:\${Account}:\${Scope}/rulegroup/\${Name}/\${Id} |
| [regexpatternset](https://docs.aws.amazon.com/waf/latest/APIReference/API_RegexPatternSet.html) | arn:\${Partition}:wafv2:\${Region}:\${Account}:\${Scope}/regexpatternset/\${Name}/\${Id} |
| [loadbalancer/app/](https://docs.aws.amazon.com/waf/latest/APIReference/API_WebACL.html) | arn:\${Partition}:elasticloadbalancing:\${Region}:\${Account}:loadbalancer/app/\${LoadBalancerName}/\${LoadBalancerId} |
| [apigateway](https://docs.aws.amazon.com/waf/latest/APIReference/API_WebACL.html) | arn:\${Partition}:apigateway:\${Region}::/restapis/\${ApiId}/stages/\${StageName} |
| [appsync](https://docs.aws.amazon.com/waf/latest/APIReference/API_WebACL.html) | arn:\${Partition}:appsync:\${Region}:\${Account}:apis/\${GraphQLAPIId} |
| [userpool](https://docs.aws.amazon.com/waf/latest/APIReference/API_WebACL.html) | arn:\${Partition}:cognito-idp:\${Region}:\${Account}:userpool/\${UserPoolId} |
| [apprunner](https://docs.aws.amazon.com/waf/latest/APIReference/API_WebACL.html) | arn:\${Partition}:apprunner:\${Region}:\${Account}:service/\${ServiceName}/\${ServiceId} |
| [verified-access-instance](https://docs.aws.amazon.com/waf/latest/APIReference/API_WebACL.html) | arn:\${Partition}:ec2:\${Region}:\${Account}:verified-access-instance/\${VerifiedAccessInstanceId} |
# Amazon WorkMail
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonworkmail.html
| Service | ARN |
|---------|-----|
| [organization](https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html) | arn:\${Partition}:workmail:\${Region}:\${Account}:organization/\${ResourceId} |
# Amazon WorkSpaces Application Manager
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonworkspacesapplicationmanager.html
| Service | ARN |
|---------|-----|
# Amazon WorkSpaces Thin Client
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonworkspacesthinclient.html
| Service | ARN |
|---------|-----|
| [environment](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_Environment.html) | arn:\${Partition}:thinclient::\${Account}:environment/\${EnvironmentId} |
| [device](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_Device.html) | arn:\${Partition}:thinclient::\${Account}:device/\${DeviceId} |
| [softwareset](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_SoftwareSet.html) | arn:\${Partition}:thinclient::\${Account}:softwareset/\${SoftwareSetId} |
# AWS X-Ray
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsx-ray.html
| Service | ARN |
|---------|-----|
| [group](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html#xray-concepts-groups) | arn:\${Partition}:xray:\${Region}:\${Account}:group/\${GroupName}/\${Id} |
| [sampling-rule](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html#xray-concepts-sampling) | arn:\${Partition}:xray:\${Region}:\${Account}:sampling-rule/\${SamplingRuleName} |
# Amazon WorkSpaces Web
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonworkspacesweb.html
| Service | ARN |
|---------|-----|
| [browserSettings](https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_CreateBrowserSettings.html) | arn:\${Partition}:workspaces-web:\${Region}:\${Account}:browserSettings/\${BrowserSettingsId} |
| [identityProvider](https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_CreateIdentityProvider.html) | arn:\${Partition}:workspaces-web:\${Region}:\${Account}:identityProvider/\${PortalId}/\${IdentityProviderId} |
| [networkSettings](https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_CreateNetworkSettings.html) | arn:\${Partition}:workspaces-web:\${Region}:\${Account}:networkSettings/\${NetworkSettingsId} |
| [portal](https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_CreatePortal.html) | arn:\${Partition}:workspaces-web:\${Region}:\${Account}:portal/\${PortalId} |
| [trustStore](https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_CreateTrustStore.html) | arn:\${Partition}:workspaces-web:\${Region}:\${Account}:trustStore/\${TrustStoreId} |
| [userSettings](https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_CreateUserSettings.html) | arn:\${Partition}:workspaces-web:\${Region}:\${Account}:userSettings/\${UserSettingsId} |
| [userAccessLoggingSettings](https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_CreateUserAccessLoggingSettings.html) | arn:\${Partition}:workspaces-web:\${Region}:\${Account}:userAccessLoggingSettings/\${UserAccessLoggingSettingsId} |
| [ipAccessSettings](https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_CreateIpAccessSettings.html) | arn:\${Partition}:workspaces-web:\${Region}:\${Account}:ipAccessSettings/\${IpAccessSettingsId} |
# Amazon WorkSpaces
Doc reference: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonworkspaces.html
| Service | ARN |
|---------|-----|
| [directoryid](https://docs.aws.amazon.com/workspaces/latest/adminguide/manage-workspaces-directory.html) | arn:\${Partition}:workspaces:\${Region}:\${Account}:directory/\${DirectoryId} |
| [workspacebundle](https://docs.aws.amazon.com/workspaces/latest/adminguide/bundles.html) | arn:\${Partition}:workspaces:\${Region}:\${Account}:workspacebundle/\${BundleId} |
| [workspaceid](https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp_workspace_management.html) | arn:\${Partition}:workspaces:\${Region}:\${Account}:workspace/\${WorkspaceId} |
| [workspaceimage](https://docs.aws.amazon.com/workspaces/latest/adminguide/bundles.html) | arn:\${Partition}:workspaces:\${Region}:\${Account}:workspaceimage/\${ImageId} |
| [workspaceipgroup](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-ip-access-control-groups.html) | arn:\${Partition}:workspaces:\${Region}:\${Account}:workspaceipgroup/\${GroupId} |
| [connectionalias](https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html) | arn:\${Partition}:workspaces:\${Region}:\${Account}:connectionalias/\${ConnectionAliasId} |
| [workspaceapplication](https://docs.aws.amazon.com/workspaces/latest/adminguide/application-bundle-management.html) | arn:\${Partition}:workspaces:\${Region}:\${Account}:workspaceapplication/\${WorkSpaceApplicationId} |
