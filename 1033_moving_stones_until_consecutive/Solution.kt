// LeetCode 1033 - Moving Stones Until Consecutive
// https://leetcode.com/problems/moving-stones-until-consecutive/

class Solution {
    fun numMovesStones(a: Int, b: Int, c: Int): IntArray {
        val arr = intArrayOf(a, b, c).sorted()
        val x = arr[0]; val y = arr[1]; val z = arr[2]
        var minMoves = 2
        if (z - x == 2) minMoves = 0
        else if (y - x <= 2 || z - y <= 2) minMoves = 1
        return intArrayOf(minMoves, z - x - 2)
    }
}
