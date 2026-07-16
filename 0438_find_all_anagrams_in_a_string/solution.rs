// LeetCode 0438 - Find All Anagrams in a String
// https://leetcode.com/problems/find-all-anagrams-in-a-string/

impl Solution {
    pub fn find_anagrams(s: String, p: String) -> Vec<i32> {
        if p.len() > s.len() {
            return Vec::new();
        }

        let s = s.as_bytes();
        let p = p.as_bytes();
        let mut need = [0i32; 26];
        let mut window = [0i32; 26];
        for &ch in p {
            need[(ch - b'a') as usize] += 1;
        }

        let mut result = Vec::new();
        let mut left = 0usize;
        for right in 0..s.len() {
            window[(s[right] - b'a') as usize] += 1;
            if right - left + 1 > p.len() {
                window[(s[left] - b'a') as usize] -= 1;
                left += 1;
            }
            if window == need {
                result.push(left as i32);
            }
        }
        result
    }
}
