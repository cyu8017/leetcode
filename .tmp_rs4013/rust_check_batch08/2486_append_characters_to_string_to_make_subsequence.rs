struct Solution;
// LeetCode 2486 - Append Characters to String to Make Subsequence
// https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

impl Solution {
    pub fn append_characters(s: String, t: String) -> i32 {
        let sb = s.as_bytes();
        let tb = t.as_bytes();
        let mut j = 0;
        for &c in sb {
            if j < tb.len() && c == tb[j] {
                j += 1;
            }
        }
        (tb.len() - j) as i32
    }
}

fn main() {}
