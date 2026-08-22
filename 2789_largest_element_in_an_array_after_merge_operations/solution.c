// LeetCode 2789 - Largest Element in an Array after Merge Operations
// https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/

long long maxArrayValue(int* nums, int numsSize) {
    long long cur = nums[numsSize - 1], ans = cur;
    for (int i = numsSize - 2; i >= 0; i--) {
        if (nums[i] <= cur) cur += nums[i];
        else cur = nums[i];
        if (cur > ans) ans = cur;
    }
    return ans;
}
