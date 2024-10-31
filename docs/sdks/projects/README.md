# Projects
(*projects*)

## Overview

### Available Operations

* [create](#create) - Create a new project
* [list](#list) - List of Projects
* [get](#get) - Retrieve a project by ID
* [delete](#delete) - Delete a project by ID

## create

Create a new project which will be used as an your Fine-Tuning workspace.

### Example Usage

```python
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
)

res = s.projects.create(request={
    "name": "my_project",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.CreateProjectRequestBody](../../models/createprojectrequestbody.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.ProjectSummary](../../models/projectsummary.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.APIErrorInvalidInput | 400                         | application/json            |
| models.SDKError             | 4XX, 5XX                    | \*/\*                       |

## list

Fetching a list of projects,


### Example Usage

```python
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
)

res = s.projects.list()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.ProjectSummary]](../../models/.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.APIErrorUnauthorized | 401                         | application/json            |
| models.SDKError             | 4XX, 5XX                    | \*/\*                       |

## get

Retrieve a project by its unique identifier.

### Example Usage

```python
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
)

res = s.projects.get(project_id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ProjectDetail](../../models/projectdetail.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.APIErrorNotFound | 404                     | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## delete

Delete a project by its unique identifier.

### Example Usage

```python
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
)

s.projects.delete(project_id="<id>")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.APIErrorNotFound | 404                     | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |