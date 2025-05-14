from funcionesPrueba import *

Menu=True
inventory = {
    "Pizza":{"price": 35.5, "quantity": 12},
    "Arroz":{"price": 5, "quantity": 30},
    "Salsa":{"price": 6.5, "quantity": 20},
    "Carne":{"price": 12.5, "quantity": 10},
    "Azucar":{"price": 7, "quantity": 7},
}

while Menu:  #Bucle para mostrar el menu principal
    print("="*75)
    print("¡Bienvenido a tu inventario!")
    print("1. Añade productos")
    print("2. Ver todos los productos")
    print("3. Buscar un producto")
    print("4. Actualizar precios")
    print("5. Borrar productos")
    print("6. Calcular valor total del inventario")
    print("7. Salir")
    print("="*75)
    while True: #loop to validate correct option for the menu
        option = input("Selecciona una opción: 1/2/3/4/5/6/7: ")
        if option.isdigit() and int(option) >= 1 and int(option) <=7:
            break
        else:
            print(WARNING + "Ingresa una opción válida" + RESET)
    if option == "1":
        while True: #While loop to keep adding products
            while True: #While loop to validate the name of the product input  
                name = input("Ingresa el nombre del producto: ")
                if name.isalpha() and name.capitalize() not in inventory.keys(): #If the product is already on the inventory, it won't let it add it again, because it would overwrite the product
                    break
                else:
                    print(WARNING + "El nombre del producto no es válido o ya se encuentra en el inventario" + RESET)
            while True: 
                try: #Try/Except to validate the price input, if a letter is given the except will take action.
                    price = float(input("Ingresa el precio del producto: "))
                    if price >= 0.0:
                        break
                    else:
                        print(WARNING + "Precio no válido, intenta nuevamente" + RESET)
                except:
                    print(WARNING+"Ingresa un precio válido"+RESET)
            while True: #While loop for quantity validation input
                quantity = input("Ingresa la cantidad de producto: ")
                if quantity.isdigit() and int(quantity) > 0: #Quantity must be above 0, I remove the possibility to add 0 items, because I believe it has no sense.
                    break
                else:
                    print(WARNING+"Por favor ingresa una cantidad válida"+RESET)
            add(name, price, quantity, inventory)
            while True: #While loop to validate if the user wants to continue adding products or not
                reset = input("¿Te gustaría añadir otro producto? 1.Si/2.No: ")
                if reset.isdigit()==False:
                    print(WARNING+"Por favor Ingresa una opción válida(1/2)"+RESET)
                elif int(reset) != 1 and int(reset) != 2:
                    print(WARNING+"Por favor Ingresa una opción válida(1/2)"+RESET)
                else:
                    break
            if int(reset) == 2:
                break
    if option == "2":
        if not inventory: # In case there are no products in the inventory
            print("No hay productos en el inventario")
        else:
            print("Tus productos son:")
            print("="*75)
            show(inventory)
    if option == "3":
        while True: #Validation of the name of the product we are searching for
            name_search = input("Ingresa el nombre del producto que estás buscando: ")
            if name_search.isalpha():
                name_search=name_search.capitalize()
                break
            else:
                print(WARNING+"Por favor ingresa un nombre válido"+RESET)
        search_item(name_search, inventory)
    if option == "4":
        while True: #Validation of the name of the product we are changing its price
            name_price = input("Ingresa el nombre del producto al que deseas cambiar su precio: ")
            if name_price.isalpha() and name_price.capitalize() in inventory.keys(): #If the product is not in the inventory, it won't let the user change its price
                name_price=name_price.capitalize()
                break
            else:
                print(WARNING+"Ingresa un nombre válido o el nombre de un producto que esté en el inventario"+RESET)
        print(f"El precio actual de {name_price} es: ${inventory[name_price]["price"]}")  #Show the current price of the product
        while True: #New price validation, the same validation as we did when adding a product
            try:
                newprice = float(input("Ingresa el nuevo precio del producto: "))
                if newprice >= 0.0:
                    break
                else:
                    print(WARNING+"Precio no válido, intenta nuevamente"+RESET)
            except:
                print(WARNING+"Ingresa un precio válido"+RESET)
        update(name_price,newprice,inventory)
        print(SUCCESS+f"El precio de {name_price} ha sido actualizado"+RESET)
    if option == "5":
        while True: #While to to validate and ask the user if an inventory deletion is needed or just need to delete one item
            delete_method = input("¿Deseas borrar todo el inventario o sólo un producto? 1.Un sólo producto/ 2. Todo el inventario: ")
            if delete_method.isdigit()==False:
                print(WARNING+"Por favor Ingresa una opción válida(1/2)"+RESET)
            elif int(delete_method) != 1 and int(delete_method) != 2:
                print(WARNING+"Por favor Ingresa una opción válida(1/2)"+RESET)
            else:
                break
        if delete_method=="1":
            while True: #Validation of the product we are deleting
                name_deletion = input("Ingresa el nombre del producto que quieres eliminar: ")
                if name_deletion.isalpha() and name_deletion.capitalize() in inventory.keys(): #It won't let delete an item that doesn't exist in the inventory
                    name_deletion=name_deletion.capitalize()
                    break
                else:
                    print(WARNING+"Ingresa un nombre válido o el nombre de un producto existente en la lista"+RESET)
            delete(name_deletion,inventory)
        else:
            inventory.clear()
            print(SUCCESS+"Todos los productos del inventario han sido eliminados exitosamente"+RESET)
    if option == "6":
        total_prices = dict(map(lambda item: (item[0], item[1]["price"] * item[1]["quantity"]), inventory.items())) #lambda gets the key of the inventory, which is the name, and multiplicates the price and quantity, and leave it as the value;
                                                                                                                    #This gets inside a tuple with items(); map() executes the lambada function with each element of the inventory. Then Dict() leaves everything in a new dictionary
        for item,price in total_prices.items(): #For loop to show the name and total price of each product
            print(SUCCESS+f"{item}{RESET}................... Precio total: {SUCCESS}${price:.2f}"+RESET)
        total=0
        for value in total_prices.values(): #For loop to get the Total price of the inventory
            total += value
        print(f"El precio total de todos los productos en el inventario es: {SUCCESS}${total:.2f}"+RESET)
    if option == "7": #Option to stop the Menu loop and finish the program
        print(SUCCESS+"¡Gracias, vuelva pronto!"+RESET)
        Menu=False
