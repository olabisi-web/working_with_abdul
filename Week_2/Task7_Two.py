# Creating Super Market Price List
# Use the input() to collect print from users
# Create the dictionary
Babyfood_price = float(input("Enter the babyfood price: "))
Book_price = float(input("Enter the book price: "))
Pen_price = float(input("Enter the pen price: "))
Item = ["Babyfood", "Book", "Pen"]
Market_list = {
    "Baby_food": Babyfood_price,
    "Book": Book_price,
    "Pen": Pen_price
}
print(f"Baby_food: {Babyfood_price}\nBook: {Book_price}\nPen:{Pen_price}")
print(Market_list.update({"Book":3000}))
print(Market_list)
