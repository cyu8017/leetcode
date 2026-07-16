// LeetCode 0360 - Sort Transformed Array
// https://leetcode.com/problems/sort-transformed-array/

impl Solution {
    pub fn sort_transformed_array(nums: Vec<i32>, a: i32, b: i32, c: i32) -> Vec<i32> {
        let transform = |value: i32| a * value * value + b * value + c;

        let mut left = 0usize;
        let mut right = nums.len() - 1;
        let mut result = vec![0; nums.len()];
        let mut index = if a > 0 { nums.len() - 1 } else { 0 };
        let step = if a > 0 { -1isize } else { 1 };

        while left <= right {
            let left_value = transform(nums[left]);
            let right_value = transform(nums[right]);

            if a > 0 {
                if left_value > right_value {
                    result[index] = left_value;
                    left += 1;
                } else {
                    result[index] = right_value;
                    right -= 1;
                }
            } else if left_value < right_value {
                result[index] = left_value;
                left += 1;
            } else {
                result[index] = right_value;
                right -= 1;
            }

            index = (index as isize + step) as usize;
        }

        result
    }
}
