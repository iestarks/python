import hvac
import os

VAULT_TOKEN = os.environ.get('VAULT_TOKEN')
roleid = os.environ.get('roleid')
secretid = os.environ.get('secretid')

print (roleid)
print (secretid)
# Connect to the Vault server
client = hvac.Client(url='http://127.0.0.1:8200', token=VAULT_TOKEN)


# List all AppRoles
app_roles = client.approle.list_roles()
print(app_roles)

# # Authenticate with the Vault server
# client.auth_approle(roleid,secretid)

# # List all policies
# policies = client.sys.list_policies()
# print(policies)


# #Check the permission of the secret
# client.sys.list_policies()


