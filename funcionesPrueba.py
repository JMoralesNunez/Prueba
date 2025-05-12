#Colors
DANGER = "\033[91m"
WARNING = "\033[93m"
SUCCESS = "\033[92m"
RESET = "\033[0m"

def add(name,price,quantity,inventory):  #Function to add items, the name will be the key. The price and quantity will be added to a dictionary that will be the value of the name
    info = {"price":float(price), "quantity":int(quantity)} # add price and quantity to a dictionary
    inventory[name.capitalize()]=info  # add the name as key, and the previous dictionary as value
    print(SUCCESS+f"{name} ha sido añadido(a) exitosamente!"+RESET)

def show(inventory): #Function to show all elements of the inventory with a For loop
    for product,info in inventory.items():
        print(f"{product}.................. Precio: ${info['price']} | Cantidad: {info['quantity']}")

def search_item(name,inventory): #function to search an item by its name
    format=inventory.get(name) #get() returns the value assossiated with the key, if there is not, it will return None
    if format == None:  
        print(DANGER+"Esté producto no existe en el inventario"+RESET)
    else:
        print(SUCCESS+f"Nombre: {name}, Precio: {format["price"]}, Cantidad: {format["quantity"]}"+RESET)

def update(name, newprice,inventory): #Function to change the price of the product
    inventory[name]["price"] = newprice  #We simply index the dictionary with the key(name) and the key("price") to update the value we want

def delete(name,inventory): #Function to delete an item
    inventory.pop(name) #We use pop to delete the key and value
    print(SUCCESS+f"{name} ha sido eliminado exitosamente"+RESET)