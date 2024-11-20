# Overwriting a file
with open("example.txt", 'w') as file:
    file.write("This is a test.\n")

# Appending to a file
with open("example.txt", 'a') as file:
    file.write("Appending a new line.\n")
