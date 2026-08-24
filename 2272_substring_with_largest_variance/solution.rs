// LeetCode 2272 - Substring With Largest Variance
// https://leetcode.com/problems/substring-with-largest-variance/

impl Solution {
    pub fn largest_variance(s: String) -> i32 {
        let mut ans = 0;
        for a in b'a'..=b'z' {
            for b in b'a'..=b'z' {
                if a == b {
                    continue;
                }
                let mut bal = 0;
                let mut has_b = false;
                for c in s.bytes() {
                    if c == a {
                        bal += 1;
                    } else if c == b {
                        bal -= 1;
                        has_b = true;
                    }
                    if has_b {
                        ans = ans.max(bal);
                    }
                    if bal < 0 {
                        bal = 0;
                        has_b = false;
                    }
                }
            }
        }
        ans
    }
}
