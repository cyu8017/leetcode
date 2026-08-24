// LeetCode 1351 - Count Negative Numbers in a Sorted Matrix
// https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution {
    fun countNegatives(grid: Array<IntArray>): Int {
        var count = 0
        for (row in grid) {
            var lo = 0
            var hi = row.size
            while (lo < hi) {
                val mid = (lo + hi) ushr 1
                if (row[mid] < 0) hi = mid else lo = mid + 1
            }
            count += row.size - lo
        }
        return count
    }
}
