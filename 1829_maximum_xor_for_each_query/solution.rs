// LeetCode 1829 - Maximum XOR for Each Query
// https://leetcode.com/problems/maximum-xor-for-each-query/

impl Solution {
    pub fn get_maximum_xor(nums: Vec<i32>, maximum_bit: i32) -> Vec<i32> {
        let limit = (1 << maximum_bit) - 1;
        let mut current = 0;
        for &num in &nums {
            current ^= num;
        }

        let mut result = Vec::with_capacity(nums.len());
        for i in (0..nums.len()).rev() {
            result.push(current ^ limit);
            current ^= nums[i];
        }
        result
    }
}
