// LeetCode 1314 - Matrix Block Sum
// https://leetcode.com/problems/matrix-block-sum/

impl Solution {
    pub fn matrix_block_sum(mat: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let m = mat.len();
        let n = mat[0].len();
        let k = k as usize;
        let mut prefix = vec![vec![0; n + 1]; m + 1];
        for r in 0..m {
            for c in 0..n {
                prefix[r + 1][c + 1] =
                    mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c];
            }
        }
        let mut answer = vec![vec![0; n]; m];
        for r in 0..m {
            for c in 0..n {
                let r1 = r.saturating_sub(k);
                let c1 = c.saturating_sub(k);
                let r2 = (r + k + 1).min(m);
                let c2 = (c + k + 1).min(n);
                answer[r][c] =
                    prefix[r2][c2] - prefix[r1][c2] - prefix[r2][c1] + prefix[r1][c1];
            }
        }
        answer
    }
}
