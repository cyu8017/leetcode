// LeetCode 3592 - Inverse Coin Change
// https://leetcode.com/problems/inverse-coin-change/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] findCoins(int[] numWays) {
        int n = numWays.length;
        int[] dp = new int[n + 1];
        var coins = new ArrayList<Integer>();
        dp[0] = 1;
        for (int amt = 1; amt <= n; amt++) {
            int ways = numWays[amt - 1];
            if (dp[amt] == ways) continue;
            if (dp[amt] + 1 == ways) {
                coins.add(amt);
                for (int x = amt; x <= n; x++) dp[x] += dp[x - amt];
                if (dp[amt] != ways) return new int[0];
                continue;
            }
            return new int[0];
        }
        return coins.stream().mapToInt(Integer::intValue).toArray();
    }
}
