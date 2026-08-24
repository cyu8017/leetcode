// LeetCode 2194 - Cells in a Range on an Excel Sheet
// https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

impl Solution {
    pub fn cells_in_range(s: String) -> Vec<String> {
        let b = s.as_bytes();
        let mut ans = Vec::new();
        for c in b[0]..=b[3] {
            for r in b[1]..=b[4] {
                ans.push(format!("{}{}", c as char, r as char));
            }
        }
        ans
    }
}
