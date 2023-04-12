package Pizzaria;

public abstract class Pizza {
    String name;
    
    public String getName()
    {
        return name;
    }
    
    void backen()
    {
        System.out.println("Pizza wird gebacken");
    }
    
    void schneiden()
    {
        System.out.println("Pizza wird geschnitten");
    }
    
    void einpacken()
    {
        System.out.println("Pizza wird eingepackt");
    }
}