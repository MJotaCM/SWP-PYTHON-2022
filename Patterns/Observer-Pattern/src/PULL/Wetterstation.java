package PULL;

public class Wetterstation {
	public static void main(String[] args) 
	{
		// PULL - Observer werden notified und müssen durch get-Methode Daten selbst holen
		
		Zentrale z = new Zentrale();
		Anzeige a1 = new Anzeige(z);
		Anzeige a2 = new Anzeige(z);
		
		z.setState(26,20);
	}
}
