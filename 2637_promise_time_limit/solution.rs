// LeetCode 2637 - Promise Time Limit
// https://leetcode.com/problems/promise-time-limit/

impl Solution {
    pub fn time_limit(f: impl Fn() -> i32, _t: i32) -> impl Fn() -> i32 {
        move || f()
    }
}
