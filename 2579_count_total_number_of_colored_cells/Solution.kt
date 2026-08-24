// LeetCode 2579 - Count Total Number of Colored Cells
// https://leetcode.com/problems/count-total-number-of-colored-cells/

class Solution {
    fun coloredCells(n: Int): Long {
        return 1 + 2L * n * (n - 1)
    }
}
