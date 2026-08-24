struct Solution;
// LeetCode 3958 - Minimum Cost To Split Into Ones II
// https://leetcode.com/problems/minimum-cost-to-split-into-ones-ii/

impl Solution {
    pub fn min_cost(n: i32) -> i64 {
        n as i64 * (n as i64 - 1) / 2
    }
}

fn main() {}
