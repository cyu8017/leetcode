// LeetCode 2207 - Maximize Number of Subsequences in a String
// https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/

impl Solution {
    pub fn maximum_subsequence_count(text: String, pattern: String) -> i64 {
        let pb: Vec<u8> = pattern.bytes().collect();
        let a = pb[0];
        let b = pb[1];
        let count = |s: &[u8]| {
            let mut ca = 0i64;
            let mut ans = 0i64;
            for &c in s {
                if c == b {
                    ans += ca;
                }
                if c == a {
                    ca += 1;
                }
            }
            ans
        };
        let mut s1 = vec![a];
        s1.extend(text.bytes());
        let mut s2 = text.into_bytes();
        s2.push(b);
        count(&s1).max(count(&s2))
    }
}
