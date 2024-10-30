# Embeddings
(*deployments.embeddings*)

## Overview

### Available Operations

* [create](#create) - Get Embeddings from a Deployment

## create

Get embeddings from a deployment using the provided input.

### Example Usage

```python
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
)

res = s.deployments.embeddings.create(project_id="<id>", deployment_id="<id>", request_body={
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