// LeetCode 2609 - Find the Longest Balanced Substring of a Binary String
// https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/

impl Solution {
    pub fn find_the_longest_balanced_substring(s: String) -> i32 {
        let mut ans = 0;
        let mut zeros = 0;
        let mut ones = 0;
        for c in s.bytes() {
            if c == b'0' {
                if ones > 0 {
                    zeros = 0;
                    ones = 0;
                }
                zeros += 1;
            } else {
                ones += 1;
                let cur = ones.min(zeros);
                if 2 * cur > ans {
                    ans = 2 * cur;
                }
            }
        }
        ans
    }
}
