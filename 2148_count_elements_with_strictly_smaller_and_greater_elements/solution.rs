// LeetCode 2148 - Count Elements With Strictly Smaller and Greater Elements
// https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/

impl Solution {
    pub fn count_elements(nums: Vec<i32>) -> i32 {
        let mn = *nums.iter().min().unwrap();
        let mx = *nums.iter().max().unwrap();
        nums.iter().filter(|&&x| x > mn && x < mx).count() as i32
    }
}
