// LeetCode 0361 - Bomb Enemy

// https://leetcode.com/problems/bomb-enemy/



class Solution {

    fun maxKilledEnemies(grid: Array<CharArray>): Int {

        if (grid.isEmpty() || grid[0].isEmpty()) {

            return 0

        }



        val rows = grid.size

        val cols = grid[0].size

        val rowHits = Array(rows) { IntArray(cols) }

        val colHits = Array(rows) { IntArray(cols) }



        for (row in 0 until rows) {

            var count = 0

            for (col in 0 until cols) {

                when (grid[row][col]) {

                    'W' -> count = 0

                    'E' -> count++

                    else -> rowHits[row][col] = count

                }

            }

            count = 0

            for (col in cols - 1 downTo 0) {

                when (grid[row][col]) {

                    'W' -> count = 0

                    'E' -> count++

                    else -> rowHits[row][col] += count

                }

            }

        }



        for (col in 0 until cols) {

            var count = 0

            for (row in 0 until rows) {

                when (grid[row][col]) {

                    'W' -> count = 0

                    'E' -> count++

                    else -> colHits[row][col] = count

                }

            }

            count = 0

            for (row in rows - 1 downTo 0) {

                when (grid[row][col]) {

                    'W' -> count = 0

                    'E' -> count++

                    else -> colHits[row][col] += count

                }

            }

        }



        var result = 0

        for (row in 0 until rows) {

            for (col in 0 until cols) {

                result = maxOf(result, rowHits[row][col] + colHits[row][col])

            }

        }

        return result

    }

}
