def func(list1, list2 = [1,2,3,4,5]):
    listResult = [n for n in list1 if n not in list2]
    return listResult

list1 = [1,2,3,4,5,6,7,8]
list3 = func(list1)
print(list3)
list4 = func(list1,list3)
print(list4)
