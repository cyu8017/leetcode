// LeetCode 1260 - Shift 2D Grid
// https://leetcode.com/problems/shift-2d-grid/

import java.util.*;

class Solution {
    public List<List<Integer>> shiftGrid(int[][] grid, int k) {
        int m = grid.length, n = grid[0].length;
        List<Integer> flat = new ArrayList<>();
        for (int[] row : grid) for (int x : row) flat.add(x);
        k %= flat.size();
        if (k > 0) {
            List<Integer> rotated = new ArrayList<>(flat.subList(flat.size() - k, flat.size()));
            rotated.addAll(flat.subList(0, flat.size() - k));
            flat = rotated;
        }
        List<List<Integer>> answer = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            answer.add(new ArrayList<>(flat.subList(i * n, (i + 1) * n)));
        }
        return answer;
    }
}

