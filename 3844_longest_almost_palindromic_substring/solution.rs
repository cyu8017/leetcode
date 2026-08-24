// LeetCode 3844 - Longest Almost Palindromic Substring
// https://leetcode.com/problems/longest-almost-palindromic-substring/

impl Solution {
    pub fn almost_palindromic(s: String) -> i32 {
        let s = s.as_bytes();
        let n = s.len() as i32;
        let f = |mut l: i32, mut r: i32| {
            while l >= 0 && r < n && s[l as usize] == s[r as usize] {
                l -= 1;
                r += 1;
            }
            let mut l1 = l - 1;
            let mut r1 = r;
            let mut l2 = l;
            let mut r2 = r + 1;
            while l1 >= 0 && r1 < n && s[l1 as usize] == s[r1 as usize] {
                l1 -= 1;
                r1 += 1;
            }
            while l2 >= 0 && r2 < n && s[l2 as usize] == s[r2 as usize] {
                l2 -= 1;
                r2 += 1;
            }
            n.min((r1 - l1 - 1).max(r2 - l2 - 1))
        };
        let mut ans = 0;
        for i in 0..n {
            ans = ans.max(f(i, i)).max(f(i, i + 1));
        }
        ans
    }
}
