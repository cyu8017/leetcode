struct Solution;
// LeetCode 2906 - Construct Product Matrix
// https://leetcode.com/problems/construct-product-matrix/

impl Solution {
    pub fn construct_product_matrix(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        const MOD: i64 = 12345;
        let m = grid.len();
        let n = grid[0].len();
        let mut ans = vec![vec![0i32; n]; m];
        let mut pref = 1i64;
        for i in 0..m {
            for j in 0..n {
                ans[i][j] = pref as i32;
                pref = pref * (grid[i][j] as i64 % MOD) % MOD;
            }
        }
        let mut suf = 1i64;
        for i in (0..m).rev() {
            for j in (0..n).rev() {
                ans[i][j] = (ans[i][j] as i64 * suf % MOD) as i32;
                suf = suf * (grid[i][j] as i64 % MOD) % MOD;
            }
        }
        ans
    }
}

fn main() {}
