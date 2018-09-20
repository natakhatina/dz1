a = 5

def foo_1():
    a = 0
    a += 1
    def bar_1():
        a = 0
        a += 2
    bar_1()

def foo_2():
    a = 0
    a += 3
    def bar_2():
        a = 0
        a += 5
    bar_2()

foo_1()
foo_2()

print(a)