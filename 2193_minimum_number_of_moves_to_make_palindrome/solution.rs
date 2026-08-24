// LeetCode 2193 - Minimum Number of Moves to Make Palindrome
// https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/

impl Solution {
    pub fn min_moves_to_make_palindrome(s: String) -> i32 {
        let mut b: Vec<u8> = s.into_bytes();
        let mut ans = 0;
        while b.len() > 1 {
            let mut j = b.len() - 1;
            while j > 0 && b[j] != b[0] {
                j -= 1;
            }
            if j == 0 {
                ans += (b.len() / 2) as i32;
                b.remove(0);
                continue;
            }
            ans += (b.len() - 1 - j) as i32;
            b.remove(j);
            b.remove(0);
        }
        ans
    }
}
