/**
 * @author Tyler
 */

public class car {
	
	// constructor
	public car(String carMake, int carYear) {
		this.make = carMake;
		this.year = carYear;
	}
	
	// public methods
	
	// getter
	public String getMake() {
		return this.make;
	}
	
	// setter
	public void setMake(String carMake) {
		this.make = carMake;
	}
	
	// getter
	public int getYear() {
		return this.year;
	}
	
	// setter
	public void setYear(int carYear) {
		this.year = carYear;
	}
	
	// private attributes
	private String make;
	private int year;
	
	// public attributes
	int array[] = new int[4];
	
	
}
