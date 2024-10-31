<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
    project_id="<id>",
)

res = s.create_project(request={
    "name": "my_project",
})

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from emissary_client_sdk import EmissaryClient
import os

async def main():
    s = EmissaryClient(
        api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
        project_id="<id>",
    )
    res = await s.create_project_async(request={
        "name": "my_project",
    })
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->