// LeetCode 1465 - Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
// https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

class Solution {
    fun maxArea(h: Int, w: Int, horizontalCuts: IntArray, verticalCuts: IntArray): Int {
        val hs = (listOf(0, h) + horizontalCuts.toList()).sorted()
        val vs = (listOf(0, w) + verticalCuts.toList()).sorted()
        var maxH = 0
        var maxV = 0
        for (i in 0 until hs.size - 1) maxH = maxOf(maxH, hs[i + 1] - hs[i])
        for (i in 0 until vs.size - 1) maxV = maxOf(maxV, vs[i + 1] - vs[i])
        return ((maxH.toLong() * maxV) % 1_000_000_007).toInt()
    }
}
