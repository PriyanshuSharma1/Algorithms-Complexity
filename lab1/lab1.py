
'''
Author name: Priyanshu Sharma
Date created : April 29, 2024
Implementation, testing and performance measurement of sorting algorithms.
'''
import random
import time
import matplotlib.pyplot as plt
import pandas as pd

# Function to implement the insertion sort algorithm
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Function to implement the selection sort algorithm
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Function to generate a random array of given length
def generate_random_array(length):
    return [random.randint(1, 1000) for _ in range(length)]

# Function to generate a sorted array (best case) of given length
def generate_sorted_array(length):
    return [i for i in range(1, length + 1)]

# Function to generate a reverse sorted array (worst case) of given length
def generate_reverse_sorted_array(length):
    return [i for i in range(length, 0, -1)]

# Function to measure the execution time of a sorting algorithm
def measure_execution_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

# Function to plot the execution times for different input sizes
def plot_execution_times(sizes, insertion_times_best, insertion_times_worst, selection_times_best, selection_times_worst):

    plt.plot(sizes, insertion_times_best, label='Insertion Sort (Best Case)')
    plt.plot(sizes, insertion_times_worst, label='Insertion Sort (Worst Case)')
    plt.plot(sizes, selection_times_best, label='Selection Sort (Best Case)')
    plt.plot(sizes, selection_times_worst, label='Selection Sort (Worst Case)')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Input Size vs Execution Time')
    plt.legend()
    plt.show()


# Main function to run the program
def main():
    sizes = [1000, 5000, 10000, 20000, 30000]
    insertion_times_best = []
    insertion_times_worst = []
    selection_times_best = []
    selection_times_worst = []
    df1 = pd.DataFrame(insertion_times_best, columns=['n', 'time'])
    df2 = pd.DataFrame(insertion_times_worst, columns=['n', 'time'])


#   convert the section sort data to dataframe
    df4 = pd.DataFrame(selection_times_best, columns=['n', 'time'])
    df5 = pd.DataFrame(selection_times_worst, columns=['n', 'time'])


    # Measure execution times for different input sizes
    for size in sizes:
        # Generate random array
        random_arr = generate_random_array(size)

        # Generate sorted array (best case) and reverse sorted array (worst case)
        sorted_arr_best = generate_sorted_array(size)
        sorted_arr_worst = generate_reverse_sorted_array(size)

        # Measure insertion sort execution time for best case
        insertion_time_best = measure_execution_time(insertion_sort, sorted_arr_best.copy())
        insertion_times_best.append(insertion_time_best)

        # Measure insertion sort execution time for worst case
        insertion_time_worst = measure_execution_time(insertion_sort, sorted_arr_worst.copy())
        insertion_times_worst.append(insertion_time_worst)

        # Measure selection sort execution time for best case
        selection_time_best = measure_execution_time(selection_sort, sorted_arr_best.copy())
        selection_times_best.append(selection_time_best)

        # Measure selection sort execution time for worst case
        selection_time_worst = measure_execution_time(selection_sort, sorted_arr_worst.copy())
        selection_times_worst.append(selection_time_worst)

    # Plot the execution times
    plot_execution_times(sizes, insertion_times_best, insertion_times_worst, selection_times_best, selection_times_worst)

# Entry point of the program
if __name__ == "__main__":
    main()
