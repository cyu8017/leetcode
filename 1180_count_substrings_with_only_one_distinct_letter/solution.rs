// LeetCode 1180 - Count Substrings with Only One Distinct Letter
// https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/

impl Solution {
    pub fn count_letters(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut ans = 1;
        let mut length = 1;
        for i in 1..bytes.len() {
            if bytes[i] == bytes[i - 1] {
                length += 1;
            } else {
                length = 1;
            }
            ans += length;
        }
        ans
    }
}
