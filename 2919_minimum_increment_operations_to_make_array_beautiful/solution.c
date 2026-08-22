// LeetCode 2919 - Minimum Increment Operations to Make Array Beautiful
// https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/

static long long min64(long long a, long long b) { return a < b ? a : b; }

long long minIncrementOperations(int* nums, int numsSize, int k) {
    long long dp0 = 0, dp1 = 0, dp2 = 0;
    for (int i = 0; i < numsSize; i++) {
        long long cost = 0;
        if (nums[i] < k) cost = k - nums[i];
        long long nd0 = cost + min64(dp0, min64(dp1, dp2));
        dp0 = dp1; dp1 = dp2; dp2 = nd0;
    }
    return min64(dp0, min64(dp1, dp2));
}
