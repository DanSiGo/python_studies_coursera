data_string = "The last season of Game of Thrones was not good"

listA = ['Stranger Things', 'S Education', 'Game of Thrones']

print("The original string : " + data_string)

print("The original list : " + str(listA))

res = [ele for ele in listA if(ele in data_string)]
print(res)


print("Does string contain any list element : " + str(bool(res)))
    

#     res = [ele ---for ele in listA--- ---if(ele in data_string)---]

res = [ele]
for ele in listA
if (ele in data_string)


"""
There are many approaches you can use to determine whether an item exists
in the list or not. For example, we have seen the following ways.

*** Using Python “in” operator

listA = ['Stranger Things', 'S Education', 'Game of Thrones']
if 'S Eductation' in listA:
    print("Yes, 'S Eductation' found in List : ", listA)

    
*** Using Python list comprehension

data_string = "The last season of Game of Thrones was not good"
listA = ['Stranger Things', 'S Education', 'Game of Thrones']
res = [ele for ele in listA if(ele in data_string)]
print("Does string contain any list element : " + str(bool(res)))

*** Using list.count() method

listA = ['Stranger Things', 'S Education', 'Game of Thrones']
if listA.count('Stranger Things') > 0:
    print("Yupp, 'Stranger Things' found in List : ", listA)
    
*** Using Python any() function

listA = ['Stranger Things', 'S Education', 'Game of Thrones']
if 'Witcher' not in listA:
    print("Yes, 'Witcher' is not found in List : ", listA)

"""
