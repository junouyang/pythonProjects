import threading
from functools import reduce

class TreeNode:
    def __init__(self, left, right, val):
        self.left = left
        self.right = right
        self.val = val


class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next_item = None


# root = None
#
# while not root:
#    print(root.val)
#    root = root.left


def test(val):
    if val:
        return val
    else:
        return


class Test1:
    def test(self):
        if hasattr(super(), "test"):
            super().test()
        print("Test1")


class Test2:
    def test(self):
        if hasattr(super(), "test"):
            super().test()
        print("Test2")


class Test3(Test1, Test2):
    pass


# name = 'name'
# age = 16
# print("{name} is {age} years old".format(name=name, age=age))


# test3 = Test3()
# test3.test()


def first_n(n):
    num = 0
    while num < n:
        yield num
        num += 1


# for i in first_n(10):
#     print(i)

# print(f"{'hi': ^10}{'there':^10}")
#
#
# print(set([3, 1, 0, 1, 2]))
#
#
class SafeIterable:
    def __init__(self):
        self.values = [1, 3, 7, 4, 5]

    def __iter__(self):
        parent = self

        class InnerIterator:
            def __init__(self):
                self.number = 0

            def __next__(self):
                if self.number < len(parent.values):
                    self.number += 1
                    return parent.values[self.number - 1]
                else:
                    raise StopIteration

        print("iter")
        return InnerIterator()


class Iterable:
    def __init__(self):
        self.values = [1, 3, 7, 4, 5]

    def __iter__(self):
        self.number = 0
        print("iter")
        return self

    def __next__(self):
        print("next")
        if self.number < 7:
            result = self.number
            self.number += 1
            return result
        else:
            raise StopIteration


iterable = SafeIterable()
# iterable = Iterable()

for j in iterable:
    print(j, end="-------")

    for i in iterable:
        print(i)

#
# print("foo bar foo".find("bar", 0, 7))
#
# a = [1, 2, 3]
# b = [4, 5, 6]
# # a += b
# a.extend(b)
# print(a)
#
# print(reduce(lambda x, y: x + y, a))


# def link(a, b):
#     if isinstance(a, LinkNode):
#         a.next_item = b
#         return a, b
#     else:
#         a[1].next_item = b
#         return a[0], b
#
#
# all_nodes = map(lambda x: LinkNode(x), [1, 2, 3, 4, 5])
# head = reduce(link, all_nodes)[0]
#
# print(head)
#
# while head:
#     print(head.val)
#     head = head.next_item
#
# for node in all_nodes:
#     print(node.val)

