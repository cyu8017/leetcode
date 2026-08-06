// LeetCode 1999 - Smallest Greater Multiple Made of Two Digits
// https://leetcode.com/problems/smallest-greater-multiple-made-of-two-digits/

use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn find_integer(k: i32, digit1: i32, digit2: i32) -> i32 {
        let mut digits = vec![digit1, digit2];
        digits.sort_unstable();
        digits.dedup();
        let mut q = VecDeque::new();
        for &d in &digits {
            if d != 0 {
                q.push_back(d as i64);
            }
        }
        if q.is_empty() {
            return -1;
        }
        let mut seen: HashSet<i64> = q.iter().copied().collect();
        let k64 = k as i64;
        while let Some(x) = q.pop_front() {
            if x > k64 && x % k64 == 0 {
                return x as i32;
            }
            for &d in &digits {
                let nx = x * 10 + d as i64;
                if nx <= i32::MAX as i64 && !seen.contains(&nx) {
                    seen.insert(nx);
                    q.push_back(nx);
                }
            }
        }
        -1
    }
}
