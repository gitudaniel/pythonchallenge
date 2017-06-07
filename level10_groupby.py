import itertools

"""
This iteration uses itertools.groupby() to find the number length pairs
The output of itertools.groupby() is a tuple of number followed by all appearances of the number(number, all appearances)
We have the initial value which we have assigned the variable value = '1'
For each iteration in the range given, we create a list of tuples of the number and a list of occurences of the number in the given value
We join the list by taking the length of the number of occurences of the number, making that a string and concantenating it with the number itself for each of the values of the tuple in the values list.
We assign the joined values to the value to continue the iteration.
"""
# Below is an example(referenced by ###) to show you how groupby renders the values
# Uncomment it to see how groupby renders the values

### value = '13112221'

### print [(i, list(j)) for i,j in itertools.groupby(value)]



value = '1'

for iteration in range(30):
    values_list = [(i, list(j)) for i, j in itertools.groupby(value)]
    value = ''.join([str(len(j)) + i for i,j in values_list])
print len(value)
