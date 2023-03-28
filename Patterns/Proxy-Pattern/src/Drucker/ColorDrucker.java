package Drucker;

public class ColorDrucker extends Drucker{

	private String fn;
	
	public ColorDrucker(String fn)
	{
		this.fn = fn;
	}
	
	
	public void newFile(String fn) 
	{
		this.fn = fn;
	}
	
	
	@Override
	public void druck() 
	{
		System.out.println("Folgendes Dokument wird gerade in farbe gedruckt:" + this.fn );
	}
}
