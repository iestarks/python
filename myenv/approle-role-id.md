(myenv) wolfpacker@Wolfpackers-MacBook-Air myenv % vault read auth/approle/role/hvac/role-id 
Key        Value
---        -----
role_id    ad7fe757-a280-a8e9-ca4b-54732152b296



(myenv) wolfpacker@Wolfpackers-MacBook-Air myenv % vault write -f auth/approle/role/hvac/secret-id
Key                   Value
---                   -----
secret_id             39a13f25-2ebb-a740-d8ad-a36907a648fb
secret_id_accessor    317ab902-f9f0-3ecc-4c62-e9ff31d0c829
secret_id_num_uses    0
secret_id_ttl         0s