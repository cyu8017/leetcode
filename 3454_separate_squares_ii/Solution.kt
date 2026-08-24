// LeetCode 3454 - Separate Squares II
// https://leetcode.com/problems/separate-squares-ii/

class Solution {
    fun separateSquares(squares: Array<IntArray>): Double {
        var total = 0
        for (sq in squares) {
            var l = sq[2]
            total += l * l
        }
        var lo = 0.0
        var hi = 2e9
        for (it in 0 until 60) {
            var mid = (lo + hi) / 2
            if (areaBelow(squares, mid) * 2 < total) lo = mid
            else hi = mid
        }
        return hi
    }

    private fun areaBelow(squares: Array<IntArray>, y: Double): Double {
        var below = 0
        for (sq in squares) {
            var yi = sq[1]
            var l = sq[2]
            var top = yi + l
            if (y <= yi) continue
            else if (y >= top) below += l * l
            else below += l * (y - yi)
        }
        return below
    }
}
