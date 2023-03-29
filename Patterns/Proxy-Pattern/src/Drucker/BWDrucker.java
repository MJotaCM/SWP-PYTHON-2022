package Drucker;

public class BWDrucker extends Drucker{

	private String fn;
	private ColorDrucker cd;
	private boolean c = false;
	
	public BWDrucker(String fn) 
	{
		this.fn = fn;
		cd = null;
	}
	
	public void newFile(String fn) 
	{
		this.fn = fn;
	}
	
	public void setColor(boolean c) 
	{
		this.c = c;
	}
	
	@Override
	public void druck() 
	{
		if(c)
		{
			switchToColor();
		}else 
		{
			System.out.println("Folgendes Dockument wird gerade in sw gedruckt:" + this.fn );
		}
	}
	
	public void switchToColor()
	{
		if(cd == null) {
			cd = new ColorDrucker(this.fn);
		}
		cd.druck();
	}
}
