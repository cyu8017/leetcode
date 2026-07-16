// LeetCode 0171 - Excel Sheet Column Number
// https://leetcode.com/problems/excel-sheet-column-number/

impl Solution {
    pub fn title_to_number(column_title: String) -> i32 {
        column_title
            .bytes()
            .fold(0, |result, ch| result * 26 + (ch - b'A' + 1) as i32)
    }
}