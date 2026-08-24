// LeetCode 3789 - Minimum Cost To Acquire Required Items
// https://leetcode.com/problems/minimum-cost-to-acquire-required-items/

impl Solution {
    pub fn minimum_cost(cost1: i32, cost2: i32, cost_both: i32, need1: i32, need2: i32) -> i64 {
        let a = need1 as i64 * cost1 as i64 + need2 as i64 * cost2 as i64;
        let b = cost_both as i64 * need1.max(need2) as i64;
        let mn = need1.min(need2);
        let c = cost_both as i64 * mn as i64
            + (need1 - mn) as i64 * cost1 as i64
            + (need2 - mn) as i64 * cost2 as i64;
        a.min(b).min(c)
    }
}
