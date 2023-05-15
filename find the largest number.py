def find_largest_number(numbers):
    if not numbers:
        return None  # Return None if the list is empty

    largest = numbers[0]  # Assume that the first number is the largest

    for number in numbers:
        if number > largest:
            largest = number  # Update the largest number if a larger one is found

    return largest

# Example usage
my_list = [65, 72, 78, 92, 16, 174, 57]
largest_number = find_largest_number(my_list)
print("The largest number is:", largest_number)