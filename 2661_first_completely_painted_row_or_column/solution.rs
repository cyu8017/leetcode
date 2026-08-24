// LeetCode 2661 - First Completely Painted Row or Column
// https://leetcode.com/problems/first-completely-painted-row-or-column/

impl Solution {
    pub fn first_complete_index(arr: Vec<i32>, mat: Vec<Vec<i32>>) -> i32 {
        let m = mat.len();
        let n = mat[0].len();
        let mut pos = vec![(0usize, 0usize); m * n + 1];
        for i in 0..m {
            for j in 0..n {
                pos[mat[i][j] as usize] = (i, j);
            }
        }
        let mut row_cnt = vec![0; m];
        let mut col_cnt = vec![0; n];
        for (i, &v) in arr.iter().enumerate() {
            let (r, c) = pos[v as usize];
            row_cnt[r] += 1;
            col_cnt[c] += 1;
            if row_cnt[r] == n || col_cnt[c] == m {
                return i as i32;
            }
        }
        -1
    }
}
