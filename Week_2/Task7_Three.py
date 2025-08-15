# Creating Days Of The Week And Activities Pairing
# Store the nweek days in a tuple
# Ask for three ndays activies from using input()
# Combine the activities collected in a variable
# Pairing the days and activities using dictionary comprehension
Week_days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
Defined_days = ('Monday', 'Tuesday', 'Sunday' )
Actv_Mon = input("Enter your monday activity here: ")
Actv_Tues = input("Enter your tuesday activity here: ")
Actv_Sun = input("Enter your sunday activity here: ")
Activities = (Actv_Mon, Actv_Tues, Actv_Sun)
Schedule = {Week_days: Activities  for Week_days,
            Activities in zip(Defined_days, Activities)}
print(Schedule)

