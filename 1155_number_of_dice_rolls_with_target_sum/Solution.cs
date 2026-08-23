// LeetCode 1155 - Number of Dice Rolls With Target Sum
// https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

public class Solution {
    public int NumRollsToTarget(int n, int k, int target) {
        const int MOD = 1000000007;
        int[] dp = new int[target + 1];
        dp[0] = 1;
        for (int dice = 0; dice < n; dice++) {
            int[] neu = new int[target + 1];
            for (int s = 0; s <= target; s++) {
                if (dp[s] == 0) continue;
                for (int face = 1; face <= k; face++) {
                    if (s + face <= target) neu[s + face] = (neu[s + face] + dp[s]) % MOD;
                }
            }
            dp = neu;
        }
        return dp[target];
    }
}
