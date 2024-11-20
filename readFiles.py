with open("example.txt", 'r') as file:
    content = file.read()  # Reads the entire file
    print(content)

# Reading line by line
with open("example.txt", 'r') as file:
    for line in file:
        print(line.strip())  # `.strip()` removes extra whitespace
