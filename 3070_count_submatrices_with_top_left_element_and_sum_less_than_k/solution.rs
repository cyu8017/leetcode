// LeetCode 3070 - Count Submatrices with Top-Left Element and Sum Less Than k
// https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

impl Solution {
    pub fn count_submatrices(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        let n = grid.len();
        let m = grid[0].len();
        let mut ans = 0;
        let mut s = vec![vec![0; m + 1]; n + 1];
        for i in 0..n {
            for j in 0..m {
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + grid[i][j];
                if s[i + 1][j + 1] <= k {
                    ans += 1;
                }
            }
        }
        ans
    }
}
