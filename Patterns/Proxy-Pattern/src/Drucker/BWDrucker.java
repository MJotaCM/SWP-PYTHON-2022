package Drucker;

public class BWDrucker extends Drucker{

	private String fn;
	private ColorDrucker cd;
	
	public BWDrucker(String fn) 
	{
		this.fn = fn;
		cd = null;
	}
	
	public void newFile(String fn) 
	{
		this.fn = fn;
	}
	
	@Override
	public void druck() 
	{
		System.out.println("Folgendes Dockument wird gerade in sw gedruckt:" + this.fn );
	}
	
	public void switchToColor()
	{
		if(cd == null) {
			cd = new ColorDrucker(this.fn);
		}
		cd.druck();
	}
}
