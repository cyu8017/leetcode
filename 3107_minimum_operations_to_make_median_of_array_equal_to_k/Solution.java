// LeetCode 3107 - Minimum Operations to Make Median of Array Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/

import java.util.Arrays;

class Solution {
    public long minOperationsToMakeMedianK(int[] nums, int k) {
        Arrays.sort(nums);
        int n = nums.length, m = n >> 1;
        long ans = Math.abs(nums[m] - k);
        if (nums[m] > k) {
            for (int i = m - 1; i >= 0 && nums[i] > k; i--) ans += nums[i] - k;
        } else {
            for (int i = m + 1; i < n && nums[i] < k; i++) ans += k - nums[i];
        }
        return ans;
    }
}
