def max_subarray(numbers, count):
    sum_of_numbers = sum(numbers[:count])
    max_sum = sum_of_numbers
    for i in range(count, len(numbers)):
        sum_of_numbers -= numbers[i-count]
        sum_of_numbers += numbers[i]
        max_sum = max(max_sum, sum_of_numbers)
    return max_sum
