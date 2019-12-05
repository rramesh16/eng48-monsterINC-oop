from monster_class import *

# Creating instances

Monster1 = Monster('Sulley',['creating chaos','disorganised'])
Monster2 = Monster('Mike', ['funny', 'friendly'])

# Calling the attributes

print(Monster1.name)
print(Monster1.skills)
print(Monster1.eat())
print(Monster1.scare_attack())


print(Monster2.name)
print(Monster2.skills)
print(Monster2.sleep())