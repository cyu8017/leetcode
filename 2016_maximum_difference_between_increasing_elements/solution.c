// LeetCode 2016 - Maximum Difference Between Increasing Elements
// https://leetcode.com/problems/maximum-difference-between-increasing-elements/

int maximumDifference(int* nums, int numsSize) {
    int ans = -1, mn = nums[0];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] > mn) {
            if (nums[i] - mn > ans) ans = nums[i] - mn;
        } else mn = nums[i];
    }
    return ans;
}
