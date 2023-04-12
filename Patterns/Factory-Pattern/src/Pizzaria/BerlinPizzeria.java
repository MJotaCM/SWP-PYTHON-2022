package Pizzaria;

public class BerlinPizzeria extends Pizzaria{
	@Override
	Pizza pizzaErstellen(String type) 
	{
		if (type.equals("Salami")){
            return new BerlinSalami();
        } else if (type.equals("Hawaii")){
            return new BerlinHawaii();
        } else if (type.equals("Calzone")){
            return new BerlinCalzone();
        } else if (type.equals("QuattroStagioni")){
            return new BerlinQuattroStagioni();
        } else return null;
	}
}
