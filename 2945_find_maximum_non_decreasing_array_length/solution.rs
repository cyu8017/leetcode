// LeetCode 2945 - Find Maximum Non-decreasing Array Length
// https://leetcode.com/problems/find-maximum-non-decreasing-array-length/

use std::collections::VecDeque;

impl Solution {
    pub fn find_maximum_length(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut pref = vec![0i64; n + 1];
        let mut last = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + nums[i] as i64;
        }
        let mut dp = vec![0; n + 1];
        let mut dq: VecDeque<(usize, i64)> = VecDeque::new();
        dq.push_back((0, 0));
        for i in 1..=n {
            while dq.len() > 1 && dq[1].1 <= pref[i] {
                dq.pop_front();
            }
            let j = dq[0].0;
            dp[i] = dp[j] + 1;
            last[i] = pref[i] - pref[j];
            let val = pref[i] + last[i];
            while !dq.is_empty() && dq.back().unwrap().1 >= val {
                dq.pop_back();
            }
            dq.push_back((i, val));
        }
        dp[n]
    }
}
