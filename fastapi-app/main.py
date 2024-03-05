from fastapi import FastAPI
from pydantic import BaseModel
from tasks import insert_key, fetch_key, delete_key

class Item(BaseModel):
    value: str

app = FastAPI()

def get_task_result(task):
    return task.get(blocking=True)

@app.get("/items/{key}")
async def read_item(key: str):
    return get_task_result(fetch_key(key))

@app.post("/items/{key}")
async def create_item(key: str, item: Item):
    return get_task_result(insert_key(key, item.value))

@app.delete("/items/{key}")
async def delete_item(key: str):
    return get_task_result(delete_key(key))
