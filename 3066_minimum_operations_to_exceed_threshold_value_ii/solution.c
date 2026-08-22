// LeetCode 3066 - Minimum Operations to Exceed Threshold Value II
// https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

#include <stdlib.h>

typedef struct { long long *a; int n, cap; } MinHeap;
static void heap_push(MinHeap* h, long long x) {
    if (h->n == h->cap) { h->cap = h->cap ? h->cap * 2 : 16; h->a = (long long*)realloc(h->a, (size_t)h->cap * sizeof(long long)); }
    int i = h->n++;
    h->a[i] = x;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h->a[p] <= h->a[i]) break;
        long long t = h->a[p]; h->a[p] = h->a[i]; h->a[i] = t; i = p;
    }
}
static long long heap_pop(MinHeap* h) {
    long long r = h->a[0];
    h->a[0] = h->a[--h->n];
    int i = 0;
    for (;;) {
        int l = 2 * i + 1, rgt = 2 * i + 2, m = i;
        if (l < h->n && h->a[l] < h->a[m]) m = l;
        if (rgt < h->n && h->a[rgt] < h->a[m]) m = rgt;
        if (m == i) break;
        long long t = h->a[i]; h->a[i] = h->a[m]; h->a[m] = t; i = m;
    }
    return r;
}

int minOperations(int* nums, int numsSize, int k) {
    MinHeap h = {NULL, 0, 0};
    for (int i = 0; i < numsSize; i++) heap_push(&h, nums[i]);
    int ans = 0;
    while (h.n > 1 && h.a[0] < k) {
        long long x = heap_pop(&h), y = heap_pop(&h);
        heap_push(&h, x * 2 + y);
        ans++;
    }
    free(h.a);
    return ans;
}
