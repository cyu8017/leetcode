// LeetCode 2007 - Find Original Array From Doubled Array
// https://leetcode.com/problems/find-original-array-from-doubled-array/

use std::collections::HashMap;

impl Solution {
    pub fn find_original_array(mut changed: Vec<i32>) -> Vec<i32> {
        if changed.len() % 2 == 1 {
            return vec![];
        }
        changed.sort_unstable();
        let mut freq = HashMap::new();
        for &x in &changed {
            *freq.entry(x).or_insert(0) += 1;
        }
        let mut ans = Vec::new();
        for &x in &changed {
            if *freq.get(&x).unwrap_or(&0) == 0 {
                continue;
            }
            *freq.get_mut(&x).unwrap() -= 1;
            let twice = x * 2;
            if *freq.get(&twice).unwrap_or(&0) == 0 {
                return vec![];
            }
            *freq.get_mut(&twice).unwrap() -= 1;
            ans.push(x);
        }
        ans
    }
}
