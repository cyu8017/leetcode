// LeetCode 2163 - Minimum Difference in Sums After Removal of Elements
// https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/

#include <stdlib.h>

typedef struct { int* a; int n; int maxh; } Heap;

static void heapSwap(int* a, int i, int j) { int t = a[i]; a[i] = a[j]; a[j] = t; }

static void heapUp(Heap* h, int i) {
    while (i > 0) {
        int p = (i - 1) / 2;
        int better = h->maxh ? h->a[i] > h->a[p] : h->a[i] < h->a[p];
        if (!better) break;
        heapSwap(h->a, i, p); i = p;
    }
}

static void heapDown(Heap* h, int i) {
    for (;;) {
        int l = 2 * i + 1, r = l + 1, best = i;
        if (l < h->n) {
            int better = h->maxh ? h->a[l] > h->a[best] : h->a[l] < h->a[best];
            if (better) best = l;
        }
        if (r < h->n) {
            int better = h->maxh ? h->a[r] > h->a[best] : h->a[r] < h->a[best];
            if (better) best = r;
        }
        if (best == i) break;
        heapSwap(h->a, i, best); i = best;
    }
}

static void heapPush(Heap* h, int x) { h->a[h->n] = x; heapUp(h, h->n++); }
static int heapPop(Heap* h) { int x = h->a[0]; h->a[0] = h->a[--h->n]; heapDown(h, 0); return x; }

long long minimumDifference(int* nums, int numsSize) {
    int n = numsSize / 3;
    long long* left = (long long*)calloc((size_t)numsSize, sizeof(long long));
    long long* right = (long long*)calloc((size_t)numsSize, sizeof(long long));
    Heap hmax = { .a = (int*)malloc((size_t)(2 * n + 5) * sizeof(int)), .n = 0, .maxh = 1 };
    long long sum = 0;
    for (int i = 0; i < n; i++) { heapPush(&hmax, nums[i]); sum += nums[i]; }
    left[n - 1] = sum;
    for (int i = n; i < 2 * n; i++) {
        heapPush(&hmax, nums[i]);
        sum += nums[i];
        sum -= heapPop(&hmax);
        left[i] = sum;
    }
    Heap hmin = { .a = (int*)malloc((size_t)(2 * n + 5) * sizeof(int)), .n = 0, .maxh = 0 };
    sum = 0;
    for (int i = numsSize - 1; i >= 2 * n; i--) { heapPush(&hmin, nums[i]); sum += nums[i]; }
    right[2 * n] = sum;
    for (int i = 2 * n - 1; i >= n; i--) {
        heapPush(&hmin, nums[i]);
        sum += nums[i];
        sum -= heapPop(&hmin);
        right[i] = sum;
    }
    long long ans = left[n - 1] - right[n];
    for (int i = n; i < 2 * n; i++) {
        long long diff = left[i] - right[i + 1];
        if (diff < ans) ans = diff;
    }
    free(hmax.a); free(hmin.a); free(left); free(right);
    return ans;
}
