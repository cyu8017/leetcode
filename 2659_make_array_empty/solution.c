// LeetCode 2659 - Make Array Empty
// https://leetcode.com/problems/make-array-empty/

#include <stdlib.h>

typedef struct { int val, idx; } P2659;
static int cmp2659(const void* a, const void* b) {
    return ((const P2659*)a)->val - ((const P2659*)b)->val;
}

long long countOperationsToEmptyArray(int* nums, int numsSize) {
    P2659* idx = (P2659*)malloc((size_t)numsSize * sizeof(P2659));
    for (int i = 0; i < numsSize; i++) { idx[i].val = nums[i]; idx[i].idx = i; }
    qsort(idx, (size_t)numsSize, sizeof(P2659), cmp2659);
    long long ans = numsSize;
    for (int i = 1; i < numsSize; i++)
        if (idx[i].idx < idx[i - 1].idx) ans += (long long)(numsSize - i);
    free(idx);
    return ans;
}
