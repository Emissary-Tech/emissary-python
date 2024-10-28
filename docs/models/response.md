# Response


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `embeddings`                                                      | [Optional[models.Embeddings]](../models/embeddings.md)            | :heavy_minus_sign:                                                | N/A                                                               |
| `cosine_score`                                                    | *Optional[float]*                                                 | :heavy_minus_sign:                                                | The cosine similarity between the embeddings if cosine = true     |
| `manhattan_distance`                                              | *Optional[float]*                                                 | :heavy_minus_sign:                                                | The Manhattan distance between the embeddings if manhattan = true |
| `euclidean_distance`                                              | *Optional[float]*                                                 | :heavy_minus_sign:                                                | The Euclidean distance between the embeddings if euclidean = true |