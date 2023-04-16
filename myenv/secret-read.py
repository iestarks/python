import hvac

# Read the secret
secret = client.secrets.kv.v2.read_secret(path='secret/myapp')
