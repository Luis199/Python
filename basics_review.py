

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
#Sprint(team.ljust(2))

#print(family_members)



#Tuples
my_house = (2,78,True, False, "Luis")
trivial_stuff = ("my house", 'The Park', True, 69, "Tekashi")
numbers = (100, 1.00, 1000, 0.23)
#print(my_house)



#Sets
my_set = {76,"Luis", False, "Last Dance"}
your_set = {89, 'Jose', 'John', True}
#print(my_set.union(your_set))
#print(my_set.intersection(your_set))
#print(my_set.difference(your_set))
my_set.add(False)
my_set.pop()
my_set.clear()



#Dictionaries

capitals = {"Iowa":'DesMoine', 'Wiscosin':'Madison'}
capitals['Utah'] = 'SaltLakeCity'
#print(capitals['Iowa'])
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())


#string formatting 

#name = input('Please enter your name: ')
#print('%s is a great person. '%(name))



#object oriented design

class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print(self.num, '/', self.den)

myf = Fraction(3,5)
print(myf.show())