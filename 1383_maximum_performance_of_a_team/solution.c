// LeetCode 1383 - Maximum Performance of a Team
// https://leetcode.com/problems/maximum-performance-of-a-team/

#include <stdlib.h>

typedef struct { int e, s; } Pair;
static int cmp_pair(const void* a, const void* b) { return ((const Pair*)b)->e - ((const Pair*)a)->e; }

typedef struct { int* data; int size; int cap; } MinHeap;
static void hpush(MinHeap* h, int v) {
    if (h->size == h->cap) { h->cap *= 2; h->data = (int*)realloc(h->data, h->cap * sizeof(int)); }
    int i = h->size++;
    h->data[i] = v;
    while (i > 0) { int p = (i - 1) / 2; if (h->data[p] <= h->data[i]) break;
        int t = h->data[p]; h->data[p] = h->data[i]; h->data[i] = t; i = p; }
}
static int hpop(MinHeap* h) {
    int res = h->data[0];
    h->data[0] = h->data[--h->size];
    int i = 0;
    while (1) {
        int l = 2 * i + 1, r = 2 * i + 2, s = i;
        if (l < h->size && h->data[l] < h->data[s]) s = l;
        if (r < h->size && h->data[r] < h->data[s]) s = r;
        if (s == i) break;
        int t = h->data[i]; h->data[i] = h->data[s]; h->data[s] = t; i = s;
    }
    return res;
}

int maxPerformance(int n, int* speed, int speedSize, int* efficiency, int efficiencySize, int k) {
    (void)speedSize; (void)efficiencySize;
    Pair* pairs = (Pair*)malloc(n * sizeof(Pair));
    for (int i = 0; i < n; i++) { pairs[i].e = efficiency[i]; pairs[i].s = speed[i]; }
    qsort(pairs, n, sizeof(Pair), cmp_pair);
    MinHeap h = { (int*)malloc(16 * sizeof(int)), 0, 16 };
    long long total = 0, ans = 0;
    for (int i = 0; i < n; i++) {
        hpush(&h, pairs[i].s);
        total += pairs[i].s;
        if (h.size > k) total -= hpop(&h);
        long long cand = total * pairs[i].e;
        if (cand > ans) ans = cand;
    }
    free(pairs); free(h.data);
    return (int)(ans % 1000000007LL);
}
