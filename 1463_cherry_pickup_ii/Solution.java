// LeetCode 1463 - Cherry Pickup Ii
// https://leetcode.com/problems/cherry-pickup-ii/

import java.util.*;

class Solution {
    public int cherryPickup(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        Map<Long, Integer> dp = new HashMap<>();
        dp.put(key(0, n - 1), grid[0][0] + (n > 1 ? grid[0][n - 1] : 0));
        for (int r = 1; r < m; r++) {
            Map<Long, Integer> nxt = new HashMap<>();
            for (Map.Entry<Long, Integer> e : dp.entrySet()) {
                long k = e.getKey();
                int a = (int) (k >> 32), b = (int) k, score = e.getValue();
                for (int na = a - 1; na <= a + 1; na++) {
                    for (int nb = b - 1; nb <= b + 1; nb++) {
                        if (na < 0 || na >= n || nb < 0 || nb >= n) continue;
                        int val = score + grid[r][na] + (na != nb ? grid[r][nb] : 0);
                        long nk = key(na, nb);
                        nxt.merge(nk, val, Math::max);
                    }
                }
            }
            dp = nxt;
        }
        int ans = 0;
        for (int v : dp.values()) ans = Math.max(ans, v);
        return ans;
    }

    private long key(int a, int b) {
        return ((long) a << 32) | (b & 0xffffffffL);
    }
}
