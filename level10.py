import re, urllib2

"""
This prints out all the values in the look and say sequence in a given range
Given range(0, 10) we will get 10 values of the look and say sequence.

We initialize the sequence with a string representation of the number 1 (a = '1')
We also initialize another variable as an empty string. (b = '')

For each number in the range given we initialize two variables previous and count both equal to 0 (for i in range(<enter range parameters here>))

While the value of previous is less than the length of a, we check whether the value of the count is less than the length of a and whether the corresponding digit at index count in a is equal to the digit at index previous in a.
Remember that both previous and count are numbers.
If count = 0 and previous = 0, a[count] = a[0] and a[previous] = a[0]
If a[count] == a[previous] we increment count by 1 and check whether the condition count < len(a) is still true.
If it is we check that a[count] == a[previous], if this is true we increment count again by one and continue the loop.
If count is not less than the length of a or a[count] != a[previous], we break out of the inner loop and assign to the variable b the string representation of count-previous + a[previous]
Note that a is a string of digits and we are turning count-previous into a string using str(count-previous). This is a concantenation of two strings
We then assign the value of count to previous and check to confirm that previous is still less than the length of a.
If it isn't we break out of the loop and assign the value of b to a (a = b) and make b an empty string.
Assigning a = b gives us the next value of a and assigning b = '' enables us to go to the next iteration with the new value of a
"""

a = '1'
b = ''

for i in range(0, 30):
    previous = 0
    count = 0

    while previous < len(a):
        while count < len(a) and a[count] == a[previous]: 
            count += 1 
        b += str(count-previous) + a[previous]
        previous = count
    a = b
    b = ''
print len(a)
