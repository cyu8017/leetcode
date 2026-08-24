// LeetCode 0286 - Walls and Gates
// https://leetcode.com/problems/walls-and-gates/

import java.util.ArrayDeque

class Solution {
    fun wallsAndGates(rooms: Array<IntArray>) {
        if (rooms.isEmpty() || rooms[0].isEmpty()) {
            return
        }
        val rows = rooms.size
        val cols = rooms[0].size
        val queue = ArrayDeque<IntArray>()
        for (row in 0 until rows) {
            for (col in 0 until cols) {
                if (rooms[row][col] == 0) {
                    queue.add(intArrayOf(row, col))
                }
            }
        }
        val directions = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        while (queue.isNotEmpty()) {
            val cell = queue.removeFirst()
            val row = cell[0]
            val col = cell[1]
            for (direction in directions) {
                val nextRow = row + direction[0]
                val nextCol = col + direction[1]
                if (nextRow in 0 until rows && nextCol in 0 until cols && rooms[nextRow][nextCol] == 2147483647) {
                    rooms[nextRow][nextCol] = rooms[row][col] + 1
                    queue.add(intArrayOf(nextRow, nextCol))
                }
            }
        }
    }
}
