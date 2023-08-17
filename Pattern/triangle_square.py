## Code : Triangular Star Pattern
## Send Feedback
## Print the following pattern for the given N number of rows.
## Pattern for N = 4
##  *
##  **
##  ***
##  ****

n = int(input())

i = 0

while i < n:
    j = 0
    while j <= i:
        print('*',end="")
        j +=1
    print()
    i +=1