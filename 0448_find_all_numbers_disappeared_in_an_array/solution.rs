// LeetCode 0448 - Find All Numbers Disappeared in an Array
// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

impl Solution {
    pub fn find_disappeared_numbers(nums: &mut Vec<i32>) -> Vec<i32> {
        for number in nums.clone() {
            let index = number.unsigned_abs() as usize - 1;
            if nums[index] > 0 {
                nums[index] = -nums[index];
            }
        }

        nums.iter()
            .enumerate()
            .filter_map(|(index, value)| {
                if *value > 0 {
                    Some(index as i32 + 1)
                } else {
                    None
                }
            })
            .collect()
    }
}
