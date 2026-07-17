// LeetCode 1750 - Minimum Length of String After Deleting Similar Ends
// https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

impl Solution {
    pub fn minimum_length(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut left = 0i64;
        let mut right = bytes.len() as i64 - 1;
        while left < right && bytes[left as usize] == bytes[right as usize] {
            let ch = bytes[left as usize];
            while left <= right && bytes[left as usize] == ch {
                left += 1;
            }
            while left <= right && bytes[right as usize] == ch {
                right -= 1;
            }
        }
        (right - left + 1) as i32
    }
}
