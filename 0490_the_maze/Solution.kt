// LeetCode 0490 - The Maze
// https://leetcode.com/problems/the-maze/

class Solution {
    fun hasPath(maze: Array<IntArray>, start: IntArray, destination: IntArray): Boolean {
        val rows = maze.size
        val cols = maze[0].size
        val directions = arrayOf(intArrayOf(-1, 0), intArrayOf(1, 0), intArrayOf(0, -1), intArrayOf(0, 1))
        val visited = mutableSetOf<String>()
        val stack = ArrayDeque<IntArray>()
        stack.addLast(intArrayOf(start[0], start[1]))

        while (stack.isNotEmpty()) {
            val (row, col) = stack.removeLast()
            val key = "$row,$col"
            if (key in visited) {
                continue
            }
            visited.add(key)
            if (row == destination[0] && col == destination[1]) {
                return true
            }
            for ((dr, dc) in directions) {
                var nr = row
                var nc = col
                while (nr + dr in 0 until rows && nc + dc in 0 until cols && maze[nr + dr][nc + dc] == 0) {
                    nr += dr
                    nc += dc
                }
                val nextKey = "$nr,$nc"
                if (nextKey !in visited) {
                    stack.addLast(intArrayOf(nr, nc))
                }
            }
        }
        return false
    }
}
