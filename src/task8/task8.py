"""Advanced Python cources. Homework#8, Task #1.Maxim Belov.

Implement metaclass that creates properties automatically.
Borrowed from
https://eli.thegreenplace.net/2011/08/14/python-metaclasses-by-example
Ely Bendersky. Python metaclasses by Example.
Code was refactored cause I dislike some parts of this solution.
"""


class AccessorType(type):
    """Metaclass creates properties for class automatically."""

    def __init__(self, name, bases, d):
        type.__init__(self, name, bases, d)
        accessors = {}
        prefixes = ["get_", "set_", "del_"]
        # I dislike "for i in range(3)" and
        # "setdefault(key, [None,None,None])[i]". I prefer to use dict
        # {prefix: None} dict instead of list here.
        default_values = {prefix: None for prefix in prefixes}
        for key in d.keys():
            v = getattr(self, key)
            for prefix in prefixes:
                if key.startswith(prefix):
                    var = accessors.setdefault(key[4:], default_values.copy())
                    var[prefix] = v
        for name, (getter, setter, deleter) in accessors.items():
            setattr(self, name, property(accessors[name][getter],
                                         accessors[name][setter],
                                         accessors[name][deleter],
                                         ""))


class TestClass(metaclass=AccessorType):
    """Test class for AccessorType metaclass."""

    def __init__(self):
        self._x = None

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def del_x(self):
        print('x-deleter')

    def get_y(self):
        return 'y-getter'

    def del_y(self):
        print('y-deleter')


if __name__ == "__main__":
    ex = TestClass()
    ex.x = 255
    print(ex.x)
    del(ex.x)
    try:
        ex.y = 1
    except AttributeError:
        print("Can't set y value. Setter not implemented.")
    print(ex.y)
    del(ex.y)
