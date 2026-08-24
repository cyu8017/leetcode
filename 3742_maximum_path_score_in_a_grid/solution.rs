// LeetCode 3742 - Maximum Path Score in a Grid
// https://leetcode.com/problems/maximum-path-score-in-a-grid/

impl Solution {
    pub fn max_path_score(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut f = vec![vec![vec![-1; (k + 1) as usize]; n]; m];

        fn dfs(
            i: i32,
            j: i32,
            kk: i32,
            grid: &[Vec<i32>],
            f: &mut [Vec<Vec<i32>>],
        ) -> i32 {
            const INF: i32 = 1 << 30;
            if i < 0 || j < 0 || kk < 0 {
                return -INF;
            }
            if i == 0 && j == 0 {
                return 0;
            }
            let ui = i as usize;
            let uj = j as usize;
            let uk = kk as usize;
            if f[ui][uj][uk] != -1 {
                return f[ui][uj][uk];
            }
            let mut res = grid[ui][uj];
            let mut nk = kk;
            if grid[ui][uj] != 0 {
                nk -= 1;
            }
            let a = dfs(i - 1, j, nk, grid, f);
            let b = dfs(i, j - 1, nk, grid, f);
            res += a.max(b);
            f[ui][uj][uk] = res;
            res
        }

        let ans = dfs((m - 1) as i32, (n - 1) as i32, k, &grid, &mut f);
        if ans < 0 { -1 } else { ans }
    }
}
