// LeetCode 0317 - Shortest Distance from All Buildings

// https://leetcode.com/problems/shortest-distance-from-all-buildings/



class Solution {

    fun shortestDistance(grid: Array<IntArray>): Int {

        if (grid.isEmpty() || grid[0].isEmpty()) {

            return -1

        }



        val rows = grid.size

        val cols = grid[0].size

        var buildings = 0

        val distances = Array(rows) { IntArray(cols) }

        val reach = Array(rows) { IntArray(cols) }

        val directions = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))



        for (row in 0 until rows) {

            for (col in 0 until cols) {

                if (grid[row][col] == 1) {

                    buildings++

                }

            }

        }



        for (row in 0 until rows) {

            for (col in 0 until cols) {

                if (grid[row][col] != 1) {

                    continue

                }

                val queue = ArrayDeque<IntArray>()

                queue.add(intArrayOf(row, col, 0))

                val visited = Array(rows) { BooleanArray(cols) }

                visited[row][col] = true

                while (queue.isNotEmpty()) {

                    val current = queue.removeFirst()

                    val currentRow = current[0]

                    val currentCol = current[1]

                    val distance = current[2]

                    for (direction in directions) {

                        val nextRow = currentRow + direction[0]

                        val nextCol = currentCol + direction[1]

                        if (nextRow !in 0 until rows || nextCol !in 0 until cols) {

                            continue

                        }

                        if (grid[nextRow][nextCol] != 0 || visited[nextRow][nextCol]) {

                            continue

                        }

                        visited[nextRow][nextCol] = true

                        distances[nextRow][nextCol] += distance + 1

                        reach[nextRow][nextCol]++

                        queue.add(intArrayOf(nextRow, nextCol, distance + 1))

                    }

                }

            }

        }



        var best = Int.MAX_VALUE

        for (row in 0 until rows) {

            for (col in 0 until cols) {

                if (grid[row][col] == 0 && reach[row][col] == buildings) {

                    best = minOf(best, distances[row][col])

                }

            }

        }

        return if (best == Int.MAX_VALUE) -1 else best

    }

}

