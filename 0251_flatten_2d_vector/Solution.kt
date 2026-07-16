// LeetCode 0251 - Flatten 2D Vector
// https://leetcode.com/problems/flatten-2d-vector/

class Vector2D(vec: Array<IntArray>) {
    private val vec = vec
    private var row = 0
    private var col = 0

    init {
        advance()
    }

    fun next(): Int {
        val value = vec[row][col]
        col += 1
        advance()
        return value
    }

    fun hasNext(): Boolean {
        advance()
        return row < vec.size
    }

    private fun advance() {
        while (row < vec.size && col >= vec[row].size) {
            row += 1
            col = 0
        }
    }
}
