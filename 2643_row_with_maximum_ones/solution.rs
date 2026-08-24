// LeetCode 2643 - Row With Maximum Ones
// https://leetcode.com/problems/row-with-maximum-ones/

impl Solution {
    pub fn row_and_maximum_ones(mat: Vec<Vec<i32>>) -> Vec<i32> {
        let mut best_row = 0;
        let mut best_cnt = -1;
        for (i, row) in mat.iter().enumerate() {
            let cnt: i32 = row.iter().sum();
            if cnt > best_cnt {
                best_cnt = cnt;
                best_row = i as i32;
            }
        }
        vec![best_row, best_cnt]
    }
}
