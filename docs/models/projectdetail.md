# ProjectDetail

Project Object


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | The unique identifier for the project                              | ms-12345                                                           |
| `name`                                                             | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | The name of the project                                            | my_project                                                         |
| `datasets`                                                         | List[[models.DatasetSummary](../models/datasetsummary.md)]         | :heavy_minus_sign:                                                 | N/A                                                                |                                                                    |
| `training_jobs`                                                    | List[[models.TrainingJobSummary](../models/trainingjobsummary.md)] | :heavy_minus_sign:                                                 | N/A                                                                |                                                                    |
| `deployments`                                                      | List[[models.DeploymentSummary](../models/deploymentsummary.md)]   | :heavy_minus_sign:                                                 | N/A                                                                |                                                                    |