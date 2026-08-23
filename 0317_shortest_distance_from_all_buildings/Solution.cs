// LeetCode 0317 - Shortest Distance from All Buildings

// https://leetcode.com/problems/shortest-distance-from-all-buildings/



using System.Collections.Generic;



public class Solution {

    public int ShortestDistance(int[][] grid) {

        if (grid.Length == 0 || grid[0].Length == 0) {

            return -1;

        }



        int rows = grid.Length;

        int cols = grid[0].Length;

        int buildings = 0;

        int[][] distances = new int[rows][];

        int[][] reach = new int[rows][];

        int[][] directions = { new[] { 1, 0 }, new[] { -1, 0 }, new[] { 0, 1 }, new[] { 0, -1 } };

        for (int row = 0; row < rows; row++) {

            distances[row] = new int[cols];

            reach[row] = new int[cols];

        }



        for (int row = 0; row < rows; row++) {

            for (int col = 0; col < cols; col++) {

                if (grid[row][col] == 1) {

                    buildings++;

                }

            }

        }



        for (int row = 0; row < rows; row++) {

            for (int col = 0; col < cols; col++) {

                if (grid[row][col] != 1) {

                    continue;

                }

                Queue<int[]> queue = new();

                queue.Enqueue(new[] { row, col, 0 });

                bool[,] visited = new bool[rows, cols];

                visited[row, col] = true;

                while (queue.Count > 0) {

                    int[] current = queue.Dequeue();

                    int currentRow = current[0];

                    int currentCol = current[1];

                    int distance = current[2];

                    foreach (int[] direction in directions) {

                        int nextRow = currentRow + direction[0];

                        int nextCol = currentCol + direction[1];

                        if (nextRow < 0 || nextRow >= rows || nextCol < 0 || nextCol >= cols) {

                            continue;

                        }

                        if (grid[nextRow][nextCol] != 0 || visited[nextRow, nextCol]) {

                            continue;

                        }

                        visited[nextRow, nextCol] = true;

                        distances[nextRow][nextCol] += distance + 1;

                        reach[nextRow][nextCol]++;

                        queue.Enqueue(new[] { nextRow, nextCol, distance + 1 });

                    }

                }

            }

        }



        int best = int.MaxValue;

        for (int row = 0; row < rows; row++) {

            for (int col = 0; col < cols; col++) {

                if (grid[row][col] == 0 && reach[row][col] == buildings) {

                    best = System.Math.Min(best, distances[row][col]);

                }

            }

        }

        return best == int.MaxValue ? -1 : best;

    }

}

