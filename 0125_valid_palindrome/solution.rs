// LeetCode 0125 - Valid Palindrome
// https://leetcode.com/problems/valid-palindrome/

impl Solution { pub fn is_palindrome(s: String) -> bool { let bytes=s.as_bytes();let(mut left,mut right)=(0,bytes.len());while left<right{while left<right&&!bytes[left].is_ascii_alphanumeric(){left+=1;}while left<right&&!bytes[right-1].is_ascii_alphanumeric(){right-=1;}if left<right&&bytes[left].to_ascii_lowercase()!=bytes[right-1].to_ascii_lowercase(){return false;}left+=1;right=right.saturating_sub(1);}true } }