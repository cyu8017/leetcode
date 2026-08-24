// LeetCode 2623 - Memoize
// https://leetcode.com/problems/memoize/

use std::collections::HashMap;

impl Solution {
    pub fn memoize(f: impl Fn(i32) -> i32) -> impl FnMut(i32) -> i32 {
        let mut cache = HashMap::new();
        move |x| {
            if let Some(&v) = cache.get(&x) {
                return v;
            }
            let v = f(x);
            cache.insert(x, v);
            v
        }
    }
}
