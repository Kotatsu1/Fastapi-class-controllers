from .base import BaseController, router
from services.items_service import ItemsService


class ItemsController(BaseController):
    def __init__(self):
        super().__init__(prefix="/items")
        self.items_service = ItemsService()


    @router.get("/list")
    async def list_items(self):
        return await self.items_service.get_all_items()


    @router.get("/buy/{item}")
    async def buy(self, item: str):
        item = await self.items_service.search_for_item(item)

        if item:
            return f"Got {item}"

        return "No such item"

