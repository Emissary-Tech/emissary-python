# TrainingJobs
(*training_jobs*)

## Overview

### Available Operations

* [create](#create) - Create a new Training Job
* [list](#list) - List of Training Jobs
* [retrieve](#retrieve) - Retrieve a training job by ID
* [delete](#delete) - Delete a training job by ID
* [cancel](#cancel) - Cancel a training job by ID
* [list_checkpoints](#list_checkpoints) - List of Checkpoints

## create

Create a new training job for the project.

### Example Usage

```python
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
)

res = s.training_jobs.create(project_id="<id>", request_body={
    "base_model": "Llama-3.2-1B-Instruct",
    "train_dataset_id": "ds-12345",
    "test_dataset_id": "ds-67890",
    "train_test_split_ratio": 0.2,
    "name": "training-1",
    "description": "Fine-tuning the model on my dataset",
    "parameters": {
        "key": "<value>",
    },
    "hf_model_link": "https://huggingface.co/my_model",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `project_id`                                                                        | *str*                                                                               | :heavy_check_mark:                                                                  | The ID of the project to create a training job for                                  |
| `request_body`                                                                      | [models.CreateTrainingJobRequestBody](../../models/createtrainingjobrequestbody.md) | :heavy_check_mark:                                                                  | Provide your training job details                                                   |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.TrainingJobSummary](../../models/trainingjobsummary.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.APIErrorInvalidInput | 400                         | application/json            |
| models.SDKError             | 4XX, 5XX                    | \*/\*                       |

## list

Fetching a list of training jobs

### Example Usage

```python
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
)

res = s.training_jobs.list(project_id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID of the project to retrieve training jobs for                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.TrainingJobSummary]](../../models/.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.APIErrorUnauthorized | 401                         | application/json            |
| models.SDKError             | 4XX, 5XX                    | \*/\*                       |

## retrieve

Retrieve a training job by its unique identifier.

### Example Usage

```python
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
)

res = s.training_jobs.retrieve(project_id="<id>", training_job_id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID of the project to retrieve training jobs for                 |
| `training_job_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The ID of the training job to retrieve                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TrainingJobDetail](../../models/trainingjobdetail.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.APIErrorNotFound | 404                     | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## delete

Delete a training job by its unique identifier.

### Example Usage

```python
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
)

s.training_jobs.delete(project_id="<id>", training_job_id="<id>")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID of the project to retrieve training jobs for                 |
| `training_job_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The ID of the training job to delete                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.APIErrorNotFound | 404                     | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## cancel

Cancel a training job by its unique identifier.

### Example Usage

```python
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
)

s.training_jobs.cancel(project_id="<id>", training_job_id="<id>")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID of the project to retrieve training jobs for                 |
| `training_job_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The ID of the training job to cancel                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.APIErrorNotFound | 404                     | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## list_checkpoints

Fetching a list of checkpoints for a training job

### Example Usage

```python
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
)

res = s.training_jobs.list_checkpoints(project_id="<id>", training_job_id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID of the project to retrieve checkpoints for                   |
| `training_job_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The ID of the training job to retrieve checkpoints for              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.TrainingJobCheckpoint]](../../models/.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.APIErrorNotFound | 404                     | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |