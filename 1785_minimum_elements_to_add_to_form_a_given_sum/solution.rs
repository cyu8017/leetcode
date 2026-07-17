// LeetCode 1785 - Minimum Elements to Add to Form a Given Sum
// https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/

impl Solution {
    pub fn min_elements(nums: Vec<i32>, limit: i32, goal: i32) -> i32 {
        let sum: i64 = nums.iter().map(|&x| x as i64).sum();
        let diff = (sum - goal as i64).abs();
        let limit = limit as i64;
        ((diff + limit - 1) / limit) as i32
    }
}
