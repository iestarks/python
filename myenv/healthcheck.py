#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Health check

# Check if the server is initialized
is_initialized = client.is_initialized()
print("Is initialized: ", is_initialized)

# Check if the server is sealed
is_sealed = client.is_sealed()
print("Is sealed: ", is_sealed)

# Get the current leader of the cluster
leader = client.get_leader()
print("Leader: ", leader)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>