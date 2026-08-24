// LeetCode 0499 - The Maze III
// https://leetcode.com/problems/the-maze-iii/

import java.util.PriorityQueue

class Solution {
    fun findShortestWay(maze: Array<IntArray>, ball: IntArray, hole: IntArray): String {
        val rows = maze.size
        val cols = maze[0].size
        val holeRow = hole[0]
        val holeCol = hole[1]
        val directions = arrayOf(
            intArrayOf(1, 0),
            intArrayOf(0, -1),
            intArrayOf(0, 1),
            intArrayOf(-1, 0),
        )
        val labels = arrayOf("d", "l", "r", "u")
        val best = mutableMapOf<String, Best>()
        val heap = PriorityQueue<State>()
        heap.offer(State(0, "", ball[0], ball[1]))

        while (heap.isNotEmpty()) {
            val current = heap.poll()
            val stateKey = "${current.row},${current.col}"
            val recorded = best[stateKey]
            if (recorded != null) {
                if (current.dist > recorded.dist) continue
                if (current.dist == recorded.dist && current.path >= recorded.path) continue
            }
            best[stateKey] = Best(current.dist, current.path)

            if (current.row == holeRow && current.col == holeCol) {
                return current.path
            }

            for (direction in directions.indices) {
                val dr = directions[direction][0]
                val dc = directions[direction][1]
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
                    if (nextRow == holeRow && nextCol == holeCol) break
                }
                if (nextRow == current.row && nextCol == current.col) continue
                val newDist = current.dist + traveled
                val newPath = current.path + labels[direction]
                val targetKey = "$nextRow,$nextCol"
                val existing = best[targetKey]
                if (existing == null
                    || newDist < existing.dist
                    || (newDist == existing.dist && newPath < existing.path)
                ) {
                    heap.offer(State(newDist, newPath, nextRow, nextCol))
                }
            }
        }
        return "impossible"
    }

    private data class Best(val dist: Int, val path: String)

    private data class State(
        val dist: Int,
        val path: String,
        val row: Int,
        val col: Int,
    ) : Comparable<State> {
        override fun compareTo(other: State): Int {
            if (dist != other.dist) return dist.compareTo(other.dist)
            return path.compareTo(other.path)
        }
    }
}
