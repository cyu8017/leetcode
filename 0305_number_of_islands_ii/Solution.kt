// LeetCode 0305 - Number of Islands II
// https://leetcode.com/problems/number-of-islands-ii/

class Solution {
    private val parent = HashMap<Int, Int>()
    private val rank = HashMap<Int, Int>()

    fun numIslands2(m: Int, n: Int, positions: Array<IntArray>): List<Int> {
        val result = mutableListOf<Int>()
        var islands = 0
        val directions = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))

        for (position in positions) {
            val row = position[0]
            val col = position[1]
            val index = row * n + col
            if (parent.containsKey(index)) {
                result.add(islands)
                continue
            }
            parent[index] = index
            rank[index] = 0
            islands++

            for (direction in directions) {
                val nextRow = row + direction[0]
                val nextCol = col + direction[1]
                if (nextRow !in 0 until m || nextCol !in 0 until n) {
                    continue
                }
                val neighbor = nextRow * n + nextCol
                if (parent.containsKey(neighbor) && union(index, neighbor)) {
                    islands--
                }
            }
            result.add(islands)
        }
        return result
    }

    private fun find(index: Int): Int {
        var root = parent.getValue(index)
        if (root != index) {
            root = find(root)
            parent[index] = root
        }
        return root
    }

    private fun union(left: Int, right: Int): Boolean {
        val rootLeft = find(left)
        val rootRight = find(right)
        if (rootLeft == rootRight) {
            return false
        }
        val leftRank = rank.getValue(rootLeft)
        val rightRank = rank.getValue(rootRight)
        if (leftRank < rightRank) {
            parent[rootLeft] = rootRight
        } else if (leftRank > rightRank) {
            parent[rootRight] = rootLeft
        } else {
            parent[rootRight] = rootLeft
            rank[rootLeft] = leftRank + 1
        }
        return true
    }
}
