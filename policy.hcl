path "hvac/*" {
  capabilities = ["read", "list"]
}

path "hvac/temperatures" {
  capabilities = ["create", "read", "update", "delete"]
}
