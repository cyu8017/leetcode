// LeetCode 0466 - Count The Repetitions
// https://leetcode.com/problems/count-the-repetitions/

use std::collections::HashMap;

impl Solution {
    pub fn get_max_repetitions(s1: String, n1: i32, s2: String, n2: i32) -> i32 {
        if s2.is_empty() {
            return 0;
        }

        let s1_chars: Vec<char> = s1.chars().collect();
        let s2_bytes = s2.as_bytes();
        let mut index = 0usize;
        let mut s2_count = 0i32;
        let mut record: HashMap<usize, (i32, i32)> = HashMap::new();

        for repeat in 0..n1 {
            for ch in &s1_chars {
                if *ch as u8 == s2_bytes[index] {
                    index += 1;
                    if index == s2_bytes.len() {
                        index = 0;
                        s2_count += 1;
                    }
                }
            }
            if let Some(&(previous_repeat, previous_count)) = record.get(&index) {
                let cycle = repeat - previous_repeat;
                let count_cycle = s2_count - previous_count;
                let remaining = n1 - repeat - 1;
                s2_count += (remaining / cycle) * count_cycle;
                if repeat + (remaining / cycle) * cycle >= n1 - 1 {
                    break;
                }
            }
            record.insert(index, (repeat, s2_count));
        }

        s2_count / n2
    }
}
