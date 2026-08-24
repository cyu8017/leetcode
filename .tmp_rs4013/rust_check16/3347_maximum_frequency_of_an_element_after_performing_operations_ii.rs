struct Solution;
// LeetCode 3347 - Maximum Frequency of an Element After Performing Operations II
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn max_frequency(mut nums: Vec<i32>, k: i32, num_operations: i32) -> i32 {
        nums.sort_unstable();
        let mut freq: HashMap<i32, i32> = HashMap::new();
        for &x in &nums {
            *freq.entry(x).or_insert(0) += 1;
        }
        let mut ans = 1;
        let mut candidates = Vec::new();
        let mut seen = HashSet::new();
        for &x in &nums {
            for t in [x - k, x, x + k] {
                if seen.insert(t) {
                    candidates.push(t);
                }
            }
        }
        for t in candidates {
            let lo = nums.partition_point(|&x| x < t - k);
            let hi = nums.partition_point(|&x| x <= t + k);
            let can = (hi - lo) as i32;
            let f = *freq.get(&t).unwrap_or(&0);
            let mut use_n = can;
            if use_n > f + num_operations {
                use_n = f + num_operations;
            }
            if use_n > ans {
                ans = use_n;
            }
        }
        ans
    }
}

fn main() {}
