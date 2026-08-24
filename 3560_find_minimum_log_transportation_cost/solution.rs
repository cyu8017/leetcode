// LeetCode 3560 - Find Minimum Log Transportation Cost
// https://leetcode.com/problems/find-minimum-log-transportation-cost/

impl Solution {
    pub fn min_cutting_cost(n: i32, m: i32, k: i32) -> i64 {
        let x = n.max(m);
        if x <= k {
            0
        } else {
            k as i64 * (x - k) as i64
        }
    }
}
