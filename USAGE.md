<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import os
from t742874298_1 import Petstore

with Petstore(
    api_key=os.getenv("PETSTORE_API_KEY", ""),
) as petstore:

    res = petstore.pet.update_pet(name="doggie", photo_urls=[
        "<value>",
        "<value>",
    ], id=10, category={
        "id": 1,
        "name": "Dogs",
    })

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import os
from t742874298_1 import Petstore

async def main():
    async with Petstore(
        api_key=os.getenv("PETSTORE_API_KEY", ""),
    ) as petstore:

        res = await petstore.pet.update_pet_async(name="doggie", photo_urls=[
            "<value>",
            "<value>",
        ], id=10, category={
            "id": 1,
            "name": "Dogs",
        })

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->