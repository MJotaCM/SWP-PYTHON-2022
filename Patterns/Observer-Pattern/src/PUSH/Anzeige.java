package PUSH;

public class Anzeige implements Observer{
	
	@Override
	public void update(double temp, double lf) {
		System.out.println("Werte wurde ver�ndert: Temp:" + temp + " Luftfeuchtigkeit:" + lf);
	}

}
