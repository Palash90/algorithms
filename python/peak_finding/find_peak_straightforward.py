import random
import time


def find_peaks(array):
    indexes = []
    numbers = []

    start = time.time()

    if len(array) == 1:
        indexes.append(1)
        numbers.append(array[0])
    else:
        for i in range(len(array)):
            if i != 0 and i != len(array) - 1:
                if array[i] >= array[i - 1] and array[i] >= array[i + 1]:
                    indexes.append(i + 1)
                    numbers.append(array[i])
            if i == 0:
                if array[i] >= array[i + 1]:
                    indexes.append(i + 1)
                    numbers.append(array[i])
            if i == len(array) - 1:
                if array[i] >= array[i - 1]:
                    indexes.append(i + 1)
                    numbers.append(array[i])

    end = time.time()
    print("Peaks are at indexes", indexes, "with values", numbers)
    print(f"Time taken: {end - start} \n")


num_of_elements = 200  # Must be positive Integer

array = [_ + 1 for _ in range(num_of_elements)]
print(array)
find_peaks(array)

array = [num_of_elements - _ for _ in range(num_of_elements)]
print(array)
find_peaks(array)

array = [random.random() for _ in range(num_of_elements)]
print(array)
find_peaks(array)
