
class ItemsService:
    items = ["hello", "world"]

    async def get_all_items(self):
        return {"items": self.items}

    
    async def search_for_item(self, item: str):
        for i in self.items:
            if i == item:
                return item

        return None
