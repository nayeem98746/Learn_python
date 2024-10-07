 stri1 = "this is \n a string"
 print(stri1)


strin = "this is a string"
string = "this is a string"
print(len(strin+string))

print(strin[5:len(strin)])

print(string.endswith("ing"))
print(string.capitalize())

print(strin.replace("this" , "that"))
print(strin.find("a"))
print(strin.count("a"))

name = input("type you name")

print(len(name))

name = ""

if (name == "nayeem"):
    print("he is good boy")
elif(name == "madafaker"):
    print("he's name is dihan")
elif(name == "nucha"):
    print("he's hasib")
else: 
    print("he is not guy")


age = 18 

if(age >= 18 ):
    print("he can vote")
else:
    print("he can't vote")