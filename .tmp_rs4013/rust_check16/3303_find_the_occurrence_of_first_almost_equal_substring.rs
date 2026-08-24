struct Solution;
// LeetCode 3303 - Find the Occurrence of First Almost Equal Substring
// https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/

impl Solution {
    pub fn min_starting_index(s: String, pattern: String) -> i32 {
        let n = s.len();
        let m = pattern.len();
        let sb = s.as_bytes();
        let pb = pattern.as_bytes();
        for i in 0..=n.saturating_sub(m) {
            let mut diff = 0;
            for j in 0..m {
                if sb[i + j] != pb[j] {
                    diff += 1;
                    if diff > 1 {
                        break;
                    }
                }
            }
            if diff <= 1 {
                return i as i32;
            }
        }
        -1
    }
}

fn main() {}
