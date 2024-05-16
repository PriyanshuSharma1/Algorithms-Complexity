import matplotlib.pyplot as plt
from mergesort import merge_sort
from quicksort import quick_sort
from quicksort import quick_sort
from lab2.generatearray import generate_random_array, measure_execution_time, generate_reverse_sorted_array,generate_sorted_array

def run_case(arr):
    # Generate random inputs
    input_sizes = [10, 100, 1000, 10000]  # Add more sizes as needed
    execution_times_merge = []
    execution_times_quick = []
    for size in input_sizes:
        execution_time_merge = measure_execution_time(merge_sort, arr)
        execution_time_quick = measure_execution_time(quick_sort, arr)
        execution_times_merge.append(execution_time_merge)
        execution_times_quick.append(execution_time_quick)

    # Plot input size vs execution time graph
    plt.plot(input_sizes, execution_times_merge, label='Merge Sort')
    plt.plot(input_sizes, execution_times_quick, label='Quick Sort')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Input Size vs Execution Time')
    plt.legend()
    plt.show()