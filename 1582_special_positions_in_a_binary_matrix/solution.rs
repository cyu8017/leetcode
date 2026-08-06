// LeetCode 1582 - Special Positions in a Binary Matrix
// https://leetcode.com/problems/special-positions-in-a-binary-matrix/

impl Solution {
    pub fn num_special(mat: Vec<Vec<i32>>) -> i32 {
        let rows: Vec<i32> = mat.iter().map(|row| row.iter().sum()).collect();
        let cols: Vec<i32> = (0..mat[0].len())
            .map(|j| mat.iter().map(|row| row[j]).sum())
            .collect();
        let mut ans = 0;
        for i in 0..mat.len() {
            for j in 0..mat[0].len() {
                if mat[i][j] == 1 && rows[i] == 1 && cols[j] == 1 {
                    ans += 1;
                }
            }
        }
        ans
    }
}
