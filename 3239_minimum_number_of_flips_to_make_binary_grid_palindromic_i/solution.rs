// LeetCode 3239 - Minimum Number of Flips to Make Binary Grid Palindromic I
// https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/

impl Solution {
    pub fn min_flips(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut cnt1 = 0;
        let mut cnt2 = 0;
        for row in &grid {
            for j in 0..n / 2 {
                if row[j] != row[n - j - 1] {
                    cnt1 += 1;
                }
            }
        }
        for j in 0..n {
            for i in 0..m / 2 {
                if grid[i][j] != grid[m - i - 1][j] {
                    cnt2 += 1;
                }
            }
        }
        cnt1.min(cnt2)
    }
}
