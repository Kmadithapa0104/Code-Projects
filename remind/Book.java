package remind;

import java.util.Map;
import java.util.TreeMap;

public class Book{
	
	/**
	 * 
	 * @param nameList - receives an array of names
	 * @return - returns a map containing keys as names and values 
	 *            indicating how many times a certain name repeats.
	 */
	public static Map<String, Integer> aggregateNames(String[] nameList){
		
		Map<String, Integer> map = new TreeMap<String, Integer>();
		
		final int ONE = 1;
		
		map.put(nameList[0], ONE);
		
		for (int i = 1; i < nameList.length; i++) {
			
			if (map.containsKey(nameList[i])) {
				
				//increment the value mapped to the name key by 1
				map.put(nameList[i], map.get(nameList[i]) + ONE);
			}
			else {
				map.put(nameList[i], ONE);
			}
			
		}
			return map;
	}
}
