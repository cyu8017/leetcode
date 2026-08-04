// LeetCode 1262 - Greatest Sum Divisible by Three
// https://leetcode.com/problems/greatest-sum-divisible-by-three/

class Solution {
    public int maxSumDivThree(int[] nums) {
        long impossible = -1_000_000_000_000_000_000L;
        long[] dp = {0, impossible, impossible};
        for (int value : nums) {
            long[] old = dp.clone();
            for (int total = 0; total < 3; total++) {
                if (old[total] != impossible) {
                    int remainder = (int) ((old[total] + value) % 3);
                    dp[remainder] = Math.max(dp[remainder], old[total] + value);
                }
            }
        }
        return (int) dp[0];
    }
}
