// LeetCode 0028 - Find the Index of the First Occurrence in a String
// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        if needle.is_empty() {
            return 0;
        }
        let needle_len = needle.len();
        if haystack.len() < needle_len {
            return -1;
        }
        for i in 0..=haystack.len() - needle_len {
            if haystack[i..i + needle_len] == needle {
                return i as i32;
            }
        }
        -1
    }
}
