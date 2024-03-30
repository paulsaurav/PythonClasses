def my_generator(max_number):
    current = 0
    while current < max_number:
        yield current
        current +=1

gen = my_generator(5)
for num in gen:
    print(num)
