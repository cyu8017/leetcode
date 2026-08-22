// LeetCode 3914 - Minimum Operations To Make Array Non Decreasing
// https://leetcode.com/problems/minimum-operations-to-make-array-non-decreasing/

long long minOperations(int* nums, int numsSize) {
    long long ans = 0;
    for (int i = 1; i < numsSize; i++) {
        long long d = (long long)nums[i - 1] - nums[i];
        if (d > 0) ans += d;
    }
    return ans;
}
