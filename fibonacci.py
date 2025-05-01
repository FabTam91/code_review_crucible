def fibonacci(n):
    numbers = [0, 1]
    for _ in range(2, n):
        new_number = numbers[-1] + numbers[-2]
        numbers.append(new_number)
    for number in numbers:
        print(number)
