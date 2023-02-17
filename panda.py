import pandas as pd
dt = pd.DataFrame({"name":['remat','priti','thmsy','bhavi','harsh','manjit'],
                    "age":[20,21,23,24,25,26],
                    "sex":['f','f','f','f','m','m'],
                  })
# print(dt)
# print(dt["age"])
ages = pd.Series([20,21,23,24,25,26])
print(ages)
# print(dt["age"].max())
# dt.describe()