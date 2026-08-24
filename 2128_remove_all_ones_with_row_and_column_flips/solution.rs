// LeetCode 2128 - Remove All Ones With Row and Column Flips
// https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/

impl Solution {
    pub fn remove_ones(grid: Vec<Vec<i32>>) -> bool {
        let m = grid.len();
        let n = grid[0].len();
        for i in 1..m {
            let same = grid[i][0] == grid[0][0];
            for j in 0..n {
                if (grid[i][j] == grid[0][j]) != same {
                    return false;
                }
            }
        }
        true
    }
}
