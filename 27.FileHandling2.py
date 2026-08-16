# read(5) read only first five chars
# read(5) now move to next five before i read
# f.tell() give the file pointer
# f.seek() ---> move to the first char
# f.seek(5) -- >means now it will start after 5 


f = open("Practice/abc.txt")
f.seek(0);

for line in f:
    print(line)

# f.readline() --> 1st line
# f.readline() --> 2nd line
# f.readline(20) --> will read the first 20 chars
# f.readlines() --> Will read all the lines and show in the form of list
