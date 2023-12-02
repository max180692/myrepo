import collections

a = {'a':'A','c':'C'}
b = {'b':'B','c':'D'}

# поиск в нескольких словарях
m = collections.ChainMap(a,b)
#вывод значений
print(m['a'])
print(m['b'])
#получение ключей и значений
print(list(m.keys()),'=======')
print(list(m.values()),'((((((')

# вывод объединеных  
print(m.maps)

# реверсивное перемещение элементов 
print(list(reversed(m.maps)))

# изменение значений в коллекции  словаря а
a['c'] = 'T'
print(m['c'])
print(m) 


# создание нового словаря в коллекции
m2 = m.new_child()
#вывод новой коллекции без значений
print(m2)
# заполнение коллекции в которой есть пуустой словарь новым значением 
m2['c'] = 'p'
#вывод на консоль новой коллекции
print(m2)

# создание словаря
d = {'r':'py'}
# создание новой коллекции в переменной
m3 = m.new_child(d)
print(m3)

print(type(m3))

m = m.new_child(d)
print('-----',m)


# создание счетчика коллекции 
ned = collections.Counter()
#заполнение коллекции счетчиков
ned.update('eddfrgggtyas')
 #  на выводе будет словарь  {'t':4,'g':3}
#  подсчет символов в строке
print(ned)
#  вывод на консоль значение из словаря с ключом  't' 
print(ned['t'])


ned['z'] = 7
print(ned)
print(list(ned.elements()))


#

a = 'B'
print(list(m.values()))
if a in list(m.values()):
    print('ok',a)


#  создание именного кортежа
Mobile = collections.namedtuple('Mobile','marka model')
#вывод именного кортежа на консоль
print(Mobile)
#использование именного кортежа и вывод на консоль 
samsung = Mobile(marka='samsung',model='s23')
print(samsung.marka)


 
