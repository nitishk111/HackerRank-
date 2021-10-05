#include<stdio.h>
#include<malloc.h>
main()
{
	int *a;
	int i,n;
	scanf("%d",&n);a=(int*)malloc(4*n);
	for(i=0;i<n;i++)
	{
	scanf("%d",a+i);
	}int j,temp;
	for(j=0;j<n-1;j++)
	{
	
	for(i=0;i<n-1;i++)
	{
		if(*(a+i)>*(a+i+1))
		{
			temp=*(a+i);
			*(a+i)=*(a+i+1);
			*(a+i+1)=temp;
		}
	}}
	for(i=0;i<n;i++)
	printf("%d ",*(a+i));
}
