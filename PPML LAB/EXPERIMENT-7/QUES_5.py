my_list = [1, 2, 3, 4, 5]
my_tuple = (6, 7, 8, 9, 10)

list_result = list(map(str, my_list))
tuple_result = list(map(str, my_tuple))

print("List of Strings:", list_result)
print("Tuple converted to List of Strings:", tuple_result)