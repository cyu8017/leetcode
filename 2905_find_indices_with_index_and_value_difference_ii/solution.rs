// LeetCode 2905 - Find Indices With Index and Value Difference II
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/

impl Solution {
    pub fn find_indices(nums: Vec<i32>, index_difference: i32, value_difference: i32) -> Vec<i32> {
        let n = nums.len();
        let mut min_idx = 0usize;
        let mut max_idx = 0usize;
        let start = index_difference as usize;
        for j in start..n {
            let i = j - start;
            if nums[i] < nums[min_idx] {
                min_idx = i;
            }
            if nums[i] > nums[max_idx] {
                max_idx = i;
            }
            if nums[j] - nums[min_idx] >= value_difference {
                return vec![min_idx as i32, j as i32];
            }
            if nums[max_idx] - nums[j] >= value_difference {
                return vec![max_idx as i32, j as i32];
            }
        }
        vec![-1, -1]
    }
}
