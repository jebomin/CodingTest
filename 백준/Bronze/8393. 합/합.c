#include<stdio.h>

int main()
{
	int a, i;
	scanf("%d", &a);

	int sum = 0;
	for (i = 1; i <= a; i++)
	{
		sum += i;
	}
	printf("%d", sum);
	return 0;
}