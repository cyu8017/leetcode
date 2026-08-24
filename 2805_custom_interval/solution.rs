// LeetCode 2805 - Custom Interval
// https://leetcode.com/problems/custom-interval/

impl Solution {
    pub fn custom_interval(_fn: impl Fn(), _delay: i32, _period: i32) -> Box<dyn FnMut()> {
        let mut cancelled = false;
        Box::new(move || {
            cancelled = true;
        })
    }
}
