// LeetCode 0296 - Best Meeting Point
// https://leetcode.com/problems/best-meeting-point/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public int minTotalDistance(int[][] grid) {
        List<Integer> rows = new ArrayList<>();
        List<Integer> cols = new ArrayList<>();
        for (int rowIndex = 0; rowIndex < grid.length; rowIndex++) {
            for (int colIndex = 0; colIndex < grid[rowIndex].length; colIndex++) {
                if (grid[rowIndex][colIndex] == 1) {
                    rows.add(rowIndex);
                    cols.add(colIndex);
                }
            }
        }
        Collections.sort(cols);
        int rowMedian = rows.get(rows.size() / 2);
        int colMedian = cols.get(cols.size() / 2);
        int total = 0;
        for (int row : rows) {
            total += Math.abs(row - rowMedian);
        }
        for (int col : cols) {
            total += Math.abs(col - colMedian);
        }
        return total;
    }
}
