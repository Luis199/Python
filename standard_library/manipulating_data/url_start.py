import urllib.parse

sample_url = 'https://www.codecademy.com/catalog'

result = urllib.parse.urlparse(sample_url)
# print(result)

# print(result.scheme, result.hostname, result.path)

# print(result.geturl())

sample_string = "Hello El Nino"
print(urllib.parse.quote(sample_string))
print(urllib.parse.quote_plus(sample_string))
