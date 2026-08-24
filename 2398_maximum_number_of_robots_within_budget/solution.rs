// LeetCode 2398 - Maximum Number of Robots Within Budget
// https://leetcode.com/problems/maximum-number-of-robots-within-budget/

use std::collections::VecDeque;

impl Solution {
    pub fn maximum_robots(charge_times: Vec<i32>, running_costs: Vec<i32>, budget: i64) -> i32 {
        let n = charge_times.len();
        let mut left = 0usize;
        let mut sum = 0i64;
        let mut dq = VecDeque::new();
        let mut ans = 0i32;
        for right in 0..n {
            while !dq.is_empty() && charge_times[*dq.back().unwrap()] <= charge_times[right] {
                dq.pop_back();
            }
            dq.push_back(right);
            sum += running_costs[right] as i64;
            while left <= right
                && charge_times[*dq.front().unwrap()] as i64 + (right as i64 - left as i64 + 1) * sum
                    > budget
            {
                if *dq.front().unwrap() == left {
                    dq.pop_front();
                }
                sum -= running_costs[left] as i64;
                left += 1;
            }
            if left <= right {
                ans = ans.max((right - left + 1) as i32);
            }
        }
        ans
    }
}
