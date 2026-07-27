// LeetCode 1624 - Largest Substring Between Two Equal Characters
// https://leetcode.com/problems/largest-substring-between-two-equal-characters/

impl Solution {
    pub fn max_length_between_equal_characters(s: String) -> i32 {
        let mut first = [-1i32; 26];
        let mut ans = -1;
        for (i, ch) in s.bytes().enumerate() {
            let idx = (ch - b'a') as usize;
            if first[idx] >= 0 {
                ans = ans.max(i as i32 - first[idx] - 1);
            } else {
                first[idx] = i as i32;
            }
        }
        ans
    }
}
