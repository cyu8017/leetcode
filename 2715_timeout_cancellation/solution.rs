// LeetCode 2715 - Timeout Cancellation
// https://leetcode.com/problems/timeout-cancellation/

use std::cell::Cell;
use std::rc::Rc;

impl Solution {
    pub fn cancellable(
        f: impl Fn() -> i32,
        _t: i32,
    ) -> (impl Fn(), impl Fn() -> Option<i32>) {
        let cancelled = Rc::new(Cell::new(false));
        let c1 = cancelled.clone();
        let cancel = move || c1.set(true);
        let result = move || {
            if cancelled.get() {
                None
            } else {
                Some(f())
            }
        };
        (cancel, result)
    }
}
