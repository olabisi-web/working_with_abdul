# I am designing a mock ussd interface for a mobile service.

print("Welcome to GLO USSD service")
recharge = input("Dial *121#: ")
print("1. \"Check Balance\"\n2. \"Buy Airtime\"\n3. \"Buy Data\"")
choice = input(f"Choose an option, 1, 2 or 3: ")
print(f"You have chosen option {choice}")
Amount = int(input("Indicate how much you want to buy: ₦"))
print(f"You have chosen option {choice} worth ₦{Amount}")