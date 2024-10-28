# CreateDeploymentRequestBody

Provide you deployment details


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            | Example                                                |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `training_job_id`                                      | *str*                                                  | :heavy_check_mark:                                     | The training job ID to use for deployment              | tr-12345                                               |
| `checkpoint`                                           | *int*                                                  | :heavy_check_mark:                                     | The checkpoint number to use for deployment            | 4                                                      |
| `server_type`                                          | [Optional[models.ServerType]](../models/servertype.md) | :heavy_minus_sign:                                     | N/A                                                    | on-demand                                              |
| `name`                                                 | *Optional[str]*                                        | :heavy_minus_sign:                                     | The name of the deployment                             | deployment-1                                           |
| `description`                                          | *Optional[str]*                                        | :heavy_minus_sign:                                     | A description of the deployment                        | Deployment for my training job                         |