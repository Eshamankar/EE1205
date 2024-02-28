#include <stdio.h>
#include <math.h>

#define N 10

int main() {
    int n;
    double y_o;

    printf("n\t\t y_o(n)\n");
    printf("------------------------\n");

    for (n = 0; n <= N; ++n) {
        y_o = 2 * (n + 1) + (pow(3, n + 2) - 1) / 2.0;
        printf("%d\t\t %.2lf\n", n, y_o);
    }

    return 0;
}
