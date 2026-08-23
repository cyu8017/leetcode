// LeetCode 0286 - Walls and Gates
// https://leetcode.com/problems/walls-and-gates/

using System.Collections.Generic;

public class Solution {
    public void WallsAndGates(int[][] rooms) {
        if (rooms.Length == 0 || rooms[0].Length == 0) {
            return;
        }
        int rows = rooms.Length;
        int cols = rooms[0].Length;
        Queue<int[]> queue = new();
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (rooms[row][col] == 0) {
                    queue.Enqueue(new[] { row, col });
                }
            }
        }
        int[][] directions = { new[] { 1, 0 }, new[] { -1, 0 }, new[] { 0, 1 }, new[] { 0, -1 } };
        while (queue.Count > 0) {
            int[] cell = queue.Dequeue();
            int row = cell[0];
            int col = cell[1];
            foreach (int[] direction in directions) {
                int nextRow = row + direction[0];
                int nextCol = col + direction[1];
                if (nextRow >= 0 && nextRow < rows && nextCol >= 0 && nextCol < cols
                        && rooms[nextRow][nextCol] == 2147483647) {
                    rooms[nextRow][nextCol] = rooms[row][col] + 1;
                    queue.Enqueue(new[] { nextRow, nextCol });
                }
            }
        }
    }
}
