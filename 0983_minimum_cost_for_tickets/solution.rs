// LeetCode 0983 - Minimum Cost For Tickets
// https://leetcode.com/problems/minimum-cost-for-tickets/

use std::collections::HashSet;

impl Solution {
    pub fn mincost_tickets(days: Vec<i32>, costs: Vec<i32>) -> i32 {
        let dayset: HashSet<i32> = days.iter().copied().collect();
        let last = *days.last().unwrap();
        let mut dp = vec![0; (last + 1) as usize];
        for d in 1..=last {
            if !dayset.contains(&d) {
                dp[d as usize] = dp[(d - 1) as usize];
            } else {
                dp[d as usize] = (dp[(d - 1) as usize] + costs[0])
                    .min(dp[(d - 7).max(0) as usize] + costs[1])
                    .min(dp[(d - 30).max(0) as usize] + costs[2]);
            }
        }
        dp[last as usize]
    }
}
