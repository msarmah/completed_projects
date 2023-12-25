# Question: Implement each sort/search function.

"""
You may use the following codes to implement your sorting algorithm
    - https://www.geeksforgeeks.org/sorting-algorithms-in-python/
    - https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm
    - https://stackabuse.com/sorting-algorithms-in-python/
Be sure to comment your code.
"""

import csv
import json
import time
import ast 



def linear_search(arr,queries):
    ary = []
    qs = list(queries)

    for target in qs: # go through the query 
        for p in arr: # go through arr 
            if p[1] == target: # if the price from array = the price from query
                ary.append(p) # append it to our ary
                break # there may be many of the same targets; we only want one

    return ary

def bubble_sort(arr):
    lst = [i for i in arr] # move all elements of arr into lst 

    for i in range(len(lst)): # go through all values in lst
        for j in range(len(lst)-1): # go through every value in lst except the last
            curr_price = lst[j][1] # the price of j 
            next_price = lst[j+1][1] # the price of the element after j

            if curr_price > next_price:
                lst[j], lst[j+1] = lst[j+1], lst[j] # swap the order if the current price is greater than the next price to maintain sort
                
    return lst


def other_sort(arr):
    return sorted(arr, key = lambda x: x[1])
    # return a sorted version of array --> doesn't touch main

def other_search(arr,queries): # implemented binary search
    ary = []
    qs = list(queries)
    s_arr = other_sort(arr) # the arr is now sorted 

    for val in qs: # loop through queries
        first = 0
        last = len(s_arr)-1
        index = -1
        while (first <= last) and (index == -1): # 
            mid = (first+last)//2 # find the center value
            if s_arr[mid][1] == val: # if it is the value
                index = mid # our index is the mid
            else:
                if val<s_arr[mid][1]: 
                    last = mid -1 # move the mid value to the left
                else:
                    first = mid +1 # move the mid value to the right
        ary.append(s_arr[index])

    return ary
    
def main():
    arr = []
    
    with open("data.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile) # read data 

        for row in reader:
            date = row["Date"]
            price = row["Price"]

            arr.append([date,price]) # as arr

    with open("queries.json","r") as f:
        queries = json.load(f) # load queries file 

    # calculate the time and return values for each 4 method calls

    #linear search
    t_ls = time.time()
    ret1 = linear_search(arr,queries)
    t1 = time.time()-t_ls

    # bubble sort
    t_b = time.time()
    ret2 = bubble_sort(arr)
    t2 = time.time()-t_b

    # other sort
    t_o = time.time()
    ret3 = other_sort(arr)
    t3 = time.time()-t_o

    # other search
    t_os = time.time()
    ret4 = other_search(arr,queries)
    t4 = time.time()-t_os

    # write in our output file
    with open("output.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["Name", "Time", "Output"])
        writer.writeheader()
        writer.writerow({"Name":"Linear Search", "Time":t1, "Output":ret1})
        writer.writerow({"Name":"Bubble Sort", "Time":t2, "Output":ret2})
        writer.writerow({"Name":"Other Sort", "Time":t3, "Output":ret3})
        writer.writerow({"Name":"Other Search", "Time":t4, "Output":ret4})

main()
