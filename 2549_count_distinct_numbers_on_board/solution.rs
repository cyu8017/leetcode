// LeetCode 2549 - Count Distinct Numbers on Board
// https://leetcode.com/problems/count-distinct-numbers-on-board/

impl Solution {
    pub fn distinct_integers(n: i32) -> i32 {
        if n == 1 {
            1
        } else {
            n - 1
        }
    }
}
