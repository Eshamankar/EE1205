#include <stdio.h>
#include <math.h>

#define N 10

int main() {
    int n;
    double x;

    printf("n\t\t x(n)\n");
    printf("------------------------\n");

    for (n = 0; n <= N; ++n) {
        x = 2 * (n + 1) + (pow(3, n + 2) - 1) / 2.0;
        printf("%d\t\t %.2lf\n", n, x);
    }

    return 0;
}

