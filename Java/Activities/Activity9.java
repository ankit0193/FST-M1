package activities;

import java.util.ArrayList;

public class Activity9 {

	public static void main(String[] args) {
		ArrayList<String> myList = new ArrayList<String>();
		myList.add("Ram");
        myList.add("Hari");
        myList.add("Shyam");
        myList.add("Dev");
        myList.add("Gopal");
        
        for(String str : myList) {
        	System.out.println(str);
        }

        System.out.println("3rd element in the list is: " + myList.get(2));
        System.out.println("Is Kali is in list: " + myList.contains("Kali"));
        System.out.println("Size of List: " + myList.size());

        myList.remove("Dev");
        
        System.out.println("New Size of List: " + myList.size());

	}

}
