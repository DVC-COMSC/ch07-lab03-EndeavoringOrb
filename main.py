numbers = []

for i in range(5):
    numbers.append(int(input()))

avg = sum(numbers)/len(numbers)
count = 0

for i in (numbers):
    if numbers[i] > avg:
        count += 1