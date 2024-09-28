numbers = [1, 2, 3, 2, 3, 4, 4, 4, 5, 4, 5, 6]
mean = sum(numbers) / len(numbers)
sorted_numbers = sorted(numbers)
n = len(sorted_numbers)
if n % 2 == 0:
    median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
else:
    median = sorted_numbers[n // 2]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
max_frequency = max(frequency.values())
modes = [num for num, freq in frequency.items() if freq == max_frequency]
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {modes}")
