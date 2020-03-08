package in.palash90.sort.algorithms;

import in.palash90.sort.util.Utils;

public class BubbleSort extends Sort{
	public int[] sort(int[] array) {
		System.out.println("Bubble Sort");
		for (int i = 0; i < array.length - 1; i++) {
			for (int j = 0; j < (array.length - i - 1); j++) {
				if (array[j] > array[j+1]) {
					Utils.swap(array, j, j+1);
				}
			}
		}
		return array;
	}
}
