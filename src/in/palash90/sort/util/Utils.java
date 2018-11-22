/**
 * 
 */
package in.palash90.sort.util;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * @author palash
 *
 */
public class Utils {
	public static int[] getIntegersInLine() throws IOException {
		String input;
		System.out.println("Enter comma separated list of integers to be sorted:");
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		input = br.readLine();
		String[] inputArr = input.split(",");
		int[] intArr = new int[inputArr.length];
		for (int i = 0; i < inputArr.length; i++) {
			intArr[i] = Integer.parseInt(inputArr[i]);
		}

		return intArr;
	}

	public static void printArray(int[] array) {
		System.out.print("\n[");
		for (int i = 0; i < array.length; i++) {
			System.out.print(array[i] + " ");
		}
		System.out.print("]\n");
	}

	public static void swap(int[] array, int source, int destination) {
		int temp = array[source];
		array[source] = array[destination];
		array[destination] = temp;
	}
}
