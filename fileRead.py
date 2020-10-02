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

#matches only the beginning of the string
# match()
if re.match('Mad', cerseiSpeech):
  print("Pattern matched!")
else:
  print("No pattern match.")

# search()
pattern = "your"
if re.search(pattern, cerseiSpeech):
  print("Pattern matched!")
else:
  print("No pattern match.")

# findall()
pattern = "your"
results = re.findall(pattern, cerseiSpeech)
print(results)

# sub()
results1 = re.sub ('her', 'HER', cerseiSpeech)
results2 = re.sub ('she', 'SHE', results1)
print(results2)
