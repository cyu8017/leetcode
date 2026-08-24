// LeetCode 2391 - Minimum Amount of Time to Collect Garbage
// https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

use std::collections::HashMap;

impl Solution {
    pub fn garbage_collection(garbage: Vec<String>, travel: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut last = HashMap::new();
        for (i, g) in garbage.iter().enumerate() {
            ans += g.len() as i32;
            for c in g.chars() {
                last.insert(c, i);
            }
        }
        let mut pref = vec![0; travel.len() + 1];
        for i in 0..travel.len() {
            pref[i + 1] = pref[i] + travel[i];
        }
        for typ in ['M', 'P', 'G'] {
            ans += pref[*last.get(&typ).unwrap_or(&0)];
        }
        ans
    }
}
