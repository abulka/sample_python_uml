async def func(a,b): pass  # this line force force gituml to retry with python 3

class A:
    def __init__(self):
        self.x = 100
        self.y = func(a='hi', b(=1+'')  # syntax error on this line
        self.z = self.x + self.y

a = A()
print a
print a.z
