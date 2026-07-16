// LeetCode 0542 - 01 Matrix
// https://leetcode.com/problems/01-matrix/

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;

class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int rows = mat.length;
        int cols = mat[0].length;
        int[][] dist = new int[rows][cols];
        Queue<int[]> queue = new ArrayDeque<>();

        for (int row = 0; row < rows; row++) {
            Arrays.fill(dist[row], 1_000_000_000);
            for (int col = 0; col < cols; col++) {
                if (mat[row][col] == 0) {
                    dist[row][col] = 0;
                    queue.offer(new int[] { row, col });
                }
            }
        }

        int[][] directions = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int row = cell[0];
            int col = cell[1];
            for (int[] direction : directions) {
                int nr = row + direction[0];
                int nc = col + direction[1];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols
                        && dist[nr][nc] > dist[row][col] + 1) {
                    dist[nr][nc] = dist[row][col] + 1;
                    queue.offer(new int[] { nr, nc });
                }
            }
        }

        return dist;
    }
}
