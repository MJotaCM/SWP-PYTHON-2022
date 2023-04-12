package Pizzaria;

public class Bestellung {
	public static void main(String[]args)
	{
        Pizzaria hp = new BerlinPizzeria();
        Pizza p = hp.pizzaBestellen("QuattroStagioni");
        
        Pizzaria bp = new HamburgPizzeria();
        Pizza p3 = bp.pizzaBestellen("Hawaii");
    }
}
