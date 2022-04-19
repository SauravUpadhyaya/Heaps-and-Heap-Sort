# Project:  CS 617
# Program:  Heaps and heapsort
# Purpose:  Implement and test heap data structures, and implement heapsort algorithm
# Author:   Saurav Upadhyaya
# Source:   - T. H. Cormen, C. E. Leiserson, R. L. Rivest, and C. Stein,
#             Introduction to Algorithms, Third Edition, The MIT Press, Cambridge MA, 2009
#           - M. Petty, Heaps, Lecture 10, 2022
#           - M. Petty, Heapsort and Priority Queues, Lecture 11, 2022
# Created:  2022-02-24
# Modified: 2022-03-01

import re
import math

# Set input and output file
input_file = "test_cases.txt"
output_file = open('output_files.txt', 'w')

# Functions from lecture pseudocode 
def parent(i):
    return (math.floor(i/2))

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def max_heapify(A, heap_size, i):   # heap_size is passed as a parameter unlike in psuedocode
    l = left(i)
    r = right(i)
    if l < heap_size and A[l] > A[i]:  # Less than or equal to sign has been replaced by less than due to 0-based
        largest = l                    # indexing in python     
    else:
        largest = i
    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        max_heapify(A,heap_size, largest)

def convert_list_to_string(A):      # Converts list to string with proper format for writing to the output file
    return ' '.join([str(i) for i in A])

def build_max_heap(A, heap_size):
    for i in range(int(math.floor(heap_size/2))-1, -1, -1): # Adjustment of indexes of psuedocode for 0-based indexing
        max_heapify(A,heap_size,i)
    write_to_out_file("after build  = " + convert_list_to_string(A) + '\n') # Added for writing string to the output file

def verify_heap(A, heap_size):      # Referenced from Dr. Petty's R code sample
    okay = True
    for i in range(1, int(math.floor(heap_size/2) + 1)):
        if ((left(i) < heap_size) and (A[left(i)] > A[i])): # Adjustment of indexes for 0-based indexing
            okay = False
        if ((right(i) < heap_size) and (A[right(i)] > A[i])):
            okay = False
    return okay

def heapsort(A):
    heap_size = len(A)
    build_max_heap(A, heap_size)
    write_to_out_file("verified     = " + str(verify_heap(A, heap_size)).upper() + '\n')
    for i in range(heap_size-1, 0, -1):    # Adjustment of indexes of psuedocode for 0-based indexing
        temp = A[i]
        A[i] = A[0]
        A[0] = temp
        heap_size = heap_size - 1
        max_heapify(A, heap_size, 0)
    write_to_out_file("after sort   = " + convert_list_to_string(A) + '\n\n')

def write_to_out_file(string): # Writes to the output file
    global output_file
    output_file.write(string)

def run_test_cases(filename): # Reads each test cases line by line
    with open(filename, 'r') as test_file:
        test_count = 0
        for file_line in test_file:
            line = file_line.rstrip('\n').split(" ") # Converts each test case into a list
            if re.match("[-+]?\d+$", line[0]):
                global A
                A = [int(x) for x in line if x!=''] 
                test_count +=1 
                write_to_out_file("test case    = " + str(test_count) + '\n')
                write_to_out_file("before build = " + file_line)
                heapsort(A)
            else:
                continue

if __name__ == "__main__":
    run_test_cases(input_file)  # Reads the input file
    
