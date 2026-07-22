// LeetCode 1679 - Max Number of K-Sum Pairs
// https://leetcode.com/problems/max-number-of-k-sum-pairs/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int maxOperations(int* nums, int numsSize, int k) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt);
    int lo = 0, hi = numsSize - 1, ans = 0;
    while (lo < hi) {
        int s = nums[lo] + nums[hi];
        if (s == k) { ans++; lo++; hi--; }
        else if (s < k) lo++;
        else hi--;
    }
    return ans;
}
