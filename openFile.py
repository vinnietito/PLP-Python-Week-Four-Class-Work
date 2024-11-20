# Open a file in read mode
file = open("example.txt", 'r')

# Always close after use
file.close()




# # Open the file in write mode (this creates the file if it doesn't exist)
# try:
#     writedoc = open("myDataFile.txt", 'w')  # 'w' creates/overwrites the file
#     writedoc.write("This is a write test")  # Write content to the file
#     print("Content written successfully!")
# except Exception as e:
#     print(f"An error occurred: {e}")  # Handle potential errors
# finally:
#     writedoc.close()  # Close the file


# file


# f1 = open("myDataFile.txt", "r")

# print(f1)


# f1 = open("myDataFile.txt", "r")
# content = f1.read()
# print(content)
# f1.close()


# f1 = open("myDataFile.txt", "r")
# for line in f1:
#     print(line.strip())  # `.strip()` removes leading/trailing whitespaces including `\n`
# f1.close()
