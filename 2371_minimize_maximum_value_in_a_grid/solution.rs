// LeetCode 2371 - Minimize Maximum Value in a Grid
// https://leetcode.com/problems/minimize-maximum-value-in-a-grid/

impl Solution {
    pub fn min_score(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = grid.len();
        let n = grid[0].len();
        let mut arr = Vec::with_capacity(m * n);
        for i in 0..m {
            for j in 0..n {
                arr.push((grid[i][j], i, j));
            }
        }
        arr.sort_unstable_by_key(|&(v, _, _)| v);
        let mut row_max = vec![0; m];
        let mut col_max = vec![0; n];
        let mut ans = vec![vec![0; n]; m];
        for &(_, r, c) in &arr {
            let val = row_max[r].max(col_max[c]) + 1;
            ans[r][c] = val;
            row_max[r] = val;
            col_max[c] = val;
        }
        ans
    }
}
