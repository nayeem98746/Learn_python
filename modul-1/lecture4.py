my_list= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

indx = 0

while indx < len(my_list):

    # print(my_list[indx])

    indx += 1



herons = ["Heron of Alexandria", "Heron of Antioch", "Heron of Byzantium"]

ind = 0

while ind < len(herons):

    # print(herons[ind])
    ind += 1


num = (1, 2, 3, 4, 52, 63, 723, 823, 9, 1023)

numind = 0
x = 823
while numind < len(num):

    if(num[numind] == x):
        print("Found the number" , numind)
        break

    numind += 1