
class Learn:

    def __init__(self):
        self.a = "a"

    def test(self):
        x = "x"
        print(x)
        print(self.a)

if __name__ == "__main__":
    learn = Learn()
    learn.test()


def test(numbers, cal):
    for n in numbers:
        yield cal(n)

nums = [1, 2, 3, 4, 5]

# print(test(nums, lambda x : x*x))
for x in test(nums, lambda x1: x1*x1):
    print(x)
