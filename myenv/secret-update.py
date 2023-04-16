import hvac



# Update the secret
client.secrets.kv.v2.create_or_update_secret(path='secret/myapp', data={'username': 'newuser', 'password': 'newpassword'})
