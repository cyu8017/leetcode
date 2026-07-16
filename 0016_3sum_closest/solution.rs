// LeetCode 0016 - 3Sum Closest
// https://leetcode.com/problems/3sum-closest/

impl Solution {
    pub fn three_sum_closest(nums: Vec<i32>, target: i32) -> i32 {
        let mut nums = nums;
        nums.sort_unstable();
        let mut closest = nums[0] + nums[1] + nums[2];

        for i in 0..nums.len().saturating_sub(2) {
            let mut left = i + 1;
            let mut right = nums.len() - 1;
            while left < right {
                let total = nums[i] + nums[left] + nums[right];
                if (total - target).abs() < (closest - target).abs() {
                    closest = total;
                }
                if total < target {
                    left += 1;
                } else if total > target {
                    right -= 1;
                } else {
                    return total;
                }
            }
        }

        closest
    }
}
