# a = input("your name?")
# print(3)


person = {"name":"ajay", "age":30,"subject":"python"}

city = dict(name="jaipur",pin=302017)
print(city)


person["hometown"] = city

for p in person:
    print(p)


for (prop,value) in person.items():
    print(prop,value)

for i in range(1,10,2):
    print(i)

person["name"] = "abc"
print(person)
print(person["age"])
person["email"] = "contact@youstart.in"
print(person)

person2 = person
person2["name"]= "zyx"
print(person)
print("----------------------")
print(person["hometown"]["pin"])
person["hometown"]["pin"] = 302016
person["phones"] = ["1","2"]
print(person["phones"][1])
