// LeetCode 0427 - Construct Quad Tree
// https://leetcode.com/problems/construct-quad-tree/

class Node(
    var `val`: Boolean = false,
    var isLeaf: Boolean = false,
    var topLeft: Node? = null,
    var topRight: Node? = null,
    var bottomLeft: Node? = null,
    var bottomRight: Node? = null,
)

class Solution {
    fun construct(grid: Array<IntArray>): Node {
        fun build(row: Int, col: Int, size: Int): Node {
            if (size == 1) {
                return Node(grid[row][col] == 1, true)
            }

            val half = size / 2
            val topLeft = build(row, col, half)
            val topRight = build(row, col + half, half)
            val bottomLeft = build(row + half, col, half)
            val bottomRight = build(row + half, col + half, half)

            if (
                topLeft.isLeaf &&
                topRight.isLeaf &&
                bottomLeft.isLeaf &&
                bottomRight.isLeaf &&
                topLeft.`val` == topRight.`val` &&
                topLeft.`val` == bottomLeft.`val` &&
                topLeft.`val` == bottomRight.`val`
            ) {
                return Node(topLeft.`val`, true)
            }

            return Node(true, false, topLeft, topRight, bottomLeft, bottomRight)
        }

        return build(0, 0, grid.size)
    }
}
