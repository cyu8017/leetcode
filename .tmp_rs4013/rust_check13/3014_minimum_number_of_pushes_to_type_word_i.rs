#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 3014 - Minimum Number of Pushes to Type Word I
// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

impl Solution {
    pub fn minimum_pushes(word: String) -> i32 {
        let n = word.len() as i32;
        let mut ans = 0;
        let mut k = 1;
        for _ in 0..(n / 8) {
            ans += k * 8;
            k += 1;
        }
        ans += k * (n % 8);
        ans
    }
}
