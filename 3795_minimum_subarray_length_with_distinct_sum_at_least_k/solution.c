// LeetCode 3795 - Minimum Subarray Length With Distinct Sum At Least K
// https://leetcode.com/problems/minimum-subarray-length-with-distinct-sum-at-least-k/

#include <stdlib.h>
#include <string.h>

int minLength(int* nums, int numsSize, int k) {
    int n = numsSize;
    int ans = n + 1;
    /* value range unknown; use open addressing map via sorted unique + fenwick-like counts with dynamic hash */
    int* keys = (int*)malloc((size_t)n * sizeof(int));
    int* cnt = (int*)calloc((size_t)n, sizeof(int));
    int ksz = 0;
    int l = 0;
    long long s = 0;
    for (int r = 0; r < n; r++) {
        int x = nums[r];
        int idx = -1;
        for (int i = 0; i < ksz; i++) if (keys[i] == x) { idx = i; break; }
        if (idx < 0) { idx = ksz; keys[ksz++] = x; }
        cnt[idx]++;
        if (cnt[idx] == 1) s += x;
        while (s >= (long long)k && l <= r) {
            if (r - l + 1 < ans) ans = r - l + 1;
            int y = nums[l];
            int idy = -1;
            for (int i = 0; i < ksz; i++) if (keys[i] == y) { idy = i; break; }
            cnt[idy]--;
            if (cnt[idy] == 0) s -= y;
            l++;
        }
    }
    free(keys); free(cnt);
    return ans > n ? -1 : ans;
}
