// LeetCode 0984 - String Without AAA or BBB
// https://leetcode.com/problems/string-without-aaa-or-bbb/

impl Solution {
    pub fn str_without3a3b(mut a: i32, mut b: i32) -> String {
        let mut ans = String::new();
        while a > 0 || b > 0 {
            let write_a = if ans.len() >= 2 && ans.as_bytes()[ans.len() - 1] == ans.as_bytes()[ans.len() - 2] {
                *ans.as_bytes().last().unwrap() == b'b'
            } else {
                a >= b
            };
            if write_a {
                ans.push('a');
                a -= 1;
            } else {
                ans.push('b');
                b -= 1;
            }
        }
        ans
    }
}
