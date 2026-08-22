// LeetCode 3397 - Maximum Number of Distinct Elements After Operations
// https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int maxDistinctElements(int* nums, int numsSize, int k) {
    qsort(nums, numsSize, sizeof(int), cmp_int);
    int ans = 0;
    long long prev = -1000000000000000000LL;
    for (int i = 0; i < numsSize; i++) {
        long long cur = (long long)nums[i] - k;
        if (cur <= prev) cur = prev + 1;
        if (cur > (long long)nums[i] + k) continue;
        ans++;
        prev = cur;
    }
    return ans;
}
