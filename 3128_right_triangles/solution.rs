// LeetCode 3128 - Right Triangles
// https://leetcode.com/problems/right-triangles/

impl Solution {
    pub fn number_of_right_triangles(grid: Vec<Vec<i32>>) -> i64 {
        let m = grid.len();
        let n = grid[0].len();
        let mut rows = vec![0i32; m];
        let mut cols = vec![0i32; n];
        for i in 0..m {
            for j in 0..n {
                rows[i] += grid[i][j];
                cols[j] += grid[i][j];
            }
        }
        let mut ans = 0i64;
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 1 {
                    ans += (rows[i] - 1) as i64 * (cols[j] - 1) as i64;
                }
            }
        }
        ans
    }
}
