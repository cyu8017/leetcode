// LeetCode 3662 - Filter Characters by Frequency
// https://leetcode.com/problems/filter-characters-by-frequency/

impl Solution {
    pub fn filter_characters(s: String, k: i32) -> String {
        let mut cnt = [0i32; 26];
        for c in s.bytes() {
            cnt[(c - b'a') as usize] += 1;
        }
        s.chars()
            .filter(|&c| cnt[(c as u8 - b'a') as usize] < k)
            .collect()
    }
}
