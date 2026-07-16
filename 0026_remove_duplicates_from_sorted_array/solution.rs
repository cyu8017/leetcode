// LeetCode 0026 - Remove Duplicates from Sorted Array
// https://leetcode.com/problems/remove-duplicates-from-sorted-array/

impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        if nums.is_empty() {
            return 0;
        }
        let mut write = 1;
        for read in 1..nums.len() {
            if nums[read] != nums[write - 1] {
                nums[write] = nums[read];
                write += 1;
            }
        }
        write as i32
    }
}
