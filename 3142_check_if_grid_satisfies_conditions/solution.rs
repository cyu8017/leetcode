// LeetCode 3142 - Check if Grid Satisfies Conditions
// https://leetcode.com/problems/check-if-grid-satisfies-conditions/

impl Solution {
    pub fn satisfies_conditions(grid: Vec<Vec<i32>>) -> bool {
        let m = grid.len();
        let n = grid[0].len();
        for i in 0..m {
            for j in 0..n {
                let x = grid[i][j];
                if i + 1 < m && x != grid[i + 1][j] {
                    return false;
                }
                if j + 1 < n && x == grid[i][j + 1] {
                    return false;
                }
            }
        }
        true
    }
}
