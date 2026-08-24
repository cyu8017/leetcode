// LeetCode 2908 - Minimum Sum of Mountain Triplets I
// https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/

impl Solution {
    pub fn minimum_sum(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 1 << 30;
        for j in 1..n - 1 {
            let mut left = 1 << 30;
            let mut right = 1 << 30;
            for i in 0..j {
                if nums[i] < nums[j] && nums[i] < left {
                    left = nums[i];
                }
            }
            for k in j + 1..n {
                if nums[k] < nums[j] && nums[k] < right {
                    right = nums[k];
                }
            }
            if left < (1 << 30) && right < (1 << 30) {
                ans = ans.min(left + nums[j] + right);
            }
        }
        if ans == (1 << 30) { -1 } else { ans }
    }
}
