// LeetCode 1155 - Number of Dice Rolls With Target Sum
// https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

class Solution {
    public int numRollsToTarget(int n, int k, int target) {
        final int MOD = 1_000_000_007;
        int[] dp = new int[target + 1];
        dp[0] = 1;
        for (int dice = 0; dice < n; dice++) {
            int[] next = new int[target + 1];
            for (int s = 0; s <= target; s++) {
                if (dp[s] == 0) continue;
                for (int face = 1; face <= k && s + face <= target; face++) {
                    next[s + face] = (next[s + face] + dp[s]) % MOD;
                }
            }
            dp = next;
        }
        return dp[target];
    }
}
