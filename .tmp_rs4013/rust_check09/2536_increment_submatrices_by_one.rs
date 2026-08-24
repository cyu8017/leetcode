struct Solution;

// LeetCode 2536 - Increment Submatrices by One
// https://leetcode.com/problems/increment-submatrices-by-one/

impl Solution {
    pub fn range_add_queries(n: i32, queries: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = n as usize;
        let mut diff = vec![vec![0; n + 1]; n + 1];
        for q in queries {
            let r1 = q[0] as usize;
            let c1 = q[1] as usize;
            let r2 = q[2] as usize;
            let c2 = q[3] as usize;
            diff[r1][c1] += 1;
            diff[r1][c2 + 1] -= 1;
            diff[r2 + 1][c1] -= 1;
            diff[r2 + 1][c2 + 1] += 1;
        }
        let mut mat = vec![vec![0; n]; n];
        for i in 0..n {
            for j in 0..n {
                let mut v = diff[i][j];
                if i > 0 {
                    v += mat[i - 1][j];
                }
                if j > 0 {
                    v += mat[i][j - 1];
                }
                if i > 0 && j > 0 {
                    v -= mat[i - 1][j - 1];
                }
                mat[i][j] = v;
            }
        }
        mat
    }
}

fn main() {}
