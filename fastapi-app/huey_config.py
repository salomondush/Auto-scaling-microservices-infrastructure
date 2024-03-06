from huey import RedisHuey
from redis import Redis

# Configure Huey instance with Redis backend
huey = RedisHuey('image_transform_app', host='redis', port=6379, db=0)

# Initialize Redis client
redis_client = Redis(host='redis', port=6379, db=0, decode_responses=True)
