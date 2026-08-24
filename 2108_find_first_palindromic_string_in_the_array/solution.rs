// LeetCode 2108 - Find First Palindromic String in the Array
// https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

impl Solution {
    pub fn first_palindrome(words: Vec<String>) -> String {
        for w in words {
            let b = w.as_bytes();
            let mut l = 0;
            let mut r = b.len().saturating_sub(1);
            let mut ok = true;
            while l < r {
                if b[l] != b[r] {
                    ok = false;
                    break;
                }
                l += 1;
                r -= 1;
            }
            if ok {
                return w;
            }
        }
        String::new()
    }
}
