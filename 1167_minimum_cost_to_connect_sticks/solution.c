// LeetCode 1167 - Minimum Cost to Connect Sticks
// https://leetcode.com/problems/minimum-cost-to-connect-sticks/

#include <stdlib.h>

static void heapSwap(int* a, int* b) { int t = *a; *a = *b; *b = t; }
static void heapPush(int* h, int* n, int v) {
    int i = (*n)++;
    h[i] = v;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p] <= h[i]) break;
        heapSwap(&h[p], &h[i]);
        i = p;
    }
}
static int heapPop(int* h, int* n) {
    int top = h[0];
    h[0] = h[--(*n)];
    int i = 0;
    while (1) {
        int l = 2 * i + 1, r = 2 * i + 2, best = i;
        if (l < *n && h[l] < h[best]) best = l;
        if (r < *n && h[r] < h[best]) best = r;
        if (best == i) break;
        heapSwap(&h[best], &h[i]);
        i = best;
    }
    return top;
}

int connectSticks(int* sticks, int sticksSize) {
    if (sticksSize <= 1) return 0;
    int* heap = (int*)malloc((size_t)sticksSize * sizeof(int));
    int n = 0;
    for (int i = 0; i < sticksSize; i++) heapPush(heap, &n, sticks[i]);
    int ans = 0;
    while (n > 1) {
        int cost = heapPop(heap, &n) + heapPop(heap, &n);
        ans += cost;
        heapPush(heap, &n, cost);
    }
    free(heap);
    return ans;
}
