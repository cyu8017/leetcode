// LeetCode 2036 - Maximum Alternating Subarray Sum
// https://leetcode.com/problems/maximum-alternating-subarray-sum/

class Solution {
    public long maximumAlternatingSubarraySum(int[] nums) {
        long ans = Long.MIN_VALUE, even = 0, odd = 0;
        for (int i = 0; i < nums.length; i++) {
            long x = nums[i];
            if (i % 2 == 0) even += x;
            else even = Math.max(0L, even - x);
            ans = Math.max(ans, even);
        }
        odd = 0;
        for (int i = 1; i < nums.length; i++) {
            long x = nums[i];
            if (i % 2 == 1) odd += x;
            else odd = Math.max(0L, odd - x);
            ans = Math.max(ans, odd);
        }
        return ans;
    }
}
