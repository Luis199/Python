import zipfile

zfile = zipfile.ZipFile('archive.zip', "w")
zfile.write('sample_data.csv')
zfile.write('testfile.txt')
zfile.close()

print(zipfile.is_zipfile('archive.zip'))