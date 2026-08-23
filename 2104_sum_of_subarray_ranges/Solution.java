// LeetCode 2104 - Sum of Subarray Ranges
// https://leetcode.com/problems/sum-of-subarray-ranges/

class Solution {
    public long subArrayRanges(int[] nums) {
        int n = nums.length;
        long ans = 0;
        for (int i = 0; i < n; i++) {
            int mn = nums[i], mx = nums[i];
            for (int j = i; j < n; j++) {
                mn = Math.min(mn, nums[j]);
                mx = Math.max(mx, nums[j]);
                ans += mx - mn;
            }
        }
        return ans;
    }
}
