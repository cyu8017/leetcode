// LeetCode 0764 - Largest Plus Sign
// https://leetcode.com/problems/largest-plus-sign/

import java.util.*;

class Solution {
    public int orderOfLargestPlusSign(int n, int[][] mines) {
        Set<Integer> banned = new HashSet<>();
        for (int[] mine : mines) banned.add(mine[0] * n + mine[1]);
        int[][] arms = new int[n][n];
        int best = 0;
        for (int r = 0; r < n; r++) {
            int count = 0;
            for (int c = 0; c < n; c++) {
                count = banned.contains(r * n + c) ? 0 : count + 1;
                arms[r][c] = count;
            }
            count = 0;
            for (int c = n - 1; c >= 0; c--) {
                count = banned.contains(r * n + c) ? 0 : count + 1;
                arms[r][c] = Math.min(arms[r][c], count);
            }
        }
        for (int c = 0; c < n; c++) {
            int count = 0;
            for (int r = 0; r < n; r++) {
                count = banned.contains(r * n + c) ? 0 : count + 1;
                arms[r][c] = Math.min(arms[r][c], count);
            }
            count = 0;
            for (int r = n - 1; r >= 0; r--) {
                count = banned.contains(r * n + c) ? 0 : count + 1;
                arms[r][c] = Math.min(arms[r][c], count);
                best = Math.max(best, arms[r][c]);
            }
        }
        return best;
    }
}
