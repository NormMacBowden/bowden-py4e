my_fname = input("Enter a file name: ")
my_file = open(my_fname)
my_word = input("Enter a word to count: ")
import re
x = re.findall(my_word, my_file.read(), flags = re.I)
print("\""+ my_word +"\"","appears",len(x),"times.")