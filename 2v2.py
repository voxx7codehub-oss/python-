r=int(input("enter number of rows"))
c=int(input("enter number of coloums:"))
matrix = []
print("enter elements ( 0 to 1):")
for i in range(r):
    row = []
    for j in range(c):
        val=int (input())
        row.append(val)
    matrix.append(row)
max_count = 0
row_index = 0
for i in  range(r):
    count = matrix[i].count(1)
    if count > max_count:
        max_count = count
row_index = i + 1
print(row_index)
