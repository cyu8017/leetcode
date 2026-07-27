// LeetCode 1632 - Rank Transform of a Matrix
// https://leetcode.com/problems/rank-transform-of-a-matrix/

import java.util.*;

class Solution {
    public int[][] matrixRankTransform(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        Map<Integer, List<int[]>> groups = new TreeMap<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                groups.computeIfAbsent(matrix[i][j], k -> new ArrayList<>()).add(new int[] {i, j});
            }
        }
        int[] rank = new int[m + n];
        int[][] ans = new int[m][n];
        for (List<int[]> cells : groups.values()) {
            Map<Integer, Integer> parent = new HashMap<>();
            for (int[] cell : cells) {
                int a = find(parent, cell[0]);
                int b = find(parent, m + cell[1]);
                parent.put(a, b);
            }
            Map<Integer, Integer> best = new HashMap<>();
            for (int[] cell : cells) {
                int root = find(parent, cell[0]);
                best.put(root, Math.max(best.getOrDefault(root, 0),
                        Math.max(rank[cell[0]], rank[m + cell[1]])));
            }
            for (int[] cell : cells) {
                int r = best.get(find(parent, cell[0])) + 1;
                ans[cell[0]][cell[1]] = r;
            }
            for (int[] cell : cells) {
                int i = cell[0], j = cell[1];
                rank[i] = Math.max(rank[i], ans[i][j]);
                rank[m + j] = Math.max(rank[m + j], ans[i][j]);
            }
        }
        return ans;
    }

    private int find(Map<Integer, Integer> parent, int x) {
        parent.putIfAbsent(x, x);
        if (!parent.get(x).equals(x)) parent.put(x, find(parent, parent.get(x)));
        return parent.get(x);
    }
}
