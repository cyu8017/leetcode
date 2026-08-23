// LeetCode 0329 - Longest Increasing Path in a Matrix

// https://leetcode.com/problems/longest-increasing-path-in-a-matrix/



public class Solution {

    private int[][] matrix;

    private int[][] memo;



    private static readonly int[][] Directions = {

        new[] {1, 0}, new[] {-1, 0}, new[] {0, 1}, new[] {0, -1},

    };



    public int LongestIncreasingPath(int[][] matrix) {

        if (matrix.Length == 0 || matrix[0].Length == 0) {

            return 0;

        }

        this.matrix = matrix;

        memo = new int[matrix.Length][];

        for (int row = 0; row < matrix.Length; row++) {

            memo[row] = new int[matrix[0].Length];

        }

        int best = 0;

        for (int row = 0; row < matrix.Length; row++) {

            for (int col = 0; col < matrix[0].Length; col++) {

                best = System.Math.Max(best, Dfs(row, col));

            }

        }

        return best;

    }



    private int Dfs(int row, int col) {

        if (memo[row][col] != 0) {

            return memo[row][col];

        }

        int best = 1;

        foreach (int[] direction in Directions) {

            int nextRow = row + direction[0];

            int nextCol = col + direction[1];

            if (nextRow >= 0 && nextRow < matrix.Length && nextCol >= 0 && nextCol < matrix[0].Length

                && matrix[nextRow][nextCol] > matrix[row][col]) {

                best = System.Math.Max(best, 1 + Dfs(nextRow, nextCol));

            }

        }

        memo[row][col] = best;

        return best;

    }

}

