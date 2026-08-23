// LeetCode 0361 - Bomb Enemy

// https://leetcode.com/problems/bomb-enemy/



class Solution {

    public int maxKilledEnemies(char[][] grid) {

        if (grid.length == 0 || grid[0].length == 0) {

            return 0;

        }



        int rows = grid.length;

        int cols = grid[0].length;

        int[][] rowHits = new int[rows][cols];

        int[][] colHits = new int[rows][cols];



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

                result = Math.max(result, rowHits[row][col] + colHits[row][col]);

            }

        }

        return result;

    }

}
