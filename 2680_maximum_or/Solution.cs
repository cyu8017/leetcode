// LeetCode 2680 - Maximum OR
// https://leetcode.com/problems/maximum-or/

public class Solution {
    public long MaximumOr(int[] nums, int k) {
        int n = nums.Length;
        long[] pref = new long[n + 1], suf = new long[n + 1];
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] | (uint)nums[i];
        for (int i = n - 1; i >= 0; i--) suf[i] = suf[i + 1] | (uint)nums[i];
        long ans = 0;
        for (int i = 0; i < n; i++) {
            long cur = pref[i] | ((long)nums[i] << k) | suf[i + 1];
            if (cur > ans) ans = cur;
        }
        return ans;
    }
}
