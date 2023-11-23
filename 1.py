def method2():
    return Example.st_var1 + Example.st_var2


class Example:
    st_var1 = 10
    st_var2 = 20

    def __init__(self, var1, var2):
        self.a = None
        self.var1 = var1
        self.var2 = var2

    def method1(self):
        self.a = "Hello World!"

    def method3(self):
        return self.var1 ** self.var2


example = Example(2, 3)

print("a:", example.method1())
print("summa:", method2())
print("x1^x2:", example.method3())
