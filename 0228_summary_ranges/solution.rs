// LeetCode 0228 - Summary Ranges
// https://leetcode.com/problems/summary-ranges/

impl Solution {
    pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
        let mut result = Vec::new();
        let mut index = 0;

        while index < nums.len() {
            let start = nums[index];
            while index + 1 < nums.len() && nums[index + 1] == nums[index] + 1 {
                index += 1;
            }
            if start == nums[index] {
                result.push(start.to_string());
            } else {
                result.push(format!("{}->{}", start, nums[index]));
            }
            index += 1;
        }

        result
    }
}
