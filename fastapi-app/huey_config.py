from huey import RedisHuey

# Configure Huey instance with Redis backend
huey = RedisHuey('my_app', host='localhost', port=6379, db=0)
