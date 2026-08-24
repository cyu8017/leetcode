// LeetCode 2057 - Smallest Index With Equal Value
// https://leetcode.com/problems/smallest-index-with-equal-value/

impl Solution {
    pub fn smallest_equal(nums: Vec<i32>) -> i32 {
        for (i, &v) in nums.iter().enumerate() {
            if (i % 10) as i32 == v {
                return i as i32;
            }
        }
        -1
    }
}
