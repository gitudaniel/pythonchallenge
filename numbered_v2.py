"""
Here we see that if we take every second number starting from 100 and use that to form the sequence, the sum of those numbers will equal 10000
The sequence is (100, 99, 99, 98), (98, 97, 97, 96), (96, 95, 95, 94)...(2, 1, 1, 0)
"""

number = []
number_sum = []

for i in range(100, 1, -2):
    iteration = (i, i-1, i-1, i-2)
    number.append(iteration) # append the iteration to the list number then move to the next iteration

for i in number:
    summation = sum(i) # take a single tuple in the list of tuples and get its sum
    number_sum.append(summation) # append that sum to the list number_sum

print sum(number_sum) # get the sum of everything in the list number_sum
