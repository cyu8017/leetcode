// LeetCode 2233 - Maximum Product After K Increments
// https://leetcode.com/problems/maximum-product-after-k-increments/

#include <stdlib.h>

static void heap_swap(int* a, int i, int j) {
    int t = a[i]; a[i] = a[j]; a[j] = t;
}

static void heap_up(int* a, int i) {
    while (i > 0) {
        int p = (i - 1) / 2;
        if (a[p] <= a[i]) break;
        heap_swap(a, p, i);
        i = p;
    }
}

static void heap_down(int* a, int n, int i) {
    for (;;) {
        int l = 2 * i + 1, r = l + 1, s = i;
        if (l < n && a[l] < a[s]) s = l;
        if (r < n && a[r] < a[s]) s = r;
        if (s == i) break;
        heap_swap(a, i, s);
        i = s;
    }
}

int maximumProduct(int* nums, int numsSize, int k) {
    const int MOD = 1000000007;
    int* h = (int*)malloc((size_t)numsSize * sizeof(int));
    int hn = numsSize;
    for (int i = 0; i < numsSize; i++) h[i] = nums[i];
    for (int i = numsSize / 2 - 1; i >= 0; i--) heap_down(h, hn, i);
    for (int i = 0; i < k; i++) {
        int x = h[0] + 1;
        h[0] = h[hn - 1];
        hn--;
        if (hn > 0) heap_down(h, hn, 0);
        h[hn++] = x;
        heap_up(h, hn - 1);
    }
    long long ans = 1;
    for (int i = 0; i < hn; i++) ans = ans * h[i] % MOD;
    free(h);
    return (int)ans;
}
