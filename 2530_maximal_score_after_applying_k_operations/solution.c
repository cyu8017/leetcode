// LeetCode 2530 - Maximal Score After Applying K Operations
// https://leetcode.com/problems/maximal-score-after-applying-k-operations/

#include <stdlib.h>

static void pushMax(int* h, int* n, int x) {
    int i = (*n)++;
    h[i] = x;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p] >= h[i]) break;
        int t = h[p]; h[p] = h[i]; h[i] = t;
        i = p;
    }
}
static int popMax(int* h, int* n) {
    int res = h[0];
    h[0] = h[--(*n)];
    int i = 0;
    for (;;) {
        int l = i * 2 + 1, r = l + 1, best = i;
        if (l < *n && h[l] > h[best]) best = l;
        if (r < *n && h[r] > h[best]) best = r;
        if (best == i) break;
        int t = h[i]; h[i] = h[best]; h[best] = t;
        i = best;
    }
    return res;
}

long long maxKelements(int* nums, int numsSize, int k) {
    int* h = (int*)malloc((size_t)numsSize * sizeof(int));
    int hn = 0;
    for (int i = 0; i < numsSize; i++) pushMax(h, &hn, nums[i]);
    long long ans = 0;
    for (int i = 0; i < k; i++) {
        int x = popMax(h, &hn);
        ans += x;
        pushMax(h, &hn, (x + 2) / 3);
    }
    free(h);
    return ans;
}
