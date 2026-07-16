// LeetCode 0213 - House Robber II
// https://leetcode.com/problems/house-robber-ii/

impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        if nums.len() == 1 {
            return nums[0];
        }
        Self::rob_linear(&nums[..nums.len() - 1])
            .max(Self::rob_linear(&nums[1..]))
    }

    fn rob_linear(houses: &[i32]) -> i32 {
        let (mut previous_two, mut previous_one) = (0, 0);
        for &value in houses {
            let current = previous_one.max(previous_two + value);
            previous_two = previous_one;
            previous_one = current;
        }
        previous_one
    }
}
