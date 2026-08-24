// LeetCode 2133 - Check if Every Row and Column Contains All Numbers
// https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/

impl Solution {
    pub fn check_valid(matrix: Vec<Vec<i32>>) -> bool {
        let n = matrix.len();
        for i in 0..n {
            let mut row = vec![false; n + 1];
            let mut col = vec![false; n + 1];
            for j in 0..n {
                let rv = matrix[i][j] as usize;
                let cv = matrix[j][i] as usize;
                if row[rv] || col[cv] {
                    return false;
                }
                row[rv] = true;
                col[cv] = true;
            }
        }
        true
    }
}
