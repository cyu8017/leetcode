// LeetCode 2725 - Interval Cancellation
// https://leetcode.com/problems/interval-cancellation/

impl Solution {
    pub fn cancellable<F: FnMut() -> i32>(mut f: F, _t: i32, times: i32) -> Vec<i32> {
        let mut results = Vec::new();
        for _ in 0..times {
            results.push(f());
        }
        results
    }
}
