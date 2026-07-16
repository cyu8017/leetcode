// LeetCode 0487 - Max Consecutive Ones II
// https://leetcode.com/problems/max-consecutive-ones-ii/

impl Solution {
    pub fn find_max_consecutive_ones(nums: Vec<i32>) -> i32 {
        let mut left = 0usize;
        let mut best = 0;
        let mut zeros = 0;
        for (right, &num) in nums.iter().enumerate() {
            if num == 0 {
                zeros += 1;
            }
            while zeros > 1 {
                if nums[left] == 0 {
                    zeros -= 1;
                }
                left += 1;
            }
            best = best.max((right - left + 1) as i32);
        }
        best
    }
}
