// LeetCode 3381 - Maximum Subarray Sum With Length Divisible by K
// https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

class Solution {
    public long maxSubarraySum(int[] nums, int k) {
        int n = nums.length;
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
        final long INF = 1L << 62;
        long[] best = new long[k];
        for (int i = 0; i < k; i++) best[i] = INF;
        best[0] = 0;
        long ans = -(1L << 62);
        for (int i = 1; i <= n; i++) {
            int r = i % k;
            if (best[r] != INF) {
                long cand = pref[i] - best[r];
                if (cand > ans) ans = cand;
            }
            if (pref[i] < best[r]) best[r] = pref[i];
        }
        return ans;
    }
}
