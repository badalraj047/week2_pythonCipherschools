
names=['Badal', 'Baasu','Bharti']
for name in enumerate(names):
    print(name)

for i,name in enumerate(names):
    print(i,"-",name)


scores=[80,70.90,91]

for name,score in zip(names,scores):
    print(name,"-",score)