// LeetCode 2599 - Make the Prefix Sum Non-negative
// https://leetcode.com/problems/make-the-prefix-sum-non-negative/

#include <stdlib.h>

static void siftUp(int* h, int i) {
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p] <= h[i]) break;
        int t = h[p]; h[p] = h[i]; h[i] = t;
        i = p;
    }
}
static void siftDown(int* h, int n, int i) {
    while (1) {
        int l = 2 * i + 1, r = 2 * i + 2, best = i;
        if (l < n && h[l] < h[best]) best = l;
        if (r < n && h[r] < h[best]) best = r;
        if (best == i) break;
        int t = h[i]; h[i] = h[best]; h[best] = t;
        i = best;
    }
}

int makePrefSumNonNegative(int* nums, int numsSize) {
    int* h = (int*)malloc((size_t)numsSize * sizeof(int));
    int hs = 0;
    long long sum = 0;
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        sum += nums[i];
        if (nums[i] < 0) {
            h[hs] = nums[i];
            siftUp(h, hs);
            hs++;
        }
        if (sum < 0) {
            int worst = h[0];
            h[0] = h[--hs];
            if (hs) siftDown(h, hs, 0);
            sum -= worst;
            ans++;
        }
    }
    free(h);
    return ans;
}
