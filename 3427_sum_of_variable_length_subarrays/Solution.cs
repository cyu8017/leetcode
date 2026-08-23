// LeetCode 3427 - Sum of Variable Length Subarrays
// https://leetcode.com/problems/sum-of-variable-length-subarrays/

public class Solution {
    public int SubarraySum(int[] nums) {
        int n = nums.Length;
        int[] pref = new int[n + 1];
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int start = i - nums[i];
            if (start < 0) start = 0;
            ans += pref[i + 1] - pref[start];
        }
        return ans;
    }
}
