// LeetCode 1931 - Painting a Grid With Three Different Colors
// https://leetcode.com/problems/painting-a-grid-with-three-different-colors/

import java.util.*;

class Solution {
    static final int MOD = 1_000_000_007;
    int m, n;
    List<Integer> states = new ArrayList<>();
    Map<Integer, List<Integer>> compat = new HashMap<>();
    Map<Long, Integer> memo = new HashMap<>();

    public int colorTheGrid(int m, int n) {
        this.m = m;
        this.n = n;
        int total = (int) Math.pow(3, m);
        for (int s = 0; s < total; s++) if (validColumn(s)) states.add(s);
        for (int a : states) {
            List<Integer> list = new ArrayList<>();
            int[] ca = colors(a);
            for (int b : states) {
                int[] cb = colors(b);
                boolean ok = true;
                for (int i = 0; i < m; i++) if (ca[i] == cb[i]) { ok = false; break; }
                if (ok) list.add(b);
            }
            compat.put(a, list);
        }
        return dp(0, -1);
    }

    private int dp(int col, int prev) {
        if (col == n) return 1;
        long key = ((long) col << 20) | (prev + 1);
        if (memo.containsKey(key)) return memo.get(key);
        int total = 0;
        List<Integer> cands = prev == -1 ? states : compat.get(prev);
        for (int cur : cands) total = (total + dp(col + 1, cur)) % MOD;
        memo.put(key, total);
        return total;
    }

    private boolean validColumn(int mask) {
        int prev = -1;
        for (int i = 0; i < m; i++) {
            int c = mask % 3;
            if (c == prev) return false;
            prev = c;
            mask /= 3;
        }
        return true;
    }

    private int[] colors(int mask) {
        int[] cols = new int[m];
        for (int i = 0; i < m; i++) {
            cols[i] = mask % 3;
            mask /= 3;
        }
        return cols;
    }
}
