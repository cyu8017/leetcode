// LeetCode 2245 - Maximum Trailing Zeros in a Cornered Path
// https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/

#include <stdlib.h>

typedef struct { int two, five; } Pair;

static Pair fact(int x) {
    Pair p = {0, 0};
    while (x % 2 == 0) { p.two++; x /= 2; }
    while (x % 5 == 0) { p.five++; x /= 5; }
    return p;
}

static int mini(int a, int b) { return a < b ? a : b; }

int maxTrailingZeros(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    Pair** left = (Pair**)malloc((size_t)m * sizeof(Pair*));
    Pair** up = (Pair**)malloc((size_t)m * sizeof(Pair*));
    for (int i = 0; i < m; i++) {
        left[i] = (Pair*)malloc((size_t)n * sizeof(Pair));
        up[i] = (Pair*)malloc((size_t)n * sizeof(Pair));
        for (int j = 0; j < n; j++) {
            Pair p = fact(grid[i][j]);
            left[i][j] = p;
            up[i][j] = p;
            if (j > 0) {
                left[i][j].two += left[i][j - 1].two;
                left[i][j].five += left[i][j - 1].five;
            }
            if (i > 0) {
                up[i][j].two += up[i - 1][j].two;
                up[i][j].five += up[i - 1][j].five;
            }
        }
    }
    int ans = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            Pair cell = fact(grid[i][j]);
            Pair L = left[i][j];
            int Rtwo = left[i][n - 1].two - left[i][j].two + cell.two;
            int Rfive = left[i][n - 1].five - left[i][j].five + cell.five;
            Pair U = up[i][j];
            int Dtwo = up[m - 1][j].two - up[i][j].two + cell.two;
            int Dfive = up[m - 1][j].five - up[i][j].five + cell.five;
            Pair cands[4] = {
                {L.two + U.two - cell.two, L.five + U.five - cell.five},
                {L.two + Dtwo - cell.two, L.five + Dfive - cell.five},
                {Rtwo + U.two - cell.two, Rfive + U.five - cell.five},
                {Rtwo + Dtwo - cell.two, Rfive + Dfive - cell.five},
            };
            for (int t = 0; t < 4; t++) {
                int z = mini(cands[t].two, cands[t].five);
                if (z > ans) ans = z;
            }
        }
    }
    for (int i = 0; i < m; i++) { free(left[i]); free(up[i]); }
    free(left); free(up);
    return ans;
}
