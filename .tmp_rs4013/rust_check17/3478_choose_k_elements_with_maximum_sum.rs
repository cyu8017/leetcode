struct Solution;
// LeetCode 3478 - Choose K Elements With Maximum Sum
// https://leetcode.com/problems/choose-k-elements-with-maximum-sum/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn find_max_sum(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> Vec<i64> {
        let n = nums1.len();
        let mut arr: Vec<(i32, i32, usize)> = (0..n).map(|i| (nums1[i], nums2[i], i)).collect();
        arr.sort_by_key(|a| a.0);
        let mut ans = vec![0i64; n];
        let mut h = BinaryHeap::new();
        let mut sum = 0i64;
        let mut i = 0;
        while i < n {
            let v = arr[i].0;
            let start = i;
            while i < n && arr[i].0 == v {
                i += 1;
            }
            for t in start..i {
                ans[arr[t].2] = sum;
            }
            for t in start..i {
                h.push(Reverse(arr[t].1));
                sum += arr[t].1 as i64;
                if h.len() > k as usize {
                    if let Some(Reverse(top)) = h.pop() {
                        sum -= top as i64;
                    }
                }
            }
        }
        ans
    }
}

fn main() {}
