#include<stdio.h>

int main()
{
	int h, m;
	scanf("%d %d", &h, &m);
	if (m < 45)
	{
		m += 60;
		h--;
		if (h < 0)
			h = 23;
	}
	printf("%d %d", h, m - 45);
}

