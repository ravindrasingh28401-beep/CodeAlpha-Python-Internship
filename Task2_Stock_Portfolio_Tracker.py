stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 165,
    "MSFT": 300,
    "AMZN": 140
}

total = 0

n = int(input("Enter number of stocks: "))

for i in range(n):
    name = input("Enter stock name: ").upper()

    if name in stocks:
        quantity = int(input("Enter quantity: "))
        investment = stocks[name] * quantity
        total += investment
        print(f"{name} = {quantity} x {stocks[name]} = {investment}")
    else:
        print("Stock not found!")

print("Total Investment Value =", total)

with open("portfolio.txt", "w") as file:
    file.write("Total Investment Value = " + str(total))

print("Portfolio saved in portfolio.txt")
