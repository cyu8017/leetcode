// LeetCode 2650 - Design Cancellable Function
// https://leetcode.com/problems/design-cancellable-function/

use std::cell::Cell;
use std::rc::Rc;

impl Solution {
    pub fn cancellable(
        generator: impl Fn() -> i32,
    ) -> (impl Fn(), impl FnMut() -> (i32, bool)) {
        let cancelled = Rc::new(Cell::new(false));
        let done = Rc::new(Cell::new(false));
        let result = Rc::new(Cell::new(0));
        let c1 = cancelled.clone();
        let cancel = move || c1.set(true);
        let cancelled2 = cancelled;
        let run = move || {
            if done.get() {
                return (result.get(), true);
            }
            let r = generator();
            result.set(r);
            done.set(true);
            (r, !cancelled2.get())
        };
        (cancel, run)
    }
}
