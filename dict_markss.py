class marksheet(object):
    def __init__(self,name,total,per):
        self.name = name
        self.total = total
        self.per = per

    def get_total(self):
        return self.total
    
    def get_per(self):
        return self.per
    
    def __str__(self):
        return self.name + ':' + str(self.get_total()) +'  :'+ str(self.get_per())
           

def marks(rec,name,total,per):
    rec.append(marksheet(name,total,per))
    #rec["Name"].append(marksheet(name))
    # rec["Total"].append(marksheet(total))
    # rec["Per"].append(marksheet(per))
    return rec


record =[] 

x = 'y'
while x == 'y':
    name = input('Enter name :')
    sb1 = int(input('Enter DSP marks:'))
    sb2 = int(input('Enter DIVP marks:'))
    sb3 = int(input('Enter IOT marks:'))
    total = sb1 + sb2 + sb3
    per = (total/300)*100
    record = marks(record,name,total,per)
    x = input('anothe student(y/n):')

#n = 1 
for s in record:
    a = s.get_total()    
    b = s.name
    c = s.get_per()
    dct = {"Name":b, "Total":a, "Percentage":c}
    #d = {"Name":[s], "Total":[s+1], "Per":[s+2]}
    #res_dct = {record[s]: record[s + 1]  for s in range(0, len(record), 3)}
    #n = n + 1
    print(dct)
    

