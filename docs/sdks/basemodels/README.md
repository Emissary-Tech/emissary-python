# BaseModels
(*base_models*)

## Overview

### Available Operations

* [list](#list) - List of Base Models
* [get](#get) - Retrieve a base model

## list

Fetching a list of base models

### Example Usage

```python
from emissary_client_sdk import EmissaryClient
import os

with EmissaryClient(
    api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
) as emissary_client:

    res = emissary_client.base_models.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.BaseModelSummary]](../../models/.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.APIErrorInvalidInput | 400                         | application/json            |
| models.APIErrorUnauthorized | 401                         | application/json            |
| models.SDKError             | 4XX, 5XX                    | \*/\*                       |

## get

Retrieve a base model by its name.

### Example Usage

```python
from emissary_client_sdk import EmissaryClient
import os

with EmissaryClient(
    api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
) as emissary_client:

    res = emissary_client.base_models.get(base_model_name="<value>")

    # Handle response
    print(res)

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