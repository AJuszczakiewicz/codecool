numbers = input("Gimme some numbers to sort: ").split()
print(numbers)
iterations = 1
N = len(numbers)
while iterations < N:
    j = 0
    while j <= N:
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        j = j+1
    iterations = iterations + 1
