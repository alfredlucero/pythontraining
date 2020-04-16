# python files.py
# Input and Output
# input()
# print()

# File Input and Output
# open()
# read()
# seek(offset) - go to X byte in file
# tell() current position in file
# .mode
# write()
lists_file = open("./lists.py")
lists_file_contents = lists_file.read()
print(lists_file_contents)
print(lists_file.seek(10))
print(lists_file.tell())
lists_file.close()
print(lists_file.closed)

# Automatically close file after this block
with open("helloworld.py") as helloworld:
    print("File closed?", helloworld.closed)
    print(helloworld.read())

print("Finished reading file")
print("File closed", helloworld.closed)

with open("functions.py") as functions_file:
    for line in functions_file:
        print("Line", line.rstrip())
