import hvac
import os




# Define the client variable
client = hvac.Client(url='http://localhost.com')

client.sys.is_initialized()
shares = 1
threshold = 1
result = client.sys.initialize(shares, threshold)
root_token = result['VAULT_TOKEN']
keys = result['keys']
client.sys.is_initialized()


client.token = VAULT_TOKEN

client.sys.is_sealed()


VAULT_TOKEN = os.environ.get('VAULT_TOKEN')

print(VAULT_TOKEN)



# Unseal a Vault cluster with individual keys
unseal_response1 = client.sys.submit_unseal_key(keys[0])

client.sys.is_sealed()

