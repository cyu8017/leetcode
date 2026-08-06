// LeetCode 1365 - How Many Numbers Are Smaller Than the Current Number
// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

impl Solution {
    pub fn smaller_numbers_than_current(nums: Vec<i32>) -> Vec<i32> {
        let mut sorted = nums.clone();
        sorted.sort_unstable();
        nums.into_iter()
            .map(|x| sorted.partition_point(|&v| v < x) as i32)
            .collect()
    }
}
