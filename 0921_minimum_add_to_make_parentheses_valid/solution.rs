// LeetCode 0921 - Minimum Add to Make Parentheses Valid
// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

impl Solution {
    pub fn min_add_to_make_valid(s: String) -> i32 {
        let mut open_need = 0;
        let mut close_need = 0;
        for ch in s.chars() {
            if ch == '(' {
                close_need += 1;
            } else if close_need > 0 {
                close_need -= 1;
            } else {
                open_need += 1;
            }
        }
        open_need + close_need
    }
}
