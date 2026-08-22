// LeetCode 2593 - Find Score of an Array After Marking All Elements
// https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

#include <stdlib.h>
#include <stdbool.h>

static int* gnums;
static int cmpIdx(const void* a, const void* b) {
    int ia = *(const int*)a, ib = *(const int*)b;
    if (gnums[ia] != gnums[ib]) return gnums[ia] - gnums[ib];
    return ia - ib;
}

long long findScore(int* nums, int numsSize) {
    int* idx = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) idx[i] = i;
    gnums = nums;
    qsort(idx, (size_t)numsSize, sizeof(int), cmpIdx);
    bool* marked = (bool*)calloc((size_t)numsSize, sizeof(bool));
    long long ans = 0;
    for (int k = 0; k < numsSize; k++) {
        int i = idx[k];
        if (marked[i]) continue;
        ans += nums[i];
        marked[i] = true;
        if (i > 0) marked[i - 1] = true;
        if (i + 1 < numsSize) marked[i + 1] = true;
    }
    free(idx); free(marked);
    return ans;
}
