#include<stdio.h>
#pragma warning(disable:4996)
int main()
{
	int N;
	int R;
	int A, B, C, D;
	int count = 0;

	scanf("%d", &N);
	R = N;

	while (1)
	{
		A = N / 10;
		B = N % 10;
		C = (A + B) % 10;
		D = (B * 10) + C;
		N = D;
		count++;
		if (D == R)
			break;
	}
	printf("%d", count);
}