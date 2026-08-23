// LeetCode 3250 - Find the Count of Monotonic Pairs I
// https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i/

public class Solution {
    public int CountOfPairs(int[] nums) {
        const int mod = 1000000007;
        int n = nums.Length;
        int[] dp = new int[51];
        for (int a = 0; a <= nums[0]; a++) dp[a] = 1;
        for (int i = 1; i < n; i++) {
            int[] ndp = new int[51];
            int[] pref = new int[52];
            for (int a = 0; a <= 50; a++) pref[a + 1] = (pref[a] + dp[a]) % mod;
            for (int a2 = 0; a2 <= nums[i]; a2++) {
                int b2 = nums[i] - a2;
                int maxA1 = a2;
                int lim = nums[i - 1] - b2;
                if (lim < maxA1) maxA1 = lim;
                if (maxA1 < 0) continue;
                if (maxA1 > 50) maxA1 = 50;
                ndp[a2] = pref[maxA1 + 1];
            }
            dp = ndp;
        }
        int ans = 0;
        foreach (int v in dp) ans = (ans + v) % mod;
        return ans;
    }
}
