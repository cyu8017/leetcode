// LeetCode 3120 - Count the Number of Special Characters I
// https://leetcode.com/problems/count-the-number-of-special-characters-i/

impl Solution {
    pub fn number_of_special_chars(word: String) -> i32 {
        let mut s = [false; 128];
        for c in word.bytes() {
            s[c as usize] = true;
        }
        let mut ans = 0;
        for i in 0..26 {
            if s[b'a' as usize + i] && s[b'A' as usize + i] {
                ans += 1;
            }
        }
        ans
    }
}
