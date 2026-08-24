// LeetCode 2546 - Apply Bitwise Operations to Make Strings Equal
// https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/

impl Solution {
    pub fn make_strings_equal(s: String, target: String) -> bool {
        let has1s = s.bytes().any(|c| c == b'1');
        let has1t = target.bytes().any(|c| c == b'1');
        has1s == has1t
    }
}
