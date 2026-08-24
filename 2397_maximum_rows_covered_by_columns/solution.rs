// LeetCode 2397 - Maximum Rows Covered by Columns
// https://leetcode.com/problems/maximum-rows-covered-by-columns/

impl Solution {
    pub fn maximum_rows(matrix: Vec<Vec<i32>>, num_select: i32) -> i32 {
        let m = matrix.len();
        let n = matrix[0].len();
        let mut ans = 0;
        fn dfs(
            col: usize,
            chosen: i32,
            mask: i32,
            num_select: i32,
            n: usize,
            m: usize,
            matrix: &[Vec<i32>],
            ans: &mut i32,
        ) {
            if chosen == num_select {
                let mut covered = 0;
                for i in 0..m {
                    let mut ok = true;
                    for j in 0..n {
                        if matrix[i][j] == 1 && ((mask >> j) & 1) == 0 {
                            ok = false;
                            break;
                        }
                    }
                    if ok {
                        covered += 1;
                    }
                }
                *ans = (*ans).max(covered);
                return;
            }
            if col == n {
                return;
            }
            dfs(col + 1, chosen + 1, mask | (1 << col), num_select, n, m, matrix, ans);
            dfs(col + 1, chosen, mask, num_select, n, m, matrix, ans);
        }
        dfs(0, 0, 0, num_select, n, m, &matrix, &mut ans);
        ans
    }
}
