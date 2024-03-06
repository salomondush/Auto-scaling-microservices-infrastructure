from fastapi import FastAPI
from pydantic import BaseModel
from tasks import encrypt_key_data, decrypt_key_data, delete_key_data
import uuid


class Data(BaseModel):
    key: str
    value: str


app = FastAPI()


def get_task_result(task):
    return task.get(blocking=True)


@app.get("/")
def default():
    return "Fast API Server"


@app.get("/test/")
async def load_test():
    """
    Perform a load test by generating a random key and data,
    encrypting and decrypting the data using the key,
    and then deleting the data using the key.

    Returns:
        dict: A dictionary with a message indicating that the load test is completed.
    """
    key = str(uuid.uuid4())
    data = "a" * 1000000

    get_task_result(encrypt_key_data(key, data))
    get_task_result(decrypt_key_data(key))
    get_task_result(delete_key_data(key))

    return {"message": "Load Test Completed!!"}


@app.get("/decrypt/")
async def decrypt_endpoint(key: str):
    return get_task_result(decrypt_key_data(key))


@app.post("/encrypt/")
async def encrypt_endpoint(data: Data):
    return get_task_result(encrypt_key_data(data.key, data.value))


@app.delete("/delete/{key}")
async def delete_item(key: str):
    return get_task_result(delete_key_data(key))
