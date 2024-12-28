import rsa
import random

def save_keys_into_file(file_name, key):
    with open(file_name, 'wb') as f:
        f.write(key.save_pkcs1("PEM"))
        

student_id = "0424312032"
random.seed(student_id) 

(pub_key_1024, priv_key_1024) = rsa.newkeys(1024)
(pub_key_2048, priv_key_2048) = rsa.newkeys(2048)

save_keys_into_file('RSA_pub_key_1024.pem', pub_key_1024)
save_keys_into_file('RSA_priv_key_1024.pem', priv_key_1024)
save_keys_into_file('RSA_pub_key_2048.pem', pub_key_2048)
save_keys_into_file('RSA_priv_key_2048.pem', priv_key_2048)

print("RSA 1024-bit Public Key:", pub_key_1024)
print("RSA 1024-bit Private Key:", priv_key_1024)

print("RSA 2048-bit Public Key:", pub_key_2048)
print("RSA 2048-bit Private Key:", priv_key_2048)
