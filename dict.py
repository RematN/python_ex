dict= {"a":{"age":20,"dob":"01/05"}, "b":{"age":21,"dob":"01/02"}, "c":{"age":23,"dob":"17/08"}}

# dict["s_nm"] = dict["age"]
# del dict["age"]

# print(dict)

def return_key(val):
    for key, value in dict.items():
        if key==val:
           new_nm = input("enter new name: ")
           dict[new_nm] = dict[key]
           del dict[key]

           return dict
    return('Key Not Found')
return_key('Dollar')

print(return_key(input("enter name you want to update:")))
print(dict)