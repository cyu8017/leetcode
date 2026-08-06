// LeetCode 1347 - Minimum Number of Steps to Make Two Strings Anagram
// https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

impl Solution {
    pub fn min_steps(s: String, t: String) -> i32 {
        let mut count = [0i32; 26];
        for (a, b) in s.bytes().zip(t.bytes()) {
            count[(a - b'a') as usize] += 1;
            count[(b - b'a') as usize] -= 1;
        }
        count.iter().filter(|&&c| c > 0).sum()
    }
}
