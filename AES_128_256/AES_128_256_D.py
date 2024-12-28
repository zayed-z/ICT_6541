from Crypto.Cipher import AES
import time

def decrypt_file(encrypted_data, key, output_file_name, encrypted_file_name):
    cipher = AES.new(key, AES.MODE_ECB) 
    start = time.time()
    decrypted_data = cipher.decrypt(encrypted_data)
    end = time.time()
    print(f"Decryption time for {encrypted_file_name}: {end - start:.6f} seconds with AES-{len(key)*8} bit key")
    
    decrypted_data = decrypted_data.rstrip(b" ")

    with open(output_file_name, "wb") as f:
        f.write(decrypted_data)
        

with open('aes_key_128.txt', 'rb') as f:
    key_128 = f.read()
with open('aes_key_256.txt', 'rb') as f:
    key_256 = f.read()

def get_encrypted_file(file_name):
    with open(file_name, 'rb') as f:
        return f.read()

encrypted_1MB_128 = get_encrypted_file('encrypted_1MB_128.txt')
encrypted_1MB_256 = get_encrypted_file('encrypted_1MB_256.txt')
encrypted_100MB_128 = get_encrypted_file('encrypted_100MB_128.txt')
encrypted_100MB_256 = get_encrypted_file('encrypted_100MB_256.txt')
encrypted_1024MB_128 = get_encrypted_file('encrypted_1024MB_128.txt')
encrypted_1024MB_256 = get_encrypted_file('encrypted_1024MB_256.txt')


decrypt_file(encrypted_1MB_128, key_128, "decrypted_1MB_file_128.txt", "encrypted_1MB_128.txt")
decrypt_file(encrypted_1MB_256, key_256, "decrypted_1MB_file_256.txt", "encrypted_1MB_128.txt")
decrypt_file(encrypted_100MB_128, key_128, "decrypted_100MB_file_128.txt", "encrypted_100MB_128.txt")
decrypt_file(encrypted_100MB_256, key_256, "decrypted_100MB_file_256.txt", "encrypted_100MB_256.txt")
decrypt_file(encrypted_1024MB_128, key_128, "decrypted_1024MB_file_128.txt", "encrypted_1024MB_128.txt")
decrypt_file(encrypted_1024MB_256, key_256, "decrypted_1024MB_file_256.txt", "encrypted_1024MB_256.txt")