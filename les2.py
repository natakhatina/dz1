a = 5
#не меньше 3х global и 3х a = 0
#можно добавлять дополнительные вызовы
#функций foo_1 и foo_2(глобальных)
#в результате должно быть 27
def foo_1():
    a = 0
    a += 1
    def bar_1():
        a=0
        a -= 2
        def fun_1():
            global a
            a -= 1
            def bun_1():
                a = 0
                a += 2
            bun_1()
        fun_1()
    bar_1()
foo_1()

def foo_2():
    a = 0
    a -= 3
    def bar_2():
        global a
        a += 5
        def fun_2():
            global a
            a += 3
            def bun_2():
                a = 0
                a -= 5
            bun_2()
        fun_2()
    bar_2()
foo_2()
foo_2()
foo_2()
foo_1()

print(a)