# Operation in File Handlin
# Open a file
# Read file
# Write file
# Close file

f1 = open('Practice/abc.txt')
# File modes r, w, x, a, t, b, +
# r --> read mode
# w means open file in write mode. Override the existing data and if file does not exit then it will create
# a means open a file in appending mode at the end of file without truncating. Create a new file it does not exists
# x means open a file for exclusive creation. If file already exists then operation fails
# b open in binary mode
# + open file for updating

data = f1.read()
print(data)

f = open('Practice/new.txt', 'w')
f.write("Python is important for interviews")
f.close()
