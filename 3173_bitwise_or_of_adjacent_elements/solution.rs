// LeetCode 3173 - Bitwise OR of Adjacent Elements
// https://leetcode.com/problems/bitwise-or-of-adjacent-elements/

impl Solution {
    pub fn or_array(nums: Vec<i32>) -> Vec<i32> {
        let mut ans = Vec::new();
        for i in 1..nums.len() {
            ans.push(nums[i] | nums[i - 1]);
        }
        ans
    }
}
