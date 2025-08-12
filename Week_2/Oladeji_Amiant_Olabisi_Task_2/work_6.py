
#This task is to enable me generate a neatly formatted receipt using escape sequences for line breaks.


name = input("Enter Customer's full name: ")
units = int(input("Units consumed (kWh): "))
cost_per_unit = float(input("Cost per unit of electricity used: "))
Total_cost_of_electricity = float(units * cost_per_unit)
print(f"The Total cost of electricity used is {Total_cost_of_electricity}")

print("\n")
print("=" * 40)
print("\t",        name)
print("\t       RECEIPT")
print("=" * 40)
print("\n")

print(f"Units of energy consumed in kWh:\t{units}kWh\nCost per unit of Energy used:\t\t₦{cost_per_unit}\nTotal cost of Energy:\t\t\t₦{Total_cost_of_electricity}")
print("\n")
print("=" * 40)
print("      THANK YOU FOR YOUR PURCHASE")
print("=" * 40) 
