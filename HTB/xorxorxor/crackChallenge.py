# We have the value of encrypted flag in hex in the given output.txt file
# 1. convert it back to bytes.
# 2. Get the value of key
# 3. Decrypt:


#1. 
actual_flag="134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9"
actual_flag_bytes = bytes.fromhex(actual_flag)
print("The actual flag value in bytes:", actual_flag_bytes)

#2. Retrieve the key 
known_plaintext_pattern = b"HTB{"
key = bytes([actual_flag_bytes[i] ^ known_plaintext_pattern[i] for i in range(4)])
print(f"Recovered key is: {key}")

#3. Retrieve the flag (Decrypt)
decoded_flag = b''
for i in range(len(actual_flag_bytes)):   
    decoded_flag += bytes([actual_flag_bytes[i] ^ key[i % len(key)]])
print(decoded_flag)
