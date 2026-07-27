// LeetCode 1659 - Maximize Grid Happiness
// https://leetcode.com/problems/maximize-grid-happiness/

class Solution {
    private int states;
    private int n;
    private int[] intro;
    private int[] extro;
    private int[] row;
    private int[][] compat;
    private int[] memo;
    private boolean[] seen;
    private int introMax;
    private int extroMax;

    public int getMaxGridHappiness(int m, int n, int introvertsCount, int extrovertsCount) {
        this.n = n;
        this.introMax = introvertsCount;
        this.extroMax = extrovertsCount;
        states = 1;
        for (int i = 0; i < n; i++) {
            states *= 3;
        }
        int[][] cells = new int[states][n];
        intro = new int[states];
        extro = new int[states];
        row = new int[states];
        for (int s = 0; s < states; s++) {
            int x = s;
            for (int j = 0; j < n; j++) {
                cells[s][j] = x % 3;
                x /= 3;
            }
            int val = 0;
            for (int j = 0; j < n; j++) {
                int z = cells[s][j];
                if (z == 1) {
                    intro[s]++;
                    val += 120;
                } else if (z == 2) {
                    extro[s]++;
                    val += 40;
                }
            }
            for (int j = 1; j < n; j++) {
                val += pairCost(cells[s][j - 1], cells[s][j]);
            }
            row[s] = val;
        }
        compat = new int[states][states];
        for (int a = 0; a < states; a++) {
            for (int b = 0; b < states; b++) {
                int v = 0;
                for (int j = 0; j < n; j++) {
                    v += pairCost(cells[a][j], cells[b][j]);
                }
                compat[a][b] = v;
            }
        }
        int size = (m + 1) * states * (introvertsCount + 1) * (extrovertsCount + 1);
        memo = new int[size];
        seen = new boolean[size];
        return dfs(0, 0, introvertsCount, extrovertsCount, m);
    }

    private int dfs(int r, int prev, int i, int e, int m) {
        if (r == m) {
            return 0;
        }
        int id = (((r * states + prev) * (introMax + 1) + i) * (extroMax + 1)) + e;
        if (seen[id]) {
            return memo[id];
        }
        int best = 0;
        for (int s = 0; s < states; s++) {
            if (intro[s] > i || extro[s] > e) {
                continue;
            }
            best = Math.max(best, row[s] + compat[prev][s] + dfs(r + 1, s, i - intro[s], e - extro[s], m));
        }
        seen[id] = true;
        memo[id] = best;
        return best;
    }

    private int pairCost(int a, int b) {
        if (a == 0 || b == 0) {
            return 0;
        }
        return (a == 1 ? -30 : 20) + (b == 1 ? -30 : 20);
    }
}
