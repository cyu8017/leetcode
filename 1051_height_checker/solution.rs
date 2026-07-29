// LeetCode 1051 - Height Checker
// https://leetcode.com/problems/height-checker/

impl Solution {
    pub fn height_checker(heights: Vec<i32>) -> i32 {
        let mut expected = heights.clone();
        expected.sort_unstable();
        heights
            .iter()
            .zip(expected.iter())
            .filter(|(a, b)| a != b)
            .count() as i32
    }
}
