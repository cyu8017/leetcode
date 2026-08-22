// LeetCode 2587 - Rearrange Array to Maximize Prefix Score
// https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/

#include <stdlib.h>

static int cmpDesc(const void* a, const void* b) {
    return *(const int*)b - *(const int*)a;
}

int maxScore(int* nums, int numsSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpDesc);
    long long sum = 0;
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        sum += nums[i];
        if (sum > 0) ans++;
        else break;
    }
    return ans;
}
