class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()

    def __next__(self):
        while True:
            item = next(self.items)
            check_item = item.lower() if self.ignore_case and isinstance(item, str) else item
            if check_item not in self.seen:
                self.seen.add(check_item)
                return item

    def __iter__(self):
        return self


if __name__ == '__main__':
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print("Тест 1: Unique([1, 1, 1, 1, 1, 2, 2, 2, 2, 2])")
    for val in Unique(data1):
        print(val, end=' ')
    print()
    
    data2 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print("\nТест 2: Unique(['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B'])")
    for val in Unique(data2):
        print(val, end=' ')
    print()
    
    print("\nТест 3: Unique(['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B'], ignore_case=True)")
    data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    for val in Unique(data3, ignore_case=True):
        print(val, end=' ')
    print()
