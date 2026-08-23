// LeetCode 0329 - Longest Increasing Path in a Matrix

// https://leetcode.com/problems/longest-increasing-path-in-a-matrix/



class Solution {

    private int[][] matrix;

    private int[][] memo;

    private static final int[][] DIRECTIONS = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};



    public int longestIncreasingPath(int[][] matrix) {

        if (matrix.length == 0 || matrix[0].length == 0) {

            return 0;

        }

        this.matrix = matrix;

        memo = new int[matrix.length][matrix[0].length];

        int best = 0;

        for (int row = 0; row < matrix.length; row++) {

            for (int col = 0; col < matrix[0].length; col++) {

                best = Math.max(best, dfs(row, col));

            }

        }

        return best;

    }



    private int dfs(int row, int col) {

        if (memo[row][col] != 0) {

            return memo[row][col];

        }

        int best = 1;

        for (int[] direction : DIRECTIONS) {

            int nextRow = row + direction[0];

            int nextCol = col + direction[1];

            if (nextRow >= 0 && nextRow < matrix.length && nextCol >= 0 && nextCol < matrix[0].length

                    && matrix[nextRow][nextCol] > matrix[row][col]) {

                best = Math.max(best, 1 + dfs(nextRow, nextCol));

            }

        }

        memo[row][col] = best;

        return best;

    }

}

