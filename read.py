Rfile = open('C:/python_ex/textfile.txt','r')

while Rfile:
    x = Rfile.readline()        
    print(x)
    if x == '':
        break

Rfile.close()