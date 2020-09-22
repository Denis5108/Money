def promptMoney():
    type = input("Input Money: ")
    return type

def getMoney(*dollars):
    total = 0
    for d in dollars:
        total = d
    return total

myMoney = promptMoney()
money = getMoney(myMoney)

def usDollars(money):
    return money

def canadianDollars(money):
    return float(money) * 1.33

def russianDollars(money):
    return float(money) * 76.15

def britishDollars(money):
    return float(money) * 23.5

dollars = usDollars(money)
loonie  = canadianDollars(money)
ruble  = russianDollars(money)
euro   = britishDollars(money)

def displayDollarsUS():
    print("${}".format(dollars))

def displayDollarsCanadian():
    print("C${}".format(loonie))

def displayDollarsRussian():
    print("₽{}".format(ruble))

def displayBritishDollars():
    print("Pound{}".format(euro))

def main():
    displayDollarsUS()
    displayDollarsCanadian()
    displayDollarsRussian()
    displayBritishDollars()
    return 0

main()