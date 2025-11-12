def average(numbers):
    return sum(numbers) / len(numbers)


def count_element_above_average(numbers):
    avr = average(numbers)
    count = 0
    for number in numbers:
        if number > avr:
            count += 1
    return count


def count_element_above_average_for_list(numbers):
    result = []
    for n in numbers:
        try:
            result.append(count_element_above_average(n))
        except TypeError:
            result.append(None)
        except ZeroDivisionError:
            result.append(None)

    return result


res = count_element_above_average_for_list([[1, 2, 3], [5, 6, 7], [], [3, 4, 5], ["12a", 1, 4]])
pass