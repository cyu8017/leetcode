// LeetCode 0242 - Valid Anagram
// https://leetcode.com/problems/valid-anagram/

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }
        let mut counts = [0i32; 26];
        for (left, right) in s.bytes().zip(t.bytes()) {
            counts[(left - b'a') as usize] += 1;
            counts[(right - b'a') as usize] -= 1;
        }
        counts.iter().all(|&count| count == 0)
    }
}
