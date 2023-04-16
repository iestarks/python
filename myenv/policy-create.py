import hvac



# Initialize the client
client = hvac.Client()

# Authenticate with the Vault server
#client.auth_approle("YOUR_ROLE_ID", "YOUR_SECRET_ID")

# Define the policy
policy = """
path "hvac/*" {
  capabilities = ["read", "list"]
}

path "hvac/temperatures" {
  capabilities = ["create", "read", "update", "delete"]
}
"""

# Create the policy
client.sys.create_or_update_policy("hvac", policy)
