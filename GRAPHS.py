#THIS CODE WAS CREATED ON SAGEMATH AND SCREENSHOTS WERE TAKEN FROM SAGE MATH, IT IS ONLY PLACED HERE FOR REFERENCE PURPOSES

import matplotlib.pyplot as plt

# Values of n
n_values = [0, 5, 10, 50, 100, 200, 300, 400]

# Iterative time complexities
iterative_times = [0.000004, 0.000019, 0.000019, 0.000070, 0.000124, 0.000308, 0.000301, 0.000416]

# Recursive time complexities
recursive_times = [0.000001, 0.000011, 0.000013, 0.000069, 0.000133, 0.000154, 0.000580, 0.000672]

# Sorting by weight time complexities
sort_by_weight_times = [0.0000021458, 0.0000340939, 0.0000498295, 0.0003540516, 0.0009112358, 0.0016610622, 0.0146689415, 0.0298869610]

# Sorting by price time complexities
sort_by_price_times = [0.0000011921, 0.0000209808, 0.0000591278, 0.0004420280, 0.000168417, 0.0007421284, 0.0069680214, 0.0244808197]

# Search by price time complexities
search_by_price_times = [0.000004, 0.000005, 0.000011, 0.000017, 0.000019, 0.000037, 0.000026, 0.000278]

# Plotting Iterative time complexity
plt.figure(figsize=(10, 6))
plt.plot(n_values, iterative_times, label='Iterative', marker='o', color='blue')
plt.xlabel('number of_students')
plt.ylabel('Time Complexity (seconds)')
plt.title('Iterative Time Complexity for Different Values of n')
plt.legend()
plt.grid(True)
plt.show()

# Plotting Recursive time complexity
plt.figure(figsize=(10, 6))
plt.plot(n_values, recursive_times, label='Recursive', marker='o', color='green')
plt.xlabel('number of_students')
plt.ylabel('Time Complexity (seconds)')
plt.title('Recursive Time Complexity for Different Values of n')
plt.legend()
plt.grid(True)
plt.show()

# Plotting Sorting by Weight time complexity
plt.figure(figsize=(10, 6))
plt.plot(n_values, sort_by_weight_times, label='Sort by Weight', marker='o', color='red')
plt.xlabel('number of_students')
plt.ylabel('Time Complexity (seconds)')
plt.title('Sorting by Weight Time Complexity for Different Values of n')
plt.legend()
plt.grid(True)
plt.show()

# Plotting Sorting by Price time complexity
plt.figure(figsize=(10, 6))
plt.plot(n_values, sort_by_price_times, label='Sort by Price', marker='o', color='purple')
plt.xlabel('number of_students')
plt.ylabel('Time Complexity (seconds)')
plt.title('Sorting by Price Time Complexity for Different Values of n')
plt.legend()
plt.grid(True)
plt.show()

# Plotting Search by Price time complexity
plt.figure(figsize=(10, 6))
plt.plot(n_values, search_by_price_times, label='Search by Price', marker='o', color='orange')
plt.xlabel('number of_students')
plt.ylabel('Time Complexity (seconds)')
plt.title('Search by Price Time Complexity for Different Values of n')
plt.legend()
plt.grid(True)
plt.show()