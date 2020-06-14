correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
# Define a function check_sudoku() here:
def check_sudoku(matrix):
    size=len(matrix)
    for row in matrix:
        li=[x for x in range(1,size+1)]
        for number in row:
            if number not in li:
                return False
            li.remove(number)
        if len(li)!=0:
            return False
    for col in range(size):
        li=[x for x in range(1,size+1)]
        for row in range(size):
            if matrix[row][col] not in li:
                return False
            li.remove(matrix[col][row])
        if len(li)!=0:
            return False
    return True
            

    
    
print(check_sudoku(incorrect))
#>>> False

print(check_sudoku(correct))
#>>> True

print(check_sudoku(incorrect2))
#>>> False

print(check_sudoku(incorrect3))
#>>> False

print(check_sudoku(incorrect4))
#>>> False

print(check_sudoku(incorrect5))
#>>> False


