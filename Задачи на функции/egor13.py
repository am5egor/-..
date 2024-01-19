def summa(x):
    amount = 0
    for number in x:
        if number%2 == 0:
            amount += number
    return amount

numbers = [20, 21, 22, 23, 24, 25, 26]
print(summa(numbers))