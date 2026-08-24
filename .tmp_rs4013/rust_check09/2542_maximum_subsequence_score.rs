struct Solution;

// LeetCode 2542 - Maximum Subsequence Score
// https://leetcode.com/problems/maximum-subsequence-score/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn max_score(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> i64 {
        let n = nums1.len();
        let k = k as usize;
        let mut idx: Vec<usize> = (0..n).collect();
        idx.sort_by_key(|&i| Reverse(nums2[i]));
        let mut pq: BinaryHeap<Reverse<i32>> = BinaryHeap::new();
        let mut sum = 0i64;
        let mut ans = 0i64;
        for i in idx {
            pq.push(Reverse(nums1[i]));
            sum += nums1[i] as i64;
            if pq.len() > k {
                sum -= pq.pop().unwrap().0 as i64;
            }
            if pq.len() == k {
                let cand = sum * nums2[i] as i64;
                if cand > ans {
                    ans = cand;
                }
            }
        }
        ans
    }
}

fn main() {}
