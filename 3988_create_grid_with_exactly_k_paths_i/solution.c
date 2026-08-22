// LeetCode 3988 - Create Grid With Exactly K Paths I
// https://leetcode.com/problems/create-grid-with-exactly-k-paths-i/

#include <stdlib.h>
#include <string.h>

char** createGrid(int m, int n, int k, int* returnSize) {
    /* patterns[k] is a list of small grids that have exactly k paths */
    static const char* p1[] = {"."};
    static const char* p2[] = {"..", ".."};
    static const char* p3a[] = {"..", "..", ".."};
    static const char* p3b[] = {"...", "..."};
    static const char* p4a[] = {"..", "..", "..", ".."};
    static const char* p4b[] = {"....", "...."};
    static const char* p4c[] = {"..#", "...", "#.."};

    const char** cands[8];
    int candRows[8], candCols[8], candCount = 0;

    if (k == 1) {
        cands[candCount] = p1; candRows[candCount] = 1; candCols[candCount] = 1; candCount++;
    } else if (k == 2) {
        cands[candCount] = p2; candRows[candCount] = 2; candCols[candCount] = 2; candCount++;
    } else if (k == 3) {
        cands[candCount] = p3a; candRows[candCount] = 3; candCols[candCount] = 2; candCount++;
        cands[candCount] = p3b; candRows[candCount] = 2; candCols[candCount] = 3; candCount++;
    } else if (k == 4) {
        cands[candCount] = p4a; candRows[candCount] = 4; candCols[candCount] = 2; candCount++;
        cands[candCount] = p4b; candRows[candCount] = 2; candCols[candCount] = 4; candCount++;
        cands[candCount] = p4c; candRows[candCount] = 3; candCols[candCount] = 3; candCount++;
    }

    for (int t = 0; t < candCount; t++) {
        int pr = candRows[t], pc = candCols[t];
        if (pr > m || pc > n) continue;
        char** result = (char**)malloc((size_t)m * sizeof(char*));
        for (int i = 0; i < m; i++) {
            result[i] = (char*)malloc((size_t)n + 1);
            memset(result[i], '#', (size_t)n);
            result[i][n] = '\0';
        }
        for (int i = 0; i < pr; i++) {
            for (int j = 0; j < pc; j++) result[i][j] = cands[t][i][j];
        }
        for (int i = pr; i < m; i++) result[i][pc - 1] = '.';
        for (int j = pc; j < n; j++) result[m - 1][j] = '.';
        *returnSize = m;
        return result;
    }
    *returnSize = 0;
    return NULL;
}
