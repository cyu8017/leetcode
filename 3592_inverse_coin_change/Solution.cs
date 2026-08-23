// LeetCode 3592 - Inverse Coin Change
// https://leetcode.com/problems/inverse-coin-change/

using System.Collections.Generic;

public class Solution {
    public int[] FindCoins(int[] numWays) {
        int n = numWays.Length;
        int[] dp = new int[n + 1];
        var coins = new List<int>();
        dp[0] = 1;
        for (int amt = 1; amt <= n; amt++) {
            int ways = numWays[amt - 1];
            if (dp[amt] == ways) continue;
            if (dp[amt] + 1 == ways) {
                coins.Add(amt);
                for (int x = amt; x <= n; x++) dp[x] += dp[x - amt];
                if (dp[amt] != ways) return new int[0];
                continue;
            }
            return new int[0];
        }
        return coins.ToArray();
    }
}
