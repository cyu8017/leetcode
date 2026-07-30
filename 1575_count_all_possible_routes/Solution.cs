// LeetCode 1575 - Count All Possible Routes
// https://leetcode.com/problems/count-all-possible-routes/

using System;

public class Solution {
    public int CountRoutes(int[] locations, int start, int finish, int fuel) {
        const int MOD = 1000000007;
        int n = locations.Length;
        int[,] memo = new int[n, fuel + 1];
        for (int i = 0; i < n; i++)
            for (int j = 0; j <= fuel; j++)
                memo[i, j] = -1;

        int Dp(int city, int left) {
            if (memo[city, left] != -1) return memo[city, left];
            long total = city == finish ? 1 : 0;
            for (int nxt = 0; nxt < n; nxt++) {
                int cost = Math.Abs(locations[city] - locations[nxt]);
                if (nxt != city && cost <= left)
                    total += Dp(nxt, left - cost);
            }
            return memo[city, left] = (int)(total % MOD);
        }
        return Dp(start, fuel);
    }
}
