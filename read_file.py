# Function to read the entire file content
def read_file(fname):
    try:
        with open(fname, 'r') as f:
            text_str = f.read()  # Read the file
        return text_str  # Return it
    except FileNotFoundError:
        return f"Error: File '{fname}' not found."
    except Exception as e:
        return f"An error occurred: {e}"

# Function to count the number of words in the file
def count_words_in_file(fname):
    try:
        with open(fname, 'r') as f:
            text_str = f.read()
        return len(text_str.split())
    except Exception as e:
        return f"An error occurred: {e}"

# Function to count the number of lines in the file
def count_lines_in_file(fname):
    try:
        with open(fname, 'r') as f:
            lines = f.readlines()
        return len(lines)
    except Exception as e:
        return f"An error occurred: {e}"

# Function to append content to an existing file
def append_to_file(fname, content):
    try:
        with open(fname, 'a') as f:
            f.write(content)
        print(f"Content appended to {fname}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to reverse the content of the file
def reverse_file_content(fname):
    try:
        with open(fname, 'r') as f:
            text_str = f.read()
        return text_str[::-1]
    except Exception as e:
        return f"An error occurred: {e}"

# Function to search for a specific word in the file
def search_word_in_file(fname, word):
    try:
        with open(fname, 'r') as f:
            text_str = f.read()
        return text_str.count(word)
    except Exception as e:
        return f"An error occurred: {e}"

# Function to write content to a new file
def write_to_new_file(fname, content):
    try:
        with open(fname, 'w') as f:
            f.write(content)
        print(f"Content written to {fname}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage of functions
if __name__ == "__main__":
    print(read_file('test.txt'))
    print(f"Total words: {count_words_in_file('test.txt')}")
    print(f"Total lines: {count_lines_in_file('test.txt')}")
    append_to_file('test.txt', '\nThis is new appended content.')
    print(f"Reversed content:\n{reverse_file_content('test.txt')}")
    print(f"Occurrences of 'Python': {search_word_in_file('test.txt', 'Python')}")
    write_to_new_file('new_file.txt', 'This is a completely new file.')
