import hvac

# create a client instance
client = hvac.Client(url='http://localhost:8200')

# authenticate using the root token (or another method)
client.token = 'root-token'

# enable the AppRole auth method
client.sys.enable_auth_method('approle')

# create a new AppRole
role_name = 'sandbox-approle'
client.auth.approle.create_or_update_approle(
    role_name,
    policies=['kv-create'],
    metadata={
        'description': 'My AppRole'
    }
)

# generate a new role ID and secret ID
role_id = client.auth.approle.read_role_id(role_name)['data']['role_id']
secret_id = client.auth.approle.generate_secret_id(role_id)['data']['secret_id']

# authenticate using the AppRole
client.auth.approle.login(role_id=role_id, secret_id=secret_id)
