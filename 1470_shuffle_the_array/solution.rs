// LeetCode 1470 - Shuffle the Array
// https://leetcode.com/problems/shuffle-the-array/

impl Solution {
    pub fn shuffle(nums: Vec<i32>, n: i32) -> Vec<i32> {
        let n = n as usize;
        let mut answer = Vec::with_capacity(nums.len());
        for i in 0..n {
            answer.push(nums[i]);
            answer.push(nums[i + n]);
        }
        answer
    }
}
