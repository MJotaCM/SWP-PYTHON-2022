package Pizzaria;

public abstract class Pizzaria {
    abstract Pizza pizzaErstellen(String type);
    
    public Pizza pizzaBestellen(String type)
    {
        Pizza pizza = pizzaErstellen(type);
        System.out.println("Ihre Bestellung: " + pizza.getName());
        pizza.backen();
        pizza.schneiden();
        pizza.einpacken();
        return pizza;
    }
}