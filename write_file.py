def write_file(fname):
    with open(fname,'w') as f:
        while True:
            s = input(">>")
            if not s : # Break om empyty string
                break 
            f.write(s + '\n')

write_file("test.txt")
