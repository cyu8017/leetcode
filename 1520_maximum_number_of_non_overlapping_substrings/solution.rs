// LeetCode 1520 - Maximum Number of Non-Overlapping Substrings
// https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/

use std::collections::HashMap;

impl Solution {
    pub fn max_num_of_substrings(s: String) -> Vec<String> {
        let bytes = s.as_bytes();
        let mut first = HashMap::new();
        let mut last = HashMap::new();
        for (i, &ch) in bytes.iter().enumerate().rev() {
            first.insert(ch, i);
        }
        for (i, &ch) in bytes.iter().enumerate() {
            last.insert(ch, i);
        }
        let mut intervals = Vec::new();
        for i in 0..bytes.len() {
            let ch = bytes[i];
            if first[&ch] != i {
                continue;
            }
            let mut end = last[&ch];
            let mut j = i;
            let mut valid = true;
            while j <= end {
                if first[&bytes[j]] < i {
                    valid = false;
                    break;
                }
                end = end.max(last[&bytes[j]]);
                j += 1;
            }
            if valid {
                intervals.push((end, i));
            }
        }
        intervals.sort_unstable();
        let mut answer = Vec::new();
        let mut previous_end = -1isize;
        for (end, start) in intervals {
            if start as isize > previous_end {
                answer.push(s[start..=end].to_string());
                previous_end = end as isize;
            }
        }
        answer.sort_by_key(|a| a.len());
        answer
    }
}
