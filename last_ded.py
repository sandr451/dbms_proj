import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="", database="")
cursor = db.cursor()

while True:
    print("LogIn as:")
    print("1. Customer")
    print("2. Seller")
    print("3. Delivery Person")
    x = int(input())

    print("Username:")
    username = input()
    print("password")
    password = input()

    type = {1: "customer", 2: "seller", 3: "dp"}

    cursor.execute(f'''SELECT * from logindetails l where l.Username = "{username}" and l.Password = "{password}" and l.Type= "{type[x]}"''')
    data = cursor.fetchall()
    if len(data) == 0:
        print("Invalid Username or Password")
        continue
    else:
        tup = data[0]
        person_id = tup[3]

    if x == 1:
        while True:
            print("1. View Catalog")
            print("2. View Order History")
            print("3. View Cart")
            print("4. Log Out")
            option = int(input())

            if option == 1:
                cursor.execute('''SELECT Product_ID, Name, Price, Quantity_Available from Products;''')
                data = cursor.fetchall()
                if len(data) > 0:
                    for i in data:
                        print(data[0], ": ", data[1], " ", str(data[2])+"$", " Quantity available:", data[3])

                while True:
                    print("1. Add Item to cart")
                    print("2. View Cart")
                    print("3. View Product Review")
                    print("4. Exit")
                    alpha = int(input())

                    if alpha == 1:
                        print("Enter Product_ID:")
                        pid = input()
                        print("Enter Quantity:")
                        quan = input()

                        cursor.execute(f'''select * from Cart c where c.CCustomerID = {person_id}''')
                        data = cursor.fetchall()
                        if len(data) > 0:
                            cart_id = data[0][0]
                        else:
                            cursor.execute(f'''insert into Cart (Cart_ID, CCustomerID) values ({None} , {person_id})''')
                            cursor.execute(f'''select * from Cart c where c.CCustomerID = {person_id}''')
                            data = cursor.fetchall()
                            cart_id = data[0][0]
                        cursor.execute(f'''insert into Cart_Item (id, Cart_ID, Product_ID, Quantity) 
                        values ({None}, {cart_id}, {pid}, {quan})''')

                    if alpha == 2:
                        cursor.execute(f'''Select * from Cart_Items ci where ci.cart_ID in select c.Cart_ID
                                        from Cart c where c.CCustomerID = {person_id} and c.Order_Placed = 'no';''')
                        data = cursor.fetchall()
                        if len(data) > 0:
                            for i in data:
                                print("Product ID:", str(data[2]), " Quantity :", data[3])

                            print("1. Checkout")
                            print("2. Exit")
                            charlie = int(input())
                            if charlie == 1:
                                cursor.execute(f'''select * from Cart c where c.CCustomerID = {person_id}''')
                                data = cursor.fetchall()
                                cart_id = data[0][0]
                                cursor.execute(f'''SELECT SUM(p.Price * ci.quantity) AS TotalCost
                                                    FROM Cart_Items ci
                                                    JOIN Cart c ON ci.cart_id = c.Cart_ID
                                                    JOIN Products p ON ci.product_id = p.Product_ID
                                                    WHERE c.Cart_ID = {cart_id};''')
                                data = cursor.fetchall()
                                amount = data[0][0]
                                print("Amount to be paid: ", str(amount)+"$")
                                print()
                                print('''1. UPI
                                        2. Net Banking
                                        3. Credit/Debit Card''')
                                typ = int(input())
                                print("Enter UPI ID / card number:")
                                input()
                                print("Enter Pin:")
                                input()
                                cursor.execute(f'''Select o.Order_ID 
                                                    from Orders o
                                                    where o.Cart_ID = {cart_id}''')
                                order_id = cursor.fetchall()[0][0]
                                temp = {1: 'UPI', 2: "Net banking", 3: "Card"}

                                cursor.execute(f'''insert into Payment 
                                                (Payment_ID, Order_ID, Type, Status, DatePayment, Amount)
                                                values ({None}, {order_id},{temp[typ]}, 'SUCCESSFUL', CURDATE(), {amount}''')

                        else:
                            print("Cart is Empty")

                    if alpha == 3:
                        print("Enter Product_ID:")
                        pid = input()
                        cursor.execute(f'''Select * from Reviews where Product_ID = {pid}''')
                        data = cursor.fetchall()
                        if len(data) > 0:
                            for i in data:
                                print("Product ID:", str(data[4]), " Rating :", data[2], " Review: ", data[1])

                    if alpha == 4:
                        break

            if option == 2:
                cursor.execute(f'''Select o.Order_ID, o.Date_Of_Delivery from Orders o where o.OCustomerID="{person_id}";''')
                data = cursor.fetchall()
                if len(data) > 0:
                    for i in data:
                        print("Order ID:", str(data[0]), " Date of Delivery :", data[1])

            if option == 3:
                cursor.execute(f'''Select * from Cart_Items ci where ci.cart_ID in (select c.Cart_ID
                from Cart c where c.CCustomerID = {person_id} and c.Order_Placed = 'no');''')
                data = cursor.fetchall()
                if len(data) > 0:
                    for i in data:
                        print("Product ID:", str(data[2]), " Quantity :", data[3])
                else:
                    print("Cart is Empty")

            if option == 4:
                break

    if x == 2:
        while True:
            print("1. Add Product")
            print("2. Delete Product")
            print("3. Change Price")
            print("4. Log Out")
            option = int(input())

            if option == 1:
                print("Enter Product Name:")
                pname = input()
                print("Enter Price:")
                price = input()
                print("Enter Quantity Available:")
                quantity = input()
                print("Enter Category ID:")
                category = input()
                print("Enter Time for delivery:")
                time = input()
                print("Enter Description:")
                des = input()

                cursor.execute(f'''insert into PRODUCTS 
                (Product_ID, Category_ID, Name, Price, Quantity_Available, Seller_ID, Days_to_Arrive, Description, ImageSource) 
                values ({None}, {category}, '{pname}', {price}, {quantity}, {person_id}, {time},'{des}', 'http://dummyimage.com/202x120.png/dddddd/000000');''')

            if option == 2:
                print("Enter Product ID:")
                pid = input()
                cursor.execute(f'''delete from PRODUCTS where "Product_ID"={pid} and "Seller_ID" = {person_id}''')

            if option == 3:
                print("1. Update price")
                print("2. Update quantity")
                print("3. exit")
                beta = int(input())
                print("Enter Product ID:")
                pid = input()
                if beta == 1:
                    print("Enter new price:")
                    price = input()
                    cursor.execute(f'''UPDATE `PRODUCTS` SET `Price` = {price} WHERE `Product_ID` = {pid};''')

                if beta == 2:
                    print("Enter new quantity:")
                    quan = input()
                    cursor.execute(f'''UPDATE `PRODUCTS` SET `Quantity_Available` = {quan} WHERE `Product_ID` = {pid};''')

    if x == 3:
        print("1. View Pending Deliveries")
        print("2. View Completed Deliveries")
        print("3. Log Out")
        option = int(input())

        if option == 1:
            cursor.execute(f'''Select * from deliveries d where d.DPID = {person_id} and Delivery_Status = 'Dispatched';''')
            data = cursor.fetchall()
            if len(data) > 0:
                for i in data:
                    print("Delivery ID;", str(data[0]), "Order ID:", str(data[1]), " Date of Delivery :", data[4])
                print("Mark Delivered(y/n):")
                charlie = input()
                if charlie == "y":
                    print("Enter Delivery ID:")
                    did = input()
                    cursor.execute(f'''UPDATE 'DELIVERIES' SET 'Delivery_Status' = 'Delivered'  WHERE 'Delivery_ID' = {did}''')
        if option == 2:
            cursor.execute(f'''Select * from deliveries d where d.DPID = {person_id} and Delivery_Status = 'Delivered';''')
            data = cursor.fetchall()
            if len(data) > 0:
                for i in data:
                    print("Delivery ID;", str(data[0]), "Order ID:", str(data[1]), " Date of Delivery :", data[4])

        if option == 3:
            break


