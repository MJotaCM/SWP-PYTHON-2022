package Drucker;

public class Druck {

	public static void main(String[] args) {
		Drucker d = new BWDrucker("Katzen");
		d.druck();
		d.newFile("Pandas");
		d.switchToColor();
	}
}
