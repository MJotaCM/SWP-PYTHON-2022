package PULL;

public class Anzeige implements Observer {

	private Zentrale ze;

	public Anzeige(Zentrale z)
	{
		this.ze = z;
		ze.addObserver(this);
	}
	@Override
	public void update() {
		System.out.println("Werte wurde verändert: Temp:" + ze.getTemp() + " Luftfeuchtigkeit:" + ze.getLF());
	}
	
}
