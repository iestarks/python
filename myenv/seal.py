# Seal a previously unsealed Vault cluster.
client.sys.seal()
<Response [204]>
client.sys.is_sealed()
True

# Unseal with multiple keys until threshold met
unseal_response = client.sys.submit_unseal_keys(keys)

client.sys.is_sealed()
False