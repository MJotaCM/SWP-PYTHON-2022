package PUSH;

import java.util.ArrayList;
import java.util.List;

public abstract class Observable {
	
	private final List<Observer> ol = new ArrayList<Observer>();
	
	public void addObserver(Observer o)
	{
		ol.add(o);
	}
	
	public void removeObserver(Observer o) 
	{
		ol.remove(o);
	}
	
	public void notifyAllObservers(double temp, double lf)
	{
		for (Observer o : ol) {
			o.update(temp, lf);
		}
	}
}