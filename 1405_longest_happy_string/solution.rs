// LeetCode 1405 - Longest Happy String
// https://leetcode.com/problems/longest-happy-string/

use std::collections::BinaryHeap;

impl Solution {
    pub fn longest_diverse_string(a: i32, b: i32, c: i32) -> String {
        let mut heap = BinaryHeap::new();
        for (count, ch) in [(a, b'a'), (b, b'b'), (c, b'c')] {
            if count > 0 {
                heap.push((count, ch));
            }
        }
        let mut answer = Vec::new();
        while let Some((count, ch)) = heap.pop() {
            let n = answer.len();
            if n >= 2 && answer[n - 1] == ch && answer[n - 2] == ch {
                if let Some((count2, ch2)) = heap.pop() {
                    answer.push(ch2);
                    if count2 - 1 > 0 {
                        heap.push((count2 - 1, ch2));
                    }
                    heap.push((count, ch));
                } else {
                    break;
                }
            } else {
                answer.push(ch);
                if count - 1 > 0 {
                    heap.push((count - 1, ch));
                }
            }
        }
        String::from_utf8(answer).unwrap()
    }
}
