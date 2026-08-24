struct Solution;
// LeetCode 3857 - Minimum Cost to Split Into Ones
// https://leetcode.com/problems/minimum-cost-to-split-into-ones/

impl Solution {
    pub fn min_cost(n: i32) -> i32 {
        n * (n - 1) / 2
    }
}
