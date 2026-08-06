// LeetCode 1523 - Count Odd Numbers in an Interval Range
// https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

impl Solution {
    pub fn count_odds(low: i32, high: i32) -> i32 {
        (high + 1) / 2 - low / 2
    }
}
