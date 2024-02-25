#include <stdio.h>

int main() {
    FILE *file = fopen("values.dat", "w");  // Open a text file for writing

    if (file == NULL) {
        printf("Error opening the file.\n");
        return 1;  // Return an error code
    }

    // Use fprintf to write values to the file directly without arrays
    fprintf(file, "Values for stem plot of x_1(n):\n");

    for (int i = 0; i < 33; i++) {
        int n = i;
        float x_1 = (float)(7 + 3 * n);
        fprintf(file, "%d %.2f\n", n, x_1);
    }

    fprintf(file, "\nValues for stem plot of x_2(n):\n");  // Add a newline and heading

    for (int i = 0; i < 33; i++) {
        int n = i;
        float x_2 = (float)(-18 + 2 * n);
        fprintf(file, "%d %.2f\n", n, x_2);
    }

    fprintf(file, "\nValues for stem plot of x_3(n):\n");

    for (int i = 0; i < 33; i++) {
        int n = i;
        float x_3 = (float)(15 - 3 * n);
        fprintf(file, "%d %.2f\n", n, x_3);
    }

    fprintf(file, "\nValues for stem plot of x_4(n):\n");

    for (int i = 0; i < 33; i++) {
        int n = i;
        float x_4 = (float)(18.9 + 2.5 * n);
        fprintf(file, "%d %.2f\n", n, x_4);
    }

    fprintf(file, "\nValues for stem plot of x_5(n):\n");

    for (int i = 0; i < 33; i++) {
        int n = i;
        float x_5 = (float)(18.9 + 2.5 * n);
        fprintf(file, "%d %.2f\n", n, x_5);
    }

    fclose(file);  // Close the file

    return 0;
}

