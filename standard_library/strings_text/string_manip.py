test_string = 'Barack Obama was the first  black President in the United States'

# print(test_string.upper())
# print(test_string.lower())

# result = test_string.split(" ")
# print(result)

# letters = ['a', 'b','c','d']
# # print(", ".join(letters))

# names = ['Luis', 'John', 'Jeff', "Greg"]
# biggest = max(len(name) for name in names)
# for name in names:
#     print(name.ljust(biggest+2,'-')+ ":")
# for name in names:
#     print(name.ljust(biggest+2,'-')+ ":")
# for name in names:
#     print(name.ljust(biggest+2,'-')+ ":")

trans_table = str.maketrans('abilhs','343583')
print(test_string)
print(test_string.translate(trans_table))