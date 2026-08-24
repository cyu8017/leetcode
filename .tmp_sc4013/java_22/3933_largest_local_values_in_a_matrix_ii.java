// CONFIG class=Solution method=countLocalMaximums types=None
// LeetCode 3933 - Largest Local Values in a Matrix II
// https://leetcode.com/problems/largest-local-values-in-a-matrix-ii/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int countLocalMaximums(int[][] matrix) {
        int rows = matrix.length, cols = matrix[0].length;
        List<int[]>[] positions = new ArrayList[201];
        for (int i = 0; i < 201; i++) positions[i] = new ArrayList<>();
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                int value = matrix[row][col];
                if (value > 0) positions[value].add(new int[] { row, col });
            }
        }
        int answer = 0;
        for (int value = 1; value <= 200; value++) {
            if (positions[value].isEmpty()) continue;
            int[][] prefix = new int[rows + 1][cols + 1];
            for (int row = 0; row < rows; row++) {
                for (int col = 0; col < cols; col++) {
                    int add = matrix[row][col] > value ? 1 : 0;
                    prefix[row + 1][col + 1] = prefix[row][col + 1] + prefix[row + 1][col] - prefix[row][col] + add;
                }
            }
            for (int[] pos : positions[value]) {
                int row = pos[0], col = pos[1];
                int top = Math.max(0, row - value), bottom = Math.min(rows - 1, row + value);
                int left = Math.max(0, col - value), right = Math.min(cols - 1, col + value);
                int greater = prefix[bottom + 1][right + 1] - prefix[top][right + 1] - prefix[bottom + 1][left] + prefix[top][left];
                for (int dr : new int[] { -value, value }) {
                    for (int dc : new int[] { -value, value }) {
                        int rr = row + dr, cc = col + dc;
                        if (rr >= 0 && rr < rows && cc >= 0 && cc < cols && matrix[rr][cc] > value) greater--;
                    }
                }
                if (greater == 0) answer++;
            }
        }
        return answer;
    }
}
