#1- Определить, присутствует ли в заданном списке строк, некоторое число


array = ['jhjh', 'sdh', 'skue', 'wt5tRT', 'ksjd']
y = '5'


z = list(filter(lambda str: y in str , array))
print(z)


