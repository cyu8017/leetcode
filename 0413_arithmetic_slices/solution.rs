// LeetCode 0413 - Arithmetic Slices
// https://leetcode.com/problems/arithmetic-slices/

impl Solution {
    pub fn number_of_arithmetic_slices(nums: Vec<i32>) -> i32 {
        if nums.len() < 3 {
            return 0;
        }

        let mut total = 0;
        let mut current = 0;

        for index in 2..nums.len() {
            if nums[index] - nums[index - 1] == nums[index - 1] - nums[index - 2] {
                current += 1;
                total += current;
            } else {
                current = 0;
            }
        }

        total
    }
}
