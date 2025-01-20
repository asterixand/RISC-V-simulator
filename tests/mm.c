int mm() {
    // either 10 or 100
    int N = 100; 
    int ma[N][N];
    int mb[N][N];
    int mc[N][N];

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            ma[i][j] = i * j;
            mb[i][j] = i + j;
            mc[i][j] = 0;
        }
    }

    // Perform matrix multiplication: mc = ma * mb
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            for (int k = 0; k < N; k++) {
                mc[i][j] += ma[i][k] * mb[k][j];
            }
        }
    }

    return mc[N-1][N-1];
}