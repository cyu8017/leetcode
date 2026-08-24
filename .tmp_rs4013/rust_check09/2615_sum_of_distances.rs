struct Solution;

// LeetCode 2615 - Sum of Distances
// https://leetcode.com/problems/sum-of-distances/

use std::collections::HashMap;

impl Solution {
    pub fn distance(nums: Vec<i32>) -> Vec<i64> {
        let n = nums.len();
        let mut ans = vec![0i64; n];
        let mut pos: HashMap<i32, Vec<usize>> = HashMap::new();
        for (i, &x) in nums.iter().enumerate() {
            pos.entry(x).or_default().push(i);
        }
        for idxs in pos.values() {
            let m = idxs.len();
            let mut pref = vec![0i64; m + 1];
            for i in 0..m {
                pref[i + 1] = pref[i] + idxs[i] as i64;
            }
            for j in 0..m {
                let idx = idxs[j] as i64;
                let left = j as i64 * idx - pref[j];
                let right = pref[m] - pref[j + 1] - (m as i64 - 1 - j as i64) * idx;
                ans[idxs[j]] = left + right;
            }
        }
        ans
    }
}

fn main() {}
