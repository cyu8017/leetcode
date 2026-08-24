// LeetCode 0746 - Min Cost Climbing Stairs
// https://leetcode.com/problems/min-cost-climbing-stairs/

impl Solution {
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        let mut a = 0;
        let mut b = 0;
        for i in (0..cost.len()).rev() {
            let next_a = cost[i] + a.min(b);
            b = a;
            a = next_a;
        }
        a.min(b)
    }
}
