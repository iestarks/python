import hvac
import os

# create a client instance
client = hvac.Client(url='http://localhost:8200')

# extract the token from the response

token = os.environ.get('VAULT_TOKEN')
print ('VAULT_TOKEN')
print (token)

# Authenticate with the AppRole method
 response = client.auth_root(token)

# Extract the client token from the response
client.token = response['auth']['client_token']

# Check if the AppRole authentication backend is enabled

if 'approle/' not in client.sys.list_auth_methods()['data'].keys():
    print('The AppRole authentication backend is not enabled')
    # Run your alternative command here

    # enable the AppRole auth method
    #client.sys.enable_auth_method('role_name')

else:
    print('The AppRole authentication backend is enabled')
    # Proceed with your AppRole-based workflow here
     # create a new AppRole

     # authenticate using the AppRole
#     role_name = 'sandbox-approle'
# client.auth.approle.create_or_update_approle(
#     role_name,
#     policies=['kv-create'],
#     metadata={
#         'description': 'My AppRole'
#     }
# ) 

# generate a new role ID and secret ID
# role_id = client.auth.approle.read_role_id(role_name)['data']['role_id']
# secret_id = client.auth.approle.generate_secret_id(role_id)['data']['secret_id']

# client.auth.approle.login(role_id=role_id, secret_id=secret_id)



# # Extract the client token from the response
# client.token = response['auth']['client_token']

# # Use the authenticated client to interact with Vault
# secrets = client.secrets.kv.v2.read_secret_version(path='secret/hello')
# print(secrets['data']['data']['message'])







