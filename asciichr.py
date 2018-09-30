
f= open('file.txt','w')
for i in range(33,125):
	f.write(str(i))
	f.write(' ')
	f.write(chr(i))
	f.write('  ')
f.close()
