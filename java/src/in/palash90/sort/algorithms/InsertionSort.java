package in.palash90.sort.algorithms;

public class InsertionSort extends Sort {
	public int[] sort(int[] array) {
		System.out.println("Insertion Sort");
		for (int i = 1; i < array.length; i++) {
			int key = array[i];
			int j = i - 1;
			while (j >= 0 && array[j] > key) {
				array[j + 1] = array[j];
				j--;
			}
			array[j + 1] = key;
		}
		return array;
	}
}
