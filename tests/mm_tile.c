#include <stdio.h>

int mm() {
    int N = 100;  
    int TILE_SIZE = 32;
    int ma[N][N], mb[N][N], mc[N][N];

    // Initialize matrix ma and mb
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            ma[i][j] = i * j;
            mb[i][j] = i + j;
            mc[i][j] = 0; // Initialize result matrix mc to 0
        }
    }

    // Perform matrix multiplication with tiling
    for (int ii = 0; ii < N; ii += TILE_SIZE) {
        for (int jj = 0; jj < N; jj += TILE_SIZE) {
            for (int kk = 0; kk < N; kk += TILE_SIZE) {
                // Multiply the tiles
                for (int i = ii; i < ii + TILE_SIZE && i < N; i++) {
                    for (int j = jj; j < jj + TILE_SIZE && j < N; j++) {
                        for (int k = kk; k < kk + TILE_SIZE && k < N; k++) {
                            mc[i][j] += ma[i][k] * mb[k][j];
                        }
                    }
                }
            }
        }
    }
    return mc[N-1][N-1];
}

int main() {
    int res = mm();  // Call the matrix multiplication function
    printf("Result: %d\n", res);
    return 0;
}
