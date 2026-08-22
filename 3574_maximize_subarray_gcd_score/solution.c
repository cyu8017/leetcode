// LeetCode 3574 - Maximize Subarray GCD Score
// https://leetcode.com/problems/maximize-subarray-gcd-score/

#include <stdlib.h>
#include <limits.h>

static int gcd(int a, int b) {
    while (b) { int t = a % b; a = b; b = t; }
    return a;
}

long long maxGCDScore(int* nums, int numsSize, int k) {
    int n = numsSize;
    int* cnt = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < n; i++) {
        int x = nums[i];
        while (x % 2 == 0) { cnt[i]++; x /= 2; }
    }
    long long ans = 0;
    for (int l = 0; l < n; l++) {
        int g = 0, mi = INT_MAX, t = 0;
        for (int r = l; r < n; r++) {
            g = gcd(g, nums[r]);
            if (cnt[r] < mi) { mi = cnt[r]; t = 1; }
            else if (cnt[r] == mi) t++;
            long long score = (long long)g * (r - l + 1);
            if (t <= k) score *= 2;
            if (score > ans) ans = score;
        }
    }
    free(cnt);
    return ans;
}
