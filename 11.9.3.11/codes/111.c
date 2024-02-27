#include <stdio.h>
#include <math.h>

double calculateY(int n) {
    return 2 * (n + 1) + (3 * (pow(3, n + 1) - 1)) / 2.0;
}

int main() {
    int n;
    
    printf("n\t\ty(n)\n");
    printf("------------------\n");

    for (n = 0; n <= 10; n++) {
        double result = calculateY(n);
        printf("%d\t\t%.2f\n", n, result);
    }

    return 0;
}

