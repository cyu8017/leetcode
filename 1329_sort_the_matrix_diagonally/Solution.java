// LeetCode 1329 - Sort The Matrix Diagonally
// https://leetcode.com/problems/sort-the-matrix-diagonally/

import java.util.*;

class Solution {
    public int[][] diagonalSort(int[][] mat) {
        Map<Integer, List<Integer>> diagonals = new HashMap<>();
        for (int r = 0; r < mat.length; r++) {
            for (int c = 0; c < mat[r].length; c++) {
                diagonals.computeIfAbsent(r - c, k -> new ArrayList<>()).add(mat[r][c]);
            }
        }
        for (List<Integer> values : diagonals.values()) {
            values.sort(Collections.reverseOrder());
        }
        for (int r = 0; r < mat.length; r++) {
            for (int c = 0; c < mat[r].length; c++) {
                List<Integer> list = diagonals.get(r - c);
                mat[r][c] = list.remove(list.size() - 1);
            }
        }
        return mat;
    }
}
