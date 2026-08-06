// LeetCode 1253 - Reconstruct a 2-Row Binary Matrix
// https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

impl Solution {
    pub fn reconstruct_matrix(mut upper: i32, mut lower: i32, colsum: Vec<i32>) -> Vec<Vec<i32>> {
        let mut top = vec![0; colsum.len()];
        let mut bottom = vec![0; colsum.len()];
        for (i, &value) in colsum.iter().enumerate() {
            if value == 2 {
                top[i] = 1;
                bottom[i] = 1;
                upper -= 1;
                lower -= 1;
            }
        }
        if upper < 0 || lower < 0 {
            return vec![];
        }
        for (i, &value) in colsum.iter().enumerate() {
            if value == 1 {
                if upper > 0 {
                    top[i] = 1;
                    upper -= 1;
                } else if lower > 0 {
                    bottom[i] = 1;
                    lower -= 1;
                } else {
                    return vec![];
                }
            }
        }
        if upper == 0 && lower == 0 {
            vec![top, bottom]
        } else {
            vec![]
        }
    }
}
