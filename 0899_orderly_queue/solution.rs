// LeetCode 0899 - Orderly Queue
// https://leetcode.com/problems/orderly-queue/

impl Solution {
    pub fn orderly_queue(s: String, k: i32) -> String {
        if k > 1 {
            let mut chars: Vec<char> = s.chars().collect();
            chars.sort_unstable();
            return chars.into_iter().collect();
        }
        let n = s.len();
        let doubled = s.repeat(2);
        let mut best = &s[..];
        for i in 1..n {
            let cand = &doubled[i..i + n];
            if cand < best {
                best = cand;
            }
        }
        best.to_string()
    }
}
