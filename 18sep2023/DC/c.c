#include <stdio.h>

void findUncommonFactors(int a, int b)
{
    int min_val = a < b ? a : b;
    int max_val = a > b ? a : b;

    int uncommon_factors[max_val];
    int count = 0;

    for (int i = 2; i <= min_val; i++)
    {
        if ((a % i == 0 && b % i != 0) || (b % i == 0 && a % i != 0))
        {
            uncommon_factors[count++] = i;
        }
    }

    if (count == 0)
    {
        printf("-1\n");
    }
    else
    {
        for (int i = count - 1; i >= 0; i--)
        {
            printf("%d ", uncommon_factors[i]);
        }
        printf("\n");
    }
}

int main()
{
    int a, b;
    printf("Enter the values a and b: ");
    scanf("%d %d", &a, &b);
    findUncommonFactors(a, b);
    return 0;
}
