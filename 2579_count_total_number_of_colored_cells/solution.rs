// LeetCode 2579 - Count Total Number of Colored Cells
// https://leetcode.com/problems/count-total-number-of-colored-cells/

impl Solution {
    pub fn colored_cells(n: i32) -> i64 {
        1 + 2 * n as i64 * (n as i64 - 1)
    }
}
