// LeetCode 2826 - Sorting Three Groups
// https://leetcode.com/problems/sorting-three-groups/

import java.util.Arrays;
import java.util.List;

class Solution {
    public int minimumOperations(List<Integer> nums) {
        int n = nums.size();
        final int INF = 1 << 30;
        int[][] dp = new int[n + 1][4];
        for (int i = 0; i <= n; i++) Arrays.fill(dp[i], INF);
        dp[0][1] = dp[0][2] = dp[0][3] = 0;
        for (int i = 1; i <= n; i++) {
            int v = nums.get(i - 1);
            for (int g = 1; g <= 3; g++) {
                int cost = (v != g) ? 1 : 0;
                for (int prev = 1; prev <= g; prev++)
                    dp[i][g] = Math.min(dp[i][g], dp[i - 1][prev] + cost);
            }
        }
        return Math.min(dp[n][1], Math.min(dp[n][2], dp[n][3]));
    }
}
