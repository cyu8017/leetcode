// LeetCode 3503 - Longest Palindrome After Substring Concatenation I
// https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-i/

impl Solution {
    fn expand(s: &[u8], g: &mut [i32], mut l: i32, mut r: i32) {
        let n = s.len() as i32;
        while l >= 0 && r < n && s[l as usize] == s[r as usize] {
            g[l as usize] = g[l as usize].max(r - l + 1);
            l -= 1;
            r += 1;
        }
    }

    fn calc(s: &[u8]) -> Vec<i32> {
        let n = s.len();
        let mut g = vec![0; n];
        for i in 0..n {
            Self::expand(s, &mut g, i as i32, i as i32);
            Self::expand(s, &mut g, i as i32, i as i32 + 1);
        }
        g
    }

    pub fn longest_palindrome(s: String, t: String) -> i32 {
        let s = s.into_bytes();
        let mut t = t.into_bytes();
        t.reverse();
        let m = s.len();
        let n = t.len();
        let g1 = Self::calc(&s);
        let g2 = Self::calc(&t);
        let mut ans = 0;
        for &v in &g1 {
            ans = ans.max(v);
        }
        for &v in &g2 {
            ans = ans.max(v);
        }
        let mut f = vec![vec![0; n + 1]; m + 1];
        for i in 1..=m {
            for j in 1..=n {
                if s[i - 1] == t[j - 1] {
                    f[i][j] = f[i - 1][j - 1] + 1;
                    let a = if i < m { g1[i] } else { 0 };
                    let b = if j < n { g2[j] } else { 0 };
                    ans = ans.max(f[i][j] * 2 + a);
                    ans = ans.max(f[i][j] * 2 + b);
                }
            }
        }
        ans
    }
}
