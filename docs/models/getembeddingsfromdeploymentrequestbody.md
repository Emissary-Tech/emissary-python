# GetEmbeddingsFromDeploymentRequestBody

Provide your input for embeddings


## Fields

| Field                                 | Type                                  | Required                              | Description                           | Example                               |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `source_sentence`                     | *str*                                 | :heavy_check_mark:                    | The input for which to get embeddings | What is the capital of France?        |
| `target_sentence`                     | *str*                                 | :heavy_check_mark:                    | The target sentence for comparison    | Paris is the capital of France.       |
| `cosine`                              | *Optional[bool]*                      | :heavy_minus_sign:                    | Whether to return cosine similarity   | true                                  |
| `manhattan`                           | *Optional[bool]*                      | :heavy_minus_sign:                    | Whether to return Manhattan distance  | false                                 |
| `euclidean`                           | *Optional[bool]*                      | :heavy_minus_sign:                    | Whether to return Euclidean distance  | false                                 |