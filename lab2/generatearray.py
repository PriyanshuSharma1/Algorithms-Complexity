import random
import time
import matplotlib.pyplot as plt
from mergesort import merge_sort
from quicksort import quick_sort


# Function to generate a random array of given length
def generate_random_array(length):
    return [random.randint(1, 100000000) for i in range(length)]

# Function to generate a sorted array (best case) of given length
def generate_sorted_array(length):
    return [random.randint(1, 100000000) for i in range(1, length + 1)]

# Function to generate a reverse sorted array (worst case) of given length
def generate_reverse_sorted_array(length):
    return [random.randint(1, 100000000) for i in range(length, 0, -1)]

# Function to measure the execution time of a sorting algorithm
def measure_execution_time(sort_func, arr):
    start_time = time.time()
    sorted_arr = sort_func(arr)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time



