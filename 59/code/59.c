#include <stdio.h>
#include <math.h>

int main() {
    FILE *file = fopen("values.dat", "w");
    if (file == NULL) {
        fprintf(stderr, "Error opening file.\n");
        return 1;
    }

    double t;
    for (t = 0.0; t <= 1.0; t += 0.01) {
        double V_o = 0.5 + 0.21 / 2 * sin(300 * t);
        fprintf(file, "%lf\n", V_o);
    }

    fclose(file);
    return 0;
}

