// LeetCode 3092 - Most Frequent IDs
// https://leetcode.com/problems/most-frequent-ids/

use std::collections::{BinaryHeap, HashMap};

impl Solution {
    pub fn most_frequent_ids(nums: Vec<i32>, freq: Vec<i32>) -> Vec<i64> {
        let n = nums.len();
        let mut cnt: HashMap<i32, i64> = HashMap::new();
        let mut lazy: HashMap<i64, i32> = HashMap::new();
        let mut ans = vec![0i64; n];
        let mut pq = BinaryHeap::new();
        for i in 0..n {
            let x = nums[i];
            let f = freq[i] as i64;
            let old = *cnt.get(&x).unwrap_or(&0);
            *lazy.entry(old).or_insert(0) += 1;
            let now = old + f;
            cnt.insert(x, now);
            pq.push(now);
            while let Some(&top) = pq.peek() {
                if *lazy.get(&top).unwrap_or(&0) > 0 {
                    *lazy.get_mut(&top).unwrap() -= 1;
                    pq.pop();
                } else {
                    break;
                }
            }
            if let Some(&top) = pq.peek() {
                ans[i] = top;
            }
        }
        ans
    }
}
