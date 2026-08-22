// LeetCode 3427 - Sum of Variable Length Subarrays
// https://leetcode.com/problems/sum-of-variable-length-subarrays/

#include <stdlib.h>

int subarraySum(int* nums, int numsSize) {
    int n = numsSize;
    int* pref = (int*)malloc((n + 1) * sizeof(int));
    pref[0] = 0;
    for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
    int ans = 0;
    for (int i = 0; i < n; i++) {
        int start = i - nums[i];
        if (start < 0) start = 0;
        ans += pref[i + 1] - pref[start];
    }
    free(pref);
    return ans;
}
