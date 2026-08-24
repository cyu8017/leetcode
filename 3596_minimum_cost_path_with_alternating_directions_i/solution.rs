// LeetCode 3596 - Minimum Cost Path with Alternating Directions I
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-i/

impl Solution {
    pub fn min_cost(m: i32, n: i32) -> i32 {
        if m == 1 && n == 1 {
            1
        } else if m == 1 && n == 2 {
            3
        } else if m == 2 && n == 1 {
            3
        } else {
            -1
        }
    }
}
