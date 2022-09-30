a = "python"
list2 = [1,2,3,4,5,6]
set = {x: "ok" for x in a if(x > "p")}

list = [a for a in list2 if a%2==0]

print(set)
print(list)