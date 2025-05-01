def fibonacci(n):
    numbers = []
    first_number = 0
    second_number = 1
    numbers.append(first_number)
    numbers.append(second_number)
    for k in range(2 , n) :
        new_number = numbers[-1] + numbers[-2]
        numbers.append(new_number)
    for number in numbers:
        print(number)