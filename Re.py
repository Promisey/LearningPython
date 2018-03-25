import re
str = re.search("output_(\d{4})", "output_1986.txt")
print(str.group(0))
print(str.group(1))
str2 = re.search("output_(?P<year>\d{4})", "output_1986.txt")
print(str2.group("year"))