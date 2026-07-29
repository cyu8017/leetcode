// LeetCode 1983 - Widest Pair of Indices With Equal Range Sum
// https://leetcode.com/problems/widest-pair-of-indices-with-equal-range-sum/

#include <stdlib.h>

typedef struct { long long key; int idx; } Pair;

static int cmpPair(const void* a, const void* b) {
    const Pair* x = a; const Pair* y = b;
    if (x->key < y->key) return -1;
    if (x->key > y->key) return 1;
    return x->idx - y->idx;
}

int widestPairOfIndices(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    (void)nums2Size;
    int n = nums1Size;
    Pair* arr = (Pair*)malloc((size_t)(n + 1) * sizeof(Pair));
    long long sum = 0;
    arr[0].key = 0;
    arr[0].idx = -1;
    for (int i = 0; i < n; i++) {
        sum += nums1[i] - nums2[i];
        arr[i + 1].key = sum;
        arr[i + 1].idx = i;
    }
    qsort(arr, (size_t)(n + 1), sizeof(Pair), cmpPair);
    int best = 0;
    for (int i = 0; i < n; ) {
        int j = i;
        while (j <= n && arr[j].key == arr[i].key) j++;
        int mn = arr[i].idx, mx = arr[i].idx;
        for (int k = i; k < j; k++) {
            if (arr[k].idx < mn) mn = arr[k].idx;
            if (arr[k].idx > mx) mx = arr[k].idx;
        }
        if (mx - mn > best) best = mx - mn;
        i = j;
    }
    free(arr);
    return best;
}
