groc_list=["Milk","Bread","Eggs","Peanut Butter","Jelly"]
#print("Intial List")
for x in range(len(groc_list)): 
    print(groc_list[x])
postion = groc_list.index("Peanut Butter")
#print(postion)
groc_list[postion] ="Almond Butter"
#print(groc_list)
groc_list.remove ("Jelly")
groc_list.append("Coffee")
print("Updated List")

for x in range(len(groc_list)): 
    print(groc_list[x])