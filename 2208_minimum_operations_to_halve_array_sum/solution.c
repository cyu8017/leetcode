// LeetCode 2208 - Minimum Operations to Halve Array Sum
// https://leetcode.com/problems/minimum-operations-to-halve-array-sum/

#include <stdlib.h>

typedef struct { double* a; int n; } MaxH;

static void mhSwap(double* a, int i, int j) { double t = a[i]; a[i] = a[j]; a[j] = t; }
static void mhUp(MaxH* h, int i) {
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h->a[i] <= h->a[p]) break;
        mhSwap(h->a, i, p); i = p;
    }
}
static void mhDown(MaxH* h, int i) {
    for (;;) {
        int l = 2 * i + 1, r = l + 1, b = i;
        if (l < h->n && h->a[l] > h->a[b]) b = l;
        if (r < h->n && h->a[r] > h->a[b]) b = r;
        if (b == i) break;
        mhSwap(h->a, i, b); i = b;
    }
}
static void mhPush(MaxH* h, double x) { h->a[h->n] = x; mhUp(h, h->n++); }
static double mhPop(MaxH* h) { double x = h->a[0]; h->a[0] = h->a[--h->n]; mhDown(h, 0); return x; }

int halveArray(int* nums, int numsSize) {
    MaxH h = { .a = (double*)malloc((size_t)numsSize * sizeof(double)), .n = 0 };
    double sum = 0;
    for (int i = 0; i < numsSize; i++) { mhPush(&h, (double)nums[i]); sum += nums[i]; }
    double target = sum / 2.0;
    int ans = 0;
    while (sum > target) {
        double x = mhPop(&h) / 2.0;
        sum -= x;
        mhPush(&h, x);
        ans++;
    }
    free(h.a);
    return ans;
}
