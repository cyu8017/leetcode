// LeetCode 3677 - Count Binary Palindromic Numbers
// https://leetcode.com/problems/count-binary-palindromic-numbers/

impl Solution {
    pub fn count_binary_palindromes(n: i64) -> i32 {
        if n == 0 {
            return 1;
        }
        let mut ans = 1;
        let mut s = String::new();
        let mut x = n;
        while x > 0 {
            s.push(char::from(b'0' + (x & 1) as u8));
            x >>= 1;
        }
        let s: String = s.chars().rev().collect();
        let l = s.len();
        for len_ in 1..l {
            let half = (len_ + 1) / 2;
            ans += 1 << (half - 1);
        }
        let half = (l + 1) / 2;
        let prefix = &s[..half];
        let start = 1 << (half - 1);
        let mut pref_val = 0i64;
        for c in prefix.bytes() {
            pref_val = (pref_val << 1) | (c - b'0') as i64;
        }
        ans += (pref_val - start) as i32;
        let mut pal = prefix.to_string();
        let mut i = half as i32 - 1 - (l % 2) as i32;
        while i >= 0 {
            pal.push(prefix.as_bytes()[i as usize] as char);
            i -= 1;
        }
        let mut pval = 0i64;
        for c in pal.bytes() {
            pval = (pval << 1) | (c - b'0') as i64;
        }
        if pval <= n {
            ans += 1;
        }
        ans
    }
}
