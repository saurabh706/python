## Code : Triangle Number Pattern
## Send Feedback
## Print the following pattern for the given N number of rows.
## Pattern for N = 4
##  1
##  22
##  333
##  4444

n = int(input())
i = 0

while i < n:
    j = 0

    while j <= i:
        print(i+1, end="")
        j+=1
    print()
    i+=1