// LeetCode 0198 - House Robber
// https://leetcode.com/problems/house-robber/

impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let (mut previous_two, mut previous_one) = (0, 0);
        for value in nums {
            let current = previous_one.max(previous_two + value);
            previous_two = previous_one;
            previous_one = current;
        }
        previous_one
    }
}
