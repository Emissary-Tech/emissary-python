<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from emissary_client_sdk import EmissaryClient
import os

with EmissaryClient(
    api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
) as emissary_client:

    res = emissary_client.base_models.list()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from emissary_client_sdk import EmissaryClient
import os

async def main():
    async with EmissaryClient(
        api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
    ) as emissary_client:

        res = await emissary_client.base_models.list_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->