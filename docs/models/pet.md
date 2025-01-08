# Pet


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        | Example                                            |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `name`                                             | *str*                                              | :heavy_check_mark:                                 | N/A                                                | doggie                                             |
| `photo_urls`                                       | List[*str*]                                        | :heavy_check_mark:                                 | N/A                                                |                                                    |
| `id`                                               | *Optional[int]*                                    | :heavy_minus_sign:                                 | N/A                                                | 10                                                 |
| `category`                                         | [Optional[models.Category]](../models/category.md) | :heavy_minus_sign:                                 | N/A                                                |                                                    |
| `tags`                                             | List[[models.Tag](../models/tag.md)]               | :heavy_minus_sign:                                 | N/A                                                |                                                    |
| `status`                                           | [Optional[models.Status]](../models/status.md)     | :heavy_minus_sign:                                 | pet status in the store                            |                                                    |