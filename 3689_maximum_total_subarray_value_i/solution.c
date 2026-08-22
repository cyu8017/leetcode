// LeetCode 3689 - Maximum Total Subarray Value I
// https://leetcode.com/problems/maximum-total-subarray-value-i/

long long maxTotalValue(int* nums, int numsSize, int k) {
    int mx = nums[0], mn = nums[0];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] > mx) mx = nums[i];
        if (nums[i] < mn) mn = nums[i];
    }
    return (long long)k * (mx - mn);
}
