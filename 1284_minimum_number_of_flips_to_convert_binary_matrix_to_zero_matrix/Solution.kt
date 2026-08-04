// LeetCode 1284 - Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
// https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/

class Solution {
    fun minFlips(mat: Array<IntArray>): Int {
        val m = mat.size
        val n = mat[0].size
        var start = 0
        for (r in 0 until m) {
            for (c in 0 until n) {
                if (mat[r][c] != 0) start = start or (1 shl (r * n + c))
            }
        }
        val deltas = arrayOf(intArrayOf(0, 0), intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        val masks = mutableListOf<Int>()
        for (r in 0 until m) {
            for (c in 0 until n) {
                var mask = 0
                for (d in deltas) {
                    val nr = r + d[0]
                    val nc = c + d[1]
                    if (nr in 0 until m && nc in 0 until n) mask = mask xor (1 shl (nr * n + nc))
                }
                masks.add(mask)
            }
        }
        val queue = ArrayDeque<IntArray>()
        val seen = mutableSetOf(start)
        queue.add(intArrayOf(start, 0))
        while (queue.isNotEmpty()) {
            val cur = queue.removeFirst()
            if (cur[0] == 0) return cur[1]
            for (mask in masks) {
                val nxt = cur[0] xor mask
                if (seen.add(nxt)) queue.add(intArrayOf(nxt, cur[1] + 1))
            }
        }
        return -1
    }
}
