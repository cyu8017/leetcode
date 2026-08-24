// LeetCode 1231 - Divide Chocolate
// https://leetcode.com/problems/divide-chocolate/

class Solution {
    fun maximizeSweetness(sweetness: IntArray, k: Int): Int {
        var lo = 1
        var hi = sweetness.sum() / (k + 1)
        while (lo <= hi) {
            val mid = lo + (hi - lo) / 2
            var pieces = 0
            var current = 0
            for (value in sweetness) {
                current += value
                if (current >= mid) {
                    pieces++
                    current = 0
                }
            }
            if (pieces >= k + 1) lo = mid + 1 else hi = mid - 1
        }
        return hi
    }
}
