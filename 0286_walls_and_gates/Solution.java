// LeetCode 0286 - Walls and Gates
// https://leetcode.com/problems/walls-and-gates/

import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    public void wallsAndGates(int[][] rooms) {
        if (rooms.length == 0 || rooms[0].length == 0) {
            return;
        }
        int rows = rooms.length;
        int cols = rooms[0].length;
        Queue<int[]> queue = new ArrayDeque<>();
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (rooms[row][col] == 0) {
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
                int nextRow = row + direction[0];
                int nextCol = col + direction[1];
                if (nextRow >= 0 && nextRow < rows && nextCol >= 0 && nextCol < cols
                        && rooms[nextRow][nextCol] == 2147483647) {
                    rooms[nextRow][nextCol] = rooms[row][col] + 1;
                    queue.offer(new int[] { nextRow, nextCol });
                }
            }
        }
    }
}
