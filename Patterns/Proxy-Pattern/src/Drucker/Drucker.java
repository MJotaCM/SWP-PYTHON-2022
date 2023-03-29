package Drucker;

public abstract class Drucker {
	
	public abstract void druck();
	
	public abstract void newFile(String fn);
	
	public void setColor(boolean b) 
	{
		System.out.println("Drucker wurde getauscht");
	}
}
