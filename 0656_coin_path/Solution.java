// LeetCode 0656 - Coin Path
// https://leetcode.com/problems/coin-path/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class Solution {
    public List<Integer> cheapestJump(int[] coins, int maxJump) {
        int n = coins.length;
        if (coins[n - 1] == -1) {
            return Collections.emptyList();
        }
        long inf = Long.MAX_VALUE / 4;
        long[] cost = new long[n];
        Arrays.fill(cost, inf);
        int[] nxt = new int[n];
        Arrays.fill(nxt, -1);
        cost[n - 1] = coins[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            if (coins[i] == -1) {
                continue;
            }
            for (int jump = 1; jump <= maxJump; ++jump) {
                int j = i + jump;
                if (j >= n) {
                    break;
                }
                if (cost[j] == inf) {
                    continue;
                }
                long candidate = coins[i] + cost[j];
                if (candidate < cost[i] || (candidate == cost[i] && (nxt[i] == -1 || j < nxt[i]))) {
                    cost[i] = candidate;
                    nxt[i] = j;
                }
            }
        }
        if (cost[0] == inf) {
            return Collections.emptyList();
        }
        List<Integer> path = new ArrayList<>();
        path.add(1);
        int i = 0;
        while (i != n - 1) {
            i = nxt[i];
            path.add(i + 1);
        }
        return path;
    }
}
