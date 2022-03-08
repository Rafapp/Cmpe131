from collections import Counter
import re
import collections

file = open('document.txt', encoding='utf8')
text = file.read()
file.close
print(collections.Counter(text.split(' ')).most_common)