import hvac

# Initialize the client
client = hvac.Client()

# Create the AppRole
client.create_role("hvac", policies="hvac", bound_cidr_list=["127.0.0.1/32"])

# Create the Secret ID for the AppRole
secret_id = client.create_secret_id("hvac")

# Retrieve the Role ID
role_id = client.approle.role_id("hvac")

# Print the Role ID and Secret ID
print("Role ID:", role_id)
print("Secret ID:", secret_id["secret_id"])

# Authenticate with the Vault server
client.auth_approle(role_id, secret_id)
