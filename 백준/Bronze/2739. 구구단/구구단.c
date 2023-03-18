#include<stdio.h>

int main()
{
	int a=0;
	int b;
	scanf("%d", &a);

	for (int i = 1; i < 10; i++)
	{
		b = a * i;
		printf("%d * %d = %d\n", a, i, b);
	}
}