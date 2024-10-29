# Classification
(*deployments.classification*)

## Overview

### Available Operations

* [get](#get) - Get Classification from a Deployment

## get

Get classification from a deployment using the provided input.

### Example Usage

```python
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
)

res = s.deployments.classification.get(project_id="<id>", deployment_id="<id>", request_body={
    "source_sentence": "What is the capital of France?",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `project_id`                                                                                                    | *str*                                                                                                           | :heavy_check_mark:                                                                                              | The ID of the project to retrieve deployments for                                                               |
| `deployment_id`                                                                                                 | *str*                                                                                                           | :heavy_check_mark:                                                                                              | The ID of the deployment to get classification from                                                             |
| `request_body`                                                                                                  | [models.GetClassificationFromDeploymentRequestBody](../../models/getclassificationfromdeploymentrequestbody.md) | :heavy_check_mark:                                                                                              | Provide your input for classification                                                                           |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.GetClassificationFromDeploymentResponseBody](../../models/getclassificationfromdeploymentresponsebody.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.APIErrorInvalidInput | 400                         | application/json            |
| models.APIErrorNotFound     | 404                         | application/json            |
| models.SDKError             | 4XX, 5XX                    | \*/\*                       |