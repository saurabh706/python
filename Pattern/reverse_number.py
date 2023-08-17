## Code : Reverse Number Pattern
## Send Feedback
## Print the following pattern for the given N number of rows.
## Pattern for N = 4
## 1
## 21
## 321
## 4321

n = int(input())

i = 0

while i < n:
    j = i + 1

    while j > 0:
        print(j, end="")
        j -= 1
    print()
    i+=1