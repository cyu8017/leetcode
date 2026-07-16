// LeetCode 0417 - Pacific Atlantic Water Flow

// https://leetcode.com/problems/pacific-atlantic-water-flow/



import java.util.ArrayList;

import java.util.HashSet;

import java.util.List;

import java.util.Set;



class Solution {

    public List<List<Integer>> pacificAtlantic(int[][] heights) {

        if (heights.length == 0 || heights[0].length == 0) {

            return new ArrayList<>();

        }



        int rows = heights.length;

        int cols = heights[0].length;

        Set<Long> pacific = new HashSet<>();

        Set<Long> atlantic = new HashSet<>();



        for (int row = 0; row < rows; row++) {

            dfs(row, 0, pacific, heights[row][0], heights, rows, cols);

            dfs(row, cols - 1, atlantic, heights[row][cols - 1], heights, rows, cols);

        }



        for (int col = 0; col < cols; col++) {

            dfs(0, col, pacific, heights[0][col], heights, rows, cols);

            dfs(rows - 1, col, atlantic, heights[rows - 1][col], heights, rows, cols);

        }



        List<List<Integer>> result = new ArrayList<>();



        for (long key : pacific) {

            if (atlantic.contains(key)) {

                int row = (int) (key / cols);

                int col = (int) (key % cols);

                result.add(List.of(row, col));

            }

        }



        return result;

    }



    private void dfs(

            int row,

            int col,

            Set<Long> visited,

            int previous,

            int[][] heights,

            int rows,

            int cols) {

        long key = (long) row * cols + col;



        if (visited.contains(key) || row < 0 || row >= rows || col < 0 || col >= cols) {

            return;

        }



        if (heights[row][col] < previous) {

            return;

        }



        visited.add(key);

        int height = heights[row][col];



        dfs(row + 1, col, visited, height, heights, rows, cols);

        dfs(row - 1, col, visited, height, heights, rows, cols);

        dfs(row, col + 1, visited, height, heights, rows, cols);

        dfs(row, col - 1, visited, height, heights, rows, cols);

    }

}
