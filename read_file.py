def read_file(fname):
    with open(fname,'r') as f:
        text_str = f.read() # Read the file
    return text_str # Return it.

print(read_file('test.txt')) # pass the test.txt
