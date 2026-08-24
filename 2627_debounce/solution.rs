// LeetCode 2627 - Debounce
// https://leetcode.com/problems/debounce/

impl Solution {
    pub fn debounce(f: impl Fn(), _t: i32) -> impl Fn() {
        move || f()
    }
}
