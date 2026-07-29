// LeetCode 1007 - Minimum Domino Rotations For Equal Row
// https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

class Solution {
    fun minDominoRotations(tops: IntArray, bottoms: IntArray): Int {
        val ans = minOf(check(tops, bottoms, tops[0]), check(tops, bottoms, bottoms[0]))
        return if (ans == Int.MAX_VALUE / 2) -1 else ans
    }

    private fun check(tops: IntArray, bottoms: IntArray, target: Int): Int {
        var rotTop = 0; var rotBot = 0
        for (i in tops.indices) {
            if (tops[i] != target && bottoms[i] != target) return Int.MAX_VALUE / 2
            if (tops[i] != target) rotTop++
            if (bottoms[i] != target) rotBot++
        }
        return minOf(rotTop, rotBot)
    }
}
