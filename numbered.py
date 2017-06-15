number = [(100, 99, 99, 98)]
number_sum = []

"""
Derives the sum of the numbers in the sequence (n, n-1, n-1, n-2) from 100 to 1.
Assumption is that in the next sequence n becomes what was n-1 in the previous sequence

We first get the sequence tuples.
Then we get the sum of the numbers in each tuple in the list of tuples.
We create a new list from the sum of the tuples
Get the sum of that new list.
"""

for i in range(100):
    iteration = (number[i][1], number[i][-1], number[i][-1], number[i][-1]-1)
    number.append(iteration)

for i in number:  # i gives each tuple in the list number
    summation = sum(i) # sum of each tuple
    number_sum.append(summation)
#print sum(number_sum)
print number
