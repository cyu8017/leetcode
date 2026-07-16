// LeetCode 0542 - 01 Matrix
// https://leetcode.com/problems/01-matrix/

using System.Collections.Generic;

public class Solution {
    public int[][] UpdateMatrix(int[][] mat) {
        int rows = mat.Length;
        int cols = mat[0].Length;
        int[][] dist = new int[rows][];
        Queue<int[]> queue = new Queue<int[]>();

        for (int row = 0; row < rows; row++) {
            dist[row] = new int[cols];
            for (int col = 0; col < cols; col++) {
                dist[row][col] = 1_000_000_000;
                if (mat[row][col] == 0) {
                    dist[row][col] = 0;
                    queue.Enqueue(new int[] { row, col });
                }
            }
        }

        int[][] directions = new int[][] {
            new int[] { 1, 0 },
            new int[] { -1, 0 },
            new int[] { 0, 1 },
            new int[] { 0, -1 },
        };

        while (queue.Count > 0) {
            int[] cell = queue.Dequeue();
            int row = cell[0];
            int col = cell[1];
            foreach (int[] direction in directions) {
                int nr = row + direction[0];
                int nc = col + direction[1];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols
                        && dist[nr][nc] > dist[row][col] + 1) {
                    dist[nr][nc] = dist[row][col] + 1;
                    queue.Enqueue(new int[] { nr, nc });
                }
            }
        }

        return dist;
    }
}
