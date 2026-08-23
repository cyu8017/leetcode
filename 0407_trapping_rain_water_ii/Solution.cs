// LeetCode 0407 - Trapping Rain Water II

// https://leetcode.com/problems/trapping-rain-water-ii/



public class Solution {

    public int TrapRainWater(int[][] heightMap) {

        if (heightMap.Length == 0 || heightMap[0].Length == 0) {

            return 0;

        }



        int rows = heightMap.Length;

        int cols = heightMap[0].Length;



        if (rows < 3 || cols < 3) {

            return 0;

        }



        bool[,] visited = new bool[rows, cols];

        PriorityQueue<(int height, int row, int col), int> heap = new();



        for (int row = 0; row < rows; row++) {

            for (int col = 0; col < cols; col++) {

                if (row == 0 || row == rows - 1 || col == 0 || col == cols - 1) {

                    heap.Enqueue((heightMap[row][col], row, col), heightMap[row][col]);

                    visited[row, col] = true;

                }

            }

        }



        int trapped = 0;

        int[][] directions = {

            new[] { 1, 0 },

            new[] { -1, 0 },

            new[] { 0, 1 },

            new[] { 0, -1 },

        };



        while (heap.Count > 0) {

            (int height, int row, int col) = heap.Dequeue();



            foreach (int[] direction in directions) {

                int nextRow = row + direction[0];

                int nextCol = col + direction[1];



                if (nextRow < 0 || nextRow >= rows || nextCol < 0 || nextCol >= cols

                        || visited[nextRow, nextCol]) {

                    continue;

                }



                visited[nextRow, nextCol] = true;

                int nextHeight = heightMap[nextRow][nextCol];

                trapped += int.Max(0, height - nextHeight);

                int boundary = int.Max(height, nextHeight);

                heap.Enqueue((boundary, nextRow, nextCol), boundary);

            }

        }



        return trapped;

    }

}
