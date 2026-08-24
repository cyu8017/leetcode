// LeetCode 3889 - Mirror Frequency Distance
// https://leetcode.com/problems/mirror-frequency-distance/

use std::collections::HashMap;

impl Solution {
    pub fn mirror_frequency(s: String) -> i32 {
        let mut freq = HashMap::new();
        for c in s.chars() {
            *freq.entry(c).or_insert(0) += 1;
        }
        let mut ans = 0;
        let mut vis = HashMap::new();
        for (&c, &v) in &freq {
            let m = if c.is_ascii_lowercase() {
                (b'a' + 25 - (c as u8 - b'a')) as char
            } else {
                (b'0' + (9 - (c as u8 - b'0'))) as char
            };
            if *vis.get(&m).unwrap_or(&false) {
                continue;
            }
            vis.insert(c, true);
            let mv = *freq.get(&m).unwrap_or(&0);
            ans += (v - mv).abs();
        }
        ans
    }
}
