// LeetCode 0505 - The Maze II
// https://leetcode.com/problems/the-maze-ii/

import java.util.PriorityQueue

class Solution {
    fun shortestDistance(maze: Array<IntArray>, start: IntArray, destination: IntArray): Int {
        val rows = maze.size
        val cols = maze[0].size
        val targetRow = destination[0]
        val targetCol = destination[1]
        val directions = arrayOf(
            intArrayOf(-1, 0),
            intArrayOf(1, 0),
            intArrayOf(0, -1),
            intArrayOf(0, 1),
        )
        val best = mutableMapOf<String, Int>()
        val heap = PriorityQueue<State>()
        heap.offer(State(0, start[0], start[1]))

        while (heap.isNotEmpty()) {
            val current = heap.poll()
            if (current.row == targetRow && current.col == targetCol) {
                return current.dist
            }
            val stateKey = "${current.row},${current.col}"
            if (best.getOrDefault(stateKey, Int.MAX_VALUE) <= current.dist) {
                continue
            }
            best[stateKey] = current.dist
            for (direction in directions) {
                val dr = direction[0]
                val dc = direction[1]
                var nextRow = current.row
                var nextCol = current.col
                var traveled = 0
                while (nextRow + dr in 0 until rows
                    && nextCol + dc in 0 until cols
                    && maze[nextRow + dr][nextCol + dc] == 0
                ) {
                    nextRow += dr
                    nextCol += dc
                    traveled++
                }
                if (nextRow == current.row && nextCol == current.col) continue
                val newDist = current.dist + traveled
                val targetKey = "$nextRow,$nextCol"
                if (newDist < best.getOrDefault(targetKey, Int.MAX_VALUE)) {
                    heap.offer(State(newDist, nextRow, nextCol))
                }
            }
        }
        return -1
    }

    private data class State(val dist: Int, val row: Int, val col) : Comparable<State> {
        override fun compareTo(other: State): Int = dist.compareTo(other.dist)
    }
}
