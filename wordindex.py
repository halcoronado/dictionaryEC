

infile = open("book of John text.txt",'r')

SC = [ ',' , '.' , '”' , "'" , '"' , "'"  , '?' , '!' , '&', '@', '*' , '#', ')','(', '%' ]
SC=str(SC)
words = infile.readline()
for x in SC:
    words = words.replace(x,' ')
words = words.split()

wordlist = []
for i in words:
    wordlist.append(i)

word_dict= {}
for n in wordlist:
    counter = wordlist.count(n)
    word_dict[n] = {counter}

for key in list(word_dict.keys()):
    print(key, ":",word_dict[key], sep = '')

     if key == 'Father':
         print(key, ":",word_dict[key], sep = '')
     elif key == 'God':
        print(key, ":",word_dict[key], sep = '')
     elif key == 'Christ':
        print(key, ":",word_dict[key], sep = '')
     elif key == 'Spirit':
        print(key, ":",word_dict[key], sep = '')
     elif key == 'spirit':
        print(key, ":",word_dict[key], sep = '')
     elif key == 'life':
        print(key, ":",word_dict[key], sep = '')
     elif key == 'man':
        print(key, ":",word_dict[key], sep = '')
    

infile.close()
