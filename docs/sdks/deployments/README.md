# Deployments
(*deployments*)

## Overview

### Available Operations

* [create](#create) - Create a new Deployment
* [list](#list) - List of Deployments
* [get](#get) - Retrieve a deployment by ID
* [delete](#delete) - Delete a deployment by ID
* [cancel](#cancel) - Cancel a deployment by ID
* [get_completions](#get_completions) - Get Completions from a Deployment
* [get_embeddings](#get_embeddings) - Get Embeddings from a Deployment

## create

Create a new deployment for the project.

### Example Usage

```python
import emissary_client_sdk
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARYCLIENT_API_KEY", ""),
)

res = s.deployments.create(project_id="<id>", request_body={
    "training_job_id": "tr-12345",
    "checkpoint": 4,
    "server_type": emissary_client_sdk.ServerType.ON_DEMAND,
    "name": "deployment-1",
    "description": "Deployment for my training job",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `project_id`                                                                      | *str*                                                                             | :heavy_check_mark:                                                                | The ID of the project to create a deployment for                                  |
| `request_body`                                                                    | [models.CreateDeploymentRequestBody](../../models/createdeploymentrequestbody.md) | :heavy_check_mark:                                                                | Provide you deployment details                                                    |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.DeploymentSummary](../../models/deploymentsummary.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.APIErrorInvalidInput | 400                         | application/json            |
| models.SDKError             | 4XX, 5XX                    | \*/\*                       |

## list

Fetching a list of deployments

### Example Usage

```python
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARYCLIENT_API_KEY", ""),
)

res = s.deployments.list(project_id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID of the project to retrieve deployments for                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListDeploymentsResponseBody](../../models/listdeploymentsresponsebody.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.APIErrorUnauthorized | 401                         | application/json            |
| models.SDKError             | 4XX, 5XX                    | \*/\*                       |

## get

Retrieve a deployment by its unique identifier.

### Example Usage

```python
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARYCLIENT_API_KEY", ""),
)

res = s.deployments.get(project_id="<id>", deployment_id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID of the project to retrieve deployments for                   |
| `deployment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The ID of the deployment to retrieve                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeploymentDetail](../../models/deploymentdetail.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.APIErrorNotFound | 404                     | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## delete

Delete a deployment by its unique identifier.

### Example Usage

```python
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARYCLIENT_API_KEY", ""),
)

s.deployments.delete(project_id="<id>", deployment_id="<id>")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID of the project to retrieve deployments for                   |
| `deployment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The ID of the deployment to delete                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.APIErrorNotFound | 404                     | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## cancel

Cancel a deployment by its unique identifier.

### Example Usage

```python
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARYCLIENT_API_KEY", ""),
)

s.deployments.cancel(project_id="<id>", deployment_id="<id>")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID of the project to retrieve deployments for                   |
| `deployment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The ID of the deployment to cancel                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.APIErrorNotFound | 404                     | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_completions

Get completions from a deployment using the provided input.

### Example Usage

```python
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARYCLIENT_API_KEY", ""),
)

res = s.deployments.get_completions(project_id="<id>", deployment_id="<id>", request_body={
    "prompt": "What is the capital of France?",
    "temperature": 0.7,
    "max_new_tokens": 500,
    "top_p": 0.9,
    "top_k": 50,
    "no_repeat_ngram_size": 2,
    "do_sample": True,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `project_id`                                                                                              | *str*                                                                                                     | :heavy_check_mark:                                                                                        | The ID of the project to retrieve deployments for                                                         |
| `deployment_id`                                                                                           | *str*                                                                                                     | :heavy_check_mark:                                                                                        | The ID of the deployment to get completions from                                                          |
| `request_body`                                                                                            | [models.GetCompletionsFromDeploymentRequestBody](../../models/getcompletionsfromdeploymentrequestbody.md) | :heavy_check_mark:                                                                                        | Provide you prompt input for completions                                                                  |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.GetCompletionsFromDeploymentResponseBody](../../models/getcompletionsfromdeploymentresponsebody.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.APIErrorInvalidInput | 400                         | application/json            |
| models.APIErrorNotFound     | 404                         | application/json            |
| models.SDKError             | 4XX, 5XX                    | \*/\*                       |

## get_embeddings

Get embeddings from a deployment using the provided input.

### Example Usage

```python
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARYCLIENT_API_KEY", ""),
)

res = s.deployments.get_embeddings(project_id="<id>", deployment_id="<id>", request_body={
    "source_sentence": "What is the capital of France?",
    "target_sentence": "Paris is the capital of France.",
    "cosine": True,
    "manhattan": False,
    "euclidean": False,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `project_id`                                                                                            | *str*                                                                                                   | :heavy_check_mark:                                                                                      | The ID of the project to retrieve deployments for                                                       |
| `deployment_id`                                                                                         | *str*                                                                                                   | :heavy_check_mark:                                                                                      | The ID of the deployment to get embeddings from                                                         |
| `request_body`                                                                                          | [models.GetEmbeddingsFromDeploymentRequestBody](../../models/getembeddingsfromdeploymentrequestbody.md) | :heavy_check_mark:                                                                                      | Provide your input for embeddings                                                                       |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.GetEmbeddingsFromDeploymentResponseBody](../../models/getembeddingsfromdeploymentresponsebody.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.APIErrorInvalidInput | 400                         | application/json            |
| models.APIErrorNotFound     | 404                         | application/json            |
| models.SDKError             | 4XX, 5XX                    | \*/\*                       |