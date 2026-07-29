// LeetCode 1040 - Moving Stones Until Consecutive II
// https://leetcode.com/problems/moving-stones-until-consecutive-ii/

class Solution {
    fun numMovesStonesII(stones: IntArray): IntArray {
        stones.sort()
        val n = stones.size
        val maxMoves = maxOf(stones[n - 1] - stones[1] - n + 2, stones[n - 2] - stones[0] - n + 2)
        var minMoves = maxMoves
        var i = 0
        for (j in 0 until n) {
            while (stones[j] - stones[i] + 1 > n) i++
            val inside = j - i + 1
            var cur = n - inside
            if (inside == n - 1 && stones[j] - stones[i] + 1 == n - 1) cur = 2
            minMoves = minOf(minMoves, cur)
        }
        return intArrayOf(minMoves, maxMoves)
    }
}
