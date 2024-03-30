class MyIterator:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max_num:
            self.current +=1
            return self.current
        else:
            raise StopIteration

my_iter = MyIterator(5)
for num in my_iter:
    print(num)

