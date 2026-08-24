// LeetCode 2850 - Minimum Moves to Spread Stones Over Grid
// https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/

impl Solution {
    pub fn minimum_moves(grid: Vec<Vec<i32>>) -> i32 {
        let mut extras = Vec::new();
        let mut zeros = Vec::new();
        for i in 0..3 {
            for j in 0..3 {
                if grid[i][j] == 0 {
                    zeros.push((i as i32, j as i32));
                } else if grid[i][j] > 1 {
                    for _ in 0..grid[i][j] - 1 {
                        extras.push((i as i32, j as i32));
                    }
                }
            }
        }
        if zeros.is_empty() {
            return 0;
        }
        fn dfs(i: usize, cost: i32, extras: &mut [(i32, i32)], zeros: &[(i32, i32)], best: &mut i32) {
            if cost >= *best {
                return;
            }
            if i == zeros.len() {
                *best = cost;
                return;
            }
            for j in 0..extras.len() {
                if extras[j].0 < 0 {
                    continue;
                }
                let e = extras[j];
                extras[j].0 = -1;
                let d = (e.0 - zeros[i].0).abs() + (e.1 - zeros[i].1).abs();
                dfs(i + 1, cost + d, extras, zeros, best);
                extras[j] = e;
            }
        }
        let mut best = 1 << 30;
        dfs(0, 0, &mut extras, &zeros, &mut best);
        best
    }
}
