# Importing the random module for generating random numbers
import random

# Importing the Enum class from the enum module
from enum import Enum

# Defining an enum class for different types of chocolates available
class ChocolateType(Enum):
    ''' Enum representing different types of chocolates '''

    Milk = 'Milk Chocolate'
    Dark = 'Dark Chocolate'
    White = 'White Chocolate'
    Hazelnut = 'Hazelnut Chocolate'
    Caramel = 'Caramel Chocolate'
    Coconut = 'Coconut Chocolate'

# Defining a Chocolate class to represent chocolates with different attributes
class Chocolate:
    ''' Class representing a chocolate '''
    def __init__(self, id_, weight, price, choc_type):
        self.id = id_
        self.weight = weight
        self.price = price
        self.choc_type = choc_type

# Generating a list of chocolates with random attributes
def generate_chocolates(num_chocolates):
    chocolates = []
    for i in range(1, num_chocolates + 1):
        # Generating random values for weight, price, and choc_type
        weight = random.randint(1, 10)
        price = random.randint(10, 20)
        choc_type = random.choice(list(ChocolateType))
        # Creating a Chocolate object with the random attributes
        chocolate = Chocolate(i, weight, price, choc_type)
        # Adding the chocolate to the list using .append
        chocolates.append(chocolate)
        # Returning the list of chocolates
    return chocolates

    '''Task 1 '''

# Distributing chocolates iteratively among students
def distribute_chocolates_iteratively(chocolates, num_students):
    distribution = []
    # Iterating over the minimum of num_students and the number of available chocolates
    for i in range(min(num_students, len(chocolates))):
        chocolate = chocolates[i]
        # Assigning a student name based on the current index
        student_name = f"Student {i+1}"
        distribution.append((student_name, chocolate))
        # Returning the distribution list
    return distribution

# Distributing chocolates recursively among a given number of students
def distribute_chocolates_recursively(chocolates, num_students, index=0, distribution=None):
    # Initialize the distribution list if it is not provided
    if distribution is None:
        distribution = []

    # Base cases for recursion: if the index exceeds the number of students or the number of chocolates
    if index >= num_students or index >= len(chocolates):
        return distribution

    # Assign a student name based on the index
    student_name = f"Student {index + 1}"
    # Get the chocolate object at the current index
    chocolate = chocolates[index]
    # Add the student name and chocolate to the distribution list
    distribution.append((student_name, chocolate))

    # Recursive call: increment the index and call the function again
    return distribute_chocolates_recursively(chocolates, num_students, index + 1, distribution)

# Setting the number of students
num_students = -5

# Generating a list of chocolates
chocolates = generate_chocolates(num_students)

# Checking if there are any students available
if num_students <= 0:
    print("There are no students available.")
else:
    # Performing iterative distribution of chocolates among students
    iterative_distribution = distribute_chocolates_iteratively(chocolates, num_students)
    print("Iterative Distribution:")
    # Printing the details of each student's chocolate
    for student, chocolate in iterative_distribution:
        print(f"{student} received {chocolate.choc_type.value}.")
        print(f"Chocolate ID: {chocolate.id}")
        print(f"Price: {chocolate.price} AED")
        print(f"Weight: {chocolate.weight}g")
        print()

    # Performing recursive distribution of chocolates among students
    recursive_distribution = distribute_chocolates_recursively(chocolates, num_students)
    print("Recursive Distribution:")
    # Printing the details of each student's chocolate
    for student, chocolate in recursive_distribution:
        print(f"{student} received {chocolate.choc_type.value}.")
        print(f"Chocolate ID: {chocolate.id}")
        print(f"Price: {chocolate.price} AED")
        print(f"Weight: {chocolate.weight}g")
        print()

''' Task 2 '''


# merge sort on a list of chocolates based on a specified key
def merge_sort(chocolates, key):
    # Checking if there are more than 1 element in the list
    if len(chocolates) > 1:
        # Calculating the midpoint of the list
        mid = len(chocolates) // 2
        # Split the list into two halves
        left_half = chocolates[:mid]
        right_half = chocolates[mid:]

        # Recursive calls to perform merge sort on the left and right halves
        merge_sort(left_half, key)
        merge_sort(right_half, key)

        # Initializing indices for left_half, right_half, and chocolates list
        i = j = k = 0

        # Mergeing the two halves while sorting based on the specified key
        while i < len(left_half) and j < len(right_half):
            if getattr(left_half[i], key) <= getattr(right_half[j], key):
                chocolates[k] = left_half[i]
                i += 1
            else:
                chocolates[k] = right_half[j]
                j += 1
            k += 1

        # Copying any remaining elements from the left_half
        while i < len(left_half):
            chocolates[k] = left_half[i]
            i += 1
            k += 1

        # Copying any remaining elements from the right_half
        while j < len(right_half):
            chocolates[k] = right_half[j]
            j += 1
            k += 1


# Sorting the list of chocolates by weight and price using merge sort
def sort_chocolates(chocolates):
    # Creating copies of the original list
    sorted_by_weight = chocolates[:]
    sorted_by_price = chocolates[:]

    # Sorting the copies using merge sort based on weight and price respectively
    merge_sort(sorted_by_weight, "weight")
    merge_sort(sorted_by_price, "price")

    # Return the sorted copies
    return sorted_by_weight, sorted_by_price

# sorting the chocolates
sorted_by_weight, sorted_by_price = sort_chocolates(chocolates)
print("Sorted by Weight:")
# Iterating over the chocolates sorted by weight and print their ID and weight
for chocolate in sorted_by_weight:
    print(f"ID: {chocolate.id}, Weight: {chocolate.weight}g")

print("\nSorted by Price:")
# Iterating over the chocolates sorted by price and print their ID and price
for chocolate in sorted_by_price:
    print(f"ID: {chocolate.id}, Price: {chocolate.price} AED")


''' Task 3 '''

def binary_search_chocolates_by_price(chocolates, target_price):
    # Initializing the low and high indices for the binary search
    low = 0
    high = len(chocolates) - 1
    # Create a list to store the indices of found chocolates
    found_indices = []

    while low <= high:
        # Calculating the midpoint
        mid = (low + high) // 2
        # Getting the price of the chocolate at the midpoint
        mid_price = chocolates[mid].price

        # Checking if the midpoint price matches the target price
        if mid_price == target_price:
            # Adding the index of the chocolate to the found_indices list
            found_indices.append(mid)
            left = mid - 1
            right = mid + 1

            # Checking for more chocolates with the same price on the left side
            while left >= low and chocolates[left].price == target_price:
                found_indices.append(left)
                left -= 1

            # Checking for more chocolates with the same price on the right side
            while right <= high and chocolates[right].price == target_price:
                found_indices.append(right)
                right += 1

            # Returning the chocolates with the target price
            return [chocolates[i] for i in found_indices]

        # If the midpoint price is less than the target price, search the right half
        elif mid_price < target_price:
            low = mid + 1
        # If the midpoint price is greater than the target price, search the left half
        else:
            high = mid - 1

    # If no chocolates with the target price are found, return None
    return None

# Example usage:
target_price = 15  # The price we're searching for

# Calling the binary_search_chocolates_by_price function on the sorted_by_price list
found_chocolates = binary_search_chocolates_by_price(sorted_by_price, target_price)

# Checking if any chocolates with the target price are found
if found_chocolates:
    print(f"\nChocolates with price {target_price} found:")
    # Iterating over the found chocolates and print their ID and price
    for chocolate in found_chocolates:
        print(f"ID: {chocolate.id}, Price: {chocolate.price} AED")
else:
    print("No chocolates found with the specified price.")