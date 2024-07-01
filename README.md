# Fastapi-class-controllers

```Python

class ItemsController(BaseController):
    def __init__(self):
        super().__init__(prefix="/items")
        self.items_service = ItemsService()


    @router.get("/list")
    async def list_items(self):
        return await self.items_service.get_all_items()
```
