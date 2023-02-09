f = open('C:/python_ex/textfile.txt','w') 
a = ['\n hello', '\n hii', '\n world']
b = 'hello python'
f.write(b)
f.writelines(a)
f.close()

f = open('C:/python_ex/textfile.txt','r') 
print(f.read())
f.close()



