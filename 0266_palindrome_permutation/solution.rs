// LeetCode 0266 - Palindrome Permutation
// https://leetcode.com/problems/palindrome-permutation/

impl Solution {
    pub fn can_permute_palindrome(s: String) -> bool {
        let mut counts = [0; 26];
        for byte in s.bytes() {
            counts[(byte - b'a') as usize] += 1;
        }
        counts.iter().filter(|&&count| count % 2 != 0).count() <= 1
    }
}
