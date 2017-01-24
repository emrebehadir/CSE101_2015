#include<stdio.h>

int drawerMenu();
int traingleDrawer();
int rhomboidDrawer();
int circleDrawer();	

int main( )

{	int user_choise;
	
	//drawerMenu();

	while (1)
		{
		drawerMenu();
		printf ("->\n") ;
		scanf ("%d",&user_choise) ;

		if (user_choise ==1)
		{
			traingleDrawer();
		}

		else if (user_choise ==2)
		{
			rhomboidDrawer();
		}

		else if (user_choise ==3)
		{
			circleDrawer();	
		}	

		else if (user_choise ==4)

		{	   
			 break ;
		}
		
		else
		{
			printf ("invalid input,please try again!");
		}

		}

}


int drawerMenu()
{

	printf ("Welcome To Drawer's Home!\n"	);
	printf ("[1] Triangle\n");
	printf ("[2] Rhomboid\n");
	printf ("[3] Circle\n");
	printf ("[4] Exit\n");
	printf( "Select a Shape:\n");

}

int traingleDrawer()
{	

	int i=1,k=0,space,h ;
	
	printf(" Enter height of triangle ->\n");
	scanf("%d",&h);
	while (i<=h)
		
	{
		space =1;
		while (space<=h-i)
		{
			printf(" ");
			space+=1;
		}

		while (k != 2*i-1)
		{
			printf("*");
			k+=1;
		}

		k=0;
		i+=1;
		printf("\n");
	}
	return ;
}

int rhomboidDrawer()

{	
	int w,h,i=0,j,x;
	printf("Enter w side size->\n");
	scanf("%d",&w);
	printf("Enter h side size->\n");
	scanf( "%d",&h);

	for   ( i=0;i<h;i++ )            
		{
		j=0;
		for (x=0;x<i;x++ )    
		
		{
			printf(" "); 
		}
		
		for(j=0;j<w;j++  )    
		{
			
			printf("* ");
		}
		
		
		printf("\n");    

	    }
  
  return;
  
}

int circleDrawer()
{	
	int r,y;
	float x,value,r_out;
	printf("Enter Radius ->\n");
	scanf ("%d",&r);

	r_out = r + 0.4;
	y = r;
	while (y >= -r)
		{

		x = -r  ;
		
		while (x < r_out)
			
			{
			
			value = (x * x )+ (y * y);
			if (value <= (r_out * r_out))
		{
				printf("*");
		}        
				
			else
		{
				printf(" ");
		}            
				
			x =x+ 0.5 ;
			
		}  

		printf("\n");
		y-=1 ;

	    }

return ;
}