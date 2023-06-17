product_quality=True
product_price=False
if product_quality and product_price:
	print("Buy the product")
else:
	print("Not buy the product")

if product_quality or product_price:
	print("Buy the product")
else:
    print("Not buy the product")

if product_quality and not product_price:
    print("Buy")
else:
    print("Not buy")

age=input("Enter the age: ")
height=input("Enter the height: ")

if int(age)>5 and int(height)>100:
	print("Eligible to Join the school")
	
else:
	print("Not eligible to Join the school")
