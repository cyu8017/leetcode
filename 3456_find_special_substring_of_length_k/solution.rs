// LeetCode 3456 - Find Special Substring of Length K
// https://leetcode.com/problems/find-special-substring-of-length-k/

impl Solution {
    pub fn has_special_substring(s: String, k: i32) -> bool {
        let n = s.len();
        let k = k as usize;
        let bytes = s.as_bytes();
        for i in 0..=n.saturating_sub(k) {
            let mut ok = true;
            for j in i + 1..i + k {
                if bytes[j] != bytes[i] {
                    ok = false;
                    break;
                }
            }
            if !ok {
                continue;
            }
            if i > 0 && bytes[i - 1] == bytes[i] {
                continue;
            }
            if i + k < n && bytes[i + k] == bytes[i] {
                continue;
            }
            return true;
        }
        false
    }
}
