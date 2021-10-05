#include<stdio.h>
main()
{
	int i=0,j=0;
	printf("And Gate--\n");
	for(i=0;i<=1;i++)
	{
		for(j=0;j<=1;j++)
		printf("%d && %d  %d\n",i,j,i&&j);
		
	}
	printf("OR Gate--\n");
	for(i=0;i<=1;i++)
	{
		for(j=0;j<=1;j++)
		printf("%d || %d  %d\n",i,j,i||j);
		
	}
	printf("XOR Gate--\n");
	for(i=0;i<=1;i++)
	{
		for(j=0;j<=1;j++)
		printf("%d ^ %d  %d\n",i,j,i^j);
		
	}
	printf("Not Gate--\n");
	for(i=0;i<=1;i++)
	{
		printf("%d!  %d\n",i,!i);
		
	}
		printf("XoOR Gate--\n");
	for(i=0;i<=1;i++)
	{
		for(j=0;j<=1;j++)
		printf("%d ^ %d  %d\n",i,j,i|j);
		
	}
}
