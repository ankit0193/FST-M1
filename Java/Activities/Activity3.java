package activities;

public class Activity3 {

	public static void main(String[] args) {
		double Sec = 1000000000 ;
		double EarthSec = 31557600;
		double MercurySec = 0.2408467;
		double VenusSec = 0.61519726;
		double MarsSec = 1.8808158;
		double JupiterSec = 11.862615;
		double SaturnSec = 29.447498;
		double UranusSec = 84.016846;
		double NeptuneSec = 164.79132;
		

        System.out.println("Age on Mercury: " + Sec / EarthSec / MercurySec);
        System.out.println("Age on Venus: " + Sec / EarthSec / VenusSec);
        System.out.println("Age on Earth: " + Sec / EarthSec);
        System.out.println("Age on Mars: " + Sec / EarthSec / MarsSec);
        System.out.println("Age on Jupiter: " + Sec / EarthSec / JupiterSec);
        System.out.println("Age on Saturn: " + Sec / EarthSec / SaturnSec);
        System.out.println("Age on Uranus: " + Sec / EarthSec / UranusSec);
        System.out.println("Age on Neptune: " + Sec / EarthSec / NeptuneSec);

	}

}
