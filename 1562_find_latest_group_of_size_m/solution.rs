// LeetCode 1562 - Find Latest Group of Size M
// https://leetcode.com/problems/find-latest-group-of-size-m/

use std::collections::HashMap;

impl Solution {
    pub fn find_latest_step(arr: Vec<i32>, m: i32) -> i32 {
        if m == arr.len() as i32 {
            return m;
        }
        let mut lengths = HashMap::new();
        let mut answer = -1;
        for (step, &x) in arr.iter().enumerate() {
            let step = (step + 1) as i32;
            let left = *lengths.get(&(x - 1)).unwrap_or(&0);
            let right = *lengths.get(&(x + 1)).unwrap_or(&0);
            let size = left + 1 + right;
            lengths.insert(x - left, size);
            lengths.insert(x + right, size);
            if left == m || right == m {
                answer = step - 1;
            }
        }
        answer
    }
}
