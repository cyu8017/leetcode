// LeetCode 2943 - Maximize Area of Square Hole in Grid
// https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/

class Solution {
    private fun maxGap(bars: IntArray): Int {
        if (bars.size == 0) return 1
        bars.sort()
        var best = 1
        var cur = 1
        for (i in 1 until bars.size) {
            if (bars[i] == bars[i - 1] + 1) cur++
            else cur = 1
            if (cur > best) best = cur
        }
        return best + 1
    }

    fun maximizeSquareHoleArea(n: Int, m: Int, hBars: IntArray, vBars: IntArray): Int {
        var side = maxGap(hBars.clone())
        var vs = maxGap(vBars.clone())
        if (vs < side) side = vs
        return side * side
    }
}
