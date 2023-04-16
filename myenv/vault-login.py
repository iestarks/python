import hvac
import os

env_vars = os.environ

# Get the value of the "HOME" environment variable
vaulttoken = os.environ.get('VAULT_TOKEN')

# Create a client object with the Vault server URL and token
client = hvac.Client(
    url='http://localhost:8200',
    # Log in with a root token
    token=vaulttoken
)
    # Verify if authentication was successful
if client.is_authenticated():
        print("Successfully authenticated with Vault")
else: 
        print("No Token set, unable to authenticate")

# Use the client object to interact with Vault's API
# For example, to read a secret:
secret = client.secrets.kv.v2.read_secret_version(
    mount_point='secret',
    path='creds',
)

print(secret['data']['data'])