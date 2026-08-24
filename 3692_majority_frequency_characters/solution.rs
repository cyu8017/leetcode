// LeetCode 3692 - Majority Frequency Characters
// https://leetcode.com/problems/majority-frequency-characters/

use std::collections::HashMap;

impl Solution {
    pub fn majority_frequency_group(s: String) -> String {
        let mut cnt = [0i32; 26];
        for c in s.bytes() {
            cnt[(c - b'a') as usize] += 1;
        }
        let mut f: HashMap<i32, String> = HashMap::new();
        for i in 0..26 {
            if cnt[i] > 0 {
                f.entry(cnt[i]).or_default().push(char::from(b'a' + i as u8));
            }
        }
        let mut mx = 0;
        let mut mv = 0;
        let mut ans = String::new();
        for (v, cs) in f {
            if cs.len() as i32 > mx || (cs.len() as i32 == mx && v > mv) {
                mx = cs.len() as i32;
                mv = v;
                ans = cs;
            }
        }
        ans
    }
}
