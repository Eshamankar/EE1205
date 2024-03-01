#include <stdio.h>
#include <math.h>

int main() {
    FILE *file = fopen("values_v.dat", "w");  // Open a text file for writing

    if (file == NULL) {
        printf("Error opening the file.\n");
        return 1;  // Return an error code
    }

    // Use fprintf to write values to the file directly without arrays
    fprintf(file, "Values for stem plot of V_o(t):\n");

    for (float t = 0.0; t <= 0.1; t += 0.005) {
        float V_o = 0.5 + (0.21 / 2) * sin(300 * t);

        fprintf(file, "%.3f %.4f\n", t, V_o);
    }

    fclose(file);  // Close the file

    return 0;
}

