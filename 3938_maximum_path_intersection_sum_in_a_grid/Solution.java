// LeetCode 3938 - Maximum Path Intersection Sum in a Grid
// https://leetcode.com/problems/maximum-path-intersection-sum-in-a-grid/

class Solution {
    public int maxPathSum(int[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        int answer = Integer.MIN_VALUE;
        for (int row = 0; row < rows; row++) {
            final int r = row;
            answer = Math.max(answer, checkLine(cols, col -> grid[r][col]));
        }
        for (int col = 0; col < cols; col++) {
            final int c = col;
            answer = Math.max(answer, checkLine(rows, row -> grid[row][c]));
        }
        for (int row = 1; row + 1 < rows; row++) {
            for (int col = 1; col + 1 < cols; col++) {
                if (grid[row][col] > answer) answer = grid[row][col];
            }
        }
        return answer;
    }

    private interface IntAt { int get(int i); }

    private int checkLine(int length, IntAt value) {
        int answer = Integer.MIN_VALUE;
        int bestEnding = value.get(0) + value.get(1);
        if (bestEnding > answer) answer = bestEnding;
        for (int i = 2; i < length; i++) {
            if (value.get(i - 1) + value.get(i) > bestEnding + value.get(i)) bestEnding = value.get(i - 1) + value.get(i);
            else bestEnding += value.get(i);
            if (bestEnding > answer) answer = bestEnding;
        }
        return answer;
    }
}
