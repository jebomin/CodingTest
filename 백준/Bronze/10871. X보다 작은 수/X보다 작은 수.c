#include<stdio.h>
int main()
{
	int n, x, i;
	int a;
	scanf("%d %d", &n, &x);

	for (i = 0; i < n; i++)
	{
		scanf("%d", &a);

		if (a < x)
			printf("%d ", a);
	}
	return 0;
}