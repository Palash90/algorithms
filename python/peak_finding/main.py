import random

from peak_finding.find_peak_straightforward import find_peaks_brute_force

num_of_elements = 200  # Must be positive Integer

array = [_ + 1 for _ in range(num_of_elements)]
print(array)
find_peaks_brute_force(array, True)

array = [num_of_elements - _ for _ in range(num_of_elements)]
print(array)
find_peaks_brute_force(array, True)

array = [random.random() for _ in range(num_of_elements)]
print(array)
find_peaks_brute_force(array, True)
