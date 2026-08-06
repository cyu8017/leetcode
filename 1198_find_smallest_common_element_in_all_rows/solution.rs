// LeetCode 1198 - Find Smallest Common Element in All Rows
// https://leetcode.com/problems/find-smallest-common-element-in-all-rows/

use std::collections::HashSet;

impl Solution {
    pub fn smallest_common_element(mat: Vec<Vec<i32>>) -> i32 {
        let mut common: HashSet<i32> = mat[0].iter().copied().collect();
        for row in &mat[1..] {
            let row_set: HashSet<i32> = row.iter().copied().collect();
            common.retain(|x| row_set.contains(x));
            if common.is_empty() {
                return -1;
            }
        }
        *common.iter().min().unwrap()
    }
}
