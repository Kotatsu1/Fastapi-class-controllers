import uvicorn
from fastapi import FastAPI
from controllers.items_controller import ItemsController

app = FastAPI()

app.include_router(ItemsController().router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)
