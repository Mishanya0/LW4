class Example:
    st_var1 = 10
    st_var2 = 20

    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def method1(self):
        self.a = "Hello World!"

    def method2(self):
        return Example.st_var1 + Example.st_var2

    def method3(self):
        return self.var1 ** self.var2


example = Example(2, 3)

print("a:", example.method1())
print("summa:", example.method2())
print("x1^x2:", example.method3())
