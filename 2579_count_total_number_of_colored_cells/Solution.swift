// LeetCode 2579 - Count Total Number of Colored Cells
// https://leetcode.com/problems/count-total-number-of-colored-cells/

class Solution {
    func coloredCells(_ n: Int) -> Int {
        1 + 2 * n * (n - 1)
    }
}
