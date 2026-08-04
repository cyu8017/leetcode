// LeetCode 1465 - Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
// https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

class Solution {
    fun maxArea(h: Int, w: Int, horizontalCuts: IntArray, verticalCuts: IntArray): Int {
        val hs = IntArray(horizontalCuts.size + 2)
        hs[0] = 0
        hs[hs.size - 1] = h
        System.arraycopy(horizontalCuts, 0, hs, 1, horizontalCuts.size)
        hs.sort()
        val vs = IntArray(verticalCuts.size + 2)
        vs[0] = 0
        vs[vs.size - 1] = w
        System.arraycopy(verticalCuts, 0, vs, 1, verticalCuts.size)
        vs.sort()
        var maxH = 0L
        var maxV = 0L
        for (i in 1 until hs.size) maxH = maxOf(maxH, (hs[i] - hs[i - 1]).toLong())
        for (i in 1 until vs.size) maxV = maxOf(maxV, (vs[i] - vs[i - 1]).toLong())
        return ((maxH * maxV) % 1_000_000_007L).toInt()
    }
}
