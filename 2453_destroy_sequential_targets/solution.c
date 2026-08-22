// LeetCode 2453 - Destroy Sequential Targets
// https://leetcode.com/problems/destroy-sequential-targets/

#include <stdlib.h>
#include <limits.h>

int destroyTargets(int* nums, int numsSize, int space) {
    /* count by residue using open addressing */
    int cap = 1;
    while (cap < numsSize * 2 + 16) cap <<= 1;
    int* keys = (int*)malloc((size_t)cap * sizeof(int));
    int* vals = (int*)calloc((size_t)cap, sizeof(int));
    char* used = (char*)calloc((size_t)cap, 1);
    for (int i = 0; i < numsSize; i++) {
        int mod = nums[i] % space;
        unsigned h = (unsigned)mod * 2654435761u;
        int idx = (int)(h & (unsigned)(cap - 1));
        while (used[idx] && keys[idx] != mod) idx = (idx + 1) & (cap - 1);
        keys[idx] = mod;
        used[idx] = 1;
        vals[idx]++;
    }
    int bestCnt = 0;
    for (int i = 0; i < cap; i++) if (used[i] && vals[i] > bestCnt) bestCnt = vals[i];
    int ans = INT_MAX;
    for (int i = 0; i < numsSize; i++) {
        int mod = nums[i] % space;
        unsigned h = (unsigned)mod * 2654435761u;
        int idx = (int)(h & (unsigned)(cap - 1));
        while (used[idx] && keys[idx] != mod) idx = (idx + 1) & (cap - 1);
        if (vals[idx] == bestCnt && nums[i] < ans) ans = nums[i];
    }
    free(keys); free(vals); free(used);
    return ans;
}
