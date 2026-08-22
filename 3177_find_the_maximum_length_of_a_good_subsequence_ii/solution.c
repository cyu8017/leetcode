// LeetCode 3177 - Find the Maximum Length of a Good Subsequence II
// https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/

#include <stdlib.h>
#include <string.h>

enum { H3177 = 10007 };
typedef struct { int key, val, used; } E3177;

static int* mpget3177(E3177* ht, int key) {
    unsigned h = ((unsigned)key * 2654435761u) % H3177;
    for (;;) {
        if (!ht[h].used) { ht[h].used = 1; ht[h].key = key; ht[h].val = 0; return &ht[h].val; }
        if (ht[h].key == key) return &ht[h].val;
        h = (h + 1) % H3177;
    }
}

int maximumLength(int* nums, int numsSize, int k) {
    int n = numsSize;
    int* f = calloc(n * (k + 1), sizeof(int));
    E3177* mp = calloc((k + 1) * H3177, sizeof(E3177));
    int (*g)[3] = calloc(k + 1, sizeof(int[3]));
    int ans = 0;
    for (int i = 0; i < n; i++) {
        for (int h = 0; h <= k; h++) {
            int* cell = &f[i * (k + 1) + h];
            *cell = *mpget3177(&mp[h * H3177], nums[i]);
            if (h > 0) {
                if (g[h - 1][0] != nums[i]) {
                    if (g[h - 1][1] > *cell) *cell = g[h - 1][1];
                } else {
                    if (g[h - 1][2] > *cell) *cell = g[h - 1][2];
                }
            }
            (*cell)++;
            int* pv = mpget3177(&mp[h * H3177], nums[i]);
            if (*cell > *pv) *pv = *cell;
            if (g[h][0] != nums[i]) {
                if (*cell >= g[h][1]) {
                    g[h][2] = g[h][1]; g[h][1] = *cell; g[h][0] = nums[i];
                } else if (*cell > g[h][2]) g[h][2] = *cell;
            } else if (*cell > g[h][1]) g[h][1] = *cell;
            if (*cell > ans) ans = *cell;
        }
    }
    free(f); free(mp); free(g);
    return ans;
}
