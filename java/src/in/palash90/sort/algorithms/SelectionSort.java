package in.palash90.sort.algorithms;

import in.palash90.sort.util.Utils;

public class SelectionSort extends Sort {
	public int[] sort(int[] array) {
		System.out.println("Selection Sort");
		for (int i = 0; i < array.length - 1; i++) {
			System.out.println("Iteration " + (i + 1));
			int minIndex = i;
			for (int j = (i + 1); j < array.length; j++) {
				if (array[minIndex] > array[j]) {
					minIndex = j;
				}
			}
			Utils.swap(array, minIndex, i);
			Utils.printArray(array);
		}
		return array;
	}
}
