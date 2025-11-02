def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for item in items:
            value = item.get(args[0])
            if value is not None:
                yield value
    else:
        for item in items:
            result = {}
            for key in args:
                value = item.get(key)
                if value is not None:
                    result[key] = value
            if result:
                yield result


if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]
    
    print("Тест 1: field(goods, 'title')")
    for val in field(goods, 'title'):
        print(val)
    
    print("\nТест 2: field(goods, 'title', 'price')")
    for val in field(goods, 'title', 'price'):
        print(val)
