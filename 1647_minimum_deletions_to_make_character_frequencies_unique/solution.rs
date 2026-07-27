// LeetCode 1647 - Minimum Deletions to Make Character Frequencies Unique
// https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

use std::collections::HashSet;

impl Solution {
    pub fn min_deletions(s: String) -> i32 {
        let mut freq = [0i32; 26];
        for ch in s.bytes() {
            freq[(ch - b'a') as usize] += 1;
        }
        let mut used = HashSet::new();
        let mut ans = 0;
        for mut x in freq {
            while x > 0 && used.contains(&x) {
                x -= 1;
                ans += 1;
            }
            if x > 0 {
                used.insert(x);
            }
        }
        ans
    }
}
