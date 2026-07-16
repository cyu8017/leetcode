// LeetCode 0283 - Move Zeroes
// https://leetcode.com/problems/move-zeroes/

impl Solution {
    pub fn move_zeroes(nums: &mut Vec<i32>) {
        let mut insert = 0;
        for &num in nums.iter() {
            if num != 0 {
                nums[insert] = num;
                insert += 1;
            }
        }
        for index in insert..nums.len() {
            nums[index] = 0;
        }
    }
}
