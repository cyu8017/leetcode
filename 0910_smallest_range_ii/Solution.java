// LeetCode 0910 - Smallest Range II
// https://leetcode.com/problems/smallest-range-ii/

import java.util.Arrays;

class Solution {
    public int smallestRangeII(int[] nums, int k) {
        Arrays.sort(nums);
        int ans = nums[nums.length - 1] - nums[0];
        for (int i = 0; i + 1 < nums.length; i++) {
            int lo = Math.min(nums[0] + k, nums[i + 1] - k);
            int hi = Math.max(nums[nums.length - 1] - k, nums[i] + k);
            ans = Math.min(ans, hi - lo);
        }
        return ans;
    }
}
