// LeetCode 3148 - Maximum Difference Score in a Grid
// https://leetcode.com/problems/maximum-difference-score-in-a-grid/

impl Solution {
    pub fn max_score(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        const INF: i32 = 1 << 30;
        let mut f = vec![vec![0; n]; m];
        let mut ans = -INF;
        for i in 0..m {
            for j in 0..n {
                let x = grid[i][j];
                let mut mi = INF;
                if i > 0 {
                    mi = mi.min(f[i - 1][j]);
                }
                if j > 0 {
                    mi = mi.min(f[i][j - 1]);
                }
                ans = ans.max(x - mi);
                f[i][j] = x.min(mi);
            }
        }
        ans
    }
}
