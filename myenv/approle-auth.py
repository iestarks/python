import hvac
import secrets
import os
import getpass

client = hvac.Client(url='http://localhost:8200')

value = getpass.getpass(prompt='Enter the value for VAULT_ADDR: ')
os.environ['VAULT_ADDR'] = value


# Log in with a root token

token = os.environ.get(value)
root_token = value

# Log in with a root token
client.token = root_token
client.auth_token = client.token


# Verify if authentication was successful
if client.is_authenticated():
    print("Successfully authenticated with Vault")
else:
    print("Authentication failed")






# Define a 32-character random lease ID
lease_id = secrets.token_hex(16)

# Print the lease ID
print(lease_id)


# List all AppRoles
app_roles = client.list_auth_approle_roles()

# Print the list of AppRoles
print(app_roles['data']['keys'])

# # Your AppRole credentials
# role_id = 'YOUR_ROLE_ID'
# secret_id = 'YOUR_SECRET_ID'

# # Read the AppRole role configuration
# role_config = client.read_auth_approle_role(role_id=role_id)

# # Print the role configuration
# print(role_config)

# # Authenticate with the AppRole method
# response = client.auth_approle(role_id, secret_id)

# # Extract the client token from the response
# client.token = response['auth']['client_token']

# # Use the authenticated client to interact with Vault
# secrets = client.secrets.kv.v2.read_secret_version(path='secret/hello')
# print(secrets['data']['data']['message'])
