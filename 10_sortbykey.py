# sort by key

def sort_by_sum(x):
    return x[0]+x[1]


lst = [[1, 2], [3, 4], [4, 2], [-1, 3], [4, 5], [2, 3]]
lst.sort()  # sort by the 1st element
print(lst)

lst.sort(reverse=True)  # still sort by 1st element reversely
print(lst)

lst.sort(key=lambda x: x[1])  # sort by 2nd element .. index = 1
print(lst)

lst.sort(reverse=True, key=lambda x: x[1])
print(lst)


lst.sort(key=lambda x: x[1]+x[0])  # sort by sum of elements
print(lst)

lst.sort(key=sort_by_sum)  # sort by sum of elements
print(lst)

print(sorted(lst, key=lambda x: x[1]))  # use sorted() function
