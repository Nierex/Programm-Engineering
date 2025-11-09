class Mammal:
    className = 'Mammal'

class Dog(Mammal):
    species = 'canine'
    sounds = 'wow'

class Cat(Mammal):
    species = 'feline'
    sounds = 'meow'

dog = Dog()
cat = Cat()

print(f"Dog is {dog.className}, but they say {dog.sounds}")
print(f"Cat is {cat.className}, but they say {cat.sounds}")
