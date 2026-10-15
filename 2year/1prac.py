class MyList:
    def __init__(self, *data):
        self.capacity = len(data)
        self._size = self.capacity
        self._data = [None] * self.capacity
        for i in range(self._size):
            self._data[i] = data[i]

    def count(self):
        return self._size

    def get(self, index: int):
        if not 0 <= index < self._size:
            raise IndexError("Index out of range")
        return self._data[index]

    def first(self):
        return self.get(0)

    def last(self):
        return self.get(self._size - 1)

    def includes(self, item):
        for i in range(self._size):
            if self._data[i] == item:
                return True, i
        return False, -1

    def _up_capacity(self):
        grow = max(self.capacity, 1)
        self._data.extend([None] * grow)
        self.capacity += grow

    def append(self, item):
        if self.capacity == self._size:
            self._up_capacity()
        self._data[self._size] = item
        self._size += 1

    def prepend(self, item):
        if self._size == self.capacity:
            self._up_capacity()
        self._data[1:self._size + 1] = self._data[0:self._size]
        self._data[0] = item
        self._size += 1

    def remove(self, item):
        is_include, idx = self.includes(item)
        if is_include:
            self._data[idx:self._size - 1] = self._data[idx + 1:self._size]
            self._data[self._size - 1] = None
            self._size -= 1

    def remove_first(self):
        if self._size > 0:
            self.remove(self._data[0])

    def remove_last(self):
        if self._size > 0:
            self._data[self._size - 1] = None
            self._size -= 1

    def remove_all(self):
        self._data = [None] * self.capacity
        self._size = 0


class MyIterator:
    def __init__(self, iter_obj: MyList):
        self._obj = iter_obj
        self._pos = 0
        self._obj_len = self._obj.count()

    def first(self):
        self._pos = 0

    def next(self):
        self._pos += 1

    def is_done(self):
        return self._pos >= self._obj_len

    def cur_item(self):
        if self.is_done():
            raise StopIteration
        else:
            return self._obj.get(self._pos)

    def __iter__(self):
        return self

    def __next__(self):
        item = self.cur_item()
        self.next()
        return item


class MyListIterator(MyList):
    def __iter__(self):
        return iter(MyIterator(self))


if __name__ == "__main__":
    lst = MyListIterator(1, 2, 3)
    print("Исходный список:", list(lst))
    print("count:", lst.count())
    print("first:", lst.first(), "last:", lst.last(), "get(1):", lst.get(1))
    print("includes(2):", lst.includes(2))
    print("includes(99):", lst.includes(99))

    lst.append(4)
    print("append(4):", list(lst), "capacity:", lst.capacity)

    lst.prepend(0)
    print("prepend(0):", list(lst))

    lst.remove(2)
    print("remove(2):", list(lst))

    lst.remove_first()
    print("remove_first:", list(lst))

    lst.remove_last()
    print("remove_last:", list(lst))

    print("Обход через for:", end=" ")
    for x in lst:
        print(x, end=" ")
    print()

    print("Обход через first/next/is_done/cur_item:", end=" ")
    it = MyIterator(lst)
    it.first()
    while not it.is_done():
        print(it.cur_item(), end=" ")
        it.next()
    print()

    lst.remove_all()
    print("remove_all:", list(lst), "count:", lst.count())

    try:
        lst.get(5)
    except IndexError:
        print("get(5) на пустом списке: IndexError")
