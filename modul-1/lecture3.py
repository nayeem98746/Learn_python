marks = [90, 25, 67, 45, 80]

# print(type(marks[4]))
# print((marks[4]))


string = ["nayeem", "dihan", "hasib", "nucha"]

# print(string[0])

# string[2] = "sabbir"
# print(string[2])
# string.append("sabbir")

# print(string)


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list.insert (2, 100)

list.copy()
print(list)


# python tuple 

tupleList = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# print(tupleList[2])

mylist = []

movies1 = mylist.append(input("Enter your movie: "))
movies2 = mylist.append(input("Enter your movie: "))
movies3 = mylist.append(input("Enter your movie: "))

# print(mylist)

taple = ("7", "8", '9', "10")

# print(taple.count("7"))

dictionary = {
    "name": "nayeem",
    "age": 18
}
print(type(dictionary))


collection = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , "hellow", "world"}
collection.add("nayeem")
collection.remove(4)
print(collection)
print(len(collection))


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))
print(set1.intersection(set2))


marks = {}

x = int(input("Enter your ph: "))
marks.update({"physics": x})

x = int(input("Enter your ph: "))
marks.update({"math": x})

x = int(input("Enter your ph: "))
marks.update({"bio": x})

print(marks)

values = {9 , 9.0}

print(values)
