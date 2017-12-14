fw=open('sample.txt','w') #open a file and write to it
fw.write('write some code \n')
fw.write('hello world')
fw.close()

# create a new file name sample.txt

fr=open('sample.txt','r')
text=fr.read()
print(text)
fr.close()
