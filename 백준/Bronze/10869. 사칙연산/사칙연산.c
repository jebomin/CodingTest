#include<stdio.h>
#pragma warning(disable:4996)

int main()
{
	int a = 0, b = 0;
	scanf("%d %d", &a, &b);
	printf("%d\n", a + b);
	printf("%d\n", a - b);
	printf("%d\n", a*b);
	printf("%d\n", a / b);
	printf("%d\n", a%b);
	return 0;
}