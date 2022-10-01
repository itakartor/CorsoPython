x = 100

def func():
    x = 20
    print("local: ")
    print(x)

def funcGlobal():
    global x
    x = 30
    print("global Change: ")
    print(x)

def funcLocal():
    y = 50
    def local():
        y = 10
        print("local func: ")
        print(y)
    local()
    print("not local:")
    print(y)

    def funcLocalChage():
        nonlocal y
        y = 60
        print("not local change:")
        print(y)
    funcLocalChage()
    
def main():
    func()
    print("global")
    print(x)
    funcGlobal()
    print(x)
    funcLocal()

main()