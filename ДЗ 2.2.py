number = int(input("Введіт 5-ти значне число : "))

one = number % 10
two = (number // 10) % 10
three = (number // 100) % 10
four = (number // 1000) % 10
five = (number // 10000) % 10

turn = one * 10000 + two * 1000 + three * 100 + four * 10 + five

print("Перевернуте :", turn)
print(" Дякую за увагу ! ! !")