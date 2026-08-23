// LeetCode 2680 - Maximum OR
// https://leetcode.com/problems/maximum-or/

class Solution {
    public long maximumOr(int[] nums, int k) {
        int n = nums.length;
        long[] pref = new long[n + 1], suf = new long[n + 1];
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] | (nums[i] & 0xffffffffL);
        for (int i = n - 1; i >= 0; i--) suf[i] = suf[i + 1] | (nums[i] & 0xffffffffL);
        long ans = 0;
        for (int i = 0; i < n; i++) {
            long cur = pref[i] | (((long) nums[i]) << k) | suf[i + 1];
            if (cur > ans) ans = cur;
        }
        return ans;
    }
}
