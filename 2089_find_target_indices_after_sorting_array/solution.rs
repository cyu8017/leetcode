// LeetCode 2089 - Find Target Indices After Sorting Array
// https://leetcode.com/problems/find-target-indices-after-sorting-array/

impl Solution {
    pub fn target_indices(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut less = 0;
        let mut eq = 0;
        for x in nums {
            if x < target {
                less += 1;
            } else if x == target {
                eq += 1;
            }
        }
        (0..eq).map(|i| less + i).collect()
    }
}
