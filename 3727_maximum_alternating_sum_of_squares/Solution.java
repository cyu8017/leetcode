// LeetCode 3727 - Maximum Alternating Sum of Squares
// https://leetcode.com/problems/maximum-alternating-sum-of-squares/

import java.util.Arrays;

class Solution {
    public long maxAlternatingSum(int[] nums) {
        for (int i = 0; i < nums.length; i++) nums[i] *= nums[i];
        Arrays.sort(nums);
        int m = nums.length / 2;
        long ans = 0;
        for (int i = 0; i < m; i++) ans -= nums[i];
        for (int i = m; i < nums.length; i++) ans += nums[i];
        return ans;
    }
}
