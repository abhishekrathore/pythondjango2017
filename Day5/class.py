class Animal():
    color = "blue"
    def speak(self):
        print(self.color)


animal = Animal()
print(animal.color)
animal.speak()

a = [x for x in range(0,100,5) if x%25!=0]
print(a)