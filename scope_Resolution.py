# variable scope - where a var is visible and accessible
"""scope resolution - preference(LEGB) - 
Local= vars in a fun
encolsed = vars in a nested fun
Global= vars top of script
Built-in= predefined"""

from math import e

#LOCAL SCOPE
# a is local to fun 1
def fun_1():
    a = 10
    print(a)

# b is local to fun 2
def fun_2():
    b=20
    print(b)

fun_1()
fun_2()

# enclosed vars
def fun_1():
    x = 10
    def fun_2():
        print(x)
    fun_2()

fun_1()

#Global
x = 3
def fun_1():
    print(x)

def fun_2():
    print(x)

fun_1()
fun_2()


def fun_1():
    print(e)

e = 7
fun_1()

