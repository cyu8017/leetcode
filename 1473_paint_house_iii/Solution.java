// LeetCode 1473 - Paint House Iii
// https://leetcode.com/problems/paint-house-iii/

import java.util.*;

class Solution {
    public int minCost(int[] houses, int[][] cost, int m, int n, int target) {
        long inf = (long) 1e15;
        Map<Long, Long> dp = new HashMap<>();
        dp.put(key(0, 0), 0L);
        for (int i = 0; i < m; i++) {
            Map<Long, Long> nxt = new HashMap<>();
            int painted = houses[i];
            int[] colors;
            if (painted != 0) colors = new int[]{painted};
            else {
                colors = new int[n];
                for (int c = 1; c <= n; c++) colors[c - 1] = c;
            }
            for (Map.Entry<Long, Long> e : dp.entrySet()) {
                long k = e.getKey();
                int prev = (int) (k >> 32), groups = (int) k;
                long value = e.getValue();
                for (int color : colors) {
                    int ng = groups + (color != prev ? 1 : 0);
                    if (ng <= target) {
                        long nv = value + (painted != 0 ? 0 : cost[i][color - 1]);
                        nxt.merge(key(color, ng), nv, Math::min);
                    }
                }
            }
            dp = nxt;
        }
        long ans = inf;
        for (Map.Entry<Long, Long> e : dp.entrySet()) {
            if ((int) e.getKey() == target) ans = Math.min(ans, e.getValue());
        }
        return ans == inf ? -1 : (int) ans;
    }

    private long key(int color, int groups) {
        return ((long) color << 32) | (groups & 0xffffffffL);
    }
}
