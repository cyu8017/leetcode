// LeetCode 1267 - Count Servers that Communicate
// https://leetcode.com/problems/count-servers-that-communicate/

impl Solution {
    pub fn count_servers(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut rows = vec![0; m];
        let mut cols = vec![0; n];
        for r in 0..m {
            for c in 0..n {
                rows[r] += grid[r][c];
                cols[c] += grid[r][c];
            }
        }
        let mut ans = 0;
        for r in 0..m {
            for c in 0..n {
                if grid[r][c] == 1 && (rows[r] > 1 || cols[c] > 1) {
                    ans += 1;
                }
            }
        }
        ans
    }
}
