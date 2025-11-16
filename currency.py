# Program to find the number of currency notes and coins required

# Input total amount
amount = int(input("Enter the total amount: "))

# Calculate number of notes/coins
thousand = amount // 1000
amount %= 1000

five_hundred = amount // 500
amount %= 500

fifty = amount // 50
amount %= 50

twenty = amount // 20
amount %= 20

ten = amount // 10
amount %= 10

five = amount // 5
amount %= 5

two = amount // 2
amount %= 2

one = amount // 1

# Display result
print("Currency distribution:")
print("1000 rupee notes:", thousand)
print("500 rupee notes:", five_hundred)
print("50 rupee notes:", fifty)
print("20 rupee notes:", twenty)
print("10 rupee notes:", ten)
print("5 rupee coins:", five)
print("2 rupee coins:", two)
print("1 rupee coins:", one)
