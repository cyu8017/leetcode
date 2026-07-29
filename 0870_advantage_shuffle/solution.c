// LeetCode 0870 - Advantage Shuffle
// https://leetcode.com/problems/advantage-shuffle/

#include <stdlib.h>
#include <string.h>

typedef struct { int val, idx; } Pair;

static int cmp_int(const void* a, const void* b) {
    return (*(const int*)a) - (*(const int*)b);
}
static int cmp_pair_desc(const void* a, const void* b) {
    return ((const Pair*)b)->val - ((const Pair*)a)->val;
}

int* advantageCount(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    (void)nums2Size;
    int n = nums1Size;
    int* sorted1 = (int*)malloc((size_t)n * sizeof(int));
    memcpy(sorted1, nums1, (size_t)n * sizeof(int));
    qsort(sorted1, (size_t)n, sizeof(int), cmp_int);
    Pair* order = (Pair*)malloc((size_t)n * sizeof(Pair));
    for (int i = 0; i < n; i++) order[i] = (Pair){nums2[i], i};
    qsort(order, (size_t)n, sizeof(Pair), cmp_pair_desc);
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    int lo = 0, hi = n - 1;
    for (int i = 0; i < n; i++) {
        int idx = order[i].idx, val = order[i].val;
        if (sorted1[hi] > val) ans[idx] = sorted1[hi--];
        else ans[idx] = sorted1[lo++];
    }
    free(sorted1); free(order);
    *returnSize = n;
    return ans;
}
