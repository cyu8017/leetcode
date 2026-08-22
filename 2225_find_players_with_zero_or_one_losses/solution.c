// LeetCode 2225 - Find Players With Zero or One Losses
// https://leetcode.com/problems/find-players-with-zero-or-one-losses/

#include <stdlib.h>
#include <string.h>

static int cmp_int(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int** findWinners(int** matches, int matchesSize, int* matchesColSize, int* returnSize, int** returnColumnSizes) {
    (void)matchesColSize;
    int maxId = 0;
    for (int i = 0; i < matchesSize; i++) {
        if (matches[i][0] > maxId) maxId = matches[i][0];
        if (matches[i][1] > maxId) maxId = matches[i][1];
    }
    int* lose = (int*)calloc((size_t)(maxId + 1), sizeof(int));
    char* seen = (char*)calloc((size_t)(maxId + 1), 1);
    for (int i = 0; i < matchesSize; i++) {
        seen[matches[i][0]] = 1;
        seen[matches[i][1]] = 1;
        lose[matches[i][1]]++;
    }
    int* zero = (int*)malloc((size_t)(maxId + 1) * sizeof(int));
    int* one = (int*)malloc((size_t)(maxId + 1) * sizeof(int));
    int zc = 0, oc = 0;
    for (int p = 1; p <= maxId; p++) {
        if (!seen[p]) continue;
        if (lose[p] == 0) zero[zc++] = p;
        else if (lose[p] == 1) one[oc++] = p;
    }
    free(lose);
    free(seen);
    int** ans = (int**)malloc(2 * sizeof(int*));
    ans[0] = zero;
    ans[1] = one;
    *returnSize = 2;
    *returnColumnSizes = (int*)malloc(2 * sizeof(int));
    (*returnColumnSizes)[0] = zc;
    (*returnColumnSizes)[1] = oc;
    return ans;
}
