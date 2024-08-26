def print_params(a=1,b='строка', c=True):
    print(a,b,c)


print_params()
print_params(1)
print_params(1,b='строка',c= True)
print_params(1,b=25,c=[1,2,3])

values_list = [1,'строка', True]
values_dict = {'a': 1, 'b': 2,'c':3}
print_params(*values_list)
print_params(**values_dict)

values_list_2= (1,True)
print_params(*values_list_2,42)
