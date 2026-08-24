// LeetCode 0724 - Find Pivot Index
// https://leetcode.com/problems/find-pivot-index/

impl Solution {
    pub fn pivot_index(nums: Vec<i32>) -> i32 {
        let total: i32 = nums.iter().sum();
        let mut left = 0;
        for (i, &num) in nums.iter().enumerate() {
            if left == total - left - num {
                return i as i32;
            }
            left += num;
        }
        -1
    }
}
