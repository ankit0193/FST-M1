package activities;

import java.util.HashSet;

public class Activity10 {

	public static void main(String[] args) {
		HashSet<String> hs = new HashSet<String>();
        
        hs.add("One");
        hs.add("Two");
        hs.add("Three");
        hs.add("Four");
        hs.add("Five");
        hs.add("Six");
           
        System.out.println("Size of HashSet: " + hs.size());
        
        hs.remove("Four");
        
        if(hs.remove("Ten")) {
        	System.out.println("Ten removed from the Set");
        } else {
        	System.out.println("Ten is not present in the Set");
        }
        
        System.out.println("Checking if Eight is present: " + hs.contains("Eight"));
        
        System.out.println("Updated HashSet: " + hs);
    }

}
