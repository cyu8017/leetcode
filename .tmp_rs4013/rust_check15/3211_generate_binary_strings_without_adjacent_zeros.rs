struct Solution;
// LeetCode 3211 - Generate Binary Strings Without Adjacent Zeros
// https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/

impl Solution {
    pub fn valid_strings(n: i32) -> Vec<String> {
        let n = n as usize;
        let mut ans = Vec::new();
        let mut t = String::new();
        fn dfs(i: usize, n: usize, t: &mut String, ans: &mut Vec<String>) {
            if i >= n {
                ans.push(t.clone());
                return;
            }
            for j in 0..2 {
                if (j == 0 && (i == 0 || t.as_bytes()[i - 1] == b'1')) || j == 1 {
                    t.push(char::from(b'0' + j as u8));
                    dfs(i + 1, n, t, ans);
                    t.pop();
                }
            }
        }
        dfs(0, n, &mut t, &mut ans);
        ans
    }
}

fn main() {}
