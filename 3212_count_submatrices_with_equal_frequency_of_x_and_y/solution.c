// LeetCode 3212 - Count Submatrices With Equal Frequency of X and Y
// https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/

#include <stdlib.h>
#include <string.h>

int numberOfSubmatrices(char** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0], ans = 0;
    int* s0 = calloc((m + 1) * (n + 1), sizeof(int));
    int* s1 = calloc((m + 1) * (n + 1), sizeof(int));
    #define S0(i,j) s0[(i)*(n+1)+(j)]
    #define S1(i,j) s1[(i)*(n+1)+(j)]
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            S0(i,j) = S0(i-1,j) + S0(i,j-1) - S0(i-1,j-1) + (grid[i-1][j-1] == 'X');
            S1(i,j) = S1(i-1,j) + S1(i,j-1) - S1(i-1,j-1) + (grid[i-1][j-1] == 'Y');
            if (S0(i,j) > 0 && S0(i,j) == S1(i,j)) ans++;
        }
    }
    #undef S0
    #undef S1
    free(s0); free(s1);
    return ans;
}
