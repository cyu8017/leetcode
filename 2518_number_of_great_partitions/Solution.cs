// LeetCode 2518 - Number of Great Partitions
// https://leetcode.com/problems/number-of-great-partitions/

public class Solution {
    public int CountPartitions(int[] nums, int k) {
        const int MOD = 1000000007;
        long sum = 0;
        foreach (int x in nums) sum += x;
        if (sum < 2L * k) return 0;
        int[] dp = new int[k];
        dp[0] = 1;
        foreach (int x in nums) {
            for (int s = k - 1; s >= x; s--)
                dp[s] = (dp[s] + dp[s - x]) % MOD;
        }
        int bad = 0;
        foreach (int v in dp) bad = (bad + v) % MOD;
        int total = 1;
        for (int i = 0; i < nums.Length; i++) total = total * 2 % MOD;
        return (int)((total - 2L * bad % MOD + MOD) % MOD);
    }
}
