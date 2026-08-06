// LeetCode 1320 - Minimum Distance to Type a Word Using Two Fingers
// https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/

use std::collections::HashMap;

impl Solution {
    pub fn minimum_distance(word: String) -> i32 {
        fn distance(a: i32, b: i32) -> i32 {
            if a == 26 {
                return 0;
            }
            (a / 6 - b / 6).abs() + (a % 6 - b % 6).abs()
        }
        let letters: Vec<i32> = word.bytes().map(|c| (c - b'A') as i32).collect();
        let mut dp: HashMap<i32, i32> = HashMap::new();
        dp.insert(26, 0);
        let mut previous = letters[0];
        for &current in &letters[1..] {
            let mut nxt: HashMap<i32, i32> = HashMap::new();
            for (&free, &cost) in &dp {
                let v1 = nxt.get(&free).copied().unwrap_or(i32::MAX);
                nxt.insert(free, v1.min(cost + distance(previous, current)));
                let v2 = nxt.get(&previous).copied().unwrap_or(i32::MAX);
                nxt.insert(previous, v2.min(cost + distance(free, current)));
            }
            dp = nxt;
            previous = current;
        }
        *dp.values().min().unwrap()
    }
}
