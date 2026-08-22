// LeetCode 3512 - Minimum Operations to Make Array Sum Divisible by K
// https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/

int minOperations(int* nums, int numsSize, int k) {
    long long s = 0;
    for (int i = 0; i < numsSize; i++) s += nums[i];
    return (int)(s % k);
}
