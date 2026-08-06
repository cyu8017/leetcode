// LeetCode 1594 - Maximum Non Negative Product in a Matrix
// https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/

impl Solution {
    pub fn max_product_path(grid: Vec<Vec<i32>>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let m = grid.len();
        let n = grid[0].len();
        let mut high = vec![vec![0i64; n]; m];
        let mut low = vec![vec![0i64; n]; m];
        high[0][0] = grid[0][0] as i64;
        low[0][0] = grid[0][0] as i64;
        for r in 0..m {
            for c in 0..n {
                if r == 0 && c == 0 {
                    continue;
                }
                let mut values = Vec::new();
                if r > 0 {
                    values.push(high[r - 1][c] * grid[r][c] as i64);
                    values.push(low[r - 1][c] * grid[r][c] as i64);
                }
                if c > 0 {
                    values.push(high[r][c - 1] * grid[r][c] as i64);
                    values.push(low[r][c - 1] * grid[r][c] as i64);
                }
                high[r][c] = *values.iter().max().unwrap();
                low[r][c] = *values.iter().min().unwrap();
            }
        }
        if high[m - 1][n - 1] >= 0 {
            (high[m - 1][n - 1] % MOD) as i32
        } else {
            -1
        }
    }
}
