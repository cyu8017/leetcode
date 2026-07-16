// LeetCode 0317 - Shortest Distance from All Buildings

// https://leetcode.com/problems/shortest-distance-from-all-buildings/



import java.util.ArrayDeque;

import java.util.Queue;



class Solution {

    public int shortestDistance(int[][] grid) {

        if (grid.length == 0 || grid[0].length == 0) {

            return -1;

        }



        int rows = grid.length;

        int cols = grid[0].length;

        int buildings = 0;

        int[][] distances = new int[rows][cols];

        int[][] reach = new int[rows][cols];

        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};



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

                Queue<int[]> queue = new ArrayDeque<>();

                queue.add(new int[] {row, col, 0});

                boolean[][] visited = new boolean[rows][cols];

                visited[row][col] = true;

                while (!queue.isEmpty()) {

                    int[] current = queue.poll();

                    int currentRow = current[0];

                    int currentCol = current[1];

                    int distance = current[2];

                    for (int[] direction : directions) {

                        int nextRow = currentRow + direction[0];

                        int nextCol = currentCol + direction[1];

                        if (nextRow < 0 || nextRow >= rows || nextCol < 0 || nextCol >= cols) {

                            continue;

                        }

                        if (grid[nextRow][nextCol] != 0 || visited[nextRow][nextCol]) {

                            continue;

                        }

                        visited[nextRow][nextCol] = true;

                        distances[nextRow][nextCol] += distance + 1;

                        reach[nextRow][nextCol]++;

                        queue.add(new int[] {nextRow, nextCol, distance + 1});

                    }

                }

            }

        }



        int best = Integer.MAX_VALUE;

        for (int row = 0; row < rows; row++) {

            for (int col = 0; col < cols; col++) {

                if (grid[row][col] == 0 && reach[row][col] == buildings) {

                    best = Math.min(best, distances[row][col]);

                }

            }

        }

        return best == Integer.MAX_VALUE ? -1 : best;

    }

}

