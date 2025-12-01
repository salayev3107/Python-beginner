
def sumch(a,b):
    return (a+b)
print(sumch(10,20))

#lambda

func1 = lambda x,y: x + y
func2 = lambda n : n **2
print(func1(15,29))
print(func2(15))

#map 
list1 = ['5','56','98','45','49','47']
list_int = list(map(int,list1)) # [5, 56, 98, 45, 49, 47] 
print(list_int)

list_dollars = [15, 26,98,78,132,150,200]
list_sum = list(map(lambda x: x * 12108, list_dollars,))
print(list_sum)

#filter
list_students = ['akbar','ali','anvar','aziza','dilshod','gulbahor']
list_filtr = filter(lambda name : len(name) < 4, list_students)
print(list(list_filtr))

#zip 
lista = [1,2,3,4,5]
stra = 'absd'
tuplea = (True, False, True, False)
res = list(zip(lista,stra,tuplea))
print(res)