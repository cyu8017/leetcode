// LeetCode 3251 - Find the Count of Monotonic Pairs II
// https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/

class Solution {
    public int countOfPairs(int[] nums) {
        final int mod = 1000000007;
        int n = nums.length;
        int maxV = 0;
        for (int v : nums) maxV = Math.max(maxV, v);
        int[] dp = new int[maxV + 1];
        for (int a = 0; a <= nums[0]; a++) dp[a] = 1;
        for (int i = 1; i < n; i++) {
            int[] ndp = new int[maxV + 1];
            int[] pref = new int[maxV + 2];
            for (int a = 0; a <= maxV; a++) pref[a + 1] = (pref[a] + dp[a]) % mod;
            for (int a2 = 0; a2 <= nums[i]; a2++) {
                int b2 = nums[i] - a2;
                int maxA1 = a2;
                int lim = nums[i - 1] - b2;
                if (lim < maxA1) maxA1 = lim;
                if (maxA1 < 0) continue;
                if (maxA1 > maxV) maxA1 = maxV;
                ndp[a2] = pref[maxA1 + 1];
            }
            dp = ndp;
        }
        int ans = 0;
        for (int v : dp) ans = (ans + v) % mod;
        return ans;
    }
}
