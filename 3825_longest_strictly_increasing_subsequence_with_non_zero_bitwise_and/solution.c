// LeetCode 3825 - Longest Strictly Increasing Subsequence With Non Zero Bitwise And
// https://leetcode.com/problems/longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/

#include <stdlib.h>

static int bit_len(unsigned x) {
    int n = 0; while (x) { n++; x >>= 1; } return n;
}

static int lis3825(int* arr, int n) {
    int* g = (int*)malloc((size_t)(n + 1) * sizeof(int));
    int gsz = 0;
    for (int i = 0; i < n; i++) {
        int x = arr[i];
        int lo = 0, hi = gsz;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (g[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        if (lo == gsz) g[gsz++] = x;
        else g[lo] = x;
    }
    free(g);
    return gsz;
}

int longestSubsequence(int* nums, int numsSize) {
    int mx = nums[0];
    for (int i = 1; i < numsSize; i++) if (nums[i] > mx) mx = nums[i];
    int m = bit_len((unsigned)mx);
    int ans = 0;
    int* arr = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < m; i++) {
        int asz = 0;
        for (int j = 0; j < numsSize; j++) if (((nums[j] >> i) & 1) == 1) arr[asz++] = nums[j];
        int v = lis3825(arr, asz);
        if (v > ans) ans = v;
    }
    free(arr);
    return ans;
}
