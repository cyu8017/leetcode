// LeetCode 0463 - Island Perimeter
// https://leetcode.com/problems/island-perimeter/

public class Solution {
    public int IslandPerimeter(int[][] grid) {
        int rows = grid.Length;
        int cols = grid[0].Length;
        int perimeter = 0;
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (grid[row][col] == 0) {
                    continue;
                }
                perimeter += 4;
                if (row > 0 && grid[row - 1][col] == 1) {
                    perimeter -= 2;
                }
                if (col > 0 && grid[row][col - 1] == 1) {
                    perimeter -= 2;
                }
            }
        }
        return perimeter;
    }
}
