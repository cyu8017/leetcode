// LeetCode 2630 - Memoize II
// https://leetcode.com/problems/memoize-ii/

use std::collections::HashMap;

impl Solution {
    pub fn memoize_ii(f: impl Fn(&[i32]) -> i32) -> impl FnMut(Vec<i32>) -> i32 {
        let mut cache: HashMap<String, i32> = HashMap::new();
        move |args: Vec<i32>| {
            let mut k = String::new();
            for a in &args {
                k.push('|');
                k.push_str(&a.to_string());
            }
            if let Some(&v) = cache.get(&k) {
                return v;
            }
            let v = f(&args);
            cache.insert(k, v);
            v
        }
    }
}
