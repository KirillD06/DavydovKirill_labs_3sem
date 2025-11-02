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
