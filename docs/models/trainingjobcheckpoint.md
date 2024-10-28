# TrainingJobCheckpoint

Training Job Checkpoint Object


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `checkpoint`                                             | *Optional[int]*                                          | :heavy_minus_sign:                                       | The checkpoint number                                    | 3                                                        |
| `model_download_url`                                     | *Optional[str]*                                          | :heavy_minus_sign:                                       | The URL to download the model checkpoint                 | s3:/my_model                                             |
| `test_results`                                           | [Optional[models.TestResults]](../models/testresults.md) | :heavy_minus_sign:                                       | N/A                                                      |                                                          |
| `created_at`                                             | *Optional[int]*                                          | :heavy_minus_sign:                                       | The timestamp when the checkpoint was created            | 1633036800                                               |
| `updated_at`                                             | *Optional[int]*                                          | :heavy_minus_sign:                                       | The timestamp when the checkpoint was created            | 1633036800                                               |