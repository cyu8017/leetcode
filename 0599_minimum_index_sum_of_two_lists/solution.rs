// LeetCode 0599 - Minimum Index Sum of Two Lists
// https://leetcode.com/problems/minimum-index-sum-of-two-lists/

use std::collections::HashMap;

impl Solution {
    pub fn find_restaurant(list1: Vec<String>, list2: Vec<String>) -> Vec<String> {
        let mut index1 = HashMap::new();
        for (i, s) in list1.iter().enumerate() {
            index1.insert(s.clone(), i as i32);
        }
        let mut best = i32::MAX;
        let mut answer = Vec::new();
        for (j, s) in list2.iter().enumerate() {
            if let Some(&i) = index1.get(s) {
                let total = i + j as i32;
                if total < best {
                    best = total;
                    answer = vec![s.clone()];
                } else if total == best {
                    answer.push(s.clone());
                }
            }
        }
        answer
    }
}
