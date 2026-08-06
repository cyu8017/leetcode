// LeetCode 1933 - Check if String Is Decomposable Into Value-Equal Substrings
// https://leetcode.com/problems/check-if-string-is-decomposable-into-value-equal-substrings/

impl Solution {
    pub fn is_decomposable(s: String) -> bool {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut i = 0;
        let mut twos = 0;
        while i < n {
            let mut j = i;
            while j < n && bytes[j] == bytes[i] {
                j += 1;
            }
            let length = j - i;
            if length % 3 == 1 {
                return false;
            }
            if length % 3 == 2 {
                twos += 1;
                if twos > 1 {
                    return false;
                }
            }
            i = j;
        }
        twos == 1
    }
}
