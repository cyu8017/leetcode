// LeetCode 2579 - Count Total Number of Colored Cells
// https://leetcode.com/problems/count-total-number-of-colored-cells/

public class Solution {
    public long ColoredCells(int n) {
        return 1 + 2L * n * (n - 1);
    }
}
