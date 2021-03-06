import os.path


def read_file(file_name):
    with open(file_name, mode="r") as fileread:
        for line in fileread:
            yield line


def read_lines_for_python(file_name, file_type):
    if file_type not in ("txt", "html"):
        raise ValueError("Incorrect file format")
    if not os.path.isfile(file_name):
        raise IOError("No file")
    for line in read_file(file_name):
        if line.find("Python") != -1:
            return "Word Python found"
    return False


print(read_lines_for_python("files/file_with_Python_word.txt", "txt"))
print(read_lines_for_python("files/emails.txt", "txt"))
# print(read_lines_for_python("files/emails1.txt", "txt")) # OSError: No file

if not read_lines_for_python("files/emails.txt", "txt"):
    print("There is no Python word in the file")

# read_lines_for_python("files/file_without_Python_word.json", "json") # ValueError: Incorrect file format
