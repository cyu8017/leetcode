// LeetCode 1788 - Maximize the Beauty of the Garden
// https://leetcode.com/problems/maximize-the-beauty-of-the-garden/

use std::collections::HashMap;

impl Solution {
    pub fn maximum_beauty(flowers: Vec<i32>) -> i32 {
        let mut first: HashMap<i32, usize> = HashMap::new();
        let mut prefix = vec![0i64; flowers.len() + 1];
        for (i, &value) in flowers.iter().enumerate() {
            prefix[i + 1] = prefix[i] + value.max(0) as i64;
        }
        let mut best = i64::MIN;
        for (i, &value) in flowers.iter().enumerate() {
            if let Some(&left) = first.get(&value) {
                let between = prefix[i] - prefix[left + 1];
                let candidate = flowers[left] as i64 + flowers[i] as i64 + between;
                best = best.max(candidate);
            } else {
                first.insert(value, i);
            }
        }
        best as i32
    }
}
