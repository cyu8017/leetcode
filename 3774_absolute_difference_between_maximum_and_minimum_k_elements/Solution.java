// LeetCode 3774 - Absolute Difference Between Maximum And Minimum K Elements
// https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/

import java.util.Arrays;

class Solution {
    public int absDifference(int[] nums, int k) {
        Arrays.sort(nums);
        int ans = 0, n = nums.length;
        for (int i = 0; i < k; i++) ans += nums[n - i - 1] - nums[i];
        return ans;
    }
}
