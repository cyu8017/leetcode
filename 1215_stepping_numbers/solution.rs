// LeetCode 1215 - Stepping Numbers
// https://leetcode.com/problems/stepping-numbers/

use std::collections::VecDeque;

impl Solution {
    pub fn count_stepping_numbers(low: i32, high: i32) -> Vec<i32> {
        let mut ans = Vec::new();
        if low == 0 {
            ans.push(0);
        }
        let mut q = VecDeque::new();
        for i in 1..=9 {
            q.push_back(i as i64);
        }
        let low = low as i64;
        let high = high as i64;
        while let Some(x) = q.pop_front() {
            if x > high {
                continue;
            }
            if x >= low {
                ans.push(x as i32);
            }
            let last = x % 10;
            if last > 0 {
                q.push_back(x * 10 + last - 1);
            }
            if last < 9 {
                q.push_back(x * 10 + last + 1);
            }
        }
        ans
    }
}
