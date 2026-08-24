struct Solution;

// LeetCode 2612 - Minimum Reverse Operations
// https://leetcode.com/problems/minimum-reverse-operations/

use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn min_reverse_operations(n: i32, p: i32, banned: Vec<i32>, k: i32) -> Vec<i32> {
        let n = n as usize;
        let k = k as usize;
        let ban: HashSet<i32> = banned.into_iter().collect();
        let mut ans = vec![-1; n];
        ans[p as usize] = 0;
        let mut q = VecDeque::new();
        q.push_back((p as usize, 0));
        while let Some((i, d)) = q.pop_front() {
            let mut lo = i as i32 - (k as i32 - 1);
            if lo < 0 {
                lo = 0;
            }
            let mut hi = i as i32;
            if hi > n as i32 - k as i32 {
                hi = n as i32 - k as i32;
            }
            for l in lo..=hi {
                let r = l + k as i32 - 1;
                let ni = l + r - i as i32;
                if ni < 0 || ni >= n as i32 || ban.contains(&ni) || ans[ni as usize] != -1 {
                    continue;
                }
                ans[ni as usize] = d + 1;
                q.push_back((ni as usize, d + 1));
            }
        }
        ans
    }
}

fn main() {}
