// LeetCode 3256 - Maximum Value Sum by Placing Three Rooks I
// https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-i/

#include <stdlib.h>
#include <limits.h>

typedef struct { int v, c; } Cell3256;

long long maximumValueSum(int** board, int boardSize, int* boardColSize) {
    int m = boardSize, n = boardColSize[0];
    Cell3256** tops = (Cell3256**)malloc((size_t)m * sizeof(Cell3256*));
    int* tlen = (int*)calloc((size_t)m, sizeof(int));
    for (int i = 0; i < m; i++) {
        tops[i] = (Cell3256*)malloc(3 * sizeof(Cell3256));
        tlen[i] = 0;
        for (int j = 0; j < n; j++) {
            Cell3256 cur = {board[i][j], j};
            int placed = 0;
            for (int t = 0; t < tlen[i]; t++) {
                if (cur.v > tops[i][t].v) {
                    for (int k = tlen[i]; k > t; k--) {
                        if (k < 3) tops[i][k] = tops[i][k - 1];
                    }
                    tops[i][t] = cur;
                    if (tlen[i] < 3) tlen[i]++;
                    placed = 1;
                    break;
                }
            }
            if (!placed && tlen[i] < 3) tops[i][tlen[i]++] = cur;
        }
    }
    long long ans = LLONG_MIN / 4;
    for (int i = 0; i < m; i++) {
        for (int ai = 0; ai < tlen[i]; ai++) {
            Cell3256 a = tops[i][ai];
            for (int j = i + 1; j < m; j++) {
                for (int bi = 0; bi < tlen[j]; bi++) {
                    Cell3256 b = tops[j][bi];
                    if (a.c == b.c) continue;
                    for (int k = j + 1; k < m; k++) {
                        for (int ci = 0; ci < tlen[k]; ci++) {
                            Cell3256 c = tops[k][ci];
                            if (c.c == a.c || c.c == b.c) continue;
                            long long s = (long long)a.v + b.v + c.v;
                            if (s > ans) ans = s;
                        }
                    }
                }
            }
        }
    }
    for (int i = 0; i < m; i++) free(tops[i]);
    free(tops); free(tlen);
    return ans;
}
