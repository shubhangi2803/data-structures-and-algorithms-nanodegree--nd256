def duplicate_number(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    size=len(arr)
    d=dict()
    for num in arr:
        d[num]=d.get(num,0)+1
        if d[num]==2:
            x=num
            break
    return x


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    output = duplicate_number(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arr = [0, 0]
solution = 0

test_case = [arr, solution]
test_function(test_case)

arr = [0, 2, 3, 1, 4, 5, 3]
solution = 3

test_case = [arr, solution]
test_function(test_case)

arr = [0, 1, 5, 4, 3, 2, 0]
solution = 0

test_case = [arr, solution]
test_function(test_case)

arr = [0, 1, 5, 5, 3, 2, 4]
solution = 5

test_case = [arr, solution]
test_function(test_case)

# Solution
'''
Notice carefully that
1. All the elements of the array are always non-negative
2. If array length = n, then elements would start from 0 to (n-2), i.e. Natural numbers 0,1,2,3,4,5...(n-2)
3. There is only SINGLE element which is present twice.

Therefore let's find the sum of all elements (current_sum) of the original array, and
find the sum of first (n-2) Natural numbers (expected_sum).

Trick: 
The second occurance of a particular number (say `x`) is actually occupying the space 
that would have been utilized by the number (n-1). This leads to: 
current_sum  = 0 + 1 + 2 + 3 + .... + (n-2) + x
expected_sum = 0 + 1 + 2 + 3 + .... + (n-2)
current_sum - expected_sum = x 
Tada!!! :)  

'''
def duplicate_number(arr):
    current_sum = 0
    expected_sum = 0
    
    # Traverse the original array in the forward direction 
    for num in arr:
        current_sum += num
    
    
    # Traverse from 0 to (length of array-1) to get the expected_sum
    # Alternatively, you can use the formula for sum of an Arithmetic Progression to get the expected_sum
    
    # The argument of range() functions are:
    # starting index [OPTIONAL], ending index (non exclusive), and the increment/decrement size [OPTIONAL]
    # It means that if the array length = n, loop will run form 0 to (n-2)
    for i in range(len(arr) - 1):
        expected_sum += i
    
    
    # The difference between the 
    return current_sum - expected_sum
