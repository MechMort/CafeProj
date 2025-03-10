menu_dict = {}
def CreateNewLocalOrder(**order):
    order_list =[]
    order_cost = 0
    print("Creating Order:")
    for item,number in order.items():
        order_list.append(item + " " + str(number))
        order_cost += int(menu_dict[item]) * number
    return order_list, order_cost

def MoveOrderToFile():
    newOrder = CreateNewLocalOrder(Coffee = 3, Cola = 2)
    with open('Orders.txt','r+') as file:
        lines = file.readlines()
        lines.append(newOrder)
    with open("Orders.txt", "w") as file:
        file.writelines(str(lines) + ":Order Status = Created;")    

def DisplayGreetingMessage():
    print("Hello and welcome to the Cafe!")
    print("How can we help you today!")

def AddItem(item_type,item_name,item_cost):
    with open('Menu.txt','r+') as file:
        lines = file.readlines()
        linNo = 0
        match item_type:
            case "SNACK":
                print("Adding new Snack")
                for line in lines:
                    linNo += 1
                    if   "---SNACKS---" in line:
                        lines[linNo] = lines[linNo].strip() + '\n' + str(item_name) + " : " + str(item_cost) + ";" + '\n'
            case "DRINK":
                print("Adding new Drink")
                for line in lines:
                    linNo += 1
                    if   "---DRINKS---" in line:
                        lines[linNo] = lines[linNo].strip() +  '\n' + str(item_name) + " : " + str(item_cost) + ";" + '\n'
            case _:
                print("ERROR")
    with open("Menu.txt", "w") as file:
        file.writelines(lines)
    GetMenu()

def SetUpLocalOrder(**order):
    DisplayMenu()
    responce = input("Please take your time and view our menu! Let us know what you would like : )")
    if(menu_dict.get(responce)):
        No = input((f"How many {responce} would you like to add?"))
    CreateNewLocalOrder(responce = Nogithu)
    



def GetMenu():
    current_Item = ""
    current_Price = ""
    isPrice = False
    with open('Menu.txt','r') as file:
        for line in file:
            if not line.startswith('#') and not line.startswith('-'):
                for char in line:     
                   if(isPrice == False):  
                        if(char == ':'):
                            isPrice = True
                        else:
                            current_Item += char
                   else:
                        if(char != ';'):
                            current_Price += char
                        else:
                           isPrice = False
                           current_Item = current_Item.removeprefix('\n')
                           current_Item = current_Item.removesuffix('\n')
                           menu_dict[current_Item] = current_Price
                           current_Price = ""
                           current_Item = ""
          

def DisplayMenu():
    with open("Menu.txt", "r") as file:
        lines = list(line for line in (l.strip() for l in file)if line)
        for line in lines:
            if('#' not in line):
                print(line.removeprefix('\n').removesuffix('\n'))
        print(file.read())
    return

def ManageProgramFlow():
    GetMenu()
    DisplayGreetingMessage()
    responce = input(" 1. Place a new order \n 2. Create a new menu item \n 3. Check on a current order")
    match responce:
        case "1":
            print("1")
            SetUpLocalOrder()
        case "2":
            print("2")
        case "3":
            print("3")
        case _:
            print("Please enter your resonse as a single digit")
    return
""" print(current_Item, " : " ,'£' , "{:.2f}".format(round((float(current_Price) / 100),2)))"""                     

""" AddItem('SNACK','Jelly Cats',300)
AddItem('DRINK','Jelly SODA',300)  """
""" DisplayMenu()    
 """


ManageProgramFlow()
