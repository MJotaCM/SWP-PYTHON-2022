package Pizzaria;

public class HamburgPizzeria extends Pizzaria{
	@Override
	Pizza pizzaErstellen(String type) 
	{
		if (type.equals("Salami")){
            return new HamburgSalami();
        } else if (type.equals("Hawaii")){
            return new HamburgHawaii();
        } else if (type.equals("Calzone")){
            return new HamburgCalzone();
        } else if (type.equals("QuattroStagioni")){
            return new HamburgQuattroStagioni();
        } else return null;
	}
}
