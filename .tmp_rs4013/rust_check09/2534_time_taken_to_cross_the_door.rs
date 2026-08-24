struct Solution;

// LeetCode 2534 - Time Taken to Cross the Door
// https://leetcode.com/problems/time-taken-to-cross-the-door/

use std::collections::VecDeque;

impl Solution {
    pub fn time_taken(arrival: Vec<i32>, state: Vec<i32>) -> Vec<i32> {
        let n = arrival.len();
        let mut ans = vec![0; n];
        let mut enter = VecDeque::new();
        let mut exitq = VecDeque::new();
        let mut i = 0;
        let mut t = 0;
        let mut prev = 1;
        while i < n || !enter.is_empty() || !exitq.is_empty() {
            while i < n && arrival[i] <= t {
                if state[i] == 0 {
                    enter.push_back(i);
                } else {
                    exitq.push_back(i);
                }
                i += 1;
            }
            if enter.is_empty() && exitq.is_empty() {
                if i < n {
                    t = arrival[i];
                    prev = 1;
                }
                continue;
            }
            if prev == 1 {
                if let Some(idx) = exitq.pop_front() {
                    ans[idx] = t;
                    prev = 1;
                } else if let Some(idx) = enter.pop_front() {
                    ans[idx] = t;
                    prev = 0;
                }
            } else if let Some(idx) = enter.pop_front() {
                ans[idx] = t;
                prev = 0;
            } else if let Some(idx) = exitq.pop_front() {
                ans[idx] = t;
                prev = 1;
            }
            t += 1;
        }
        ans
    }
}

fn main() {}
