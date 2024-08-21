#1. Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()
print_params(5)
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(10, b='другая строка')
#2.Распаковка параметров:
values_list = [10, 'пример', False]
values_dict = {'a': 100, 'b': 'текст', 'c': [1, 2, 3]}
print_params(*values_list)
print_params(**values_dict)
#3.Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
