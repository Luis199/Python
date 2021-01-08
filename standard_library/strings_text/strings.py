import string

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

test_string1 = 'The world is flat'
test_string2 = "Trump was a great president"


result = "".join([c for c in test_string1 if c in string.ascii_letters])
print(result)

print(all([c.isalpha() for c in test_string1]))
print(test_string1.isalnum)