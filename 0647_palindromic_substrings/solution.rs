// LeetCode 0647 - Palindromic Substrings
// https://leetcode.com/problems/palindromic-substrings/

impl Solution {
    fn expand(s: &[u8], mut left: i32, mut right: i32) -> i32 {
        let mut count = 0;
        while left >= 0 && right < s.len() as i32 && s[left as usize] == s[right as usize] {
            count += 1;
            left -= 1;
            right += 1;
        }
        count
    }

    pub fn count_substrings(s: String) -> i32 {
        let s = s.as_bytes();
        let mut total = 0;
        for i in 0..s.len() {
            total += Self::expand(s, i as i32, i as i32);
            total += Self::expand(s, i as i32, i as i32 + 1);
        }
        total
    }
}
