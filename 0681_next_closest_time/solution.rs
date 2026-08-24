// LeetCode 0681 - Next Closest Time
// https://leetcode.com/problems/next-closest-time/

use std::collections::HashSet;

impl Solution {
    pub fn next_closest_time(time: String) -> String {
        let bytes = time.as_bytes();
        let digits: HashSet<u8> = [bytes[0], bytes[1], bytes[3], bytes[4]]
            .into_iter()
            .collect();
        let start = Self::to_mins(&time);
        for delta in 1..=24 * 60 {
            let mins = (start + delta) % (24 * 60);
            let hh = mins / 60;
            let mm = mins % 60;
            let candidate = [
                b'0' + (hh / 10) as u8,
                b'0' + (hh % 10) as u8,
                b'0' + (mm / 10) as u8,
                b'0' + (mm % 10) as u8,
            ];
            if candidate.iter().all(|ch| digits.contains(ch)) {
                return format!(
                    "{}{}:{}{}",
                    candidate[0] as char,
                    candidate[1] as char,
                    candidate[2] as char,
                    candidate[3] as char
                );
            }
        }
        time
    }

    fn to_mins(time: &str) -> i32 {
        let hh: i32 = time[0..2].parse().unwrap();
        let mm: i32 = time[3..5].parse().unwrap();
        hh * 60 + mm
    }
}
