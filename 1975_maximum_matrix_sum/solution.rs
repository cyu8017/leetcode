// LeetCode 1975 - Maximum Matrix Sum
// https://leetcode.com/problems/maximum-matrix-sum/

impl Solution {
    pub fn max_matrix_sum(matrix: Vec<Vec<i32>>) -> i64 {
        let mut total: i64 = 0;
        let mut neg = 0;
        let mut mn = i64::MAX;
        for row in &matrix {
            for &x in row {
                if x < 0 {
                    neg += 1;
                }
                let ax = (x as i64).abs();
                total += ax;
                mn = mn.min(ax);
            }
        }
        if neg % 2 == 0 {
            total
        } else {
            total - 2 * mn
        }
    }
}
