// LeetCode 3651 - Minimum Cost Path with Teleportations
// https://leetcode.com/problems/minimum-cost-path-with-teleportations/

use std::collections::BTreeMap;

impl Solution {
    pub fn min_cost(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let k = k as usize;
        let inf = i32::MAX / 4;
        let mut f = vec![vec![vec![inf; n]; m]; k + 1];
        f[0][0][0] = 0;
        for i in 0..m {
            for j in 0..n {
                if i > 0 {
                    f[0][i][j] = f[0][i][j].min(f[0][i - 1][j] + grid[i][j]);
                }
                if j > 0 {
                    f[0][i][j] = f[0][i][j].min(f[0][i][j - 1] + grid[i][j]);
                }
            }
        }
        let mut g: BTreeMap<i32, Vec<(usize, usize)>> = BTreeMap::new();
        for i in 0..m {
            for j in 0..n {
                g.entry(grid[i][j]).or_default().push((i, j));
            }
        }
        for t in 1..=k {
            let mut mn = inf;
            for (_key, pos) in g.iter().rev() {
                for &(pi, pj) in pos {
                    mn = mn.min(f[t - 1][pi][pj]);
                }
                for &(pi, pj) in pos {
                    f[t][pi][pj] = mn;
                }
            }
            for i in 0..m {
                for j in 0..n {
                    if i > 0 {
                        f[t][i][j] = f[t][i][j].min(f[t][i - 1][j] + grid[i][j]);
                    }
                    if j > 0 {
                        f[t][i][j] = f[t][i][j].min(f[t][i][j - 1] + grid[i][j]);
                    }
                }
            }
        }
        let mut ans = inf;
        for t in 0..=k {
            ans = ans.min(f[t][m - 1][n - 1]);
        }
        ans
    }
}
