// LeetCode 3561 - Resulting String After Adjacent Removals
// https://leetcode.com/problems/resulting-string-after-adjacent-removals/

impl Solution {
    pub fn resulting_string(s: String) -> String {
        let is_contiguous = |a: u8, b: u8| {
            let x = (a as i32 - b as i32).abs();
            x == 1 || x == 25
        };
        let mut stk = Vec::new();
        for c in s.bytes() {
            if !stk.is_empty() && is_contiguous(*stk.last().unwrap(), c) {
                stk.pop();
            } else {
                stk.push(c);
            }
        }
        String::from_utf8(stk).unwrap()
    }
}
