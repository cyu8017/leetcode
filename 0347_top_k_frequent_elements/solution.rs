// LeetCode 0347 - Top K Frequent Elements
// https://leetcode.com/problems/top-k-frequent-elements/

use std::collections::HashMap;

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut counts: HashMap<i32, usize> = HashMap::new();
        let bucket_count = nums.len() + 1;
        for num in nums {
            *counts.entry(num).or_insert(0) += 1;
        }

        let mut buckets = vec![Vec::new(); bucket_count];
        for (value, count) in counts {
            buckets[count].push(value);
        }

        let mut result = Vec::new();
        for bucket in buckets.into_iter().rev() {
            for value in bucket {
                result.push(value);
                if result.len() as i32 == k {
                    return result;
                }
            }
        }

        result
    }
}
