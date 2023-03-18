package remind;

import java.util.Scanner;
import java.util.Map;
import java.util.TreeMap;

/**
 * @author Kholofelo Madithapa
 * Program date: 2023-03-16
 * Purpose: Collects a list of names (possibly with duplicates) from
 *          the user and arrange them on the basis of key and value.
 *          Key represents names and value represents how many times a
 *          particular name appears in the list.
 */

public class RemindMe {

	public static void main(String[] args){
		
		Scanner input = new Scanner(System.in);
		Map<String, Integer> map = new TreeMap<String, Integer>();
		
		int _nameList_size = 0;
		String[] _nameList;
		String _nameList_item;
		
		System.out.print("Enter array size: ");
		_nameList_size = Integer.parseInt(input.nextLine().trim());
		_nameList = new String[_nameList_size];
		
		for(int counter = 0; counter < _nameList_size; counter++) {
			try {
				System.out.print("Enter name: ");
				_nameList_item = input.nextLine();
			} catch(Exception e) {
				_nameList_item = null;
			}
			
			_nameList[counter] = _nameList_item;
		}
		
		map = Book.aggregateNames(_nameList);
		System.out.println();
		
		for (Map.Entry<String, Integer> entry : map.entrySet()) {
			System.out.println(entry.getKey() + " " + String.valueOf(entry.getValue()));
		}
		
		input.close();	
	}

}
