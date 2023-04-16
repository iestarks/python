import hvac

# Delete the secret
client.secrets.kv.v2.delete_secret(path='secret/myapp')
