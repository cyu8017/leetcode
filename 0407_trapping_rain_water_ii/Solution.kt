// LeetCode 0407 - Trapping Rain Water II

// https://leetcode.com/problems/trapping-rain-water-ii/



import java.util.PriorityQueue



class Solution {

    fun trapRainWater(heightMap: Array<IntArray>): Int {

        if (heightMap.isEmpty() || heightMap[0].isEmpty()) {

            return 0

        }



        val rows = heightMap.size

        val cols = heightMap[0].size



        if (rows < 3 || cols < 3) {

            return 0

        }



        val visited = Array(rows) { BooleanArray(cols) }

        val heap = PriorityQueue<Triple<Int, Int, Int>>(compareBy { it.first })



        for (row in 0 until rows) {

            for (col in 0 until cols) {

                if (row == 0 || row == rows - 1 || col == 0 || col == cols - 1) {

                    heap.offer(Triple(heightMap[row][col], row, col))

                    visited[row][col] = true

                }

            }

        }



        var trapped = 0

        val directions = arrayOf(1 to 0, -1 to 0, 0 to 1, 0 to -1)



        while (heap.isNotEmpty()) {

            val (height, row, col) = heap.poll()



            for ((dr, dc) in directions) {

                val nextRow = row + dr

                val nextCol = col + dc



                if (nextRow !in 0 until rows || nextCol !in 0 until cols || visited[nextRow][nextCol]) {

                    continue

                }



                visited[nextRow][nextCol] = true

                val nextHeight = heightMap[nextRow][nextCol]

                trapped += maxOf(0, height - nextHeight)

                heap.offer(Triple(maxOf(height, nextHeight), nextRow, nextCol))

            }

        }



        return trapped

    }

}
