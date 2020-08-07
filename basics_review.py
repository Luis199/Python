

family_members = ['Emma', 'Erismell', "Erik", 'Carmen', "Fred", "Luis"]
'''
if "Luis" in family_members:
    print("Luis")

print(len(family_members))
print(len(family_members[:2]))
'''
# Methods that could be implemented on a python list
family_members.insert(2, 'Juan')
family_members.append('Jose')
family_members.sort()
family_members.reverse()
del family_members[1]
family_members.index('Luis')
family_members.remove('Carmen')


#Methods that could be implemented on a strin
team = 'LA Lakers'
team.center(3)
team.count('a')
print(team.ljust(2))

#print(family_members)



#Tuples
my_house = (2,78,True, False, "Luis")
trivial_stuff = ("my house", 'The Park', True, 69, "Tekashi")
numbers = (100, 1.00, 1000, 0.23)
#print(my_house)



#Sets
my_set = {76,"Luis", False, "Last Dance"}
print(len(my_set))