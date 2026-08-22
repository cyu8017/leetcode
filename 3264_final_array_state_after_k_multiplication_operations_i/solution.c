// LeetCode 3264 - Final Array State After K Multiplication Operations I
// https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/

#include <stdlib.h>

typedef struct { int v, i; } MiPair;

static void heapSwap(MiPair* a, MiPair* b) { MiPair t = *a; *a = *b; *b = t; }

static int lessP(MiPair a, MiPair b) {
    if (a.v == b.v) return a.i < b.i;
    return a.v < b.v;
}

static void siftUp(MiPair* h, int i) {
    while (i > 0) {
        int p = (i - 1) / 2;
        if (!lessP(h[i], h[p])) break;
        heapSwap(&h[i], &h[p]);
        i = p;
    }
}

static void siftDown(MiPair* h, int n, int i) {
    for (;;) {
        int l = 2 * i + 1, r = l + 1, best = i;
        if (l < n && lessP(h[l], h[best])) best = l;
        if (r < n && lessP(h[r], h[best])) best = r;
        if (best == i) break;
        heapSwap(&h[i], &h[best]);
        i = best;
    }
}

int* getFinalState(int* nums, int numsSize, int k, int multiplier, int* returnSize) {
    MiPair* h = (MiPair*)malloc((size_t)numsSize * sizeof(MiPair));
    int hn = 0;
    for (int i = 0; i < numsSize; i++) {
        h[hn] = (MiPair){nums[i], i};
        siftUp(h, hn++);
    }
    for (int t = 0; t < k; t++) {
        MiPair p = h[0];
        h[0] = h[--hn];
        if (hn) siftDown(h, hn, 0);
        p.v *= multiplier;
        nums[p.i] = p.v;
        h[hn] = p;
        siftUp(h, hn++);
    }
    free(h);
    *returnSize = numsSize;
    return nums;
}
