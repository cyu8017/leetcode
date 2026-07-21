// LeetCode 1848 - Minimum Distance to the Target Element
// https://leetcode.com/problems/minimum-distance-to-the-target-element/

impl Solution {
    pub fn get_min_distance(nums: Vec<i32>, target: i32, start: i32) -> i32 {
        let mut best = nums.len() as i32;
        for (i, &value) in nums.iter().enumerate() {
            if value == target {
                best = best.min((i as i32 - start).abs());
            }
        }
        best
    }
}
