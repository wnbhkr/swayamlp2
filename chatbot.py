print("Welcome to our online shoe shop")

def brands():
    print("Available brands are: ")
    brand = ['nike','adidas','sparks']
    print(brand)

def sizes():
    print("Available sizes are: ")
    size = [8,9,10]
    print(size)

def prices():
    print("Shoes are available between price range 999 to 5000")

def colors():
    print("Available colors are: ")
    color = ["Red","Black","White"]
    print(color)

database = [(2000,'Nike','Black',9),(3000,'Adidas','Red',10)]

def check(mn,mx,brnd,clr,sz):
    for tup in database:
        if (tup[0] >= mn and tup[0] <= mx) and tup[1] == brnd and tup[2] == clr and tup[3] == sz:
            return True
        else:
            return False;

while True:
    print("Enter 1 to see brands: ")
    print("Enter 2 to see sizes available: ")
    print("Enter 3 to see price range: ")
    print("Enter 4 to see colors available: ")
    
    print("Enter 5 to check for a particalur shoe: ")
    print("Enter 6 to exit: ")
    inputt = int(input())
    if inputt == 1:
        print(brands())
    if inputt == 2:
        print(sizes())
    if inputt == 3:
        print(prices())
    if inputt == 4:
        print(colors())

    if inputt == 5:
        print(("Enter price range(min and max price): "))
        mn,mx = map(int,input().split())
        brnd = input("Enter brand you are looking for: ")
        clr = input("Enter color: ")
        sz = int(input("Enter size: "))
        if check(mn,mx,brnd,clr,sz):
            print("Required shoe is available at store")
        else:
            print('Required Shoe is not available')
