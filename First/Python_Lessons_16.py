# Аргументы *args
def func (*numbers):
    print(sum(numbers))
func(5, 6, 1, 8)

# Аргументы **kwargs
def kek (**klop):
    for x, y in klop.items():
        print (x, ":", y)
kek(a = 15, b = 51, k = 66)