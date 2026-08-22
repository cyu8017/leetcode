// LeetCode 2542 - Maximum Subsequence Score
// https://leetcode.com/problems/maximum-subsequence-score/

#include <stdlib.h>

typedef struct { int a, b; } Pair2542;

static int cmp2542(const void* x, const void* y) {
    return ((const Pair2542*)y)->b - ((const Pair2542*)x)->b;
}

static void pushMin(int* h, int* n, int x) {
    int i = (*n)++;
    h[i] = x;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p] <= h[i]) break;
        int t = h[p]; h[p] = h[i]; h[i] = t;
        i = p;
    }
}
static int popMin(int* h, int* n) {
    int res = h[0];
    h[0] = h[--(*n)];
    int i = 0;
    for (;;) {
        int l = i * 2 + 1, r = l + 1, best = i;
        if (l < *n && h[l] < h[best]) best = l;
        if (r < *n && h[r] < h[best]) best = r;
        if (best == i) break;
        int t = h[i]; h[i] = h[best]; h[best] = t;
        i = best;
    }
    return res;
}

long long maxScore(int* nums1, int nums1Size, int* nums2, int nums2Size, int k) {
    (void)nums2Size;
    int n = nums1Size;
    Pair2542* arr = (Pair2542*)malloc((size_t)n * sizeof(Pair2542));
    for (int i = 0; i < n; i++) { arr[i].a = nums1[i]; arr[i].b = nums2[i]; }
    qsort(arr, (size_t)n, sizeof(Pair2542), cmp2542);
    int* h = (int*)malloc((size_t)(k + 5) * sizeof(int));
    int hn = 0;
    long long sum = 0, ans = 0;
    for (int i = 0; i < n; i++) {
        pushMin(h, &hn, arr[i].a);
        sum += arr[i].a;
        if (hn > k) sum -= popMin(h, &hn);
        if (hn == k) {
            long long cand = sum * arr[i].b;
            if (cand > ans) ans = cand;
        }
    }
    free(arr); free(h);
    return ans;
}
