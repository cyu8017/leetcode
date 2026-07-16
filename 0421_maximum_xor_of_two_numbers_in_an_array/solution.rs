// LeetCode 0421 - Maximum XOR of Two Numbers in an Array
// https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

use std::collections::HashMap;

impl Solution {
    pub fn find_maximum_xor(nums: Vec<i32>) -> i32 {
        let maximum = *nums.iter().max().unwrap_or(&0);
        let mut max_bit = 0;
        while (1 << max_bit) <= maximum && max_bit < 31 {
            max_bit += 1;
        }

        let mut root: HashMap<i32, HashMap<i32, i32>> = HashMap::new();
        let mut next_id = 1_i32;

        for number in &nums {
            let mut node = 0;
            for bit in (0..max_bit).rev() {
                let current = (number >> bit) & 1;
                let entry = root.entry(node).or_default();
                if !entry.contains_key(&current) {
                    entry.insert(current, next_id);
                    next_id += 1;
                }
                node = *entry.get(&current).unwrap();
            }
        }

        let mut best = 0;
        for number in &nums {
            let mut node = 0;
            let mut candidate = 0;
            for bit in (0..max_bit).rev() {
                let current = (number >> bit) & 1;
                let target = 1 - current;
                let children = root.get(&node).unwrap();
                if children.contains_key(&target) {
                    candidate |= 1 << bit;
                    node = *children.get(&target).unwrap();
                } else {
                    node = *children.get(&current).unwrap();
                }
            }
            best = best.max(candidate);
        }

        best
    }
}
