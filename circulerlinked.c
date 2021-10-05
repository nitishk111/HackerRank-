#include<stdio.h>
#include<malloc.h>
struct node
{
	int data;
	struct node *next;
};
main()
{
	struct node *a,*b,*c,*head;
	head='\0';
	char ch;int i;
	printf("Enter y or Y for creat node-");
	scanf("%c",&ch);
	while(ch=='y')
	{
		fflush(stdin);
		a=(struct node*)malloc(sizeof(struct node));
		printf("\nEnter value at node-");
		scanf("%d",&a->data);
		if(head=='\0')
		{
			head=a;
			b=a;
		}
		else
		{
			b->next=a;
			b=a;
		}
		printf("Enter y or Y for creat node-");	fflush(stdin);
		scanf("%c",&ch);
	}
	b->next=head;
	printf("\n");
	a=head;
	do
	{
		printf("%d ",a->data);
		a=a->next;
	}while(a!=head);
	//insertion in node;
	a=head;
	int k,l=0;
	while(a->next!=head)
	{
		l++;
		a=a->next;
	}l++;
	printf("\nl==%d",l);
	printf("\nEnter place to insert-");
	scanf("%d",&k);
	a=head;
	if(k==1)
	{
		b=(struct node*)malloc(sizeof(struct node));
		printf("\nEnter value at node-");
		scanf("%d",&b->data);
		b->next=head;
		head=b;
	}
	/*else
	{
		if(k<l)
		while(i=2;i<k;i++)
		{
			a=a->next;
		}
		b=(struct node*)malloc(sizeof(struct node));
		printf("\nEnter value at node-");
		scanf("%d",&b->data);
		b->next=a->next->next;
		a->next;
	}
/*	a=head;
	do
	{
		a=a->next;
	}while(a!=head);
	a->next=
/*/	
	a=head;
	do
	{
		printf("%d ",a->data);
		a=a->next;
	}while(a!=head);
}
