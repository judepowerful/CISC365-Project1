import random


def array_generator(n):
    generated_array = []
    while n > 0:
        random_num = random.randint(0, 3 * n)
        generated_array.append(random_num)
        n -= 1
    # sort the array
    bubble_sort(generated_array)
    return generated_array


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
