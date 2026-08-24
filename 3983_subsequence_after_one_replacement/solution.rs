// LeetCode 3983 - Subsequence After One Replacement
// https://leetcode.com/problems/subsequence-after-one-replacement/

impl Solution {
    pub fn can_make_subsequence(s: String, t: String) -> bool {
        let s = s.as_bytes();
        let t = t.as_bytes();
        let m = s.len();
        let n = t.len();
        let mut i0 = 0;
        let mut i1 = 0;
        let mut j = 0;
        while i1 < m && j < n {
            if s[i1] == t[j] {
                i1 += 1;
            }
            if i1 < i0 + 1 {
                i1 = i0 + 1;
            }
            if s[i0] == t[j] {
                i0 += 1;
            }
            j += 1;
        }
        i1 == m
    }
}
