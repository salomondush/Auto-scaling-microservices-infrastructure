from huey_config import huey, redis_client
from cryptography.fernet import Fernet

fernet_key = b'2BSx0IYba8-biPSEpng3qDpFu6JPNf5_r3rFuBB1wso='


@huey.task()
def encrypt_key_data(key, value):
    """
    Encrypts the given value using the provided key and stores the encrypted data in Redis.

    Args:
        key (str): The task ID or key.
        value (str): The value to be encrypted.

    Returns:
        dict: A dictionary containing a message indicating the successful encryption of data for the given task ID.
    """
    cipher_suite = Fernet(fernet_key)

    # loop to model computational heavy tasks
    for _ in range(100):
        encrypted_data = cipher_suite.encrypt(value.encode())

    redis_client.set(f"crypto:{key}:encrypted", encrypted_data)
    return {"message": f"Data encrypted for task_id: {key}"}


@huey.task()
def decrypt_key_data(key):
    """
    Decrypts the encrypted data associated with the given key.

    Args:
        key (str): The key used to retrieve the encrypted data.

    Returns:
        dict: A dictionary containing the decrypted value, encrypted value, and key if the key exists.
        If the key does not exist, a dictionary with a "message" key is returned.

    """
    exists = redis_client.exists(f"crypto:{key}:encrypted")

    if exists:
        encrypted_data = redis_client.get(f"crypto:{key}:encrypted")

        cipher_suite = Fernet(fernet_key)

        # loop to model computational heavy tasks
        for _ in range(100):
            decrypted_data = cipher_suite.decrypt(
                encrypted_data.encode()).decode()

        return {"key": key, "decrypted value": decrypted_data, "encrypted value": encrypted_data}

    return {"message": "Key Not found!"}


@huey.task()
def delete_key_data(key):
    """
    Deletes the encrypted data associated with the given key from Redis.

    Args:
        key (str): The key used to identify the encrypted data.

    Returns:
        dict: A dictionary containing a message indicating the successful deletion of data for the given key.
        If the key does not exist, a dictionary with a "message" key is returned.
    """
    if redis_client.exists(f"crypto:{key}:encrypted"):
        redis_client.delete(f"crypto:{key}:encrypted")
        return {"message": f"Deleted data with key: {key}"}

    return {"message": "Key Not found!"}
