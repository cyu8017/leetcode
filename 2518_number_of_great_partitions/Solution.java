// LeetCode 2518 - Number of Great Partitions
// https://leetcode.com/problems/number-of-great-partitions/

class Solution {
    public int countPartitions(int[] nums, int k) {
        final int MOD = 1000000007;
        long sum = 0;
        for (int x : nums) sum += x;
        if (sum < 2L * k) return 0;
        int[] dp = new int[k];
        dp[0] = 1;
        for (int x : nums) {
            for (int s = k - 1; s >= x; s--)
                dp[s] = (dp[s] + dp[s - x]) % MOD;
        }
        int bad = 0;
        for (int v : dp) bad = (bad + v) % MOD;
        int total = 1;
        for (int i = 0; i < nums.length; i++) total = total * 2 % MOD;
        return (int)((total - 2L * bad % MOD + MOD) % MOD);
    }
}
