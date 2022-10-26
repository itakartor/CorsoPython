
listItem =  ["a","b","c",2]
listItem =  [1,2,3]
match listItem:
    case [a,e,f]:
        print (3)
    case [a]:
        print (1)
    case [a,d]:
        print (2)
    case _:
        print("case default")
    
match listItem:
    case [a]:
        print (1)
    case [a,d]:
        print (2)
    case [1,*resto]:
        print (f"3a {resto}")
    case _:
        print("case default")