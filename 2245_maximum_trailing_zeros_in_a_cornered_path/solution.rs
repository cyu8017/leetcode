// LeetCode 2245 - Maximum Trailing Zeros in a Cornered Path
// https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/

impl Solution {
    pub fn max_trailing_zeros(grid: Vec<Vec<i32>>) -> i32 {
        fn fact(mut x: i32) -> (i32, i32) {
            let mut t = 0;
            let mut f = 0;
            while x % 2 == 0 {
                t += 1;
                x /= 2;
            }
            while x % 5 == 0 {
                f += 1;
                x /= 5;
            }
            (t, f)
        }
        let m = grid.len();
        let n = grid[0].len();
        let mut left = vec![vec![(0, 0); n]; m];
        let mut up = vec![vec![(0, 0); n]; m];
        for i in 0..m {
            for j in 0..n {
                let p = fact(grid[i][j]);
                left[i][j] = p;
                up[i][j] = p;
                if j > 0 {
                    left[i][j].0 += left[i][j - 1].0;
                    left[i][j].1 += left[i][j - 1].1;
                }
                if i > 0 {
                    up[i][j].0 += up[i - 1][j].0;
                    up[i][j].1 += up[i - 1][j].1;
                }
            }
        }
        let mut ans = 0;
        for i in 0..m {
            for j in 0..n {
                let cell = fact(grid[i][j]);
                let l = left[i][j];
                let r_two = left[i][n - 1].0 - left[i][j].0 + cell.0;
                let r_five = left[i][n - 1].1 - left[i][j].1 + cell.1;
                let u = up[i][j];
                let d_two = up[m - 1][j].0 - up[i][j].0 + cell.0;
                let d_five = up[m - 1][j].1 - up[i][j].1 + cell.1;
                let cands = [
                    (l.0 + u.0 - cell.0, l.1 + u.1 - cell.1),
                    (l.0 + d_two - cell.0, l.1 + d_five - cell.1),
                    (r_two + u.0 - cell.0, r_five + u.1 - cell.1),
                    (r_two + d_two - cell.0, r_five + d_five - cell.1),
                ];
                for c in cands {
                    ans = ans.max(c.0.min(c.1));
                }
            }
        }
        ans
    }
}
