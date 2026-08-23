// LeetCode 0417 - Pacific Atlantic Water Flow

// https://leetcode.com/problems/pacific-atlantic-water-flow/



public class Solution {

    public IList<IList<int>> PacificAtlantic(int[][] heights) {

        if (heights.Length == 0 || heights[0].Length == 0) {

            return new List<IList<int>>();

        }



        int rows = heights.Length;

        int cols = heights[0].Length;

        HashSet<long> pacific = new();

        HashSet<long> atlantic = new();



        for (int row = 0; row < rows; row++) {

            Dfs(row, 0, pacific, heights[row][0], heights, rows, cols);

            Dfs(row, cols - 1, atlantic, heights[row][cols - 1], heights, rows, cols);

        }



        for (int col = 0; col < cols; col++) {

            Dfs(0, col, pacific, heights[0][col], heights, rows, cols);

            Dfs(rows - 1, col, atlantic, heights[rows - 1][col], heights, rows, cols);

        }



        List<IList<int>> result = new();



        foreach (long key in pacific) {

            if (atlantic.Contains(key)) {

                result.Add(new List<int> { (int)(key / cols), (int)(key % cols) });

            }

        }



        return result;

    }



    private void Dfs(

        int row,

        int col,

        HashSet<long> visited,

        int previous,

        int[][] heights,

        int rows,

        int cols) {

        long key = (long)row * cols + col;



        if (visited.Contains(key) || row < 0 || row >= rows || col < 0 || col >= cols) {

            return;

        }



        if (heights[row][col] < previous) {

            return;

        }



        visited.Add(key);

        int height = heights[row][col];



        Dfs(row + 1, col, visited, height, heights, rows, cols);

        Dfs(row - 1, col, visited, height, heights, rows, cols);

        Dfs(row, col + 1, visited, height, heights, rows, cols);

        Dfs(row, col - 1, visited, height, heights, rows, cols);

    }

}
