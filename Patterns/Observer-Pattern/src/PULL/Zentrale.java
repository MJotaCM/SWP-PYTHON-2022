package PULL;

public class Zentrale extends Observable{
	private double temp = 0;
	private double lf = 0;
	
	public double getTemp()
	{
		return temp;
	}
	
	public double getLF()
	{
		return lf;
	}
	
	public void setState(double temp, double lf)
	{
		this.temp = temp;
		this.lf = lf;
		notifyAllObservers();
	}
}
