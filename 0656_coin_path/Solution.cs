// LeetCode 0656 - Coin Path
// https://leetcode.com/problems/coin-path/

using System.Collections.Generic;

public class Solution {
    public IList<int> CheapestJump(int[] coins, int maxJump) {
        int n = coins.Length;
        if (coins[n - 1] == -1) return new List<int>();
        const long inf = long.MaxValue / 4;
        long[] cost = new long[n];
        int[] nxt = new int[n];
        for (int i = 0; i < n; ++i) {
            cost[i] = inf;
            nxt[i] = -1;
        }
        cost[n - 1] = coins[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            if (coins[i] == -1) continue;
            for (int jump = 1; jump <= maxJump; ++jump) {
                int j = i + jump;
                if (j >= n) break;
                if (cost[j] == inf) continue;
                long candidate = coins[i] + cost[j];
                if (candidate < cost[i] || (candidate == cost[i] && (nxt[i] == -1 || j < nxt[i]))) {
                    cost[i] = candidate;
                    nxt[i] = j;
                }
            }
        }
        if (cost[0] == inf) return new List<int>();
        var path = new List<int> { 1 };
        int cur = 0;
        while (cur != n - 1) {
            cur = nxt[cur];
            path.Add(cur + 1);
        }
        return path;
    }
}
