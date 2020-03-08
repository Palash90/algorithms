package in.palash90.sort.algorithms;

public class SortFactory {
	public static Sort getSort(SortType type) {
		Sort sort = null;
		switch (type) {
		case SELECTION:
			sort = new SelectionSort();
			break;
		case BUBBLE:
			sort = new BubbleSort();
			break;
		case INSERTION:
			sort=new InsertionSort();
			break;
		default:
			break;

		}
		return sort;
	}
}
