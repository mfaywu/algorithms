package search_sort;
import java.util.Scanner;

public class Binary_search {

	static Boolean binary_search_i (int[] ls, int item) {
		int first = 0;
		int last = ls.length - 1;
		Boolean found = false;
		
		while (!found && first <= last) {
			int midpoint = (first + last) / 2;
			if (ls[midpoint] == item)
				found = true;
			else if (item < ls[midpoint])
				last = midpoint - 1;
			else 
				first = midpoint + 1;
		}
		return found;
	}
	
	static Boolean binary_search_r (int[] ls, int item) {
		if (ls.length <= 0) 
			return false;
		int midpoint = ls.length / 2;
		if (ls[midpoint] == item) 
			return true;
		else if (item < ls[midpoint]) {
			int [] new_ls = new int[midpoint];
			System.arraycopy (ls, 0, new_ls, 0, new_ls.length);
			return binary_search_r (new_ls, item);
		}
		else {
			if (midpoint == ls.length - 1) return false;
			int [] new_ls = new int[midpoint];
			System.arraycopy (ls, midpoint + 1, new_ls, 0, new_ls.length);
			return binary_search_r (new_ls, item);
		}
	}
	
	public static void main(String[] args) {
		int[] ls = {1, 2, 4, 5, 9};
		System.out.print("Item list: ");
		for (int i = 0 ; i < ls.length; i++) {
			System.out.print(ls[i] + " ");
		}
		System.out.println();
		
		Scanner in = new Scanner (System.in);
		
		System.out.print("Item to look for: ");
		int item = in.nextInt();
		
		System.out.print("0 for recursive; 1 for iterative: ");
		int choice = in.nextInt();
		
		if (choice == 0) {
			if (binary_search_r (ls, item))
				System.out.println("Item found.");
			else
				System.out.println("Item not found.");
		}
		else {
			if (binary_search_i (ls, item))
				System.out.println("Item found.");
			else 
				System.out.println("Item not found.");
		}
		
		in.close();
	}

}
