// LeetCode 0358 - Rearrange String k Distance Apart
// https://leetcode.com/problems/rearrange-string-k-distance-apart/

use std::collections::{BinaryHeap, HashMap, VecDeque};

impl Solution {
    pub fn rearrange_string(s: String, k: i32) -> String {
        let mut counts: HashMap<char, i32> = HashMap::new();
        for ch in s.chars() {
            *counts.entry(ch).or_insert(0) += 1;
        }

        let max_freq = counts.values().copied().max().unwrap_or(0);
        let max_freq_chars = counts.values().filter(|&&count| count == max_freq).count() as i32;

        if (s.len() as i32 - max_freq_chars) < (max_freq - 1) * (k - 1) {
            return String::new();
        }

        let mut heap = BinaryHeap::new();
        for (ch, count) in counts {
            heap.push((count, ch));
        }

        let mut queue: VecDeque<(i32, char, i32)> = VecDeque::new();
        let mut result = String::new();
        let mut index = 0;

        while !heap.is_empty() || !queue.is_empty() {
            while let Some(front) = queue.front() {
                if front.2 <= index {
                    let (count, ch, _) = queue.pop_front().unwrap();
                    heap.push((count, ch));
                } else {
                    break;
                }
            }

            if heap.is_empty() {
                return String::new();
            }

            let (count, ch) = heap.pop().unwrap();
            result.push(ch);
            if count - 1 > 0 {
                queue.push_back((count - 1, ch, index + k));
            }
            index += 1;
        }

        result
    }
}
