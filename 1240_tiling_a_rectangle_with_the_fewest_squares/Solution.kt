// LeetCode 1240 - Tiling a Rectangle with the Fewest Squares
// https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

class Solution {
    private var best = 0

    fun tilingRectangle(n: Int, m: Int): Int {
        var nn = n
        var mm = m
        if (nn > mm) {
            val t = nn; nn = mm; mm = t
        }
        val heights = IntArray(mm)
        best = nn * mm
        search(heights, nn, mm, 0)
        return best
    }

    private fun search(heights: IntArray, n: Int, m: Int, used: Int) {
        if (used >= best) return
        val low = heights.minOrNull()!!
        if (low == n) {
            best = used
            return
        }
        var left = 0
        while (left < m && heights[left] != low) left++
        var right = left
        while (right < m && heights[right] == low) right++
        val maxSize = minOf(n - low, right - left)
        for (size in maxSize downTo 1) {
            for (i in left until left + size) heights[i] = low + size
            search(heights, n, m, used + 1)
            for (i in left until left + size) heights[i] = low
        }
    }
}
