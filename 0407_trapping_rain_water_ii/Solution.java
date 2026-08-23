// LeetCode 0407 - Trapping Rain Water II

// https://leetcode.com/problems/trapping-rain-water-ii/



import java.util.Comparator;

import java.util.PriorityQueue;



class Solution {

    public int trapRainWater(int[][] heightMap) {

        if (heightMap.length == 0 || heightMap[0].length == 0) {

            return 0;

        }



        int rows = heightMap.length;

        int cols = heightMap[0].length;



        if (rows < 3 || cols < 3) {

            return 0;

        }



        boolean[][] visited = new boolean[rows][cols];

        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(cell -> cell[0]));



        for (int row = 0; row < rows; row++) {

            for (int col = 0; col < cols; col++) {

                if (row == 0 || row == rows - 1 || col == 0 || col == cols - 1) {

                    heap.offer(new int[] {heightMap[row][col], row, col});

                    visited[row][col] = true;

                }

            }

        }



        int trapped = 0;

        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};



        while (!heap.isEmpty()) {

            int[] cell = heap.poll();

            int height = cell[0];

            int row = cell[1];

            int col = cell[2];



            for (int[] direction : directions) {

                int nextRow = row + direction[0];

                int nextCol = col + direction[1];



                if (nextRow < 0 || nextRow >= rows || nextCol < 0 || nextCol >= cols

                        || visited[nextRow][nextCol]) {

                    continue;

                }



                visited[nextRow][nextCol] = true;

                int nextHeight = heightMap[nextRow][nextCol];

                trapped += Math.max(0, height - nextHeight);

                heap.offer(new int[] {Math.max(height, nextHeight), nextRow, nextCol});

            }

        }



        return trapped;

    }

}
