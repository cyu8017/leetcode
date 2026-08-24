// LeetCode 0417 - Pacific Atlantic Water Flow

// https://leetcode.com/problems/pacific-atlantic-water-flow/



class Solution {

    fun pacificAtlantic(heights: Array<IntArray>): List<List<Int>> {

        if (heights.isEmpty() || heights[0].isEmpty()) {

            return emptyList()

        }



        val rows = heights.size

        val cols = heights[0].size

        val pacific = mutableSetOf<Long>()

        val atlantic = mutableSetOf<Long>()



        for (row in 0 until rows) {

            dfs(row, 0, pacific, heights[row][0], heights, rows, cols)

            dfs(row, cols - 1, atlantic, heights[row][cols - 1], heights, rows, cols)

        }



        for (col in 0 until cols) {

            dfs(0, col, pacific, heights[0][col], heights, rows, cols)

            dfs(rows - 1, col, atlantic, heights[rows - 1][col], heights, rows, cols)

        }



        return pacific.intersect(atlantic).map { key ->

            listOf((key / cols).toInt(), (key % cols).toInt())

        }

    }



    private fun dfs(

        row: Int,

        col: Int,

        visited: MutableSet<Long>,

        previous: Int,

        heights: Array<IntArray>,

        rows: Int,

        cols: Int,

    ) {

        val key = row.toLong() * cols + col



        if (key in visited || row < 0 || row >= rows || col < 0 || col >= cols) {

            return

        }



        if (heights[row][col] < previous) {

            return

        }



        visited.add(key)

        val height = heights[row][col]



        dfs(row + 1, col, visited, height, heights, rows, cols)

        dfs(row - 1, col, visited, height, heights, rows, cols)

        dfs(row, col + 1, visited, height, heights, rows, cols)

        dfs(row, col - 1, visited, height, heights, rows, cols)

    }

}
