// LeetCode 0541 - Reverse String II
// https://leetcode.com/problems/reverse-string-ii/

impl Solution {
    pub fn reverse_str(s: String, k: i32) -> String {
        let k = k as usize;
        let mut chars: Vec<char> = s.chars().collect();
        let mut start = 0;
        while start < chars.len() {
            let end = (start + k).min(chars.len()) - 1;
            let mut left = start;
            let mut right = end;
            while left < right {
                chars.swap(left, right);
                left += 1;
                right -= 1;
            }
            start += 2 * k;
        }
        chars.into_iter().collect()
    }
}
