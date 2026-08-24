// LeetCode 3146 - Permutation Difference between Two Strings
// https://leetcode.com/problems/permutation-difference-between-two-strings/

impl Solution {
    pub fn find_permutation_difference(s: String, t: String) -> i32 {
        let mut d = [0i32; 26];
        for (i, c) in s.bytes().enumerate() {
            d[(c - b'a') as usize] = i as i32;
        }
        let mut ans = 0;
        for (i, c) in t.bytes().enumerate() {
            ans += (d[(c - b'a') as usize] - i as i32).abs();
        }
        ans
    }
}
