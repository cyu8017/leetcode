// LeetCode 2713 - Maximum Strictly Increasing Cells in a Matrix
// https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/

impl Solution {
    pub fn max_increasing_cells(mat: Vec<Vec<i32>>) -> i32 {
        let m = mat.len();
        let n = mat[0].len();
        let mut cells = Vec::with_capacity(m * n);
        for i in 0..m {
            for j in 0..n {
                cells.push((mat[i][j], i, j));
            }
        }
        cells.sort_unstable_by_key(|&(v, _, _)| v);
        let mut row_max = vec![0; m];
        let mut col_max = vec![0; n];
        let mut dp = vec![vec![0; n]; m];
        let mut ans = 0;
        let mut i = 0;
        while i < cells.len() {
            let mut j = i;
            while j < cells.len() && cells[j].0 == cells[i].0 {
                j += 1;
            }
            let mut buf = Vec::new();
            for k in i..j {
                let r = cells[k].1;
                let c = cells[k].2;
                let best = row_max[r].max(col_max[c]);
                dp[r][c] = best + 1;
                ans = ans.max(dp[r][c]);
                buf.push((r, c, dp[r][c]));
            }
            for (r, c, val) in buf {
                row_max[r] = row_max[r].max(val);
                col_max[c] = col_max[c].max(val);
            }
            i = j;
        }
        ans
    }
}
