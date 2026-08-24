// LeetCode 3081 - Replace Question Marks in String to Minimize Its Value
// https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn minimize_string_value(s: String) -> String {
        let mut cnt = [0i32; 26];
        let mut k = 0;
        let bytes = s.as_bytes();
        for &c in bytes {
            if c == b'?' {
                k += 1;
            } else {
                cnt[(c - b'a') as usize] += 1;
            }
        }
        let mut pq = BinaryHeap::new();
        for i in 0..26 {
            pq.push(Reverse((cnt[i], i)));
        }
        let mut t = vec![0usize; k];
        for i in 0..k {
            let Reverse((freq, idx)) = pq.pop().unwrap();
            t[i] = idx;
            pq.push(Reverse((freq + 1, idx)));
        }
        t.sort_unstable();
        let mut j = 0;
        let mut out = s.into_bytes();
        for c in &mut out {
            if *c == b'?' {
                *c = t[j] as u8 + b'a';
                j += 1;
            }
        }
        String::from_utf8(out).unwrap()
    }
}
