#include<stdio.h>
#pragma warning(disable:4996)

int main()
{
	int a = 0, b = 0;
	scanf("%d %d", &a, &b);
	printf("%d\n", a*((b % 100) % 10));
	printf("%d\n", a*((b % 100) / 10));
	printf("%d\n", a*(b / 100));
	printf("%d\n", a*b);
	return 0;
}