a = "pippo è nel parco"
set = {x for x in a}
set2 = {x for x in "pippo"}
print(set)
set = set - set2
print(set)