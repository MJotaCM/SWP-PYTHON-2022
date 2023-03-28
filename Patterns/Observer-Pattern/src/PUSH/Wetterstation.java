package PUSH;

public class Wetterstation {
	public static void main(String[] args) 
	{
		// PUSH - Obsevable schickt von sich aus schon die Daten an alle Observer
		
		// Observer wird nicht ein bestimmtes Obsevable übergeben
		Zentrale z = new Zentrale();
		Anzeige a1 = new Anzeige();
		
		z.addObserver(a1);
		z.setState(26,20);
	}
}
