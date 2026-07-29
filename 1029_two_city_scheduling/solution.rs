// LeetCode 1029 - Two City Scheduling
// https://leetcode.com/problems/two-city-scheduling/

impl Solution {
    pub fn two_city_sched_cost(mut costs: Vec<Vec<i32>>) -> i32 {
        costs.sort_unstable_by_key(|c| c[0] - c[1]);
        let n = costs.len() / 2;
        costs[..n].iter().map(|c| c[0]).sum::<i32>() + costs[n..].iter().map(|c| c[1]).sum::<i32>()
    }
}
