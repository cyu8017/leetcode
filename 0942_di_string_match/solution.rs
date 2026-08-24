// LeetCode 0942 - DI String Match
// https://leetcode.com/problems/di-string-match/

impl Solution {
    pub fn di_string_match(s: String) -> Vec<i32> {
        let mut lo = 0;
        let mut hi = s.len() as i32;
        let mut ans = Vec::new();
        for ch in s.chars() {
            if ch == 'I' {
                ans.push(lo);
                lo += 1;
            } else {
                ans.push(hi);
                hi -= 1;
            }
        }
        ans.push(lo);
        ans
    }
}
