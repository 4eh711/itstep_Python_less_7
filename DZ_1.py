class GeneratorIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return self.generator()

    def generator(self):
        for item in self.data:
            yield item

# Пример использования
my_list = [1, 2, 3, 4, 5]
iterable = GeneratorIterable(my_list)

for value in iterable:
    print(value)