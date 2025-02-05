def remove_duplicates(lst):
    return list(set(lst))

lst = input("Enter a list of numbers separated by space: ").split()
lst = [int(i) for i in lst]

print("List after removing duplicates:", remove_duplicates(lst))

