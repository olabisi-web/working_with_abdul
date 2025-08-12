# Nigerian Currency Converter

Amount = float(input("Amount in Naira: "))
us_dollars = float(Amount * 1600)
Pounds = float(Amount * 1750)

print(f"Amount\tExchange rate to US Dollars\tExchange rate to British Pounds\n{Amount}\t\t₦{us_dollars:,}K\t\t\t₦{Pounds:,}K")
