// LeetCode 3780 - Maximum Sum Of Three Numbers Divisible By Three
// https://leetcode.com/problems/maximum-sum-of-three-numbers-divisible-by-three/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int maximumSum(int* nums, int numsSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    int* g[3];
    int sz[3] = {0, 0, 0};
    int cap[3] = {0, 0, 0};
    g[0] = g[1] = g[2] = NULL;
    for (int i = 0; i < numsSize; i++) {
        int r = nums[i] % 3;
        if (sz[r] == cap[r]) {
            cap[r] = cap[r] ? cap[r] * 2 : 8;
            g[r] = (int*)realloc(g[r], (size_t)cap[r] * sizeof(int));
        }
        g[r][sz[r]++] = nums[i];
    }
    int ans = 0;
    for (int a = 0; a < 3; a++) {
        if (sz[a] > 0) {
            int x = g[a][--sz[a]];
            for (int b = 0; b < 3; b++) {
                if (sz[b] > 0) {
                    int y = g[b][--sz[b]];
                    int c = (3 - (a + b) % 3) % 3;
                    if (sz[c] > 0) {
                        int z = g[c][sz[c] - 1];
                        if (x + y + z > ans) ans = x + y + z;
                    }
                    g[b][sz[b]++] = y;
                }
            }
            g[a][sz[a]++] = x;
        }
    }
    free(g[0]); free(g[1]); free(g[2]);
    return ans;
}
