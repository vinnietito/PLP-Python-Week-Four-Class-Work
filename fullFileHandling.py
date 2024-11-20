import os

# Create a file
with open("sample.txt", 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")

# Read the file
with open("sample.txt", 'r') as file:
    print("File Content:")
    print(file.read())

# Append to the file
with open("sample.txt", 'a') as file:
    file.write("Adding more lines.\n")

# Read again after appending
with open("sample.txt", 'r') as file:
    print("Updated Content:")
    print(file.read())

# Delete the file
if os.path.exists("sample.txt"):
    os.remove("sample.txt")
    print("File deleted.")
else:
    print("File not found.")
