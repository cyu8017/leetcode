// LeetCode 3501 - Maximize Active Section with Trade II
// https://leetcode.com/problems/maximize-active-section-with-trade-ii/

impl Solution {
    pub fn max_active_sections_after_trade(s: String, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let ones = s.bytes().filter(|&c| c == b'1').count() as i32;
        vec![ones; queries.len()]
    }
}
