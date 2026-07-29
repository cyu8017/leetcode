// LeetCode 0764 - Largest Plus Sign
#include <stdlib.h>
#include <string.h>

int orderOfLargestPlusSign(int n, int** mines, int minesSize, int* minesColSize) {
    (void)minesColSize;
    char* banned = (char*)calloc((size_t)n * n, 1);
    for (int i = 0; i < minesSize; i++) banned[mines[i][0] * n + mines[i][1]] = 1;
    int** arms = (int**)malloc((size_t)n * sizeof(int*));
    for (int i = 0; i < n; i++) arms[i] = (int*)calloc((size_t)n, sizeof(int));
    int best = 0;
    for (int r = 0; r < n; r++) {
        int count = 0;
        for (int c = 0; c < n; c++) { count = banned[r*n+c] ? 0 : count + 1; arms[r][c] = count; }
        count = 0;
        for (int c = n - 1; c >= 0; c--) { count = banned[r*n+c] ? 0 : count + 1; if (count < arms[r][c]) arms[r][c] = count; }
    }
    for (int c = 0; c < n; c++) {
        int count = 0;
        for (int r = 0; r < n; r++) { count = banned[r*n+c] ? 0 : count + 1; if (count < arms[r][c]) arms[r][c] = count; }
        count = 0;
        for (int r = n - 1; r >= 0; r--) {
            count = banned[r*n+c] ? 0 : count + 1;
            if (count < arms[r][c]) arms[r][c] = count;
            if (arms[r][c] > best) best = arms[r][c];
        }
    }
    for (int i = 0; i < n; i++) free(arms[i]);
    free(arms); free(banned);
    return best;
}
