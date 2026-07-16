// LeetCode 0442 - Find All Duplicates in an Array
// https://leetcode.com/problems/find-all-duplicates-in-an-array/

impl Solution {
    pub fn find_duplicates(nums: &mut Vec<i32>) -> Vec<i32> {
        let mut result = Vec::new();
        for number in nums.clone() {
            let index = number.unsigned_abs() as usize - 1;
            if nums[index] < 0 {
                result.push(number.unsigned_abs() as i32);
            } else {
                nums[index] = -nums[index];
            }
        }
        result
    }
}
