// LeetCode 0361 - Bomb Enemy

// https://leetcode.com/problems/bomb-enemy/



public class Solution {

    public int MaxKilledEnemies(char[][] grid) {

        if (grid.Length == 0 || grid[0].Length == 0) {

            return 0;

        }



        int rows = grid.Length;

        int cols = grid[0].Length;

        int[][] rowHits = new int[rows][];

        int[][] colHits = new int[rows][];

        for (int row = 0; row < rows; row++) {

            rowHits[row] = new int[cols];

            colHits[row] = new int[cols];

        }



        for (int row = 0; row < rows; row++) {

            int count = 0;

            for (int col = 0; col < cols; col++) {

                if (grid[row][col] == 'W') {

                    count = 0;

                } else if (grid[row][col] == 'E') {

                    count++;

                } else {

                    rowHits[row][col] = count;

                }

            }

            count = 0;

            for (int col = cols - 1; col >= 0; col--) {

                if (grid[row][col] == 'W') {

                    count = 0;

                } else if (grid[row][col] == 'E') {

                    count++;

                } else {

                    rowHits[row][col] += count;

                }

            }

        }



        for (int col = 0; col < cols; col++) {

            int count = 0;

            for (int row = 0; row < rows; row++) {

                if (grid[row][col] == 'W') {

                    count = 0;

                } else if (grid[row][col] == 'E') {

                    count++;

                } else {

                    colHits[row][col] = count;

                }

            }

            count = 0;

            for (int row = rows - 1; row >= 0; row--) {

                if (grid[row][col] == 'W') {

                    count = 0;

                } else if (grid[row][col] == 'E') {

                    count++;

                } else {

                    colHits[row][col] += count;

                }

            }

        }



        int result = 0;

        for (int row = 0; row < rows; row++) {

            for (int col = 0; col < cols; col++) {

                result = Math.Max(result, rowHits[row][col] + colHits[row][col]);

            }

        }

        return result;

    }

}
