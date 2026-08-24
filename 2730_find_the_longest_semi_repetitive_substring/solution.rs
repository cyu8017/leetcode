// LeetCode 2730 - Find the Longest Semi-Repetitive Substring
// https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

impl Solution {
    pub fn longest_semi_repetitive_substring(s: String) -> i32 {
        let b = s.as_bytes();
        let mut ans = 0;
        let mut left = 0;
        let mut last_pair = -1i32;
        for right in 0..b.len() {
            if right > 0 && b[right] == b[right - 1] {
                if last_pair >= left as i32 {
                    left = (last_pair + 1) as usize;
                }
                last_pair = right as i32 - 1;
            }
            ans = ans.max(right - left + 1);
        }
        ans as i32
    }
}
