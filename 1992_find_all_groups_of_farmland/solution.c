// LeetCode 1992 - Find All Groups of Farmland
// https://leetcode.com/problems/find-all-groups-of-farmland/

#include <stdlib.h>

int** findFarmland(int** land, int landSize, int* landColSize, int* returnSize, int** returnColumnSizes) {
    int m = landSize, n = landColSize[0];
    int cap = m * n;
    int** res = (int**)malloc((size_t)cap * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)cap * sizeof(int));
    int sz = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (land[i][j] == 0) continue;
            if (i > 0 && land[i - 1][j] == 1) continue;
            if (j > 0 && land[i][j - 1] == 1) continue;
            int r = i, c = j;
            while (r + 1 < m && land[r + 1][j] == 1) r++;
            while (c + 1 < n && land[i][c + 1] == 1) c++;
            res[sz] = (int*)malloc(4 * sizeof(int));
            res[sz][0] = i; res[sz][1] = j; res[sz][2] = r; res[sz][3] = c;
            (*returnColumnSizes)[sz] = 4;
            sz++;
        }
    }
    *returnSize = sz;
    return res;
}
