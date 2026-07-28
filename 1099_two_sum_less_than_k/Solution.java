// LeetCode 1099 - Two Sum Less Than K
// https://leetcode.com/problems/two-sum-less-than-k/

import java.util.Arrays;

class Solution {
    public int twoSumLessThanK(int[] nums, int k) {
        Arrays.sort(nums);
        int lo = 0, hi = nums.length - 1;
        int ans = -1;
        while (lo < hi) {
            int total = nums[lo] + nums[hi];
            if (total < k) {
                ans = Math.max(ans, total);
                lo++;
            } else {
                hi--;
            }
        }
        return ans;
    }
}
