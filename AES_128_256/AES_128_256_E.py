from Crypto.Cipher import AES
import time

def save_keys_into_file(file_name, key):
    with open(file_name, 'wb') as f:
        f.write(key)

def encrypt_file(file_name, key):
    cipher = AES.new(key, AES.MODE_ECB)  
    with open(file_name, "rb") as f:
        data = f.read()
    while len(data) % 16 != 0:
        data += b" "
    start = time.time()
    encrypted_data = cipher.encrypt(data)
    end = time.time()
    print(f"Encryption time for {file_name}: {end - start:.6f} seconds with AES-{len(key)*8} bit key")
    return encrypted_data

def save_encrypted_data(data, file_name):
    with open(file_name, 'wb') as f:
    	f.write(data)

my_student_ID = "0424312032"
ID_in_Bytes = my_student_ID.encode('utf-8')

padding_byte = b'Z'

key_128 = ID_in_Bytes.ljust(16, padding_byte)[:16]  
key_256 = ID_in_Bytes.ljust(32, padding_byte)[:32]  



save_keys_into_file('aes_key_128.txt', key_128)
save_keys_into_file('aes_key_256.txt', key_256)

print("128-bit Key:", key_128)
print("256-bit Key:", key_256)

print("128-bit Key (decoded):", key_128.decode('utf-8', errors='ignore'))
print("256-bit Key (decoded):", key_256.decode('utf-8', errors='ignore'))


encrypted_1MB_128 = encrypt_file("1MB_file.txt", key_128)
save_encrypted_data(encrypted_1MB_128, 'encrypted_1MB_128.txt')
    
encrypted_1MB_256 = encrypt_file("1MB_file.txt", key_256)
save_encrypted_data(encrypted_1MB_256, 'encrypted_1MB_256.txt')



encrypted_100MB_128 = encrypt_file("100MB_file.txt", key_128)
save_encrypted_data(encrypted_100MB_128, 'encrypted_100MB_128.txt')
 
encrypted_100MB_256 = encrypt_file("100MB_file.txt", key_256)
save_encrypted_data(encrypted_100MB_256, 'encrypted_100MB_256.txt')



encrypted_1024MB_128 = encrypt_file("1024MB_file.txt", key_128)
save_encrypted_data(encrypted_1024MB_128, 'encrypted_1024MB_128.txt')
 
encrypted_1024MB_256 = encrypt_file("1024MB_file.txt", key_256)
save_encrypted_data(encrypted_1024MB_256, 'encrypted_1024MB_256.txt')


