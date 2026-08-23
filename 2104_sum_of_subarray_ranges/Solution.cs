// LeetCode 2104 - Sum of Subarray Ranges
// https://leetcode.com/problems/sum-of-subarray-ranges/

public class Solution {
    public long SubArrayRanges(int[] nums) {
        int n = nums.Length;
        long ans = 0;
        for (int i = 0; i < n; i++) {
            int mn = nums[i], mx = nums[i];
            for (int j = i; j < n; j++) {
                mn = Math.Min(mn, nums[j]);
                mx = Math.Max(mx, nums[j]);
                ans += mx - mn;
            }
        }
        return ans;
    }
}
