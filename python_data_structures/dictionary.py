sal_info = {'Austin':91185, 'Bostion':90171}
sal_info["New York City"] = 95002
sal_info["Miami"] = 100000


sal_data = dict()
sal_data = {'Austin':91185, 'Bostion':90171}
print(sal_data)

if ('Austin' in sal_data):
    print(sal_data['Austin'])
else:
    raise "Error!"

for location in sal_data:
    print(sal_data[location])


print(sal_data.get("Dallas", "Not Found"))
print(sal_data.get("Austin", "Not Found"))
print(sal_data.keys())

print(sal_data.values())

for k,v in sal_data.items():
    print("The key is {}, and the value is {}".format(k,v))

print(min(sal_data))
print(max(sal_data))