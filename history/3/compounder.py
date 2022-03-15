
if input("months or years? (m\y): ") == "m":
    months = float(input("enter your months: "))
else:
    months = 12 * float(input("enter your years: "))

inrate = float(input("enter yearly interest: "))/100

money = float(input("enter money: "))

Done = False

current = money

years = months/12
remainder = 0
if (not years.is_integer()):
    remainder = months % 12
    years = years.__floor__()

for i in range(years.__floor__()):
    current += (current * inrate)
    # print("calculating non remainder interest: " + str(current))

if (remainder != 0):
    current += (current * (inrate/remainder))
    # print("calculating remainder interest: " + str(current))

print("how much you pay: $"+ format(current, '.2f'))
print("You are paying $" + format(current - money, '.2f') + " more than without interest")
