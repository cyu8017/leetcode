// LeetCode 2718 - Sum of Matrix After Queries
// https://leetcode.com/problems/sum-of-matrix-after-queries/

impl Solution {
    pub fn matrix_sum_queries(n: i32, queries: Vec<Vec<i32>>) -> i64 {
        let n = n as usize;
        let mut row_done = vec![false; n];
        let mut col_done = vec![false; n];
        let mut rows_left = n as i64;
        let mut cols_left = n as i64;
        let mut ans = 0i64;
        for q in queries.iter().rev() {
            let typ = q[0];
            let idx = q[1] as usize;
            let val = q[2] as i64;
            if typ == 0 {
                if !row_done[idx] {
                    ans += val * cols_left;
                    row_done[idx] = true;
                    rows_left -= 1;
                }
            } else if !col_done[idx] {
                ans += val * rows_left;
                col_done[idx] = true;
                cols_left -= 1;
            }
        }
        ans
    }
}
