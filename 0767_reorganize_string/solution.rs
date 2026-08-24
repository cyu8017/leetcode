// LeetCode 0767 - Reorganize String
// https://leetcode.com/problems/reorganize-string/

use std::collections::BinaryHeap;

impl Solution {
    pub fn reorganize_string(s: String) -> String {
        let mut freq = [0i32; 26];
        for ch in s.bytes() {
            freq[(ch - b'a') as usize] += 1;
        }
        let mut heap = BinaryHeap::new();
        for (i, &count) in freq.iter().enumerate() {
            if count > 0 {
                heap.push((count, (b'a' + i as u8) as char));
            }
        }
        if heap.peek().map_or(false, |&(c, _)| c > (s.len() as i32 + 1) / 2) {
            return String::new();
        }
        let mut result = String::new();
        while heap.len() >= 2 {
            let (c1, a) = heap.pop().unwrap();
            let (c2, b) = heap.pop().unwrap();
            result.push(a);
            result.push(b);
            if c1 - 1 > 0 {
                heap.push((c1 - 1, a));
            }
            if c2 - 1 > 0 {
                heap.push((c2 - 1, b));
            }
        }
        if let Some((_, ch)) = heap.pop() {
            result.push(ch);
        }
        result
    }
}
