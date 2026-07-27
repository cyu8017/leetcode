// LeetCode 1638 - Count Substrings That Differ by One Character
// https://leetcode.com/problems/count-substrings-that-differ-by-one-character/

impl Solution {
    pub fn count_substrings(s: String, t: String) -> i32 {
        let s = s.as_bytes();
        let t = t.as_bytes();
        let mut ans = 0;
        for i in 0..s.len() {
            for j in 0..t.len() {
                let mut diff = 0;
                let mut k = 0;
                while i + k < s.len() && j + k < t.len() {
                    if s[i + k] != t[j + k] {
                        diff += 1;
                    }
                    if diff == 1 {
                        ans += 1;
                    } else if diff > 1 {
                        break;
                    }
                    k += 1;
                }
            }
        }
        ans
    }
}
