# DatasetDetail

Dataset Object


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     | Example                                         |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `id`                                            | *Optional[str]*                                 | :heavy_minus_sign:                              | The unique identifier for the dataset           | ds-12345                                        |
| `name`                                          | *Optional[str]*                                 | :heavy_minus_sign:                              | The name of the dataset                         | my_dataset                                      |
| `is_uploaded`                                   | *Optional[bool]*                                | :heavy_minus_sign:                              | Whether the dataset has been uploaded           | true                                            |
| `dataset_download_url`                          | *Optional[str]*                                 | :heavy_minus_sign:                              | The URL to download the dataset                 | s3:/my_dataset                                  |
| `upload_by`                                     | *Optional[str]*                                 | :heavy_minus_sign:                              | The user ID who uploaded the dataset            | user-12345                                      |
| `created_at`                                    | *Optional[int]*                                 | :heavy_minus_sign:                              | The timestamp when the dataset was created      | 1633036800                                      |
| `updated_at`                                    | *Optional[int]*                                 | :heavy_minus_sign:                              | The timestamp when the dataset was last updated | 1633036800                                      |