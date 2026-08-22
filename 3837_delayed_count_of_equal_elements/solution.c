// LeetCode 3837 - Delayed Count Of Equal Elements
// https://leetcode.com/problems/delayed-count-of-equal-elements/

#include <stdlib.h>
#include <string.h>

int* delayedCount(int* nums, int numsSize, int k, int* returnSize) {
    int n = numsSize;
    int* ans = (int*)calloc((size_t)n, sizeof(int));
    /* hash map with open addressing */
    int cap = 1;
    while (cap < n * 2 + 16) cap <<= 1;
    int* keys = (int*)malloc((size_t)cap * sizeof(int));
    int* vals = (int*)calloc((size_t)cap, sizeof(int));
    char* used = (char*)calloc((size_t)cap, 1);
    for (int i = n - k - 2; i >= 0; i--) {
        int x = nums[i + k + 1];
        unsigned h = (unsigned)x * 2654435761u;
        int j = (int)(h & (unsigned)(cap - 1));
        while (used[j] && keys[j] != x) j = (j + 1) & (cap - 1);
        if (!used[j]) { used[j] = 1; keys[j] = x; vals[j] = 0; }
        vals[j]++;
        int y = nums[i];
        h = (unsigned)y * 2654435761u;
        j = (int)(h & (unsigned)(cap - 1));
        while (used[j] && keys[j] != y) j = (j + 1) & (cap - 1);
        ans[i] = (used[j] && keys[j] == y) ? vals[j] : 0;
    }
    free(keys); free(vals); free(used);
    *returnSize = n;
    return ans;
}
