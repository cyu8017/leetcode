// LeetCode 0281 - Zigzag Iterator
// https://leetcode.com/problems/zigzag-iterator/

class ZigzagIterator(v1: IntArray, v2: IntArray) {
    private val vectors = arrayOf(v1, v2)
    private val indices = intArrayOf(0, 0)
    private var turn = 0

    fun next(): Int {
        while (indices[turn] >= vectors[turn].size) {
            turn = 1 - turn
        }
        val value = vectors[turn][indices[turn]]
        indices[turn]++
        turn = 1 - turn
        return value
    }

    fun hasNext(): Boolean {
        for (index in indices.indices) {
            if (indices[index] < vectors[index].size) {
                return true
            }
        }
        return false
    }
}
