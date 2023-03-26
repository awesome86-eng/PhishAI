file=open("output.txt","r")
data = file.read().splitlines(True)
print(' '.join(data[1:]))
