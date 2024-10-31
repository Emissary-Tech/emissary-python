# BaseModel
(*base_model*)

## Overview

Deals with base models

### Available Operations

* [retrieve_base_model_by_name](#retrieve_base_model_by_name) - Retrieve a base model

## retrieve_base_model_by_name

Retrieve a base model by its name.

### Example Usage

```python
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
)

res = s.base_model.retrieve_base_model_by_name(base_model_name="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `base_model_name`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The name of the base model to retrieve                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.BaseModelSummary](../../models/basemodelsummary.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.APIErrorNotFound | 404                     | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |