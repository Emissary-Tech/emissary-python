# TrainingJobSummary

Training Job Summary Object


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         | Example                                             |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `id`                                                | *Optional[str]*                                     | :heavy_minus_sign:                                  | The unique identifier for the training job          | tr-12345                                            |
| `name`                                              | *Optional[str]*                                     | :heavy_minus_sign:                                  | The name of the training job                        | training-1                                          |
| `base_model`                                        | *Optional[str]*                                     | :heavy_minus_sign:                                  | The base model used for training                    | Llama-3.2-1B-Instruct                               |
| `status`                                            | [Optional[models.Status]](../models/status.md)      | :heavy_minus_sign:                                  | The current status of the training job              | Running                                             |
| `progress`                                          | *Optional[int]*                                     | :heavy_minus_sign:                                  | The current progress of the training job            | 75                                                  |
| `created_by`                                        | *Optional[str]*                                     | :heavy_minus_sign:                                  | The user ID who created the training job            | user-12345                                          |
| `created_at`                                        | *Optional[int]*                                     | :heavy_minus_sign:                                  | The timestamp when the TrainingJob was created      | 1633036800                                          |
| `updated_at`                                        | *Optional[int]*                                     | :heavy_minus_sign:                                  | The timestamp when the TrainingJob was last updated | 1633036800                                          |