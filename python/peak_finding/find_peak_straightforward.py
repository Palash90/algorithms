import random
import time

array = [random.random() for _ in range(10)]
print(array)

index = 0
number = array[0]

start = time.time()
for i in range(len(array) - 1):
    if number < array[i]:
        number = array[i]
        index = i
    else:
        pass

end = time.time()
print("Peak is at index", index + 1, "with value", number)
print(f"Time taken: {end - start}")
