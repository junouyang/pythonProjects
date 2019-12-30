
def func():
    output = 0
    while True:
        new = yield output
        output = new


f = func()
print(next(f))
print(next(f))
print(f.send(5))
print(next(f))


print("{} this code is {}".format("start", "end"))


a = {1, 2}
b = {3, 4}
print(a | b)
