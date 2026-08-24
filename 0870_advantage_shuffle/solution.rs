// LeetCode 0870 - Advantage Shuffle
// https://leetcode.com/problems/advantage-shuffle/

use std::collections::VecDeque;

impl Solution {
    pub fn advantage_count(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut sorted1: VecDeque<i32> = {
            let mut v = nums1.clone();
            v.sort_unstable();
            v.into()
        };
        let mut ans = vec![0; nums1.len()];
        let mut indexed: Vec<(i32, usize)> = nums2.into_iter().enumerate().map(|(i, v)| (v, i)).collect();
        indexed.sort_unstable_by(|a, b| b.0.cmp(&a.0));
        for (val, i) in indexed {
            if *sorted1.back().unwrap() > val {
                ans[i] = sorted1.pop_back().unwrap();
            } else {
                ans[i] = sorted1.pop_front().unwrap();
            }
        }
        ans
    }
}
