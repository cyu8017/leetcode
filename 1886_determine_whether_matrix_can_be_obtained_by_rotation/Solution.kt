// LeetCode 1886 - Determine Whether Matrix Can Be Obtained By Rotation
// https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution {
    fun findRotation(mat: Array<IntArray>, target: Array<IntArray>): Boolean {
        var current = mat
        repeat(4) {
            if (current.contentDeepEquals(target)) return true
            val n = current.size
            current = Array(n) { col ->
                IntArray(n) { row -> current[n - 1 - row][col] }
            }
        }
        return false
    }
}
