// LeetCode 1541 - Minimum Insertions to Balance a Parentheses String
// https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

impl Solution {
    pub fn min_insertions(s: String) -> i32 {
        let mut insertions = 0;
        let mut needed = 0;
        for ch in s.bytes() {
            if ch == b'(' {
                needed += 2;
                if needed & 1 != 0 {
                    insertions += 1;
                    needed -= 1;
                }
            } else {
                needed -= 1;
                if needed < 0 {
                    insertions += 1;
                    needed = 1;
                }
            }
        }
        insertions + needed
    }
}
