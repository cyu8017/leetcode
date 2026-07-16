// LeetCode 0548 - Split Array with Equal Sum
// https://leetcode.com/problems/split-array-with-equal-sum/

use std::collections::HashSet;

impl Solution {
    pub fn split_array(nums: Vec<i32>) -> bool {
        let n = nums.len();
        if n < 7 {
            return false;
        }

        let mut prefix = vec![0i64; n + 1];
        for (index, value) in nums.iter().enumerate() {
            prefix[index + 1] = prefix[index] + *value as i64;
        }

        for j in 3..(n - 3) {
            let mut seen = HashSet::new();
            for i in 1..(j - 1) {
                let first = prefix[i] - prefix[0];
                let second = prefix[j] - prefix[i + 1];
                if first == second {
                    seen.insert(first);
                }
            }

            for k in (j + 2)..(n - 1) {
                let third = prefix[k] - prefix[j + 1];
                let fourth = prefix[n] - prefix[k + 1];
                if third == fourth && seen.contains(&third) {
                    return true;
                }
            }
        }

        false
    }
}
