text = "Python is awesome"
words = text.split()
print("Words:", words)

a=5 #global vraible
b=2
def adtion():
    a=4 #local variable 
    b=6
    return a+b

def sub():
    return a-b

print(adtion())
print(sub())