// LeetCode 1616 - Split Two Strings to Make Palindrome
// https://leetcode.com/problems/split-two-strings-to-make-palindrome/

impl Solution {
    pub fn check_palindrome_formation(a: String, b: String) -> bool {
        Self::check(&a, &b) || Self::check(&b, &a)
    }

    fn check(x: &str, y: &str) -> bool {
        let xb = x.as_bytes();
        let yb = y.as_bytes();
        let (mut i, mut j) = (0usize, xb.len() - 1);
        while i < j && xb[i] == yb[j] {
            i += 1;
            j -= 1;
        }
        let left = if i <= j { Self::is_pal(&xb[i..=j]) } else { true };
        let right = if i <= j { Self::is_pal(&yb[i..=j]) } else { true };
        left || right
    }

    fn is_pal(s: &[u8]) -> bool {
        s.iter().eq(s.iter().rev())
    }
}
