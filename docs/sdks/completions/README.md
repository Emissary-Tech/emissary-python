# Completions
(*deployments.completions*)

## Overview

### Available Operations

* [create](#create) - Get Completions from a Deployment

## create

Get completions from a deployment using the provided input.

### Example Usage

```python
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
    project_id="<id>",
)

res = s.deployments.completions.create(deployment_id="<id>", request_body={
    "prompt": "What is the capital of France?",
    "temperature": 0.7,
    "max_new_tokens": 500,
    "top_p": 0.9,
    "top_k": 50,
    "no_repeat_ngram_size": 2,
    "do_sample": True,
}, project_id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `deployment_id`                                                                                           | *str*                                                                                                     | :heavy_check_mark:                                                                                        | The ID of the deployment to get completions from                                                          |
| `request_body`                                                                                            | [models.GetCompletionsFromDeploymentRequestBody](../../models/getcompletionsfromdeploymentrequestbody.md) | :heavy_check_mark:                                                                                        | Provide you prompt input for completions                                                                  |
| `project_id`                                                                                              | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.GetCompletionsFromDeploymentResponseBody](../../models/getcompletionsfromdeploymentresponsebody.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.APIErrorInvalidInput | 400                         | application/json            |
| models.APIErrorNotFound     | 404                         | application/json            |
| models.SDKError             | 4XX, 5XX                    | \*/\*                       |