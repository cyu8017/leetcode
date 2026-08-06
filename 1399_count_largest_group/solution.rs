// LeetCode 1399 - Count Largest Group
// https://leetcode.com/problems/count-largest-group/

use std::collections::HashMap;

impl Solution {
    pub fn count_largest_group(n: i32) -> i32 {
        let mut c = HashMap::new();
        for x in 1..=n {
            let mut s = 0;
            let mut v = x;
            while v > 0 {
                s += v % 10;
                v /= 10;
            }
            *c.entry(s).or_insert(0) += 1;
        }
        let m = *c.values().max().unwrap();
        c.values().filter(|&&v| v == m).count() as i32
    }
}
