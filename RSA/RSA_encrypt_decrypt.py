import rsa
from rsa import PublicKey, PrivateKey
import time

def load_key_from_file(file_name):
    with open(file_name, 'rb') as f:
        return f.read()
    
def rsa_encrypt(file_name,key):
    with open(file_name, 'rb') as f:
        data = f.read()
        #plain_text = data.encode()
    start = time.time()
    cipher_text = rsa.encrypt(data, key)
    end = time.time()
    print(f"Encryption time for {file_name}: {end - start:.8f} seconds with RSA-2048 bit key")
    return cipher_text


def save_RSAencrypted_file(file_name, cipher):
    with open(file_name, 'wb') as f:
        f.write(cipher)
    
def get_cipher(file_name):
    with open(file_name, 'rb') as f:
        return f.read()
    
def rsa_decrypt(cipher, key, output_file_name, encrypted_file_name):
    start = time.time()
    decrypted_data = rsa.decrypt(cipher, key)
    end = time.time()
    print(f"Decryption time for {encrypted_file_name}: {end - start:.6f} seconds with RSA-2048 bit key")
    
    with open(output_file_name, "wb") as f:
        f.write(decrypted_data)  

pub_key_bytes_1024 = load_key_from_file('RSA_pub_key_1024.pem')
priv_key_bytes_1024 = load_key_from_file('RSA_priv_key_1024.pem')
public_key_1024 = PublicKey.load_pkcs1(pub_key_bytes_1024)
private_key_1024 = PrivateKey.load_pkcs1(priv_key_bytes_1024)

pub_key_bytes_2048 = load_key_from_file('RSA_pub_key_2048.pem')
priv_key_bytes_2048 = load_key_from_file('RSA_priv_key_2048.pem')
public_key_2048 = PublicKey.load_pkcs1(pub_key_bytes_2048)
private_key_2048 = PrivateKey.load_pkcs1(priv_key_bytes_2048)

#encrypted_192B_2048 = rsa_encrypt('192B_file.txt', public_key_2048)
#save_RSAencrypted_file('encrypted_192B_2048.txt', encrypted_192B_2048)

#encrypted_100B_2048 = rsa_encrypt('100B_file.txt', public_key_2048)
#save_RSAencrypted_file('encrypted_100B_2048.txt', encrypted_100B_2048)

#encrypted_10B_2048 = rsa_encrypt('10B_file.txt', public_key_2048)
#save_RSAencrypted_file('encrypted_10B_2048.txt', encrypted_10B_2048)


cipher_192B_2048 = get_cipher('encrypted_192B_2048.txt')
cipher_100B_2048 = get_cipher('encrypted_100B_2048.txt')
cipher_10B_2048 = get_cipher('encrypted_10B_2048.txt')

rsa_decrypt(cipher_192B_2048, private_key_2048, 'decrypted_192B_2048.txt', 'encrypted_192B_2048.txt')
rsa_decrypt(cipher_100B_2048, private_key_2048, 'decrypted_100B_2048.txt', 'encrypted_100B_2048.txt')
rsa_decrypt(cipher_10B_2048, private_key_2048, 'decrypted_10B_2048.txt', 'encrypted_10B_2048.txt')