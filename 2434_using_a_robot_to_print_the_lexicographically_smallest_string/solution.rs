// LeetCode 2434 - Using a Robot to Print the Lexicographically Smallest String
// https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

impl Solution {
    pub fn robot_with_string(s: String) -> String {
        let b = s.as_bytes();
        let n = b.len();
        let mut min_suf = vec![b'z' + 1; n + 1];
        for i in (0..n).rev() {
            min_suf[i] = b[i].min(min_suf[i + 1]);
        }
        let mut stack = Vec::new();
        let mut ans = Vec::new();
        for i in 0..n {
            stack.push(b[i]);
            while !stack.is_empty() && *stack.last().unwrap() <= min_suf[i + 1] {
                ans.push(stack.pop().unwrap());
            }
        }
        while let Some(c) = stack.pop() {
            ans.push(c);
        }
        String::from_utf8(ans).unwrap()
    }
}
