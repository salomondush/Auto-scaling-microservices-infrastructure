from huey_config import huey
from redis import Redis

# Initialize Redis client
redis_client = Redis(host='redis', port=6379, db=0, decode_responses=True)

@huey.task()
def insert_key(key, value):
    redis_client.set(key, value)
    return {"message": f"Inserted key: {key}"}

@huey.task()
def fetch_key(key):
    exists = redis_client.exists(key)
    print("exists: ", exists)
    if exists:
        return {"key": key, "value": redis_client.get(key)}
    return {"message": "Key Not found!"}

@huey.task()
def delete_key(key):
    if redis_client.exists(key):
        redis_client.delete(key)
        return {"message": f"Deleted key: {key}"}
    return {"message": "Key Not found!"}
