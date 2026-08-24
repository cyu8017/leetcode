// LeetCode 2957 - Remove Adjacent Almost-Equal Characters
// https://leetcode.com/problems/remove-adjacent-almost-equal-characters/

impl Solution {
    pub fn remove_almost_equal_characters(word: String) -> i32 {
        let w = word.as_bytes();
        let n = w.len();
        let mut ans = 0;
        let mut i = 1;
        while i < n {
            if (w[i] as i32 - w[i - 1] as i32).abs() <= 1 {
                ans += 1;
                i += 2;
            } else {
                i += 1;
            }
        }
        ans
    }
}
