// LeetCode 3066 - Minimum Operations to Exceed Threshold Value II
// https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        let mut pq = BinaryHeap::new();
        for x in nums {
            pq.push(Reverse(x as i64));
        }
        let k = k as i64;
        let mut ans = 0;
        while pq.len() > 1 {
            if let Some(Reverse(x)) = pq.peek() {
                if *x >= k {
                    break;
                }
            }
            let Reverse(x) = pq.pop().unwrap();
            let Reverse(y) = pq.pop().unwrap();
            pq.push(Reverse(x * 2 + y));
            ans += 1;
        }
        ans
    }
}
