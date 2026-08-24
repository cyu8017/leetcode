// LeetCode 0917 - Reverse Only Letters
// https://leetcode.com/problems/reverse-only-letters/

impl Solution {
    pub fn reverse_only_letters(s: String) -> String {
        let mut chars: Vec<char> = s.chars().collect();
        let mut i = 0i32;
        let mut j = chars.len() as i32 - 1;
        while i < j {
            while i < j && !chars[i as usize].is_ascii_alphabetic() {
                i += 1;
            }
            while i < j && !chars[j as usize].is_ascii_alphabetic() {
                j -= 1;
            }
            chars.swap(i as usize, j as usize);
            i += 1;
            j -= 1;
        }
        chars.into_iter().collect()
    }
}
