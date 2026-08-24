struct Solution;
// LeetCode 3498 - Reverse Degree of a String
// https://leetcode.com/problems/reverse-degree-of-a-string/

impl Solution {
    pub fn reverse_degree(s: String) -> i32 {
        let mut ans = 0;
        for (i, c) in s.bytes().enumerate() {
            ans += (26 - (c - b'a') as i32) * (i as i32 + 1);
        }
        ans
    }
}

fn main() {}
