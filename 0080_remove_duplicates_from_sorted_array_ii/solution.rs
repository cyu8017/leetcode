// LeetCode 0080 - Remove Duplicates from Sorted Array II
// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        if nums.len() <= 2 {
            return nums.len() as i32;
        }
        let mut write = 2;
        for i in 2..nums.len() {
            if nums[i] != nums[write - 2] {
                nums[write] = nums[i];
                write += 1;
            }
        }
        write as i32
    }
}
