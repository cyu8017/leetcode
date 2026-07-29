// LeetCode 1004 - Max Consecutive Ones III
// https://leetcode.com/problems/max-consecutive-ones-iii/

impl Solution {
    pub fn longest_ones(nums: Vec<i32>, k: i32) -> i32 {
        let mut left = 0usize;
        let mut zeros = 0;
        let mut ans = 0;
        for (right, &x) in nums.iter().enumerate() {
            if x == 0 {
                zeros += 1;
            }
            while zeros > k {
                if nums[left] == 0 {
                    zeros -= 1;
                }
                left += 1;
            }
            ans = ans.max((right - left + 1) as i32);
        }
        ans
    }
}
