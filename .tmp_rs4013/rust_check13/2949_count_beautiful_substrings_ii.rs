#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2949 - Count Beautiful Substrings II
// https://leetcode.com/problems/count-beautiful-substrings-ii/

use std::collections::HashMap;

impl Solution {
    pub fn beautiful_substrings(s: String, k: i32) -> i64 {
        fn is_vowel(c: u8) -> bool {
            matches!(c, b'a' | b'e' | b'i' | b'o' | b'u')
        }
        let mut x = 1;
        while (x * x) % k != 0 {
            x += 1;
        }
        let mut freq: HashMap<(i32, i32), i64> = HashMap::new();
        freq.insert((0, 0), 1);
        let mut bal = 0i32;
        let mut vowels = 0i32;
        let mut ans = 0i64;
        for &ch in s.as_bytes() {
            if is_vowel(ch) {
                bal += 1;
                vowels += 1;
            } else {
                bal -= 1;
            }
            let kk = (bal, vowels % x);
            ans += *freq.get(&kk).unwrap_or(&0);
            *freq.entry(kk).or_insert(0) += 1;
        }
        ans
    }
}
