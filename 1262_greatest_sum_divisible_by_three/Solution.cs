// LeetCode 1262 - Greatest Sum Divisible by Three
// https://leetcode.com/problems/greatest-sum-divisible-by-three/

public class Solution {
    public int MaxSumDivThree(int[] nums) {
        const long impossible = -1000000000000000000L;
        long[] dp = { 0, impossible, impossible };
        foreach (int value in nums) {
            long[] old = (long[])dp.Clone();
            for (int total = 0; total < 3; total++) {
                if (old[total] != impossible) {
                    int remainder = (int)((old[total] + value) % 3);
                    dp[remainder] = System.Math.Max(dp[remainder], old[total] + value);
                }
            }
        }
        return (int)dp[0];
    }
}
