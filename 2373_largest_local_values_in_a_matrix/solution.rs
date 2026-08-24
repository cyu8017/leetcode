// LeetCode 2373 - Largest Local Values in a Matrix
// https://leetcode.com/problems/largest-local-values-in-a-matrix/

impl Solution {
    pub fn largest_local(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = grid.len();
        let mut ans = vec![vec![0; n - 2]; n - 2];
        for i in 0..n - 2 {
            for j in 0..n - 2 {
                let mut mx = 0;
                for r in i..i + 3 {
                    for c in j..j + 3 {
                        mx = mx.max(grid[r][c]);
                    }
                }
                ans[i][j] = mx;
            }
        }
        ans
    }
}
