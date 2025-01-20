#include<stdio.h>

void saxpy(int alpha, int X[], int Y[]) {
    int N = 5;
    for (int i = 0; i < N; i++) {
        Y[i] = alpha * X[i] + Y[i];
    }
}

int main() {
    int alpha = 2;  // Scalar multiplier
    int N = 5;      // Vector size
    // Input vectors X and Y
    int X[5];
    int Y[5];

    for(int i=0;i<N;i++){
        for (int j=0;j<N;j++){
            X[i] = 2*i -10;
            Y[i] = j+3;
        }
    }


    // Perform SAXPY operation
    saxpy(alpha, X, Y);

    // Y = alpha * X + Y

    int t1 = Y[0];
    int t2 = Y[1];
    int t3 = Y[3];

    int ans = t1+t2+t3;
    printf("ans: %d\n",ans);
    return 0;
}
