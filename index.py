a = 2
b = 3
print(a*b)

if a==3:
    print("ok")
elif a<5:
    print(a)
else:
    print("not ok")


def speak(text):
    print(text)
    print(text*3)
    return text


print(speak(2))
# speak("0")

name = "youstart"
print(name[:4:-1])

def palindrome(text):
    return print(text == text[::-1])


palindrome("1232111")