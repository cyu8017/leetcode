// LeetCode 0952 - Largest Component Size by Common Factor
// https://leetcode.com/problems/largest-component-size-by-common-factor/

#include <stdlib.h>

static int find(int* p, int x) {
    while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; }
    return x;
}

int largestComponentSize(int* nums, int numsSize) {
    int mx = nums[0];
    for (int i = 1; i < numsSize; i++) if (nums[i] > mx) mx = nums[i];
    int* parent = (int*)malloc((size_t)(mx + 1) * sizeof(int));
    for (int i = 0; i <= mx; i++) parent[i] = i;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i], d = 2, orig = x;
        while (d * d <= x) {
            if (x % d == 0) {
                parent[find(parent, orig)] = find(parent, d);
                while (x % d == 0) x /= d;
            }
            d++;
        }
        if (x > 1) parent[find(parent, orig)] = find(parent, x);
    }
    int* cnt = (int*)calloc((size_t)(mx + 1), sizeof(int));
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int r = find(parent, nums[i]);
        cnt[r]++;
        if (cnt[r] > ans) ans = cnt[r];
    }
    free(parent); free(cnt);
    return ans;
}
