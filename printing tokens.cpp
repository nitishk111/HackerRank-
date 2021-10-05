#include<stdio.h>
#include<string.h>
 main(){
 char s[1000];
   // scanf("%[^\n",s);
   //scanf("%[^\n]%*c",s);
    gets(s);
	char a,d[20];int i=0,j=0;a=s[j];
    while(a!='\0')
    {
        a=s[j];
        if(a!=' ')
        {
            d[i]=a;
            i++;
        }
       else
        {
            d[i]='\0';
            printf("%s\n",d);
			i=0;
        }
		j++;
    }
}


