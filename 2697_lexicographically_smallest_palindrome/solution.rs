// LeetCode 2697 - Lexicographically Smallest Palindrome
// https://leetcode.com/problems/lexicographically-smallest-palindrome/

impl Solution {
    pub fn make_smallest_palindrome(s: String) -> String {
        let mut b = s.into_bytes();
        let n = b.len();
        for i in 0..n / 2 {
            let c = b[i].min(b[n - 1 - i]);
            b[i] = c;
            b[n - 1 - i] = c;
        }
        String::from_utf8(b).unwrap()
    }
}
