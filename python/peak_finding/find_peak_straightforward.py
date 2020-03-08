import time


def find_peaks_brute_force(array, single=False):
    indexes = []
    numbers = []

    start = time.time()

    method_name(array, indexes, numbers, single)

    end = time.time()
    print("Peaks are at indexes", indexes, "with values", numbers)
    print(f"Time taken: {end - start} \n")


def method_name(array, indexes, numbers, single):
    if len(array) == 1:
        indexes.append(1)
        numbers.append(array[0])
    else:
        for i in range(len(array)):
            if i != 0 and i != len(array) - 1:
                if array[i] >= array[i - 1] and array[i] >= array[i + 1]:
                    indexes.append(i + 1)
                    numbers.append(array[i])
                    if single:
                        break
                    else:
                        pass
            if i == 0:
                if array[i] >= array[i + 1]:
                    indexes.append(i + 1)
                    numbers.append(array[i])
                    if single:
                        break
                    else:
                        pass
            if i == len(array) - 1:
                if array[i] >= array[i - 1]:
                    indexes.append(i + 1)
                    numbers.append(array[i])
                    if single:
                        break
                    else:
                        pass
