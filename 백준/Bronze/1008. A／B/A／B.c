#include<stdio.h>
#pragma warning(disable:4996)

int main()
{
	double a=0, b=0;
	scanf("%lf %lf", &a, &b);
	printf("%0.9f", a/b);
	return 0;
}