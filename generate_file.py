def generate_file(file_name, file_size_B):
	with open(file_name, 'wb') as f:
		f.write(b"A"*file_size_B)

generate_file("10B_file.txt", 10)
generate_file("50B_file.txt", 50)
generate_file("100B_file.txt", 100)
generate_file("128B_file.txt", 128)
generate_file("164B_file.txt", 164)
generate_file("192B_file.txt", 192)
generate_file("256B_file.txt", 256)
generate_file("512B_file.txt", 512)
generate_file("1024B_file.txt", 1024)
generate_file("2048B_file.txt", 2048)
