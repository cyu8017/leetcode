struct Solution;
// LeetCode 2414 - Length of the Longest Alphabetical Continuous Substring
// https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/

impl Solution {
    pub fn longest_continuous_substring(s: String) -> i32 {
        let b = s.as_bytes();
        let mut ans = 1;
        let mut cur = 1;
        for i in 1..b.len() {
            if b[i] == b[i - 1] + 1 {
                cur += 1;
                ans = ans.max(cur);
            } else {
                cur = 1;
            }
        }
        ans
    }
}

fn main() {}
