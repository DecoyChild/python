# syntax of reading and writing to a file

'''
modes: 
r = read mode
w = write mode
x = write mode (for new files)
a = Append mode (adds to the end of an existing file)
use t for text of b for binary I.E.:  rt is read mode in text where rb is read mode in binary 

'''
var1 = open(fileName, xt)

# to close (in order to release for use)
var1.close()
