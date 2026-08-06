// LeetCode 1991 - Find the Middle Index in Array
// https://leetcode.com/problems/find-the-middle-index-in-array/

impl Solution {
    pub fn find_middle_index(nums: Vec<i32>) -> i32 {
        let total: i32 = nums.iter().sum();
        let mut left = 0;
        for (i, &x) in nums.iter().enumerate() {
            if left == total - left - x {
                return i as i32;
            }
            left += x;
        }
        -1
    }
}
