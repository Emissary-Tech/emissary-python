# Chat
(*deployments.chat*)

## Overview

### Available Operations

* [complete](#complete) - Get Chat Completions from a Deployment

## complete

Get chat completions from a deployment using the provided input.

### Example Usage

```python
import emissary_client_sdk
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARYCLIENT_API_KEY", ""),
)

res = s.deployments.chat.complete(project_id="<id>", deployment_id="<id>", request_body={
    "messages": [
        {
            "role": emissary_client_sdk.Role.USER,
            "content": "Hello, how are you?",
        },
    ],
    "streaming": False,
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

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `project_id`                                                                                                      | *str*                                                                                                             | :heavy_check_mark:                                                                                                | The ID of the project to retrieve deployments for                                                                 |
| `deployment_id`                                                                                                   | *str*                                                                                                             | :heavy_check_mark:                                                                                                | The ID of the deployment to get chat completions from                                                             |
| `request_body`                                                                                                    | [models.GetChatCompletionsFromDeploymentRequestBody](../../models/getchatcompletionsfromdeploymentrequestbody.md) | :heavy_check_mark:                                                                                                | Provide your chat input for completions                                                                           |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[models.GetChatCompletionsFromDeploymentResponseBody](../../models/getchatcompletionsfromdeploymentresponsebody.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.APIErrorInvalidInput | 400                         | application/json            |
| models.APIErrorNotFound     | 404                         | application/json            |
| models.SDKError             | 4XX, 5XX                    | \*/\*                       |