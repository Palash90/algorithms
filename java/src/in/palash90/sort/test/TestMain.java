package in.palash90.sort.test;

import java.io.IOException;

import in.palash90.sort.algorithms.Sort;
import in.palash90.sort.algorithms.SortFactory;
import in.palash90.sort.algorithms.SortType;
import in.palash90.sort.util.Utils;

public class TestMain {

	public static void main(String[] args) throws IOException {
		int[] input = Utils.getIntegersInLine();
		Sort sort = SortFactory.getSort(SortType.INSERTION);
		System.out.println("Input before sorting");
		Utils.printArray(input);
		Utils.printArray(sort.sort(input));
	}

}
