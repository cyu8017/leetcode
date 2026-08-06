// LeetCode 1400 - Construct K Palindrome Strings
// https://leetcode.com/problems/construct-k-palindrome-strings/

impl Solution {
    pub fn can_construct(s: String, k: i32) -> bool {
        let mut cnt = [0i32; 26];
        for b in s.bytes() {
            cnt[(b - b'a') as usize] += 1;
        }
        let odds = cnt.iter().filter(|&&v| v % 2 == 1).count() as i32;
        odds <= k && k <= s.len() as i32
    }
}
