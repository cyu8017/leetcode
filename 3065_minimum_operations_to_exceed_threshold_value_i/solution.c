// LeetCode 3065 - Minimum Operations to Exceed Threshold Value I
// https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/

int minOperations(int* nums, int numsSize, int k) {
    int ans = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] < k) ans++;
    return ans;
}
