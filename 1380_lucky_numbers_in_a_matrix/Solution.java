// LeetCode 1380 - Lucky Numbers In A Matrix
// https://leetcode.com/problems/lucky-numbers-in-a-matrix/

import java.util.*;

class Solution {
    public List<Integer> luckyNumbers(int[][] matrix) {
        Set<Integer> mins = new HashSet<>();
        for (int[] row : matrix) {
            int m = row[0];
            for (int v : row) m = Math.min(m, v);
            mins.add(m);
        }
        Set<Integer> maxs = new HashSet<>();
        for (int c = 0; c < matrix[0].length; c++) {
            int m = matrix[0][c];
            for (int[] row : matrix) m = Math.max(m, row[c]);
            maxs.add(m);
        }
        mins.retainAll(maxs);
        return new ArrayList<>(mins);
    }
}
