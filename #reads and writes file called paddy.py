#reads and writes file called paddy.txt

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
            return content
    except FileNotFoundError:
        print("File not found")
        return None

def write_to_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
            print("Content written to the file successfully")
    except IOError:
        print("Error writing to the file")

def append_to_file(file_path, content):
    try:
        with open(file_path, 'a') as file:
            file.write("\n" + content)
            print("Content appended to the file successfully")
    except IOError:
        print("Error appending to the file")

# Example usage
file_path = "example.txt"

# Reading from the file
file_content = read_file(file_path)

if file_content:
    # Writing the content to a new file
    write_to_file("paddy.txt", file_content)

    # Appending "Hello" to the file
    append_to_file("paddy.txt", "Hello")