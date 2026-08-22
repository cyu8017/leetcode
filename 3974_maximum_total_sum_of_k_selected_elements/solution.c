// LeetCode 3974 - Maximum Total Sum Of K Selected Elements
// https://leetcode.com/problems/maximum-total-sum-of-k-selected-elements/

#include <stdlib.h>

static int cmpInt3974(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

long long maxSum(int* nums, int numsSize, int k, int mul) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt3974);
    int n = numsSize;
    long long ans = 0;
    for (int i = n - 1; i >= n - k; i--) {
        int m = mul > 1 ? mul : 1;
        ans += (long long)nums[i] * m;
        mul--;
    }
    return ans;
}
