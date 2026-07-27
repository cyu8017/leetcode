// LeetCode 1640 - Check Array Formation Through Concatenation
// https://leetcode.com/problems/check-array-formation-through-concatenation/

use std::collections::HashMap;

impl Solution {
    pub fn can_form_array(arr: Vec<i32>, pieces: Vec<Vec<i32>>) -> bool {
        let by_first: HashMap<i32, Vec<i32>> =
            pieces.into_iter().map(|p| (p[0], p)).collect();
        let mut i = 0;
        while i < arr.len() {
            let Some(p) = by_first.get(&arr[i]) else {
                return false;
            };
            for &v in p {
                if i >= arr.len() || arr[i] != v {
                    return false;
                }
                i += 1;
            }
        }
        true
    }
}
