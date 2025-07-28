package activities;

public class Activity1 {

	public static void main(String[] args) {
		// Creating object for car class
		
		Car honda = new Car(" Black "," Automatic ", 2020);
		
		honda.displayCharacteristics();
		honda.accelerate();
		honda.brake();

	}

}
