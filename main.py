numbers = []

for i in range(5):
    numbers.append(int(input()))

avg = sum(numbers)/len(numbers)
count = 0

for i in range(5):
    if numbers[i] > avg:
        count += 1