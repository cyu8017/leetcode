// LeetCode 3763 - Maximum Total Sum With Threshold Constraints
// https://leetcode.com/problems/maximum-total-sum-with-threshold-constraints/

#include <stdlib.h>

typedef struct { int* a; int n, cap; } MaxMulti;

static void mmPush(MaxMulti* m, int x) {
    if (m->n == m->cap) { m->cap = m->cap ? m->cap * 2 : 16; m->a = (int*)realloc(m->a, (size_t)m->cap * sizeof(int)); }
    int i = m->n++;
    m->a[i] = x;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (m->a[i] <= m->a[p]) break;
        int t = m->a[i]; m->a[i] = m->a[p]; m->a[p] = t;
        i = p;
    }
}
static int mmPop(MaxMulti* m) {
    int top = m->a[0];
    m->a[0] = m->a[--m->n];
    int i = 0;
    while (1) {
        int l = 2 * i + 1, r = 2 * i + 2, b = i;
        if (l < m->n && m->a[l] > m->a[b]) b = l;
        if (r < m->n && m->a[r] > m->a[b]) b = r;
        if (b == i) break;
        int t = m->a[i]; m->a[i] = m->a[b]; m->a[b] = t;
        i = b;
    }
    return top;
}

typedef struct { int idx, th; } Pair;
static int cmpPair(const void* a, const void* b) {
    return ((const Pair*)a)->th - ((const Pair*)b)->th;
}

long long maxSum(int* nums, int numsSize, int* threshold, int thresholdSize) {
    (void)thresholdSize;
    int n = numsSize;
    Pair* idx = (Pair*)malloc((size_t)n * sizeof(Pair));
    for (int i = 0; i < n; i++) { idx[i].idx = i; idx[i].th = threshold[i]; }
    qsort(idx, (size_t)n, sizeof(Pair), cmpPair);
    MaxMulti tree = {0};
    long long ans = 0;
    int i = 0;
    for (int step = 1; ; step++) {
        while (i < n && threshold[idx[i].idx] <= step) {
            mmPush(&tree, nums[idx[i].idx]);
            i++;
        }
        if (tree.n == 0) break;
        ans += mmPop(&tree);
    }
    free(tree.a); free(idx);
    return ans;
}
