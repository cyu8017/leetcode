// LeetCode 3446 - Sort Matrix by Diagonals
// https://leetcode.com/problems/sort-matrix-by-diagonals/

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int[][] sortMatrix(int[][] grid) {
        int n = grid.length;
        Map<Integer, List<Integer>> diags = new HashMap<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                diags.computeIfAbsent(i - j, k -> new ArrayList<>()).add(grid[i][j]);
            }
        }
        for (Map.Entry<Integer, List<Integer>> e : diags.entrySet()) {
            if (e.getKey() >= 0) e.getValue().sort(Collections.reverseOrder());
            else Collections.sort(e.getValue());
        }
        Map<Integer, Integer> idx = new HashMap<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int k = i - j;
                int pos = idx.getOrDefault(k, 0);
                grid[i][j] = diags.get(k).get(pos);
                idx.put(k, pos + 1);
            }
        }
        return grid;
    }
}
